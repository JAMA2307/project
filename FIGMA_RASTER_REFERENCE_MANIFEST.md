# FIGMA RASTER REFERENCE MANIFEST — Amara

| | |
|---|---|
| Ingested | 2026-08-07 |
| Source | Two agency RAR archives (`87deac69-2.rar`, `fe79fe6b-1.rar`) |
| Location | `design-sources/figma-reference/` — **original filenames preserved** |
| Design file | *Amara x Mozart* — `https://www.figma.com/design/Tm96OSYcEv6kdVzIqHYKeP/Amara-x-Mozart` |
| Status of Figma MCP | authenticates, but rate-limited — **these rasters are the visual source of truth** |
| Extraction | `unrar-free` · all 18 files non-zero · `All OK` on both archives |

Filenames are kept exactly as delivered so that any reference the agency makes resolves without translation.

---

## 1 · THE 18 FILES, AND WHAT EACH ACTUALLY IS

**All frames are 1:1.** Desktop frames are exactly **1440** wide; mobile frames are exactly **393** wide. There is no downscale, so **one raster pixel = one CSS pixel**. Every measurement below is a direct read, not a derived estimate.

| File | W × H | Canonical viewport | Notes |
|---|---|---|---|
| `Home Page _ Desktop.png` | 1440 × 7858 | **desktop 1440** | |
| `Home Page _ Desktop (1).png` | 393 × 10456 | **MOBILE 393** | ⚠️ misnamed — is mobile |
| `About Page _ Desktop.png` | 1440 × 6680 | desktop 1440 | |
| `About Page _ Mobile.png` | 393 × 8170 | mobile 393 | |
| `Services Page _ Desktop.png` | 1440 × 5748 | desktop 1440 | |
| `Services Page _ Mobile.png` | 393 × 8032 | mobile 393 | |
| `Amenities Page _ Desktop.png` | 1440 × 4392 | desktop 1440 | |
| `Amenities Page _ Desktop (1).png` | 393 × 5573 | **MOBILE 393** | ⚠️ misnamed — is mobile |
| `Careers Page _ Desktop.png` | 1440 × 6218 | desktop 1440 | |
| `Careers Page _ Mobile.png` | 393 × 7268 | mobile 393 | |
| `Contact Page _ Desktop.png` | 1440 × 4022 | desktop 1440 | |
| `Contact Page _ Mobile.png` | 393 × 4529 | mobile 393 | |
| `Privacy Policy _ Desktop.png` | 1440 × 2894 | desktop 1440 | unblocks AUX legal copy |
| `Privacy Policy _ Mobile.png` | 393 × 4018 | mobile 393 | |
| `Terms of Use _ Desktop.png` | 1440 × 2990 | desktop 1440 | unblocks AUX legal copy |
| `Terms of Use _ Mobile.png` | 393 × 3966 | mobile 393 | |
| `404 Error Page _ Desktop.png` | 1440 × **900** | desktop 1440 | exactly one viewport tall |
| `404 Error Page _ Mobile.png` | 393 × **852** | mobile 393 | exactly one viewport tall |

**The agency's filename correction is independently confirmed by the data** — both `(1)` files measure 393 wide. We did not take it on trust.

---

## 2 · THE SINGLE MOST IMPORTANT FINDING — CANONICAL MOBILE IS 393, NOT 390

Every mobile frame is **393px** wide. That is the iPhone 15 / 14 Pro logical width.

The entire responsive system in this codebase interpolates its fluid values **from 390**. Every `clamp()` endpoint, every fluid type step and the page gutter curve are anchored 3px away from the design's actual mobile frame. Small, but it means no fluid value can land exactly on its design target at the design's own mobile width.

**All target measurements in this manifest are stated at 393.**

---

## 3 · PAGE GUTTER — MEASURED, AND IT SETTLES DEF-01

| Viewport | Measured gutter | Evidence |
|---|---|---|
| **1440 desktop** | **80** | Header logo left edge = 80 on Contact, Privacy, Terms, Services, Amenities, Home. Hero photo spans x 80…1360 = 1280 wide. |
| **393 mobile** | **16** | Home mobile CTA row: left inset **16**, right inset **16**, and `16 + 188 + 16 + 157 + 16 = 393` exactly. A filled button edge is a hard geometric boundary — far more reliable than logo ink, which reads 17–19 because the mark's circle is inset within its box. |

### VERIFIED: two endpoints only

| | Value | Status |
|---|---|---|
| Gutter @ 393 | **16** | **verified** — hard button edge, `16+188+16+157+16 = 393` |
| Gutter @ 1440 | **80** | **verified** — logo left edge on 6 pages; hero photo x 80…1360 |
| Everything between | — | **NOT verified** |

### HYPOTHESIS: the curve between them

Only two frame widths were supplied — 393 and 1440. **No tablet frame exists**, and no Asana screenshot establishes an intermediate gutter. So the behaviour between the endpoints is a *choice*, not a measurement, and must not be presented as one.

A straight line through the two verified endpoints gives:

```
slope     = (80 − 16) / (1440 − 393) = 0.0611270  →  6.1127vw
intercept = 16 − 0.0611270 × 393     = −8.023px   →  −0.5014rem

padding-inline: clamp(1rem, -0.5014rem + 6.1127vw, 5rem)
```

It satisfies both endpoints exactly (393 → 16.00, 1440 → 80.00) and matches the fluid-interpolation convention already used throughout this codebase, so it is the least invasive option. **That is the argument for it — not evidence.** A stepped curve at existing breakpoints would satisfy the same two endpoints equally well.

Before changing the token: confirm the codebase's existing breakpoint conventions, pick the simplest behaviour consistent with the two verified endpoints, and **verify intermediate widths for regressions** — R1–R7 were tuned against today's too-wide gutters, so 768 and 1024 are where breakage would appear.

### Correction to our own earlier proposal

We previously derived this from a **390** mobile endpoint (−0.4857rem). The verified design endpoint is **393** (−0.5014rem). The shipped `+0.6095rem` renders **33.5px at 390** against a 16px target — wrong in the other direction and by far more.

**Per the agency's instruction this is a global atomic task** — measure, change once, verify every page at every breakpoint, then close the Asana spacing task. It must not be used to mask section-specific spacing defects.

---

## 4 · COLOUR TOKENS — SAMPLED, NOT EYEBALLED

