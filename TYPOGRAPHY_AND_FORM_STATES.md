# TYPOGRAPHY & FORM STATES — technical analysis

| | |
|---|---|
| Prepared | 2026-08-06 |
| Trigger | Agency delivered `Playfair_Display.rar` + `satoshi.zip` and reported *"typography is currently inconsistent"* |
| Sources preserved at | `design-sources/fonts/` — 26 files, 3.2 MB, all 22 font binaries validated |
| Status | **ANALYSIS ONLY — nothing implemented.** No Lovable message sent, no production code touched |

---

## 1 · FONT ARCHIVE INVENTORY

### 1.1 · Playfair Display — `6912be68-Playfair_Display.rar`

**Family name:** `Playfair Display` · **Format:** TTF (`glyf` outlines) · **unitsPerEm:** 1000 · **Embedding:** Installable (unrestricted) · **Licence:** SIL Open Font License 1.1, `OFL.txt` included, plus a Google Fonts `README.txt`. Commercial use permitted.

**Variable fonts — 2 files, both `wght 400–900`, default 400, 6 named instances each**

| File | Style | Bytes |
|---|---|---|
| `PlayfairDisplay-VariableFont_wght.ttf` | roman | 262,144 |
| `PlayfairDisplay-Italic-VariableFont_wght.ttf` | italic | 280,660 |

**Static fonts — 12 files**

| Weight | Roman | Italic |
|---|---|---|
| 400 Regular | ✅ | ✅ |
| 500 Medium | ✅ | ✅ |
| 600 SemiBold | ✅ | ✅ |
| 700 Bold | ✅ | ✅ |
| 800 ExtraBold | ✅ | ✅ |
| 900 Black | ✅ | ✅ |

**Lowest available weight is 400.** There is no Light or Thin Playfair — any design calling for a lighter serif cannot be honoured with this family.

### 1.2 · Satoshi — `bece60e3-satoshi.zip`

**Family name:** `Satoshi` · **Format:** OTF (CFF outlines) · **unitsPerEm:** 1000 · **Embedding:** Installable · **Foundry:** Indian Type Foundry (Fontshare).

| Weight | Roman | Italic |
|---|---|---|
| 300 Light | ✅ | ✅ |
| 400 Regular | ✅ | ✅ |
| 500 Medium | ✅ | ✅ |
| **600 SemiBold** | ❌ **absent** | ❌ **absent** |
| 700 Bold | ✅ | ✅ |
| 900 Black | ✅ | ✅ |

**No variable font.** 10 static files only.

### 1.3 · Three defects in the delivery itself

**D1 — Satoshi ships no licence file.** The zip contains 10 `.otf` files and nothing else: no OFL, no EULA, no readme. Satoshi is distributed by Fontshare under its own licence, which governs **self-hosting and webfont conversion** specifically. Playfair's OFL is included and unambiguous; Satoshi's is missing. **Confirm the Satoshi licence covers self-hosted webfont use before these files are deployed.**

**D2 — Satoshi italic metadata is inconsistent.** Three of the five italic files do not set the italic bit in `OS/2.fsSelection`:

| File | `fsSelection` italic bit | Correct? |
|---|---|---|
| `Satoshi-Italic.otf` | set | ✅ |
| `Satoshi-BoldItalic.otf` | set | ✅ |
| `Satoshi-LightItalic.otf` | **not set** | ❌ |
| `Satoshi-MediumItalic.otf` | **not set** | ❌ |
| `Satoshi-BlackItalic.otf` | **not set** | ❌ |

Harmless if each face is declared explicitly in its own `@font-face` with `font-style: italic` — which is what self-hosting requires anyway. It would misbehave if the fonts were installed locally and matched by the OS. Recorded so nobody later mistakes it for our bug.

**D3 — two Playfair files extracted as 0 bytes under `unar`, but the archive is fine.** `PlayfairDisplay-Italic-VariableFont_wght.ttf` and `static/PlayfairDisplay-Italic.ttf` came out empty with `unar`; the RAR listing showed them at 280,660 and 177,972 bytes, and `unrar-free` extracted both correctly. **The archive is not corrupt — the extractor was.** All 22 binaries in `design-sources/fonts/` are verified: non-zero, valid `sfnt` headers.

### 1.4 · Neither archive contains web formats

All 22 files are desktop TTF/OTF. **There is no WOFF2.** Deploying these as-is would be a serious regression:

| | Current (CDN, WOFF2, subset) | Naive self-host of these files |
|---|---|---|
| Playfair 400 | ~30 KB | **193 KB** static, or **262 KB** variable |
| Satoshi 400+500+700 | ~45 KB | **150 KB** |

