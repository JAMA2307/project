#!/usr/bin/env python3
"""H05 geometry harness.

Method rule carried from H04: headless Chromium must run with
--font-render-hinting=none, otherwise text advances inflate non-linearly
around 24px and produce false wrap discrepancies.

Images are solid-colour stand-ins at the real intrinsic sizes. Card geometry
is driven by object-cover into a fixed box, so pixel content cannot affect
any measurement taken here.
"""
import json, os, sys, pathlib
from PIL import Image
from playwright.sync_api import sync_playwright

S = pathlib.Path(__file__).resolve().parent
REPO = S.parent
FONTDIR = REPO / "design-sources" / "fonts"

def stub(name, w, h, colour):
    p = S / name
    if not p.exists():
        Image.new("RGB", (w, h), colour).save(p)
    return p.as_uri()

def build(src_html, out_name):
    html = (S / src_html).read_text()
    html = html.replace("FONTDIR", FONTDIR.as_uri())
    html = html.replace("PH1", stub("ph1.png", 1086, 1448, (150, 140, 125)))
    html = html.replace("PH2", stub("ph2.png", 1086, 1448, (120, 130, 150)))
    html = html.replace("PH3", stub("ph3.png", 1086, 1448, (135, 145, 130)))
    html = html.replace("RING", stub("ring.png", 165, 205, (220, 232, 250)))
    html = html.replace("PLANE", stub("plane.png", 21, 21, (255, 255, 255)))
    out = S / out_name
    out.write_text(html)
    return out

PROBE = """() => {
  // Document coordinates, not viewport. hover() scrolls a tall mobile page, and
  // raw viewport rects then read as layout shifts that never happened.
  const r = el => { if(!el) return null; const b = el.getBoundingClientRect();
    return {x:+(b.x+scrollX).toFixed(2), y:+(b.y+scrollY).toFixed(2),
            w:+b.width.toFixed(2), h:+b.height.toFixed(2),
            ow: el.offsetWidth, oh: el.offsetHeight}; };
  const cs = el => { const c = getComputedStyle(el);
    return {fontSize:c.fontSize, lineHeight:c.lineHeight, fontWeight:c.fontWeight,
            letterSpacing:c.letterSpacing, fontFamily:c.fontFamily.split(',')[0], color:c.color}; };
  const intro = document.getElementById('intro');
  return {
    section: r(document.getElementById('wsua')),
    grid:    r(document.getElementById('grid')),
    card1:   r(document.getElementById('card1')),
    card2:   r(document.getElementById('card2')),
    card3:   r(document.getElementById('card3')),
    pills:   [...document.querySelectorAll('.pill')].map(r),
    intro:   {rect: r(intro), type: cs(intro), width: intro.getBoundingClientRect().width},
    doc:     {scrollWidth: document.documentElement.scrollWidth, innerWidth: window.innerWidth},
  };
}"""

def run(page_file, widths, label):
    results = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                                     args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        for w in widths:
            pg = browser.new_page(viewport={"width": w, "height": 1000}, device_scale_factor=1)
            errors = []
            pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.goto(page_file.as_uri())
            pg.wait_for_timeout(400)
            base = pg.evaluate(PROBE)
            # hover each card in turn
            hov = {}
            for cid in ("card1", "card2", "card3"):
                pg.hover(f"#{cid}")
                pg.wait_for_timeout(450)
                hov[cid] = pg.evaluate(PROBE)
                pg.mouse.move(2, 2)
                pg.wait_for_timeout(450)
            after = pg.evaluate(PROBE)
            results[w] = {"base": base, "hover": hov, "after_return": after, "console_errors": errors}
            pg.close()
        browser.close()
    (S / f"measured_{label}.json").write_text(json.dumps(results, indent=1))
    return results

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "wsua-harness.html"
    label = sys.argv[2] if len(sys.argv) > 2 else "baseline"
    page = build(src, f"built_{label}.html")
    res = run(page, [1440, 393], label)

    for w, d in res.items():
        b, a = d["base"], d["after_return"]
        print(f"\n===== {w}px =====")
        print(f"section h={b['section']['h']}  grid w={b['grid']['w']}")
        for c in ("card1", "card2", "card3"):
            print(f"  {c}: {b[c]['ow']}x{b[c]['oh']}  x={b[c]['x']} y={b[c]['y']}")
        print(f"intro: {b['intro']['type']['fontSize']} / {b['intro']['type']['lineHeight']} "
              f"w={b['intro']['type']['fontWeight']} ls={b['intro']['type']['letterSpacing']} "
              f"box={round(b['intro']['width'])}")
        print(f"overflow: scrollWidth={b['doc']['scrollWidth']} innerWidth={b['doc']['innerWidth']}")
        # invariance under hover
        for hovered, hd in d["hover"].items():
            deltas = []
            for c in ("card1", "card2", "card3"):
                if hd[c]["ow"] != b[c]["ow"] or hd[c]["oh"] != b[c]["oh"]:
                    deltas.append(f"{c} SIZE {b[c]['ow']}x{b[c]['oh']}->{hd[c]['ow']}x{hd[c]['oh']}")
                if c != hovered and (hd[c]["x"] != b[c]["x"] or hd[c]["y"] != b[c]["y"]):
                    deltas.append(f"{c} MOVED {b[c]['x']},{b[c]['y']}->{hd[c]['x']},{hd[c]['y']}")
            if hd["section"]["h"] != b["section"]["h"]:
                deltas.append(f"section h {b['section']['h']}->{hd['section']['h']}")
            dy = round(hd[hovered]["y"] - b[hovered]["y"], 2)
            print(f"  hover {hovered}: hovered dy={dy}  " + ("OK" if not deltas else "!! " + "; ".join(deltas)))
        ret = all(a[c] == b[c] for c in ("card1", "card2", "card3")) and a["section"]["h"] == b["section"]["h"]
        print(f"return-to-default identical: {ret}")
        print(f"console errors: {d['console_errors'] or 'none'}")