Sampled from flat interior regions of the rasters. **Every value the brief called "approximate" samples exact.**

| Token | Sampled | Where sampled | Brief said |
|---|---|---|---|
| Primary / footer navy | **#2C2E45** | Home desktop CTA button fill | #2C2E45 ✓ |
| Shared CTA slate panel | **#56677F** | About desktop, y 5360–6010 | ~#56677F ✓ |
| 404 background | **#8CA1C1** | 404 desktop *and* mobile — identical | ~#8CA1C1 ✓ |
| Light blue surface | **#E6F0FF** | Home hero, desktop *and* mobile — identical | ~#E6F0FF ✓ |

**#56677F resolves ABOUT-05 / ADM-05.** The shared `sections/Cta.tsx` currently paints the panel `bg-primary` = #2C2E45. The design is #56677F. One shared component, three routes.

---

## 5 · HOME HERO CTA ROW — FULL GEOMETRY (settles HOME-16)

The mobile frame shows the two buttons **side by side, on one row, with the full approved labels**. Our pre-raster conclusion that they could not fit was correct *about the current button styling* and wrong about the design's intent — the design uses a smaller label and tighter padding than the site ships.

### Measured

| | Mobile @ 393 | Desktop @ 1440 |
|---|---|---|
| Row content width | 361 (= 393 − 2×16) | 1280 |
| "Explore Our Services" button | x 16 → 203, **w 188** | x 516 → 737, **w 222** |
| "Plan Your Visit" button | x 220 → 376, **w 157** | x 754 → 923, **w 170** |
| Gap | **16** | **16** |
| Button height | **44** | **46** |
| Label ink — Explore | **144** | **164** |
| Label ink — Plan | **98** | **112** |
| Horizontal padding | **22** | **28** (= the shipped `px-7`) |

### VERIFIED vs HYPOTHESIS

**Verified** — external geometry, read directly off a 1:1 raster: button boxes, gap, height, label *ink* extents, and that the row closes at exactly 393.

**Hypothesis — the label is 16px.** Reasoning: the ratio Explore ÷ Plan is 1.469 (Figma mobile), 1.464 (Figma desktop) and 1.466 (live site). Scaling 18px by the measured ratio gives 16.35 and 16.32 from the two labels independently, and the design system's own `text-button` token resolves to **16.0px at 393**.

**This does not prove anything about the typeface.** A width ratio is invariant under uniform scaling, so it is *consistent with* the same family, weight and tracking at a smaller size — but it is equally consistent with a different family whose relative advance widths happen to be similar. Raster text width is also affected by **weight**, **letter-spacing** and **antialiasing**, none of which the ratio isolates. Our earlier claim that matching ratios "prove the typeface is identical" was overstated and is withdrawn.

**How it gets settled — in the browser, not by arithmetic.** Render the two labels at 393 at each plausible design-system candidate (the `text-button` token at 16px, plus 16/17/18px at the shipped weight and tracking), screenshot, and measure the *ink* extents the same way the Figma ink was measured — so the comparison is like-for-like rather than layout-box vs ink. Target: **144** and **98**. Prefer a real token over a derived decimal; 16.3px is a calculation artefact and must not be shipped as a literal.

### Construction is NOT inferred from the raster

A raster proves external geometry and colour. It does not reveal CSS. We previously argued that one flex model "fits exactly" and therefore was the construction — that reasoning is withdrawn. Several constructions reproduce the same pixels, and picking one because it reproduces a screenshot is not evidence.

The deliverable is the **target geometry** above. The implementation should be the simplest construction that reproduces it at 393 and stays robust across widths — chosen on engineering merit, then verified by measurement.

Below 393 the design says nothing. The row must not overflow at 320, so it wraps below the width where both buttons still fit. That is an extrapolation, confined to widths the design never specifies.

## 6 · WHAT THE RASTERS RESOLVE

| Was blocked on | Now |
|---|---|
| HOME-16 CTAs side by side | **Resolved** — full geometry in §5 |
| HOME-17 badge inside the photo | **Resolved** — compact overlay, bottom-**left** on mobile, bottom-**right** on desktop |
| HOME-02 page margins | **Resolved horizontally** (§3); the vertical hero rhythm it also annotates is separate |
| ABOUT-05 / ADM-05 CTA colour | **Resolved** — #56677F |
| AUX legal copy | **Resolved** — approved copy is in the Privacy and Terms rasters |
| 404 rebuild | **Resolved** — #8CA1C1, full layout, both viewports |
| ABOUT-13 "no cards" | **Resolved** — items stay cards; the dark circular icon badges are absent from the approved mobile frame |
| SERV-06 alignment | **Resolved** — left-aligned, neither right nor centred |

### Still genuinely unresolved — do not guess

1. **ADM-04 Admissions vs Amenities.** The raster deepens rather than settles it: route `/amenities`, page designed as Amenities, hero "Life at Amara Care Center", CTA "Explore Amara Amenities" — **but the Figma navigation itself still reads "Admissions."** The design contains the very mismatch the ticket reports. Needs an agency decision.
2. Form success/failure body copy hidden under the red 1 / 2 annotations.
3. Whether a failed submission preserves entered values.
4. Whether a separate loading state is wanted.
5. Header background treatment when the revealed transparent header crosses light/dark content.
6. Testimonial identity where author and date duplicate — no person may be invented.
7. Poppins licensing/source.

---

## 8 · MEASUREMENT DISCIPLINE — what counts as evidence

Added after three of our conclusions were correctly challenged as over-stated.

### 8.1 · A detector result is not evidence until its bounds match the visible component

Our first pass at the HOME-17 badge returned **x 16…376, w 361** — the full photo width. That was discarded as soon as it contradicted the visual, but it should never have been produced as a candidate at all.

**Root cause:** the badge fill is **#E6F0FF**, byte-identical to the page background. Every "is this pixel background?" test therefore classifies the badge as background. Colour thresholding alone cannot find this element — the element and the negative space are the same colour.

**The verification that settles it** — a detected rectangle is only accepted once it survives all of:

1. High-magnification crop, edges identified visually first.
2. Multiple horizontal scanlines, including rows that pass *between* text lines where the fill is uninterrupted — y 715 and 730 both give a single clean run **32…304**.
3. Multiple vertical scanlines clear of interior content — x 36 and 300 both give **671…794**.
4. Probe-anchored runs (the run *containing* a known interior point) rather than first-contiguous-run, which stops at the first unrelated feature. This is what made columns 40–280 report the photo ending at 669: they pass through the badge.
5. Columns chosen to avoid the occluding element — x 330 and 350 sit right of the badge and give the true photo extent **384…811**.
6. Cross-check against the other frame: badge 273/345 = 0.791 wide, 126/160 = 0.788 tall. Consistent scaling between mobile and desktop.

Result: photo **361 × 428**, badge **273 × 126**, insets left 16 / bottom 16. Confirmed — and now actually proven.

### 8.2 · What a raster can and cannot establish

| Can establish | Cannot establish |
|---|---|
| External geometry — x, y, w, h, gaps, insets, radius | CSS construction — flex vs grid, which element grows |
| Flat-area colour, sampled | Padding strategy, or which value is a token vs literal |
| Relative proportion between frames | Font family, weight or letter-spacing from width alone |
| Presence, absence and stacking order of elements | Behaviour between the supplied frame widths |

Two frames give two points. Everything between them is a choice to be argued for and then verified, never a measurement to be asserted.

### 8.3 · Standing rule

**Measure target geometry first. Then choose the simplest robust implementation that reproduces it across responsive widths.** Never run the inference backwards — from a construction that happens to reproduce a screenshot, to a claim about how the design is built.

---

## 9 · ABOUT PAGE — REBASE FINDINGS

### 9.1 · ABOUT-13 — the removal is MOBILE-ONLY

The brief instructed: *"REMOVE the dark circular icon badges. DO NOT remove the value cards themselves."* Measuring both frames adds a scope qualifier the brief did not state:

| Frame | Dark circular icon badge |
|---|---|
| **About mobile 393** | **ABSENT** — verified at full resolution on the "Personalized Support" card |
| **About desktop 1440** | **PRESENT** — clearly visible top-left on the "Comfort & Wellbeing" card |

Applying the removal globally would break the desktop design. **The badge is removed at mobile widths and retained on desktop.**

### 9.2 · Measured mobile value card

| | Value |
|---|---|
| Card | x 16…376, **w 361** — full content width, gutter **16** (third independent confirmation) |
| Card padding | **24** — equals the existing `p-6` token, no new value |
| Photo | **313** wide, inset 24 left/right, 24 from card top |
| Order | photo → heading → body. No icon badge anywhere in the card |
| Card background | alternates white / pale blue between cards |

A first pass returned card x 20…372 (w 353). That was wrong — the tolerance test clipped the antialiased card edge. A luminance threshold gives x 16…376 at **every** row sampled. Recorded because it is the same failure mode as §8.1: a detector result is not evidence until it is stable across scanlines.

### 9.3 · ABOUT-08 — our earlier reading of the photo was wrong

From the 849 × 302 thumbnail we recorded *"photo flush to the card's right/top/bottom edges."* The full-resolution desktop frame shows the photo is **inset with card padding on all sides**, not flush.

The block on ABOUT-08 was therefore correct on the merits — the thumbnail produced a wrong structural reading, exactly as argued. With the full-resolution frame now in hand, ABOUT-08 becomes measurable and can be unblocked once its card geometry is measured.

### 9.4 · ABOUT-12 — mission copy confirmed

Mobile frame shows: small centred ring mark, "Our Mission" heading, then **small, centred, sans-serif** supporting copy with generous whitespace before "What We Value". The site renders `font-serif text-[26px] leading-[36px]` — a large serif. The ticket's complaint is confirmed against the design.

Only one of the two animated states appears in a static export, so the reveal sequence itself is not determinable from the raster.

### 9.5 · Possible token discrepancy — `--blue-50`

The About values section background samples **#F4F8FF** (244, 248, 255), consistently. Our token `--blue-50` is **#F2F7FF** (242, 247, 255) — 2 units off on two channels. The agency brief independently cited "very light section surface: approximately #F4F8FF."

Flagged, **not changed**: a 2-unit difference is at the edge of PNG colour-management error, and this token is used across several sections. Needs sampling on more pages before any change.

---

## 10 · SERVICES PAGE — REBASE FINDINGS

### 10.1 · Resolved from the rasters

| Ticket | Resolution |
|---|---|
| **SERV-06** alignment | **Left-aligned.** The "services overview" eyebrow, heading and body are flush left in the mobile frame. Settles the ticket's *"справа"* (right) wording, which contradicted its own arrow. |
| **SERV-04** Indian Program | **Bulleted list, same as the others.** All four mobile cards use `•` bullets — Short-Term Rehabilitation, Long-Term Care, Indian Program, Comprehensive Clinical Support. No chips anywhere. |
| Services mobile hero order | Header → title → supporting copy → "Explore Our Services" → hero image → **"Scroll to Explore" centred below the image**. Confirms the brief. |
| Mobile "Our Services" | **Four cards stacked**, each photo → serif heading → body → bullets. |
| Mobile CTA placement | **No "Plan Your Visit" button between the last service card and Testimonials.** The section ends at the fourth card. |
| Shared CTA mobile | Slate panel **above**, lifestyle image **below**, panel visibly **shorter** than the image. Confirms ABOUT-14 / ADM-08. |

### 10.2 · Second deliberate divergence from Figma — the FAQ

The Services mobile frame shows FAQ item **2 open** on load. HOME-12 asked for the accordion collapsed on mount, and we implemented that.

This is the same pattern as HOME-15: **Figma and the pre-change build agreed; the agency's ticket asked to change it.** Under the authority order an explicit Asana instruction outranks the raster, so the collapsed state stands.

Recorded so that a later raster comparison does not "correct" it back.

**Running list of deliberate divergences from Figma, all Asana-instructed:**
1. **HOME-15** — gallery button reads "View More"; Figma shows "View Amenities".
2. **HOME-12** — FAQ collapsed on mount; Figma shows an item open.

### 10.3 · BRAND LOCKUP SIZES — measured on every page

| Element | Figma | We ship | Verdict |
|---|---|---|---|
| Header logo, desktop | **188 × 52** @ x 80 | 189.3 × 52 | ✅ correct |
| Header logo, mobile | **145 × 40** @ x 16 | 160.2 × 44 | ⚠️ ours ~10% large |
| **Footer logo, desktop** | **232 × 64** @ x 80 | h 28 (≈102 × 28) | ❌ **far too small** |
| **Footer logo, mobile** | **232 × 64** @ x 16 | h 28 | ❌ **far too small** |