Conversion to WOFF2 with Latin subsetting is **mandatory**, not optional — roughly a 4–5× reduction. The variable Playfair at 262 KB → WOFF2 ≈ 60–70 KB and covers **all six weights**, which is the right choice given §2.

---

## 2 · CURRENT TYPOGRAPHY CONFIGURATION

### 2.1 · How fonts are loaded today — `src/routes/__root.tsx`

```
Google Fonts : Playfair+Display:wght@400  &  Poppins:wght@500
Fontshare    : satoshi@400,500,700
```

**There is no `@font-face` rule anywhere in the codebase.** Every font is a third-party CDN request. `src/styles.css` only names families:

```css
--font-serif: "Playfair Display", Georgia, serif;
--font-sans:  "Satoshi", ui-sans-serif, system-ui, sans-serif;
--font-label: "Poppins", ui-sans-serif, system-ui, sans-serif;
```

### 2.2 · The type scale — `src/styles.css`

| Utility | Family | Weight | Size (390 → 1440) | Line-height |
|---|---|---|---|---|
| `text-h1` | serif | **400** | 32 → 44 | 40 → 52 |
| `text-h2` | serif | **400** | 32 → 44 | 40 → 52 |
| `text-h3` | serif | **400** | 28 → 40 | 36 → 48 |
| `text-h4` | serif | **400** | 20 → 24 | 28 → 32 |
| `text-body` | sans | 400 | 16 → 18 | 22 → 24 |
| `text-body-large` | sans | 400 | 18 → 20 | 26 → 32 |
| `text-button` | sans | 500 | 16 → 18 | 20 |
| `text-label` | **Poppins** | 500 | 16 | 22 |
| `text-eyebrow` | sans | 500 | 13 → 14 | 18 → 20 |

Plus a base rule: `h1,h2,h3,h4,h5,h6 { font-family: serif; font-weight: 400 }` and `body { Satoshi 400 / 18px / 24px }`.

---

## 3 · TYPOGRAPHY MISMATCH LIST

This is the answer to *"typography is currently inconsistent"*. Eight findings, ordered by impact.

### T1 — Playfair is loaded at weight 400 only. Every heavier heading is a **browser-synthesised fake bold**. — CRITICAL

The stylesheet requests `Playfair+Display:wght@400`. Nothing else is downloaded. Any element asking for a heavier serif gets a smeared, algorithmically-oblique-free synthetic bold instead of the real Medium/SemiBold/Bold drawing.

The agency has reported this **four separate times without naming the cause**:

| Asana | Words |
|---|---|
| HOME-05 | *"increase the text and the heading — in Figma they're a bit heavier"* |
| HOME-18 | *"some headings use the wrong weight — bold vs regular etc."* |
| ABOUT-10 | *"the font family, weight and sizes look wrong"* |
| SERV-01 | *"the text at bottom-left should be heavier"* |

**Fix:** load the variable Playfair (`wght 400–900`) as a self-hosted WOFF2. One file, all six weights, ~60–70 KB.

### T2 — The type scale hard-codes `font-weight: 400` on every heading utility. — CRITICAL

`text-h1`, `text-h2`, `text-h3`, `text-h4` each set `font-weight: 400`, **and** the base `h1–h6` rule sets it again. Even once heavier files are loaded, **no heading can render heavier without overriding the utility.** T1 and T2 must be fixed together; fixing either alone changes nothing visible.

### T3 — Poppins is a third family with no official source. — MAJOR

`--font-label: "Poppins"` drives `text-label`, and Poppins 500 is fetched from Google Fonts. **The agency's official delivery contains Playfair Display and Satoshi only.** Either Poppins is legitimate and its source was omitted, or labels should be Satoshi and Poppins is a leftover. **Needs an agency ruling** — do not silently re-map, and do not silently keep it.

### T4 — Satoshi has no SemiBold, so weight 600 must never be used. — MAJOR

The archive jumps 500 → 700. Any `font-semibold` / `font-weight:600` on Satoshi will synthesise. One instance already exists in shipped code: `__root.tsx`'s error component uses `font-semibold`. A lint rule should forbid 600 on `--font-sans`.

### T5 — Satoshi 300 and 900 are supplied but not loaded. — MINOR

Fontshare is queried for `400,500,700`. The archive also provides Light 300 and Black 900. If the design uses either, it is currently synthesising or falling back.

### T6 — Buttons bypass the type scale. — MAJOR

