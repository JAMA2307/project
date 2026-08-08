# H05 — LOVABLE DISPATCH PROMPT

Status: **DISPATCHED 2026-08-08.** The §27.6 copy block was cleared by the client, who
recovered both paragraphs from the Figma comments. No slots remain pending.

---

TASK: H05 · Asana HOME-06 (`1217108334767508`) — the ticket the agency re-reported on
2026-08-06 with *"these animations aren't here"*.

PAGE: Home
SECTION: What Sets Us Apart

## CURRENT DEFECT

`src/components/home/WhatSetsUsApart.tsx` renders three cards in a fixed state:

- card 1 "Inviting spaces" — photo only, no informational state
- card 2 "Guided care" — informational panel **permanently**, and it has no photo at all
- card 3 "Connected support" — photo only, no informational state

`hover-card` in `src/styles.css` resolves to `translateY(-2px)` plus a shadow and nothing
else. **No photo→informational transition exists anywhere in the component.**

## TARGET

Every card defaults to its **photo** state and transforms into the **informational** state
on hover and on keyboard focus. The informational state is not a new design — it is exactly
the treatment card 2 already ships: `bg-secondary-bg` panel, descriptive paragraph at the
top, the large Amara ring/monogram watermark with the plane glyph pinned off its lower
right, and the same white pill.

## FILES YOU MAY CHANGE

`src/components/home/WhatSetsUsApart.tsx` — **this file only.**
Do not edit `src/styles.css`. Reuse `--ease-premium` and `--dur-hover`; do not add tokens.

## IMPLEMENTATION

Give each `<article>` two absolutely-positioned layers inside the existing box:

- **photo layer** — `absolute inset-0`, the `<img>` with `object-cover`
- **info layer** — `absolute inset-0`, `bg-secondary-bg`, `p-6`, paragraph + ring + plane

Cross-fade the info layer in on `group-hover` / `group-focus-within`. The pill stays a
single shared element outside both layers so it never fades or moves.

Because both layers are `absolute inset-0` inside a fixed-height article, **nothing in
normal flow changes**, so no neighbour can move and the grid cannot reflow. Keep
`h-[470px] lg:h-[460px]`, `rounded-card`, `overflow-hidden`, `gap-5` and the existing
`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` exactly as they are.

**Gate the transformation on `@media (hover: hover) and (pointer: fine)`** — not on a
width breakpoint. Touch devices must never enter the hover state. Below that gate, render
the approved static presentation: cards 1 and 3 photo-only, **card 2 informational**,
which is what the 393 Figma frame shows today.

Keyboard: put `tabIndex={0}` on each article so the informational state is reachable
without a mouse, revealed via `focus-within`/`focus-visible`. The paragraph must stay in
the DOM and readable by assistive tech in both states — never `display:none`, never
`aria-hidden` — so the content is not mouse-exclusive.

Motion: opacity cross-fade at `--dur-hover` (260ms) on `--ease-premium`, with at most a
4px upward settle on the paragraph. No bounce, no zoom, no rotation, no scale on the card,
no movement of the grid or the section.

## ASSETS — all already in the project

| slot | asset |
|---|---|
| card 1 photo | `@/assets/photos/wsua-inviting-spaces.png.asset.json` (unchanged) |
| card 3 photo | `@/assets/photos/wsua-connected-support.png.asset.json` (unchanged) |
| **card 2 photo (new)** | `@/assets/photos/about-values-1-personalized-support.png.asset.json` |
| watermark | `@/assets/brand/guided-care-ring-official.png` (unchanged) |
| plane glyph | `@/assets/brand/glyph-plane-official.png` (unchanged) |

Do not fetch, generate or substitute any other image. The card 2 photo is an official
Figma export, chosen under the agency's explicit instruction to *"take another one from
the same Figma, similar in theme"* — it shows a nurse walking a resident who is using a
walker, which is literally guided care. Give it accurate `alt` text describing that.

## COPY — use verbatim, do not rewrite

- card 1 · Inviting spaces — "Our newly renovated setting is designed to feel comfortable
  and easy to navigate, helping residents feel more at ease each day."
- card 2 · Guided care — "We take the time to understand each resident, creating care
  plans that reflect their individual needs and preferences." *(unchanged, already approved)*
- card 3 · Connected support — "Our team works together to provide coordinated care, with
  access to on-site therapy and ongoing medical oversight."

Recovered from the Figma comments by the client, 2026-08-08. Verbatim — no paraphrase, no
shortening, no rewrite, no smart-quote or punctuation substitution.

Pill labels stay exactly "Inviting spaces", "Guided care", "Connected support". Card 1 and
card 3 keep their `ArrowUpRight`; card 2 keeps none. Do not add or remove an arrow.

## DO NOT CHANGE

- The H04 intro paragraph — `font-sans font-normal`, the two `clamp()` values,
  `max-w-[774px]`, `[&]:text-primary`. It computes to **24px/32px, weight 400,
  letter-spacing normal, box 774** at 1440 and **16px/20px, box 361** at 393. Those are
  verified values; if any of them moves, the turn has failed. Do not restore
  `text-body-large`.
- The copy reads **"on community"** with a space. The Figma raster's "oncommunity" is a
  known artefact. Do not reproduce it.
- Section padding and `min-h-[900px]`, the eyebrow, the grid gap, card dimensions,
  the Home hero, the Services section, the mobile layout.

## DESKTOP ACCEPTANCE (1440)

- card `offsetWidth`/`offsetHeight` identical before and during hover — **413×460**
- neighbouring card document rects identical during any hover
- section height identical during any hover — **900**
- correct paragraph, watermark and plane glyph in each informational state
- transition fires on hover **and** on keyboard focus
- pointer-out returns the card cleanly to the photo state
- `document.scrollWidth <= window.innerWidth`
- no console or runtime errors

## MOBILE ACCEPTANCE (393)

- matches the approved 393 frame: photo / informational / photo, stacked
- cards 361×470, no hover or tap-to-reveal state reachable
- no overflow

## REDUCED MOTION

Under `prefers-reduced-motion: reduce` the state change is immediate. The existing global
block already forces `transition-duration: .001ms`; confirm nothing you add escapes it.

## REPORT BACK

Report in the project's standard format, and state the measured card box, the measured
section height during hover, and the computed intro font-size/line-height at both widths.
Do not report success without those numbers.