Desktop footer verified identical on Home, About, Contact and Careers. Mobile verified on Services by row profile and visual crop: x 16…246, y 7356…7419 = **231 × 64**, the full lockup.

### 10.4 · The footer logo has been shrunk away from the design, not toward it

The `Logo` component's natural aspect is 233 : 64. Figma renders the footer lockup at **exactly natural size — height 64** — at both breakpoints, on every page.

| State | Height | vs Figma 64 |
|---|---|---|
| Component default | 52 | already 19% small |
| After the first "reduce 25–30%" request | 38 | 41% small |
| **Current** | **28** | **56% small** |

Both reduction requests were made on the stated premise that the logo was *"too large compared to the Figma design."* The measurement says the opposite: it was already undersized before either change, and the footer lockup should be **64px tall, 232 wide**.

Those requests arrived through Lovable chat rather than Asana, so they are not "an explicit Asana instruction" in the authority order — and their stated goal was to match Figma. **Reported, not reverted.** The client decides; we do not unilaterally undo an instruction, nor leave a measured mismatch unreported.

Note this is a *different* element from HOME-13, which concerns the large faint watermark at the footer's bottom centre.

---

## 11 · AMENITIES / ADMISSIONS — REBASE FINDINGS

### 11.1 · ADM-04 stays open — the raster deepens the conflict rather than settling it

All four signals sit in a single frame:

| Signal | Says |
|---|---|
| Header navigation | **Admissions** |
| Section eyebrow | **admissions** |
| Hero heading | **Life at Amara Care Center** |
| Hero CTA | **Explore Amara Amenities** |
| Route | `/amenities` |

The approved design contains the exact mismatch the ticket reports. **No inference is possible.** Route and navigation naming stay untouched until the agency answers. Every Amenities item that does not depend on the naming continues.

### 11.2 · ADM-02 — the carousel target, measured

| | Figma desktop | We ship |
|---|---|---|
| Active card | x **299…1140** — left margin 299, right margin 299 | starts at the 80px container gutter |
| Card size | **842…846 × 450** | `min-[1280px]:w-[846px] h-[450px]` ✅ |
| Next card | starts x **1165**, clipped by the viewport edge | peeks, clipped by container |
| Gap | ~20–24 | `gap-5` = 20 ✅ |
| Arrows | centred **below** the carousel | centred below ✅ |

**The one real difference: the active card is centred in the viewport, not aligned to the container gutter.** Left and right margins are 299 and 299 — exact. Our track sits inside `Container`, so card 1 begins at x 80, a 219px offset from the design.

Card size and gap are already correct. Height measures **exactly 450**.

### 11.3 · Amenities mobile card order — defect confirmed

| | Order |
|---|---|
| **Figma mobile** | **image** → heading → body → bulleted list → "Book a Call" |
| **We ship** | heading → body → list → "Book a Call" → **image** |

The card is `flex-col` on mobile with the text `<div>` before the `<img>` in the DOM, so the photo lands last. Desktop is `md:flex-row` with the image right, which is correct and must not move.

Mobile is **stacked full cards** — no peeking card, no carousel mechanics. Desktop carousel behaviour must not be forced onto mobile.

### 11.4 · Gallery — "1 and 3" is literal, confirmed

Centred eyebrow and heading, then small image labelled **01** left, large image centre, small image labelled **03** right, with "Serene Courtyard Retreat" and its supporting line centred **below** the centre image. Only 01 and 03 appear. Confirms the brief.

### 11.5 · Content inconsistency inside the design — flagged, not resolved

Our three cards are Accommodations, Services and Community. Card content matches the **desktop** frame exactly for Accommodations and Services.

But the **mobile** frame shows a card headed **"Accommodations"** carrying the **Community** bullet list — large dayrooms and lounges, recreational activities, special dining events, musical entertainment, weekly dog-therapy visits. The desktop frame pairs "Accommodations" with private rooms, cable & WiFi, courtyard, air conditioning.

**The two approved frames disagree about which list belongs to which heading.** Same class as the testimonial names: the ambiguity originates in the design. We keep the desktop pairing, which is what we ship, and raise it as a content question. No list is invented, moved or merged.

### 11.6 · Noted for consistency — carousel arrows

`AmenitiesCarousel` still disables its arrows at the track ends (`disabled={atStart}` / `atEnd`). The Home testimonial arrows were changed to wrap-around and never disable, on an explicit agency ticket (HOME-09).

Both frames render the two arrows in the same enabled style, so the raster does not settle it. Raising it rather than assuming the Home decision generalises.

---

## 12 · CAREERS PAGE — REBASE FINDINGS

### 12.1 · Careers hero scrim — our overlay is provably incompatible with the design

Hero height measures exactly **900**, matching what we ship.

`CareersHero.tsx` stacks **two** full-bleed gradients:

```
linear-gradient(to top right, rgba(0,0,0,0.92), rgba(0,0,0,0.65) 45%, rgba(0,0,0,0.30))
linear-gradient(to top,       rgba(0,0,0,0.85), rgba(0,0,0,0))            /* bottom 2/3 */
```

At the bottom-left, where the heading, body and CTA sit, those compose to **1 − (1−0.92)(1−0.85) = 98.8% black**.

| Region | Figma mean luminance | Max our scrim can produce |
|---|---|---|
| **bottom-left, behind the CTA** | **143.3** | 255 × 0.012 = **3.1** |
| mid-left, behind body copy | 98.9 | ~39 |
| right, at text height | 74.8 | ~63 |

**This does not depend on the photograph.** A 98.8% black overlay cannot yield luminance 143 from any source image whatsoever — the ceiling is 3.1. The design's hero shows scrubs, shoes, tarmac and planting all clearly legible, with white text carried by the naturally darker lower third of the photo rather than by an overlay.

The fix is a scrim measurement, not a taste call: reduce until the rendered luminance in each region matches the raster. Both gradients are in scope; the bottom one is the larger offender.

### 12.2 · CAR-02 — no longer target-less, and the mismatch is large

The brief said the "Why Amara" desktop target is now supplied. Measured:

| | Figma | We ship |
|---|---|---|
| Photo | **360 × 350** at x 80 | **630 × 430** (`aspect-[630/430]`) |
| Gap | **290** | `gap-5` = **20** |
| Text column | **630**, ending at the right gutter | 630 |
| Grid | 80 + 360 + 290 + 630 + 80 = **1440** ✅ | `grid-cols-2` → two equal 630 columns |

Our photo is **nearly double the design width**, and the 290px gap — the "large white breathing room" the brief describes — is currently 20px. `min-[768px]:grid-cols-2` forces two equal columns, which is the root cause.

This is why CAR-02's screenshot carried no annotation: the whole block is proportioned differently, so there was nothing specific to circle.

**Still to measure before dispatch:** the section's own height against our `min-[1440px]:min-h-[590px]`, and the mobile stacking order.

### 12.3 · CAR-03 confirmed — no "View Full Team"

The desktop team grid runs straight into Testimonials. No button of any kind sits between them. Confirms the removal, desktop and mobile.

### 12.4 · HOME-14 independently confirmed from a second page

The Careers desktop frame carries the same shared contact block, and its heading renders on **exactly three lines**:

```
Contact our team
to learn more about
our services
```

"our", not "out". This is a second, independent confirmation of HOME-14's target from a different page's frame — so HOME-14 **stays closed**.

### 12.5 · FAQ open-state — third sighting

The Careers frame again shows an FAQ item expanded on load, as Services does. Consistent with the recorded deliberate divergence: HOME-12 asked for collapsed, and an Asana instruction outranks the raster. No change.

### 12.6 · Testimonial names — third sighting

Careers desktop again shows **"— Oliver W." on both visible cards**. The duplication is systematic across the design, not a one-frame slip. Reinforces that this is a content question for the agency, not something to resolve in code.

---

## 13 · CONTACT PAGE — REBASE FINDINGS

### 13.1 · CON-01 — hero left column, measured

Hero section is **y 0…899 = 900 tall**.

| | Figma |
|---|---|
| Photo | **630 × 720**, x 730…1359, y 100…819 — right margin **80** ✅ matches what we ship |
| Left column heading | y **383…429**, x 83…382 |
| Left column body | y **472…508**, x 80…468 (389 wide) |
| Left column button | y **546…593**, x 80…239 (160 wide) |
| "Scroll to Explore" | y 804…816 |

The heading/body/button block spans **y 383…593**, centre **488**, against a photo centred at 459.5 — so it sits low in the hero, **283px below the photo's top edge**, not anchored to the top. That is the defect CON-01 reports ("column top-anchored, h1 collides with the header row").

Stated as measured positions rather than as "centred": the block's centre is 28.5px below the photo's centre, so a strict centring rule would land it slightly high. The scroll indicator sits separately at the hero's bottom, which is why the column is not a simple centred stack.

### 13.2 · Insurance panel — full target

| | Value |
|---|---|
| Panel | **738 × 434**, x 622…1359, right margin **80** |
| Panel fill | **#8CA1C1** |
| Panel padding | **32** |
| Layout | **two columns**; column 1 at panel-relative x 32, column 2 at x **421** |
| Check circle | **28 × 28**, fill **#FFFFFF**, check drawn in the panel blue |
| Heading | "Accepted insurances include, but are not limited to:" in white |

### 13.3 · TWO COLOUR TOKEN DEFECTS — both now on two independent sightings

**`#8CA1C1` vs our `#8FA8CE`.** The insurance panel samples **#8CA1C1** — byte-identical to the 404 page background measured earlier. Two different pages, two different components, same value: this is a real design token.

Our `--blue-300` is **#8FA8CE** (143, 168, 206), and `ContactInsurance` additionally hard-codes the same literal (recorded as COD-02). Measured is (140, 161, 193).

| Channel | Ours | Figma | Δ |
|---|---|---|---|
| R | 143 | 140 | 3 |
| G | 168 | 161 | **7** |
| B | 206 | 193 | **13** |

A 13-unit difference on blue is far outside antialiasing or colour-management noise. **This is a genuine token error**, and it affects the 404 background and the insurance panel together.

**`#F4F8FF` vs our `#F2F7FF`.** Second independent sighting — the Contact insurance section background and the About values section background both sample **#F4F8FF** (244, 248, 255) against our `--blue-50` of **#F2F7FF** (242, 247, 255). Two units on two channels, now confirmed on two pages.

Both are reported, **neither changed**: they are shared tokens, and per the agency's own instruction a token change is a global atomic task requiring verification on every route.

### 13.4 · Still to measure on Contact before dispatch

- The **"Supported Transition" badge icon** inside the admissions-steps photo — the brief requires the official icon rather than a generic substitute. Present in the frame; not yet measured or matched against the asset inventory.
- Mobile Contact layout in full — the hero, the insurance panel's mobile arrangement, and the form.
- The contact form's field set is visible (Name*, Email*, Phone Number*, Your question, privacy checkbox, Submit) and matches what we ship, but S1/S2 states remain blocked on copy hidden under the annotation digits.

---

## 14 · 404 PAGE — REBASE FINDINGS

Both frames are exactly one viewport: desktop **1440 × 900**, mobile **393 × 852**. Full composition measurable.

### 14.1 · Background

**#8CA1C1**, identical on both frames and identical to the Contact insurance panel. Our `--blue-300` is `#8FA8CE` — see §13.3, the same token defect.

**Independent confirmation of the ground colour.** Deriving the watermark's alpha as white-over-background gives per-channel values of 0.061 / 0.064 / 0.065 for the faint tone and 0.191 / 0.191 / 0.194 for the stronger one. Three channels agreeing to ~0.003 is only possible if the assumed ground is correct and the overlay is pure white. A wrong background would produce three disagreeing alphas.

### 14.2 · Desktop 1440 × 900 — measured

| Element | y | x | size |
|---|---|---|---|
| Header row | 24…76 | 80…1359 | logo at the 80 gutter, "Get Started" pill ending at 1359 |
| **"404"** | **266…472** | **492…944** | **453 × 207**, centred (718 vs 720) |
| "Page was not found" | 523…549 | 598…842 | 245 wide |
| Body copy, 2 lines | 566…607 | 534…905 | 372 wide |
| "Back to Home Page" pill | 640…688 | 614…826 | **213 × 49** |

Vertical gaps: 404 → heading **51**, heading → body **17**, body → pill **33**.