`text-button` exists in `styles.css` but **no component uses it**. The `dark` and `light` button variants hard-code `font-sans text-[18px] font-medium leading-[20px] tracking-[-0.18px]` inline in `ui/button.tsx`. The utility and the inline values agree today by coincidence; they will drift. Same pattern in `home/Contact.tsx`, where the form heading is inline `font-serif text-[24px] leading-[32px]` rather than `text-h4`.

### T7 — Silent fallback to `system-ui` if a CDN fails. — MAJOR

`--font-sans` falls back to `ui-sans-serif, system-ui`. If `api.fontshare.com` is slow, blocked, or unreachable, **all body text silently renders in the system font** at different metrics — which looks exactly like "typography is inconsistent" and is invisible in code review. Self-hosting removes this failure mode entirely, and is the strongest argument for it beyond performance.

### T8 — `text-label` has a no-op `clamp()`. — MINOR

`font-size: clamp(1rem, 0.9536rem + 0.1905vw, 1rem)` — the floor and ceiling are both `1rem`, so it is a constant 16px dressed as fluid. Either it should scale or it should be a plain `1rem`.

### 3.1 · Target mapping — where each family belongs

Recommended once T1–T3 are resolved. **The weight column is a proposal, not a measured design value** — the Figma type styles have never been readable (seat quota), and none of the four Asana items above names a target weight. Confirm before implementing.

| Role | Family | Weight | Source available? |
|---|---|---|---|
| h1 / h2 (44/52 at 1440) | Playfair Display | 400, or heavier per Figma | ✅ 400–900 |
| h3 / h4 | Playfair Display | 400–600 | ✅ |
| Card & panel headings | Playfair Display | ✅ |
| Body, paragraphs | Satoshi | 400 | ✅ |
| Body large / intro | Satoshi | 400 | ✅ |
| Navigation links | Satoshi | 400 | ✅ |
| Buttons | Satoshi | 500 | ✅ |
| Eyebrows / kickers | Satoshi | 500 | ✅ |
| Form field text & placeholders | Satoshi | 400 | ✅ |
| Form labels | Satoshi | 500 | ✅ |
| Footer links & body | Satoshi | 400 | ✅ |
| `text-label` (currently Poppins) | **UNRESOLVED — T3** | — | ❌ no official source |

---

## 4 · FORM STATES

### 4.1 · The required designs cannot be read — blocked

The agency reports new form-state designs. **I have not seen them.** The only reference on the board is Asana **HOME-21** (`1217234006576129`), whose full text is:

> *"In the UI KIT section they added [states] for when messages are sent — take the one marked 1."*

That points at a **Figma UI KIT frame**, and the attached screenshot is `1217234006576131`. Both are unreachable:

| Source | Blocker |
|---|---|
| Figma UI KIT frame | Seat quota exhausted (View seat, 6 calls/month) |
| Asana screenshot `1217234006576131` | Session egress returns `403 CONNECT` for `asanausercontent.com` |

**No new Asana items appeared.** Re-read at 2026-08-06 confirms subtask counts unchanged at 21/14/7/8/3/3/3 = **59**, and every parent `modified_at` byte-identical to the earlier collection. The newest change on the board is 09:37:34 UTC, before that collection ran. **The form-state material the agency added is HOME-21, which was already captured.**

**I therefore cannot document default / focus / filled / error / disabled / loading / success / hover as designed.** Inventing eight state specifications from one sentence would be fabrication. What follows is the *current implementation*, which is the baseline the designs will be compared against.

### 4.2 · Current implementation — `src/components/home/Contact.tsx`

Renders on `/`, `/careers`, `/contact`. Validation is `zod`; feedback is `sonner` toasts.

Field class, verbatim:
```
w-full rounded-2xl border border-transparent bg-brand-white px-5 py-3
font-sans text-[18px] leading-[24px] text-primary
placeholder:text-muted-foreground/70
focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary
```

