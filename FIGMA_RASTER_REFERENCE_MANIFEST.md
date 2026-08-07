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
