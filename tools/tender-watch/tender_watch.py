#!/usr/bin/env python3
"""
tender-watch — поиск тендеров по ключевым словам на площадках Узбекистана.

Работает без внешних зависимостей (только стандартная библиотека Python 3.8+).

Три режима:
  1. online   — качает страницы сам (нужен доступ в интернет к площадке)
  2. offline  — разбирает сохранённые из браузера HTML-файлы (обходит любую авторизацию)
  3. render   — рендерит JS-страницы через Playwright, если он установлен

Примеры:
    python3 tender_watch.py --site all
    python3 tender_watch.py --site tzone --pages 5 --profile owl-studio
    python3 tender_watch.py --html-file "~/Downloads/*.html"
    python3 tender_watch.py --site etender --cookies-file cookies.txt --render
"""

from __future__ import annotations

import argparse
import csv
import glob
import gzip
import html as html_mod
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Площадки. page_param подставляется в URL для перелистывания.
SITES = {
    "tzone":      {"url": "https://trade.tzone.uz/page/tenders-all",              "page": "?page={n}"},
    "tenderzone": {"url": "https://tenderzone.uz/",                                "page": "?page={n}"},
    "etender":    {"url": "https://etender.uzex.uz/lots/2/0",                      "page": "?page={n}"},
    "xarid":      {"url": "https://xarid.uzex.uz/",                                "page": "?page={n}"},
    "exarid":     {"url": "https://exarid.uzex.uz/",                               "page": "?page={n}"},
    "tenderweek": {"url": "https://www.tenderweek.com/",                           "page": "?page={n}"},
    "goszakupka": {"url": "https://goszakupka.uz/ru/rubric/tender",                "page": "?page={n}"},
    "bicotender": {"url": "https://www.bicotender.ru/catalog/by-region/uzbekistan/", "page": "?PAGEN_1={n}"},
}

# ---------------------------------------------------------------- нормализация

_APOSTROPHES = "ʻʼ‘’`´"