Content block spans y 266…688 (423 tall), centre **477** against a viewport centre of 450 — so the block sits **27px below centre**, not vertically centred.

Nav: About Us · Services · **Admissions** · Careers · Contact.

### 14.3 · Mobile 393 × 852 — measured

| Element | y | size |
|---|---|---|
| Header | 20…52 | logo left, burger right |
| **"404"** | **267…399** | **291 × 133**, centred |
| "Page was not found" | 444…466 | 210 wide |
| Body copy, 2 lines | 484…519 | 330 wide |
| "Back to Home Page" pill | 552…596 | **197 × 45** |

Vertical gaps: **45 / 18 / 33** — against desktop's 51 / 17 / 33.

### 14.4 · Watermark treatment differs by breakpoint

| | Treatment |
|---|---|
| **Desktop** | **Two** oversized translucent AMARA marks bleeding in from the **left and right** edges. Span x 0…1438, y 24…796; more coverage in the left half (7685 px vs 5186), so the two are not mirror images. |
| **Mobile** | **One** mark rising from the **bottom** edge. x 97…295 (199 wide), y 687…851, centred at x 196. |

Watermark fill: **white** at **α ≈ 0.06** for the faint areas and **α ≈ 0.19** for the stronger areas.

### 14.5 · Exact copy

```
404
Page was not found
The page you're looking for couldn't be found.
Let's get you back on track.
[ Back to Home Page ]
```

Body copy breaks to **two lines** on both breakpoints, at the same point. Apostrophes render as straight `'` in the frame — confirm before shipping whether typographic `’` is intended.

### 14.6 · Note on the "404" numeral

Recorded as its measured glyph box — **453 × 207** desktop, **291 × 133** mobile — rather than as an inferred font-size. Per §8.3 the deliverable is target geometry; the type size that produces it can be calibrated against the Playfair binaries the same way the button labels were, and verified in the browser.

---

## 15 · PAGE-BY-PAGE REBASE — COMPLETE

All nine designed surfaces reconciled against the official rasters: Home, About, Services, Amenities, Careers, Contact, Privacy Policy, Terms of Use, 404.

### What the rasters resolved

HOME-16 · HOME-17 · HOME-02 (horizontal) · SERV-06 · SERV-04 · Services mobile hero order · ABOUT-13 (scoped to mobile) · ABOUT-08 · ABOUT-12 · ADM-02 · Amenities mobile card order · Amenities gallery · ABOUT-14 / ADM-08 · ABOUT-05 / ADM-05 colour · CAR-02 · CAR-03 · Careers hero scrim · CON-01 · AUX legal copy · 404 rebuild.

### Confirmed already correct — no turn to be spent

HOME-14 (twice, from two different pages) · HOME-19 · HOME-20 · desktop header logo · Amenities card size, gap and arrow placement · Contact hero photo 630×720 · Careers hero height 900.

### Deliberate divergences from Figma — all Asana-instructed, all recorded

1. **HOME-15** — "View More"; Figma shows "View Amenities".
2. **HOME-12** — FAQ collapsed on mount; Figma shows an item open (seen on Services *and* Careers).

### Inconsistencies **inside** the approved design — flagged, never resolved in code

1. Testimonial author duplicated — "Oliver W." on both cards, on three separate pages; mobile Home shows "Olivia T." instead.
2. Amenities card content — desktop and mobile frames pair different bullet lists with the same heading.
3. Privacy nav — 10 entries, 9 sections, "Your rights" duplicated.
4. ADM-04 — nav says "Admissions" on a page designed as Amenities.

### Token defects found — reported, none changed

| Token | Ours | Figma | Sightings |
|---|---|---|---|
| `--blue-300` | #8FA8CE | **#8CA1C1** | 404 background, Contact insurance panel |
| `--blue-50` | #F2F7FF | **#F4F8FF** | About values, Contact insurance section |
| `container-gutter` | 33.5px @390 | **16 @393** | measured on 3 pages |

### Still to measure before the affected items dispatch

Careers intro section height and mobile order · Contact "Supported Transition" badge icon · Contact mobile in full · About values desktop card internals for ABOUT-08 · Playfair heading-weight calibration for HOME-18.

---

## 16 · CORRECTION — mobile button size is NOT uniform, and DEF-02 was overstated

Measured while scoping R4-07. Every dark button in the Home mobile frame is **44 tall**, but their label sizes differ:

| Button | Figma ink | Best-fit candidate | Size |
|---|---|---|---|
| Hero "Explore Our Services" | **146** | Medium 145.1 | **16px** |
| Hero "Plan Your Visit" | **99** | Medium 100.5 | **16px** |
| Service card ×4, "Explore Our Services" | **164** | Medium 163.6 | **18px** |
| Form "Submit" | **49** | Medium 48.9 | **16px** |

All four service-card buttons measure identically (button 329 wide, ink 164), so 18px there is systematic, not a one-off.

### What this overturns

We previously wrote that the `dark`/`light` variants hard-coding `text-[18px]` is a defect because "the design says 16px at mobile". **That was based on the hero buttons alone and is too broad.** For the service-card buttons the design *does* render 18px at mobile, which is exactly what the hard-coded value produces. The hero is the deviation, not the rule.

**Revised position:**
- The hero's mobile buttons are 16px. That is a hero-specific treatment — almost certainly because two buttons must share one 361px row.
- The `text-button` token (16px @ 393 → 18px @ 1440) matches the hero and Submit but **not** the service buttons.
- So the design is not internally consistent about mobile button size, and "apply the token globally" would be wrong.

### Consequence for scope

R4-07 is therefore **local to `home/Hero.tsx`**. Touching `ui/button.tsx` would shrink every button on nine routes to 16px at mobile and break the service cards. The brief says so explicitly, and carries a regression check on `/services` at 393 that must still report **18px** — that check exists precisely to catch a shared-component edit.

Weight remains **Medium 500** everywhere; only the size varies. The earlier calibration stands.

### Also measured, deliberately not fixed here

Figma's mobile buttons are **44** tall and desktop **46**; we render **48** at both via `size="l"` (`h-12`). A real deviation, but height is not what HOME-16 asks for, so it is recorded for a separate item rather than folded in.

---

## 17 · HOME HERO — CTA ROW GEOMETRY, AND THE GUTTER ROOT CAUSE

