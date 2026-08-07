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

### The correct curve

Design endpoints are **16 @ 393 → 80 @ 1440**:

```
slope     = (80 − 16) / (1440 − 393) = 64 / 1047 = 0.0611270  →  6.1127vw
intercept = 16 − 0.0611270 × 393     = −8.023px               →  −0.5014rem

padding-inline: clamp(1rem, -0.5014rem + 6.1127vw, 5rem)
```

Verify: at 393 → −8.023 + 24.023 = **16.00** ✓ · at 1440 → −8.023 + 88.02 = **80.00** ✓

### Correction to our own earlier proposal

Before the rasters arrived we derived the fix from **390 → 1440**, giving an intercept of −0.4857rem. The design's mobile endpoint is **393**, giving **−0.5014rem**. Our earlier number was wrong — small, but this is a global token and we are not shipping an approximation. The current shipped value, `+0.6095rem`, remains wrong in the other direction and by far more: it renders **33.5px at 390** against a 16px target.

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

### Cross-checks that make these trustworthy

- Label ratio Explore ÷ Plan: Figma mobile **1.469**, Figma desktop **1.464**, our live site at 18px **1.466**. Agreement to 0.2% proves the typeface is the same in all three and only the *size* differs.
- Implied mobile label size: 144/158.5 × 18 = **16.35px**; 98/108.1 × 18 = **16.32px**. Two independent labels agree.
- The design system's own `text-button` token resolves to **16.0px at 393**. The measurement is 16.0–16.4 including ink-vs-advance error, so **the mobile label is the `text-button` token** — which the `dark`/`light` variants currently bypass by hard-coding `text-[18px]`. That is DEF-02, and the raster confirms it is a real defect rather than a stylistic quibble.
- Row arithmetic closes exactly: 16 + 188 + 16 + 157 + 16 = **393**.

### Construction

Two models reproduce the measurements; the second fits exactly:

- padding 28, dark `flex-1`, light auto → dark 188 ✓, light **154** vs 157 measured
- **padding 22, dark content-sized, light `flex-1`** → dark **188** ✓, light **157** ✓

Below 393 the design says nothing. The row must not overflow at 320, so the row wraps below the point where both fit. That is the one extrapolation here and it is confined to widths the design never specifies.

---

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
