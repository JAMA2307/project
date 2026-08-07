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
