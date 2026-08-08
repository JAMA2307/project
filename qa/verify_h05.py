#!/usr/bin/env python3
"""H05 verification — default / hover / focus / return, at 1440 and 393.

Three things this script exists to avoid getting wrong:

1. Headless Chromium reports `hover:hover, pointer:fine` at EVERY viewport width.
   Measuring 393 in a plain context therefore exercises the DESKTOP branch and
   would falsely confirm "mobile is static". The 393 pass runs with touch
   emulation and asserts the media features actually flipped.
2. hover() scrolls a tall page, so all rects are taken in DOCUMENT coordinates.
   Viewport rects read scroll offset as layout shift (see manifest §28.1).
3. --font-render-hinting=none, per the H04 method rule.
"""
import json, sys, pathlib
from PIL import Image
from playwright.sync_api import sync_playwright

S = pathlib.Path(__file__).resolve().parent
FONTDIR = S.parent / "design-sources" / "fonts"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def stub(name, w, h, colour):
    p = S / name
    if not p.exists():
        Image.new("RGB", (w, h), colour).save(p)
    return p.as_uri()


def build():
    html = (S / "wsua-harness.html").read_text().replace("FONTDIR", FONTDIR.as_uri())
    for k, (w, h, c) in {"PH1": (1086, 1448, (150, 140, 125)),
                         "PH2": (1086, 1448, (120, 130, 150)),
                         "PH3": (1086, 1448, (135, 145, 130)),
                         "RING": (165, 205, (220, 232, 250)),
                         "PLANE": (21, 21, (255, 255, 255))}.items():
        html = html.replace(k, stub(k.lower() + ".png", w, h, c))
    out = S / "built_h05.html"
    out.write_text(html)
    return out


PROBE = """() => {
  const r = el => { const b = el.getBoundingClientRect();
    return {x:+(b.x+scrollX).toFixed(2), y:+(b.y+scrollY).toFixed(2),
            w:+b.width.toFixed(2), h:+b.height.toFixed(2), ow:el.offsetWidth, oh:el.offsetHeight}; };
  const intro = document.getElementById('intro');
  const ic = getComputedStyle(intro);
  const layer = i => { const el = document.querySelectorAll('[data-info-layer]')[i];
    const c = getComputedStyle(el);
    return {opacity:+(+c.opacity).toFixed(3), dur:c.transitionDuration,
            display:c.display, visibility:c.visibility}; };
  return {
    media: {hover: matchMedia('(hover: hover)').matches,
            fine:  matchMedia('(pointer: fine)').matches,
            coarse:matchMedia('(pointer: coarse)').matches,
            rm:    matchMedia('(prefers-reduced-motion: reduce)').matches},
    section: r(document.getElementById('wsua')),
    cards: [0,1,2].map(i => r(document.getElementById('card'+(i+1)))),
    layers: [0,1,2].map(layer),
    intro: {fontSize: ic.fontSize, lineHeight: ic.lineHeight, fontWeight: ic.fontWeight,
            letterSpacing: ic.letterSpacing, color: ic.color,
            box: +intro.getBoundingClientRect().width.toFixed(1)},
    doc: {sw: document.documentElement.scrollWidth, iw: window.innerWidth},
  };
}"""


def pass_(page, label, width, touch, reduced):
    out = {"label": label}
    errs = []
    page.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: errs.append(str(e)))
    page.goto(build().as_uri())
    page.wait_for_timeout(400)
    out["base"] = page.evaluate(PROBE)
    out["states"] = {}
    for i, cid in enumerate(("card1", "card2", "card3")):
        if not touch:
            page.hover(f"#{cid}")
            page.wait_for_timeout(500)
            out["states"][f"hover_{cid}"] = page.evaluate(PROBE)
            page.mouse.move(2, 2)
            page.wait_for_timeout(500)
            page.eval_on_selector(f"#{cid}", "el => el.focus()")
            page.wait_for_timeout(500)
            out["states"][f"focus_{cid}"] = page.evaluate(PROBE)
            page.eval_on_selector(f"#{cid}", "el => el.blur()")
            page.wait_for_timeout(500)
    out["after"] = page.evaluate(PROBE)
    out["errors"] = errs
    return out


