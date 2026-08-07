
---

## 9 · REBASE ON THE OFFICIAL FIGMA RASTERS · 2026-08-07

18 full-page exports ingested — see `FIGMA_RASTER_REFERENCE_MANIFEST.md` for the full manifest, canonical viewports, gutter derivation and sampled colours. Frames are **1:1**, desktop **1440**, mobile **393**, so every target below is a direct pixel read.

### 9.1 · Two of our own conclusions reversed

| Item | We said | The raster says | Action |
|---|---|---|---|
| **HOME-16** | Blocked — "the row needs 398.6px against 323 available; shorten the labels" | Buttons **are** side by side with the **approved labels**. The design uses a 16px label and 22px padding, not our 18px/28px | **Withdrawn** — correction posted `1217266686280914` |
| **HOME-17** | Blocked — "the panel would cover 74% of the photo" | Our **option (c)** was right: the mobile photo is **361 × 428**, not 3:2. The panel covers **29%** | **Withdrawn** — correction posted `1217270152922439` |

Both blocks were sound reasoning against the *shipped* styling and wrong about *design intent*. The questions were well-posed — HOME-17's answer was one of the four options we offered — but a block is still a block, and the corrections say plainly that we were wrong rather than reframing it.

### 9.2 · Measured targets now held

**HOME-16 · hero CTA row**

| | Mobile 393 | Desktop 1440 |
|---|---|---|
| Dark button | x 16, **w 188** | x 516, **w 222** |
| Light button | x 220, **w 157** | x 754, **w 170** |
| Gap | 16 | 16 |
| Height | 44 | 46 |
| Label ink (Explore / Plan) | 144 / 98 | 164 / 112 |
| H-padding | **22** | **28** (= shipped `px-7`) |

Row closes exactly: `16 + 188 + 16 + 157 + 16 = 393`.

**HOME-17 · hero photo and badge**

| | Mobile 393 | Desktop 1440 |
|---|---|---|
| Photo | 361 × **428** (w/h 0.8435) | 1280 × 720 (**16:9**) |
| Badge | 273 × 126 | 345 × 160 |
| Badge anchor | bottom-**left**, insets 16 / 16 | bottom-**right**, insets 24 / 24 |
| Badge fill | **#E6F0FF**, opaque | same |

**Desktop needs no change** — 1280×720 and 345×160 at 24px insets is what we already ship. The entire ticket is mobile.

The site ships `aspect-[3/2]` on mobile (1.5) against the design's 0.8435. That single wrong aspect is what made the overlay look impossible.

### 9.3 · DEF-01 resolved, and our own proposed fix corrected

Design endpoints measured as **16 @ 393 → 80 @ 1440**, giving `clamp(1rem, -0.5014rem + 6.1127vw, 5rem)`.

We had earlier proposed −0.4857rem, derived from a **390** mobile endpoint. The design's endpoint is **393**. Our number was wrong. Shipped is `+0.6095rem` → 33.5px at 390 against a 16px target.

Per the agency's instruction this is a **global atomic task**: measure, change once, verify every route at every breakpoint, then close. It must not be allowed to mask HOME-02's separate *vertical* hero-spacing complaint.

### 9.4 · Canonical mobile is 393, not 390

Every fluid `clamp()` in this codebase interpolates from **390**. The design's mobile frame is **393**. Every fluid value is anchored 3px off its own design endpoint. Recorded here because it affects the type scale as well as the gutter.