| State | Implemented today | Gap |
|---|---|---|
| **Default** | `border-transparent`, white fill, 24px radius, Satoshi 18/24, placeholder at 70% muted | — |
| **Focus** | `border-primary` + `ring-1 ring-primary`; `focus:outline-none` **overrides the global `:focus-visible` 2px outline** for form fields only | Deliberate or accidental? Needs the design |
| **Filled** | **none** — no styling distinguishes a filled field | **There are no visible labels at all** — only placeholders, which vanish on input. A filled field loses its name entirely. Any "filled" design will likely need a floating or persistent label |
| **Validation error** | **none inline.** No `aria-invalid`, no red border, no message under the field. Only `parsed.error.issues[0]` — **the first error only** — as a toast | Largest gap. Five fields can be wrong; the user is told about one, in a transient popup, detached from the field |
| **Disabled** | **none** on fields. Buttons have `disabled:pointer-events-none disabled:cursor-not-allowed`, `disabled:opacity-50` base / `disabled:opacity-40` on `dark`/`light` | Fields need a disabled treatment |
| **Loading / submitting** | **none.** `onSubmit` is fully synchronous — no pending flag, no spinner, no double-submit guard | Needed |
| **Success** | `toast.success("Thank you — we'll be in touch shortly.")` + `form.reset()` | HOME-21 asks for a *designed* sent-state, variant "1". A toast is almost certainly not it |
| **Hover** | **none** on fields. Buttons use `hover-lift` (−2px translate + shadow) | Fields may need one |
| **Checkbox** | `h-5 w-5 !rounded-[4px]`, controlled by `agree` state | **On the regression watch — the square shape must not change.** CON-03 asks only for a colour change |

### 4.3 · Accessibility note, and a correction to the record

Field accessible names come from **`aria-label` attributes**, not `<label>` elements — `aria-label="Name"`, `"Email"`, `"Phone number"`, `"Your question"`. Only the checkbox sits inside a real `<label>`.

This corrects the Wave R6 report, which stated each field had *"a real `<label>`"*. Accessible naming works either way, so no assistive-technology defect follows — but there are **no visible labels anywhere in the form**, which matters directly to the filled/error states above.

### 4.4 · What is needed to specify the states

1. The Figma **UI KIT** frame — needs a Dev/Full Figma seat.
2. Attachment `1217234006576131` — needs `asanausercontent.com` allowed in the egress policy.

Either one unblocks the work. Both together give the full picture.

---

## FONT CALIBRATION AGAINST THE FIGMA RASTERS · 2026-08-07

Run on the Home hero button labels, because they are the one string that appears at a known size in **both** the 1440 and the 393 frame. Method per the agency's instruction: test real design-system candidates and compare rendered geometry, rather than trusting a ratio calculation.

### Method

Rendered `Explore Our Services` and `Plan Your Visit` from the **official Satoshi binaries** at 8× supersample, character-by-character with CSS letter-spacing applied between glyphs, then measured the ink bounding box. Compared against ink measured off the rasters with a **midpoint-luminance threshold** inside corner-safe boxes.

Two measurement errors were found and corrected along the way, both of which had inflated earlier numbers:

1. Boxes that clipped the buttons' rounded corners let the pale page background register as "white text", returning the **button width** (184, 218) instead of the ink.
2. The earlier desktop figures (164 / 112) came from the gaps between button-fill runs, not from ink.

Corrected targets, stable to ±1px across luminance thresholds from 200 to 248:

| | Explore Our Services | Plan Your Visit |
|---|---|---|
| Desktop 1440 | **163** | **112** |
| Mobile 393 | **146** | **99** |

### Result — tracking fixed at the token's −0.01em ≈ −0.18px

| Frame | Candidate | Explore | Plan | max error |
|---|---|---|---|---|
| **Desktop @ 18px** | Regular 400 | 158.4 (−4.6) | 109.4 (−2.6) | 4.62 |
| | **Medium 500** | **163.6 (+0.6)** | **113.4 (+1.4)** | **1.38** |
| | Bold 700 | 169.8 (+6.8) | 118.0 (+6.0) | 6.75 |
| **Mobile @ 16px** | Regular 400 | 140.4 (−5.6) | 96.8 (−2.2) | 5.62 |
| | **Medium 500** | **145.1 (−0.9)** | **100.5 (+1.5)** | **1.50** |
| | Bold 700 | 150.5 (+4.5) | 104.5 (+5.5) | 5.50 |

**Satoshi Medium (500) wins on both frames independently, by a factor of 3–4×.** The two frames are separate measurements of separate images, so agreeing on the same weight is a real cross-check rather than one fit.

The sizes that work — **18px at 1440, 16px at 393** — are exactly the existing `text-button` token: `clamp(1rem, 0.9536rem + 0.1905vw, 1.125rem)`.

### Conclusion

| | |
|---|---|
| Family / weight | **Satoshi Medium 500** — already what `font-medium` asks for |
| Size | **the `text-button` token**, unchanged |
| Tracking | token's `-0.01em` (= −0.18px at 18px, −0.16px at 16px) |