Measured for correction **H10**. Both frames read at 1:1, probe-anchored: horizontal
extents taken on a scanline through the button's vertical middle, vertical extents
taken down a column that is clear of glyphs. Mid-row extents alone are unusable here
because the dark button holds white text and the light button holds navy text, so each
button's fill colour reappears inside the other.

### 17.1 Mobile — `Home Page _ Desktop (1).png` (393 wide), scanline y = 321

| x range | content |
|---|---|
| 0–15 | page background `#E6F0FF` |
| **16–203** | dark button `#2C2E45` — **188 wide** |
| 204–219 | page background — **gap 16** |
| **220–376** | light button `#FFFFFF` — **157 wide** |
| 377–392 | page background |

Vertical: both buttons **y 300–343 = 44 tall**. Corner inset is 14px at the top row,
so the radius is roughly 16–18 — *not* a pill. Radius is not asserted further; it was
not needed for H10.

The row spans **16 → 376 = 361**, which is the full content width at a **16px gutter**.
The hero photo below it spans the same 16 → 376 (solid 361-wide runs at y 430, 440, 620),
so row and photo share both edges in the design.

Label ink: dark **x 37–182 = 146**, light **x 249–349 = 101**.

### 17.2 Desktop — `Home Page _ Desktop.png` (1440 wide), scanline y = 335

| x range | content |
|---|---|
| **516–737** | dark button — **222 wide** |
| 738–753 | **gap 16** |
| **754–923** | light button — **170 wide** |

Row centre = (516 + 923) / 2 = 719.5 ≈ **720**, i.e. centred on the 1440 frame.

Vertical, probed clear of glyphs at x = 600 (dark) and x = 860 (light):
both **y 312–359 = 48 tall**.

### 17.3 Correction to §16

§16 recorded "Figma's mobile buttons are **44** tall and desktop **46**". The mobile
figure is confirmed. **The desktop figure was wrong — it is 48, not 46**, verified by
two independent glyph-free column probes. We render 48 on desktop, so desktop height
is *correct as shipped* and there is no desktop height item to raise. The mobile 44
remains a real deviation and was folded into H10.

### 17.4 A padding error of mine, and why it happened

For H10 I specified `px-[22px]`, derived from the raster as (188 − 146 ink) / 2 = 21.
That is wrong. **CSS padding applies to the advance box, not the ink box.** With the
label's ~2.7px total side bearing the advance width is 151.4, giving (188 − 151.4) / 2
= **18.3 → `px-[18px]`**, which is what the implementer measured in-browser and used.

Rule going forward: **never convert a raster ink extent straight into a CSS padding
value.** Ink → advance first, or measure the advance in-browser.

The light button does not share that padding: content-sizing it would give
104.3 + 36.6 = 140.9, not 157. One construction that reproduces the measured 157 is
letting it absorb the remaining track width. Per the standing rule, that is recorded as
*a* construction consistent with the measurement, **not** as proof of the Figma
implementation.

### 17.5 DEF-01 — root cause found, and it is a transcription slip

```css
/* Fluid page gutter: 16px at 390 → 80px at 1440, clamped at both ends. */
@utility container-gutter { padding-inline: clamp(1rem, 0.6095rem + 6.0952vw, 5rem); }
```

The comment states the correct intent and the **slope is right**: 64 / 1050 = 0.060952
→ `6.0952vw`. The intercept should then be 16 − 0.060952 × 390 = −7.771px =
**−0.4857rem**. The shipped value is **+0.6095rem** — the slope's own leading digits,
with the wrong sign and the wrong magnitude. That single slip is the whole of DEF-01:
it yields **33.71px at 393 instead of 16px**.

Refit to the canonical 393 endpoint (§2) rather than 390:

- slope = 64 / (1440 − 393) = 0.0611270 → **6.1127vw**
- intercept = 16 − 0.0611270 × 393 = −8.0229px → **−0.5014rem**

```css
/* Fluid page gutter: 16px at 393 → 80px at 1440, clamped at both ends. */
@utility container-gutter { padding-inline: clamp(1rem, -0.5014rem + 6.1127vw, 5rem); }
```

393 → 16.00 and 1440 → 80.00, and **both land exactly on the clamp bounds**, so the
floor and ceiling do real work instead of masking the fit.

**Evidence status.** Both endpoints are now *measured*, not assumed: 16 @ 393 from
§17.1 above, 80 @ 1440 previously verified. **Linearity between them remains a choice**,
not a measurement — every official frame is either 393 or 1440, so nothing constrains
the interior. It matches the form the token already used. Widths 1152–1440 change most
against the previous build (the old curve saturated at 80 from 1152 up; the new one
reaches 80 only at 1440) and are the place to look first if an intermediate width
regresses.

### 17.6 Why the first H10 turn was rejected

The implementer reached the target numbers with
`mx-[calc(1rem-clamp(1rem,0.6095rem+6.0952vw,5rem))]` = **−17.71px per side at 393**.
Two independent grounds for rejection:

1. It is a negative margin used as layout architecture — prohibited outright.
2. It introduced a **new visible defect**: the CTA row moved to a 16px page margin
   while the hero photo directly beneath it stayed at 33.71px, so the buttons overhung
   the photo by ~17.7px per side across 320–639. Before that turn they were aligned.

The diagnosis behind it was sound — the gutter really is wrong — but the fix belonged
in the token, not in the section.

---

## 18 · HOME DESKTOP HERO — VERTICAL GEOMETRY (H01 / H03)

`Home Page _ Desktop.png`, 1440 wide. Text rows are ink bounds; the CTA row, the photo
and the section boundary are hard edges. Both a strict ink threshold and a loose
antialiasing envelope are given, because a text gap measured ink-to-ink and a gap
measured box-to-box are not the same number and must not be compared across methods.

| element | ink (strict) | envelope | height |
|---|---|---|---|
| header / nav | 28–71 | 24–75 | 44 |
| H1 "Comfort You Can Trust" | 168–200 | 165–200 | 33 |
| paragraph line 1 | 238–251 | 237–254 | 14 |
| paragraph line 2 | 262–275 | 261–278 | 14 |
| CTA row (hard edge) | **312–359** | — | **48** |
| hero photo (hard edge) | **440–1159** | — | **720** |
| blue hero section ends (hard edge) | **1199** | — | — |