def run():
    results = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME,
                               args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        for label, width, touch, reduced in [
                ("desktop-1440", 1440, False, False),
                ("touch-393", 393, True, False),
                ("desktop-1440-reduced", 1440, False, True)]:
            ctx = b.new_context(viewport={"width": width, "height": 1000}, device_scale_factor=1,
                                has_touch=touch, is_mobile=touch,
                                reduced_motion="reduce" if reduced else "no-preference")
            pg = ctx.new_page()
            results.append(pass_(pg, label, width, touch, reduced))
            ctx.close()
        b.close()
    (S / "measured_h05.json").write_text(json.dumps(results, indent=1))
    return results


BASE = {"1440": {"card": (413, 460), "section": 900.0, "fs": "23.9998px", "lh": "31.9998px", "box": 774.0},
        "393":  {"card": (361, 470), "fs": "16px", "lh": "20.0002px", "box": 361.0}}

if __name__ == "__main__":
    ok = True
    for p in run():
        b = p["base"]
        m = b["media"]
        print(f"\n===== {p['label']} =====")
        print(f"media: hover={m['hover']} fine={m['fine']} coarse={m['coarse']} reduced-motion={m['rm']}")
        print(f"section h={b['section']['h']}  cards=" +
              " ".join(f"{c['ow']}x{c['oh']}" for c in b["cards"]))
        print(f"intro: {b['intro']['fontSize']} / {b['intro']['lineHeight']} "
              f"w={b['intro']['fontWeight']} ls={b['intro']['letterSpacing']} "
              f"{b['intro']['color']} box={b['intro']['box']}")
        print(f"default info-layer opacity: {[l['opacity'] for l in b['layers']]}  "
              f"dur={[l['dur'] for l in b['layers']][0]}  display={[l['display'] for l in b['layers']][0]}")
        print(f"overflow: scrollWidth={b['doc']['sw']} innerWidth={b['doc']['iw']}"
              + ("  OK" if b["doc"]["sw"] <= b["doc"]["iw"] else "  !! OVERFLOW"))

        for name, st in p["states"].items():
            idx = int(name[-1]) - 1
            deltas = []
            for j in range(3):
                if st["cards"][j]["ow"] != b["cards"][j]["ow"] or st["cards"][j]["oh"] != b["cards"][j]["oh"]:
                    deltas.append(f"card{j+1} SIZE")
                if j != idx and (st["cards"][j]["x"] != b["cards"][j]["x"]
                                 or st["cards"][j]["y"] != b["cards"][j]["y"]):
                    deltas.append(f"card{j+1} MOVED")
            if st["section"]["h"] != b["section"]["h"]:
                deltas.append(f"section {b['section']['h']}->{st['section']['h']}")
            if st["intro"]["fontSize"] != b["intro"]["fontSize"]:
                deltas.append("INTRO TYPE MOVED")
            dy = round(st["cards"][idx]["y"] - b["cards"][idx]["y"], 2)
            print(f"  {name}: dy={dy} opacity={[l['opacity'] for l in st['layers']]}  "
                  + ("OK" if not deltas else "!! " + "; ".join(deltas)))
            if deltas:
                ok = False

        same = all(p["after"]["cards"][j] == b["cards"][j] for j in range(3)) \
            and p["after"]["section"]["h"] == b["section"]["h"] \
            and [l["opacity"] for l in p["after"]["layers"]] == [l["opacity"] for l in b["layers"]]
        print(f"  return-to-default identical: {same}")
        if not same:
            ok = False
        print(f"  console errors: {p['errors'] or 'none'}")
    print("\n==== " + ("ALL GEOMETRY INVARIANTS HELD" if ok else "FAILURES PRESENT") + " ====")