def normalize(text: str) -> str:
    """Приводит текст к виду, удобному для поиска по основам слов."""
    text = html_mod.unescape(text or "").lower().replace("ё", "е")
    for ch in _APOSTROPHES:
        text = text.replace(ch, "'")
    text = re.sub(r"[   ]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------- HTML → блоки

RECORD_TAGS = {"tr", "li", "article"}
RECORD_CLASS_RE = re.compile(
    r"(card|item|lot|tender|row|result|listing|list-item|product|announce|zayav)", re.I)


class BlockParser(HTMLParser):
    """Собирает из HTML «блоки-записи»: текст + первая ссылка внутри блока."""

    SKIP = {"script", "style", "noscript", "svg", "head"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[dict] = []
        self.blocks: list[dict] = []
        self.skip_depth = 0
        self.json_blobs: list[str] = []
        self._in_json = False
        self._json_buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "script":
            t = (attrs_d.get("type") or "").lower()
            if "json" in t or attrs_d.get("id") in ("__NEXT_DATA__", "__NUXT_DATA__"):
                self._in_json, self._json_buf = True, []
        if tag in self.SKIP:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return

        cls = " ".join(filter(None, (attrs_d.get("class"), attrs_d.get("id"))))
        is_record = tag in RECORD_TAGS or bool(RECORD_CLASS_RE.search(cls))
        frame = {"tag": tag, "record": is_record, "text": [], "href": None, "void": tag in (
            "br", "hr", "img", "input", "meta", "link", "source")}
        if tag == "a" and attrs_d.get("href"):
            frame["self_href"] = attrs_d["href"]
        if not frame["void"]:
            self.stack.append(frame)
        elif tag == "br":
            self._push_text(" ")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            if tag == "script" and self._in_json:
                self.json_blobs.append("".join(self._json_buf))
                self._in_json = False
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                frame = self.stack.pop(i)
                del self.stack[i:]
                text = " ".join(frame["text"])
                href = frame.get("self_href") or frame.get("href")
                if frame["record"] and href and 20 <= len(text.strip()) <= 4000:
                    self.blocks.append({"text": text, "href": href})
                if self.stack:
                    parent = self.stack[-1]
                    parent["text"].append(text)
                    if href and not parent.get("href"):
                        parent["href"] = href
                break

    def handle_data(self, data):
        if self._in_json:
            self._json_buf.append(data)
        if self.skip_depth or not data.strip():
            return
        self._push_text(data)

    def _push_text(self, data):
        if self.stack:
            self.stack[-1]["text"].append(data)


def walk_json(node, out, depth=0):
    """Достаёт записи из встроенного JSON (Next.js / Nuxt / API-ответы)."""
    if depth > 12:
        return
    if isinstance(node, dict):
        keys = {k.lower() for k in node}
        titleish = keys & {"name", "title", "subject", "lotname", "tendername",
                           "productname", "description", "nomi", "naименование"}
        if titleish and len(node) >= 3:
            parts = []
            explicit_url = path_url = id_url = None
            for k, v in node.items():
                if isinstance(v, (str, int, float)) and not isinstance(v, bool):
                    s = str(v)
                    if len(s) < 500:
                        parts.append(f"{k}: {s}")
                    if k.lower() in ("url", "link", "href", "detailurl") and explicit_url is None:
                        explicit_url = s
                    elif path_url is None and re.match(r"^/|^https?://", s):
                        path_url = s
                    elif id_url is None and k.lower() in ("id", "lotid", "tenderid"):
                        id_url = f"#{s}"
            href = explicit_url or path_url or id_url
            text = " | ".join(parts)
            if len(text) >= 20:
                out.append({"text": text, "href": href or "#"})
        for v in node.values():
            walk_json(v, out, depth + 1)
    elif isinstance(node, list):
        for v in node:
            walk_json(v, out, depth + 1)


def guess_base_url(page_html: str, fallback: str) -> str:
    """Для сохранённых файлов восстанавливает адрес сайта, чтобы ссылки были кликабельны."""
    m = re.search(r'<base[^>]+href="(https?://[^"]+)"', page_html, re.I)
    if not m:
        m = re.search(r'(?:href|src|content)="(https?://[^"/]+)', page_html, re.I)
    return m.group(1) if m else fallback


def extract_records(page_html: str, base_url: str) -> list[dict]:
    if base_url.startswith("file://"):
        base_url = guess_base_url(page_html, base_url)
    parser = BlockParser()
    try:
        parser.feed(page_html)
        parser.close()
    except Exception:
        pass

    records = list(parser.blocks)

    for blob in parser.json_blobs:
        try:
            walk_json(json.loads(blob), records)
        except Exception:
            continue
    for m in re.finditer(r"window\.__(?:NUXT|NEXT_DATA|INITIAL_STATE)__\s*=\s*(\{.*?\})\s*[;<]",
                         page_html, re.S):
        try:
            walk_json(json.loads(m.group(1)), records)
        except Exception:
            continue

    # запасной вариант: если разметка нестандартная — берём сами ссылки
    if len(records) < 3:
        for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', page_html, re.S | re.I):
            text = normalize(re.sub(r"<[^>]+>", " ", m.group(2)))
            if len(text) >= 25:
                records.append({"text": text, "href": m.group(1)})

    seen, out = set(), []
    for r in records:
        href = urllib.parse.urljoin(base_url, r["href"]) if r["href"] != "#" else base_url
        key = (href, normalize(r["text"])[:120])
        if key in seen:
            continue
        seen.add(key)
        out.append({"text": normalize(r["text"]), "url": href})
    return out


# ---------------------------------------------------------------- поля лота

MONEY_RE = re.compile(
    r"(\d[\d\s.,]{3,})\s*(сум|so'm|som|uzs|у\.е\.|usd|\$|долл)", re.I)
PRICE_FIELD_RE = re.compile(
    r"(?:price|amount|summa|сумма|стоимост|нач\w*\s*цен|start[_ ]?price|boshlang\w*)"
    r"\W{0,4}(\d[\d\s.,]{4,})", re.I)
DATE_RE = re.compile(r"\b(\d{1,2}[.\-/]\d{1,2}[.\-/]\d{4}|\d{4}-\d{2}-\d{2})"
                     r"(?:\s+\d{1,2}:\d{2})?\b")
CUSTOMER_RE = re.compile(
    r"(?:заказчик|организац|покупател|буюртмачи|buyurtmachi|tashkilot|customer)"
    r"\s*[:\-–]\s*([^|;]{3,90})", re.I)
LOTNO_RE = re.compile(r"(?:лот|lot|№|no\.?|раqam|raqam)\s*[:\-#]?\s*([a-z]{0,4}[\d\-/]{4,})", re.I)
DEADLINE_RE = re.compile(
    r"(?:до|окончан|завершен|дедлайн|приём|прием|tugash|muddat|deadline|подач)"
    r"[^|]{0,40}?(\d{1,2}[.\-/]\d{1,2}[.\-/]\d{4}|\d{4}-\d{2}-\d{2})", re.I)


CUSTOMER_STOP_RE = re.compile(
    r"\s+(?:\d[\d\s.,]{3,}|окончан|оконч|до\s|срок|цена|стоимост|сум\b|so'm|muddat|price|deadline)",
    re.I)


def trim_customer(value: str) -> str:
    """Обрезает имя заказчика там, где в строке начинается сумма или срок."""
    stop = CUSTOMER_STOP_RE.search(value)
    return (value[:stop.start()] if stop else value).strip(" .,;:-|")


def extract_fields(text: str) -> dict:
    money = MONEY_RE.search(text) or PRICE_FIELD_RE.search(text)
    deadline = DEADLINE_RE.search(text)
    dates = DATE_RE.findall(text)
    customer = CUSTOMER_RE.search(text)
    lotno = LOTNO_RE.search(text)
    return {
        "price": (money.group(0).strip() if money else ""),
        "deadline": (deadline.group(1) if deadline else (dates[-1] if dates else "")),
        "customer": (trim_customer(customer.group(1)) if customer else ""),
        "lot_no": (lotno.group(1) if lotno else ""),
    }


# ---------------------------------------------------------------- матчинг

def kw_hit(text: str, keyword: str) -> bool:
    """'+' = все части должны быть в тексте лота (в любом порядке)."""
    return all(part in text for part in keyword.split("+") if part)


def match_profiles(text: str, profiles: dict) -> list[dict]:
    results = []
    for name, prof in profiles.items():
        if name.startswith("_"):
            continue
        strong = [k for k in prof.get("strong", []) if kw_hit(text, k)]
        broad = [k for k in prof.get("broad", []) if kw_hit(text, k)]
        score = 3 * len(strong) + len(broad)
        if score:
            results.append({"profile": name, "title": prof.get("title", name),
                            "score": score, "strong": strong, "broad": broad})
    results.sort(key=lambda r: -r["score"])
    return results


# ---------------------------------------------------------------- загрузка

def load_cookies(path: str) -> str:
    """Netscape cookies.txt (экспорт расширением из браузера) → заголовок Cookie."""
    pairs = []
    with open(os.path.expanduser(path), encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 7:
                pairs.append(f"{parts[5]}={parts[6]}")
    return "; ".join(pairs)


def fetch(url: str, cookie_header: str = "", timeout: int = 40) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru,uz;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
    })
    if cookie_header:
        req.add_header("Cookie", cookie_header)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        enc = (resp.headers.get("Content-Encoding") or "").lower()
        if enc == "gzip":
            raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
        elif enc == "deflate":
            raw = zlib.decompress(raw, -zlib.MAX_WBITS)
        charset = resp.headers.get_content_charset() or "utf-8"
    return raw.decode(charset, errors="replace")


def fetch_rendered(url: str, cookie_header: str = "", wait_ms: int = 3500) -> str:
    """JS-страницы через Playwright (Chromium уже стоит в окружении)."""
    from playwright.sync_api import sync_playwright  # импорт по требованию
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(user_agent=UA, locale="ru-RU")
        if cookie_header:
            host = urllib.parse.urlparse(url).hostname or ""
            ctx.add_cookies([
                {"name": n.strip(), "value": v.strip(), "domain": "." + host, "path": "/"}
                for n, _, v in (c.partition("=") for c in cookie_header.split(";")) if n.strip()
            ])
        page = ctx.new_page()
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(wait_ms)
        content = page.content()
        browser.close()
    return content


# ---------------------------------------------------------------- отчёты

def write_csv(rows: list[dict], path: str) -> None:
    cols = ["profile", "score", "title", "lot_no", "customer", "price",
            "deadline", "matched", "source", "url"]
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_markdown(rows: list[dict], path: str, profiles: dict, stats: dict) -> None:
    lines = ["# Тендеры по ключевым словам", ""]
    lines.append(f"Проверено страниц: **{stats['pages']}**, "
                 f"найдено лотов всего: **{stats['records']}**, "
                 f"подошло под профили: **{len(rows)}**")
    lines.append("")
    for name, prof in profiles.items():
        if name.startswith("_"):
            continue
        sub = [r for r in rows if r["profile"] == name]
        lines += [f"## {prof.get('title', name)}", ""]
        if not sub:
            lines += ["_Совпадений нет._", ""]
            continue
        lines.append("| Балл | Лот | Заказчик | Сумма | Срок | Сработало | Ссылка |")
        lines.append("|---:|---|---|---|---|---|---|")
        for r in sub:
            title = r["title"].replace("|", "/")[:150]
            lines.append(
                f"| {r['score']} | {title} | {r['customer'][:60]} | {r['price']} | "
                f"{r['deadline']} | {r['matched'][:60]} | [{r['source']}]({r['url']}) |")
        lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ---------------------------------------------------------------- main

def collect(pages_html: list[tuple[str, str, str]], profiles: dict,
            min_score: int, only_profile: str | None) -> tuple[list[dict], int]:
    rows, total = [], 0
    for source, url, page_html in pages_html:
        records = extract_records(page_html, url)
        total += len(records)
        for rec in records:
            matches = match_profiles(rec["text"], profiles)
            for m in matches:
                if only_profile and m["profile"] != only_profile:
                    continue
                if m["score"] < min_score:
                    continue
                fields = extract_fields(rec["text"])
                rows.append({
                    "profile": m["profile"],
                    "score": m["score"],
                    "title": rec["text"][:220],
                    "matched": ", ".join(m["strong"] + m["broad"]),
                    "source": source,
                    "url": rec["url"],
                    **fields,
                })
                break  # лот относим к самому релевантному профилю
    rows.sort(key=lambda r: (r["profile"], -r["score"]))
    return rows, total


def main() -> int:
    ap = argparse.ArgumentParser(description="Поиск тендеров по ключевым словам")
    ap.add_argument("--site", action="append", default=[],
                    help=f"площадка: {', '.join(SITES)} или all")
    ap.add_argument("--url", action="append", default=[], help="произвольный URL")
    ap.add_argument("--html-file", action="append", default=[],
                    help="сохранённый HTML (можно маску: '*.html')")
    ap.add_argument("--base-url", help="адрес сайта для сохранённых файлов, "
                                       "чтобы ссылки на лоты были рабочими")
    ap.add_argument("--pages", type=int, default=1, help="сколько страниц листать")
    ap.add_argument("--profile", help="искать только по одному профилю")
    ap.add_argument("--keywords", default=os.path.join(HERE, "keywords.json"))
    ap.add_argument("--min-score", type=int, default=3)
    ap.add_argument("--cookies-file", help="Netscape cookies.txt для закрытых площадок")
    ap.add_argument("--render", action="store_true", help="рендерить JS через Playwright")
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    ap.add_argument("--delay", type=float, default=1.0, help="пауза между запросами, сек")
    args = ap.parse_args()

    with open(args.keywords, encoding="utf-8") as fh:
        profiles = json.load(fh)
    if args.profile and args.profile not in profiles:
        print(f"Нет профиля '{args.profile}'. Есть: "
              f"{', '.join(k for k in profiles if not k.startswith('_'))}", file=sys.stderr)
        return 2

    targets: list[tuple[str, str]] = []
    for site in args.site:
        chosen = list(SITES) if site == "all" else [site]
        for name in chosen:
            if name not in SITES:
                print(f"Неизвестная площадка: {name}", file=sys.stderr)
                return 2
            cfg = SITES[name]
            targets.append((name, cfg["url"]))
            for n in range(2, args.pages + 1):
                suffix = cfg["page"].format(n=n)
                if "?" in cfg["url"]:
                    suffix = "&" + suffix.lstrip("?")
                targets.append((name, cfg["url"] + suffix))
    targets += [("custom", u) for u in args.url]

    cookie_header = load_cookies(args.cookies_file) if args.cookies_file else ""
    pages_html: list[tuple[str, str, str]] = []

    for pattern in args.html_file:
        matched = glob.glob(os.path.expanduser(pattern))
        if not matched:
            print(f"Файлы не найдены: {pattern}", file=sys.stderr)
        for path in matched:
            with open(path, encoding="utf-8", errors="replace") as fh:
                base = args.base_url or ("file://" + os.path.abspath(path))
                pages_html.append((os.path.basename(path), base, fh.read()))
            print(f"[файл] {path}")

    for source, url in targets:
        try:
            page = fetch_rendered(url, cookie_header) if args.render else fetch(url, cookie_header)
            pages_html.append((source, url, page))
            print(f"[ок]  {url}  ({len(page)} байт)")
        except urllib.error.HTTPError as exc:
            print(f"[{exc.code}] {url} — {exc.reason}", file=sys.stderr)
        except Exception as exc:
            print(f"[ошибка] {url} — {exc}", file=sys.stderr)
        time.sleep(args.delay)

    if not pages_html:
        print("Нечего разбирать: ни одна страница не загрузилась.", file=sys.stderr)
        return 1

    rows, total = collect(pages_html, profiles, args.min_score, args.profile)

    os.makedirs(args.out, exist_ok=True)
    csv_path = os.path.join(args.out, "tenders.csv")
    md_path = os.path.join(args.out, "tenders.md")
    write_csv(rows, csv_path)
    write_markdown(rows, md_path, profiles, {"pages": len(pages_html), "records": total})

    print(f"\nЛотов просмотрено: {total}   подошло: {len(rows)}")
    for name in (k for k in profiles if not k.startswith("_")):
        n = sum(1 for r in rows if r["profile"] == name)
        print(f"  {name:14s} {n}")
    for r in rows[:15]:
        print(f"\n[{r['profile']} {r['score']}] {r['title'][:110]}"
              f"\n    сумма: {r['price'] or '—'}   срок: {r['deadline'] or '—'}"
              f"\n    {r['url']}")
    print(f"\nОтчёты: {md_path}\n         {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