Derived gaps, strict ink to strict ink except where both sides are hard edges:

| gap | Figma |
|---|---|
| header ink bottom → H1 ink top | **97** (envelope 90) |
| H1 ink bottom → paragraph ink top | **38** (envelope 37) |
| paragraph ink bottom → CTA row top | **37** (envelope 34) |
| **CTA row bottom → photo top** | **81** (both hard edges — exact) |
| **photo bottom → blue section end** | **40** (both hard edges — exact) |

Paragraph line pitch is 238 → 262 = **24**, matching `text-body`'s 1.5rem line-height
at 1440. H1 ink height 33 is consistent with Playfair Display at the 44px `text-h1`
clamp maximum, so **H1 size is already correct** — H01 is spacing only.

Rows 1166–1188 carry a faint `#E3EDFC` band under the photo. That is a **drop shadow on
the photo**, not a section boundary; the section boundary is the hard `#E6F0FF` →
`#FFFFFF` step between y 1199 and y 1200. Recorded, not actioned.

### 18.1 Where H01's defect actually sits

The shipped chain at 1440 reconstructs exactly from the measured H1 box and the source
spacing utilities: H1 box 162–214, `mt-6` → paragraph 238–286, `mt-6` → CTA 310–358,
`mt-10` → photo top **398**. That reproduces the implementer's independently measured
photo top of 398, so the reconstruction is sound.

Against Figma: the CTA row is within **2px** of target (310 vs 312), but the photo top
is **398 vs 440 — 42px short**. The agency's note that "the current CTA → hero-image gap
is visibly too small" is therefore correct and *localised*: the `mt-10` (40px) between
the CTA row and the photo needs to become **81px**, and the remaining three gaps are
close to correct already.

This is exactly why the brief says to tune the four gaps individually and **not** to
translate the hero group as a whole — a group translation would move three correct gaps
to fix one wrong one.

### 18.2 Mobile hero vertical geometry (393), for comparison

| element | ink / hard edge |
|---|---|
| header | 20–51 |
| H1 line 1 | 106–134 |
| H1 line 2 | 151–178 |
| paragraph lines | 216–223 · 236–243 · 256–263 |
| CTA row (hard edge) | **300–343** |
| hero photo top (hard edge) | **384** |

| gap | mobile | desktop |
|---|---|---|
| header → H1 | 54 | 97 |
| H1 → paragraph | **38** | **38** |
| paragraph → CTA row | **37** | **37** |
| CTA row → photo | **40** | **81** |

The middle two gaps are **identical across both frames**; only the header offset and the
CTA→photo gap are viewport-dependent. The mobile CTA→photo gap of 40 is exactly the
`mt-10` already shipped, so **mobile is already correct** and H01 is a desktop-only
change. Any fix must not move the mobile values.

Ink gaps are **not** comparable to CSS margins — the 38 and 37 above include the
descender space of the block above and the ascender space of the block below. The only
sound way to compare is to measure the shipped render as a raster with the same scan,
and that is how H01 is being verified.

---

## 19 · ROUTE INVENTORY — established while verifying H10

`src/routes/` contains exactly: `index.tsx`, `about.tsx`, `amenities.tsx`,
`careers.tsx`, `contact.tsx`, `services.tsx`, **`privacy-policy.tsx`**,
**`terms-of-use.tsx`**, `$.tsx` (catch-all 404), `__root.tsx`.

Two consequences:

1. **The legal pages exist**, at `/privacy-policy` and `/terms-of-use`. The H10 turn
   reported that "`/privacy` and `/terms` don't exist as routes and render the 404
   page" — that was the implementer guessing the paths and hitting the catch-all, not
   a finding about the site. Corrected here so it does not propagate. It does mean the
   H10 regression sweep covered the catch-all twice and **never covered the two real
   legal routes**; that gap is carried into the H01 turn rather than re-spending a
   credit on two prose pages.
2. **There is no `/admissions` route at all.** R01 is filed as "Admissions navbar
   currently routes to `/amenities`", but the underlying fact is that `/amenities` is
   the only target that exists. Recorded as evidence for R01. Per the instruction,
   R01 is **investigate only — not mutated.**

---

## 20 · HOME HERO BADGE — MEASURED FOR H02 (prep, not yet dispatched)

`Home Page _ Desktop.png` at 1440. Hero photo occupies x 80–1359, y 440–1159.

| property | measured |
|---|---|
| badge bounds | x **991–1335**, y **976–1135** |
| badge size | **345 × 160** |
| inset from photo right | **24** |
| inset from photo bottom | **24** |
| badge fill | **#E6F0FF** — identical to the page background |

The 24/24 insets match the shipped `lg:bottom-6 lg:right-6` exactly. Shipped
`lg:max-w-[340px]` against a measured 345 is a 5px difference — noted, not asserted,
and not part of H02's colour scope.

The fill being byte-identical to the page background is the same property that
invalidated the first HOME-17 badge detector run; any future badge measurement must be
probe-anchored rather than fill-detected.

### 20.1 Text colours — the three treatments the brief asks to check separately

Ink bands inside the badge, and the dominant exact colour in each:

| element | band | measured colour | shipped | verdict |
|---|---|---|---|---|
| icon tile | y 992–1031 | **#56677F** (`--blue-500`) | `bg-accent` → `--blue-500` | **correct** |
| heading "Where Healing Feels Like Home" | y 992–1031 | **#2C2E45** (`--blue-800`) | `text-label-brown` → **#441802** | **WRONG** |
| body, 3 lines | 1054–1070 · 1078–1094 · 1102–1118 | **#4B5066** (`--blue-700`) | `text-muted-foreground` → `--blue-700` | **correct** |

Body line pitch is 1078 − 1054 = **24**, matching the shipped `leading-[24px]`.

So the agency's "the text reads too black/heavy" resolves to **one** element, not the
card: the heading is rendered in brand brown **#441802** where Figma uses navy
**#2C2E45**. Body colour and icon treatment are already right.

This is exactly why the brief says "Do NOT apply one blanket opacity to the entire
card" — a blanket change would have wrecked two correct values to fix one wrong one.
H02 must change the heading colour only.

Note this is the colour half of H02. The other half — "use the approved reception image,
preserve the crop, and do not read the hand-drawn marks on the AMARA wall sign as an
instruction to remove the sign" — is a separate check to run when H02 is dispatched.