The defect is **not** the weight and **not** the token. It is that the `dark` and `light` button variants hard-code `text-[18px] font-medium leading-[20px] tracking-[-0.18px]` and therefore never apply `text-button` at all — so mobile renders 18px where the design says 16px.

`text-button` already declares `font-sans`, `font-weight: 500`, `line-height: 1.25rem` (= the hard-coded 20px) and `-0.01em`. It is a **drop-in replacement** that changes only the size. No new value is introduced.

### Two claims withdrawn

- **"Matching width ratios prove the typeface is identical."** They do not — a ratio is invariant under uniform scaling and isolates neither weight nor tracking. Superseded by this calibration, which tests candidates directly.
- **"Satoshi Medium is not loading; the site renders 400."** Wrong. `__root.tsx` loads `satoshi@400,500,700` from Fontshare — **500 is available**. That inference rested on a live-site width measured off a resampled phone screenshot, where ±3% is entirely plausible on a 158px string. It was not a reliable measurement and no conclusion should have been drawn from it.

### Confirmed directly, for HOME-18

`__root.tsx` requests `family=Playfair+Display:wght@400` — **400 only**. Every heading above regular weight is therefore unavailable, which is the documented root cause of the heading-weight ticket. Poppins is requested at `wght@500` only.

The same calibration method now applies to the headings: render Playfair at 400/500/600/700 against the h1–h4 crops in these rasters and pick per level. That is the next calibration, and it needs no agency answer — the rasters supply the target.

### Implementation note — construction is chosen, not measured

Target at 393: dark **188**, gap **16**, light **157**, height **44**, row filling 361.

Keeping `px-7` (28px) on both buttons and letting the dark one fill the remaining width reproduces this: light = 100.5 ink + 56 = **156.5 ≈ 157**, leaving 361 − 16 − 156.5 = **188.5 ≈ 188**. That is offered as the simplest implementation reproducing the measured geometry **without inventing a padding value** — not as a claim about how the Figma file is built.

### CORRECTION — the swap is NOT "only the size"

Claim checked property by property rather than asserted. Current `dark`/`light` variants declare `font-sans text-[18px] font-medium leading-[20px] tracking-[-0.18px]`.

| Property | Current (variant) | `text-button` | Same? |
|---|---|---|---|
| font-family | `var(--font-sans)` | `var(--font-sans)` | ✅ |
| font-weight | 500 | 500 | ✅ |
| line-height | 20px | `1.25rem` = 20px | ✅ |
| font-size | **18px fixed** | `clamp(1rem, 0.9536rem + 0.1905vw, 1.125rem)` | ❌ 16px @393 → 18px @1440 |
| letter-spacing | **−0.18px absolute** | **−0.01em relative** | ❌ −0.18px @18px, **−0.16px @16px** |

**Two properties change, not one.** Letter-spacing moves from an absolute value to a relative one, so it only coincides at 18px. At the mobile 16px it becomes −0.16px — a 0.02px difference per gap, or **0.38px** across the 19 gaps of "Explore Our Services".

That does not overturn the calibration (145.5 vs 145.1 predicted, against a 146 target — still inside 1.5px), and a size-relative tracking is arguably the more correct construction. But the earlier "changes only the size" phrasing was wrong and is withdrawn.

**Additional hazard found while checking.** The base `cva` string still carries `text-sm`, which sets font-size *and* line-height. Today `text-[18px]` and `leading-[20px]` override it. Swap those for `text-button` and whether the token wins over `text-sm` depends on generated-CSS order, not class order — the same collision class R7 catalogued. This must be verified from **computed styles in the browser**, not from reading the diff.

Mandatory acceptance: capture `getComputedStyle` for `font-family`, `font-size`, `font-weight`, `line-height` and `letter-spacing` on both buttons at 393, 768 and 1440, **before and after**, and show the two tables side by side. Only font-size and letter-spacing may differ, and only in the directions above.

### CONFIDENCE LABEL — Satoshi Medium 500

Classified **high-confidence raster calibration**, not Figma style metadata. It wins independently on two separate frames by 3–4×, which is strong. But the Figma text-style panel is unavailable, so no claim is made about what the file literally declares. If the panel later becomes readable and disagrees, the panel wins.

### SCOPE — HOME-16 and HOME-18 stay separate

They are different tickets with different components and different risk. HOME-16 is button typography in `ui/button.tsx`; HOME-18 is Playfair heading weights across the type scale, affecting 9 routes. Sharing the hero is not a reason to couple them.

**HOME-16 does not depend on the heading calibration and must not wait for it.** An earlier note said its brief "needs the heading calibration alongside it" — withdrawn. One ticket, one turn.
