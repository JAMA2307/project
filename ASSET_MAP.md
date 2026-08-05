# ASSET MAP — AMARA

Companion to `MASTER_IMPLEMENTATION_LEDGER.md`. Authoritative registry of every visual asset in the project.

| | |
|---|---|
| Project | Lovable `amara-care-site` · `63342c41-9fa9-4f01-81cb-7bab9030a9df` |
| Commit | `93fe1cf1` (Wave 1 applied; Wave 2 in flight) |
| Assets in project | **32** — 8 brand · 21 photo pointers · 2 loose JPG · 1 favicon |
| Updated | 2026-08-04 |

---

## 0 · WHAT THE ARCHIVE ACTUALLY CONTAINS — read first

What was delivered is **18 approved full-page renders** (desktop + mobile × 9 routes), not a folder of individual source files. There is no `hero.jpg`, no `logo-white.svg`, no `watermark.svg` in my possession — the directory tree in the brief describes the *shape* of the library, not files I received.

That distinction matters for exactly one reason: **a page render is a flattened, downscaled composite.** Cropping a photo out of one would be a degraded substitute — precisely what the "never substitute, never generate" rule forbids. So renders are used here for what they legitimately prove:

- **Which image occupies which slot** on every page — this is what makes the mapping below complete and verified rather than guessed.
- **What a missing asset should depict**, described precisely enough to recognise the right file when it arrives.

Every row below is therefore either a real file in the project, or a named gap. Nothing is invented.

**Evidence tags:** `[DA]` approved design render · `[SRC]` source code · `[PRJ]` project file listing.

---

## 1 · BRAND

| Filename | Section / Component | Usage | Status |
|---|---|---|---|
| `brand/logo.png` | Header, Footer · `Logo.tsx` | Full lockup: ring "A" + AMARA + REHAB AND NURSING. Rendered via CSS mask, tinted `currentColor` (navy on light, white on dark). Source 233×64, renders **189×52** | ✅ **VERIFIED** — Wave 1 corrected the size |
| `brand/glyph-ring.png` | `AboutHero`, `AboutMission`, `home/Services`, `ServicesList` | Outlined ring "A". Hero watermark, mission icon, sticky-rail active marker, panel watermark | ✅ IN USE |
| `brand/glyph-white.png` | `WhatSetsUsApart`, `CareApproach`, `ServicesList`, `Cta` | White "A". **Misused in `Cta.tsx:39`** as a 72px repeating tile standing in for `pattern-cta-bg.png` | ⚠️ **SILENT SUBSTITUTE** — AST-04 |
| `brand/hero-pattern-tile.png` | `home/Hero` | 121×114 repeating diamond, 6% opacity behind the hero | ✅ IN USE |
| `brand/footer-mark.png` | `Footer` | Oversized ringed "A" watermark, cropped by the footer edges | ✅ IN USE |
| `brand/plane-glyph.png` | `WhatSetsUsApart` — Guided care | 21×21 plane, pinned off the ring's lower-right | ✅ IN USE |
| `brand/icon-house.png` | `home/Hero` — badge | House icon in the accent chip, "Where Healing Feels Like Home" | ✅ IN USE |
| `brand/monogram-a.png` | — | No reference found in any component `[SRC]` | ⚠️ **ORPHAN** — verify before deleting |
| `public/favicon.png` | global | Browser tab icon | ✅ IN USE |

### Brand assets that do NOT exist and are being faked

| Needed | Faked by | Location | Ledger |
|---|---|---|---|
| `pattern-cta-bg.png` — diamond/logo pattern, very low opacity | `glyph-white.png` tiled at 72px | `Cta.tsx:39` | AST-04 |
| Real Figma "A" vector | **hand-drawn SVG** — `AMark`, a circle + triangle authored in code | `Logo.tsx:38` → `/services` 24/7 badge | **AST-02** |
| `icon-comfort-care.svg` — outlined nurse/person, **not a heart** | `<PlaceholderAsset>` | `CareApproach.tsx:78` | AST-05 |
| `icon-leaf.svg` — leaf in a solid navy filled circle | `<PlaceholderAsset>` | `CareApproach.tsx:105` | AST-06 |

The measured spec is explicit: *"must be the real logo asset — **never the drawn SVG**."* `AMark` violates it by name.

---

## 2 · ICONS

All UI icons are **`lucide-react`**, not files: `ArrowDown` `ArrowLeft` `ArrowRight` `ArrowUpRight` `Menu` `X` `MapPin` `Phone` `Check` `HeartPulse` `Pill` `HandHeart` `Home` `Activity` `Users`. No icon files exist in the project. Only the two brand icons above are file-based, and both are missing.

---

## 3 · BACKGROUNDS

| Asset | Component | Treatment |
|---|---|---|
| `hero-pattern-tile.png` | `home/Hero` | repeat, `opacity .06` |
| `frosted-lounge.png` | `AboutHero` | full-bleed cover + `rgba(12,16,32,.22)` scrim + bottom gradient |
| `care-team.webp` | `CareersHero` | full-bleed cover + gradient |
| `glyph-white.png` | `Cta` left card | 72px repeat — **substitute**, see §1 |
| `blurred-card-placeholder.png` | `CareApproach` 24/7 panel | cover + `bg-primary/35` + `blur-[2px]` — **a file literally named "placeholder" shipped as content** |

---

## 4 · PAGE → SECTION → COMPONENT → ASSET

### HOME · `/`
| Section | Component | Asset | Status |
|---|---|---|---|
| Hero | `home/Hero` | `reception-signage.png` — reception desk, AMARA sign, starlit ceiling | ✅ matches `[DA]` |
| Hero background | `home/Hero` | `hero-pattern-tile.png` | ✅ |
| Hero badge | `home/Hero` | `brand/icon-house.png` | ✅ |
| What sets us apart — Inviting spaces | `WhatSetsUsApart` | `great-room-piano.webp` | ✅ matches `[DA]` |
| — Guided care | `WhatSetsUsApart` | `glyph-white.png` + `plane-glyph.png` | ✅ |
| — Connected support | `WhatSetsUsApart` | `care-team.webp` | ✅ matches `[DA]` |
| Our Mission | `home/Mission` | `glyph-ring.png` | ✅ |
| Personalized Care panel 1 | `home/Services` | `clinician-resident.webp` | ✅ |
| — panel 2 | `home/Services` | `therapy-gym.webp` | ✅ |
| — panel 3 | `home/Services` | `family-album.webp` | ✅ |
| — panel 4 | `home/Services` | `lounge-dining.webp` | ✅ |
| Testimonials 1 / 2 / 3 | `Testimonials` | `family-album` / `resident-son` / `clinician-resident` | ✅ |
| Gallery — top-left | `Gallery` | `great-room-piano.webp` | ✅ |
| — bottom-left | `Gallery` | `lobby-wide.webp` | ✅ |
| — centre | `Gallery` | `reception-desk.webp` | ✅ |
| — top-right | `Gallery` | `therapy-gym.webp` | ✅ |
| — bottom-right | `Gallery` | `lounge-dining.webp` | ✅ |
| ~~CTA~~ | — | **Home has no CTA section** `[DA]` | 🔧 NEW-01, Wave 2 |

### ABOUT · `/about`
| Section | Component | Asset | Status |
|---|---|---|---|
| Hero | `AboutHero` | `frosted-lounge.png` + `glyph-ring.png` | ✅ matches `[DA]` |
| About Us — photo 1 | `AboutIntro` | `gym-session.webp` | ✅ |
| — photo 2 | `AboutIntro` | `bedside-care.webp` | ✅ |
| Our Mission | `AboutMission` | `glyph-ring.png` | ✅ |
| What We Value — card 1 | `AboutValues` | `clinician-resident.webp` | ✅ |
| — card 2 | `AboutValues` | `lounge-dining.webp` | ✅ |
| — **card 3** | `AboutValues` | `therapy-gym.webp` | ❌ **SUBSTITUTED DUPLICATE** — AST-01 |
| — **card 4** | `AboutValues` | `care-team.webp` | ❌ **SUBSTITUTED DUPLICATE** — AST-01 |
| Meet the Team | `AboutTeam` | initials only, no photos | ✅ matches `[DA]` |
| CTA | `Cta` | `garden-walk.webp` | ✅ matches `[DA]` |

> The measured spec named these two slots as **knowingly missing**: *"Keep the two knowingly-missing slots (About values 3-4 photos, Amenities Community card) as-is."* They were filled with photos already used on four other sections. This is the single clearest violation of "never reuse another section's image."

### SERVICES · `/services`
| Section | Component | Asset | Status |
|---|---|---|---|
| Hero | `ServicesHero` | `parallel-bars-therapy.webp` | ✅ matches `[DA]` |
| Care approach — left top | `CareApproach` | `building-entrance.webp` | ✅ |
| — blue card icon | `CareApproach` | `icon-comfort-care.svg` | ❌ **MISSING** |
| — centre | `CareApproach` | `walker-hallway.webp`, `object-position 50% 35%` | ✅ |
| — centre overlay icon | `CareApproach` | `icon-leaf.svg` | ❌ **MISSING** |
| — 24/7 background | `CareApproach` | `blurred-card-placeholder.png` | ❌ **SILENT PLACEHOLDER** — AST-03 |
| — 24/7 badge | `Logo.AMark` | hand-drawn SVG | ❌ **DRAWN SUBSTITUTE** — AST-02 |
| Our Services — Short-Term Rehab | `ServicesList` | `service-short-term-rehab.jpg` | ❌ **MISSING** |
| — Long-Term Care | `ServicesList` | `lounge-dining.webp` | ✅ |
| — Indian Program | `ServicesList` | `resident-son.webp`, alt reads *"Freshly prepared meal"* | ⚠️ **alt mismatch** — CNT-08 |
| — Clinical Support | `ServicesList` | `clinician-resident.webp` | ✅ |
| FAQ | `Faq` | none | 🔧 moving here, Wave 2 |
| CTA | `Cta` | `garden-walk.webp` | ✅ |

### AMENITIES · `/amenities`
| Section | Component | Asset | Status |
|---|---|---|---|
| Hero | `AmenitiesHero` | `amenities-hero-woman-reading.png` 2048×768 | ❌ **MISSING** — `HERO_IMAGE = null` |
| Carousel — Accommodations | `AmenitiesCarousel` | `admissions-room.png` | ❌ MISSING — **see §6 lead** |
| — Services | `AmenitiesCarousel` | `admissions-salon.png` | ❌ MISSING |
| — Community | `AmenitiesCarousel` | `admissions-lounge.png` | ❌ MISSING — *spec-acknowledged* |
| Gallery — centre | `AmenitiesGallery` | `amenities-courtyard.jpg` "Serene Courtyard Retreat" | ✅ matches `[DA]` |
| Gallery — sides 01 / 03 | `AmenitiesGallery` | therapy gym / piano lounge | ✅ matches `[DA]` |
| CTA | `Cta` | `garden-walk.webp` | ✅ |

### CAREERS · `/careers`
| Section | Component | Asset | Status |
|---|---|---|---|
| Hero | `CareersHero` | `care-team.webp` — staff group outside the building | ✅ matches `[DA]` |
| Why Amara | `CareersIntro` | **photo missing** — `[DA]` shows an older couple embracing outdoors, left of the text | 🔧 **NEW-02**, Wave 2 |
| Open positions | `OpenPositions` | none | ✅ |
| Team | `CareersTeam` | initials only | 🔧 NEW-03 — 8-up 3-col, Wave 2 |
| Testimonials | `Testimonials` | standard family set | ✅ CNT-01 fixed Wave 1 |

### CONTACT · `/contact`
| Section | Component | Asset | Status |
|---|---|---|---|
| Hero | `ContactHero` | `reception-closeup.webp` | ✅ matches `[DA]` |
| Simple Steps to Admission | `ContactAdmissions` | `lobby-wide.webp` | ✅ matches `[DA]` |
| Insurance | `ContactInsurance` | `clinician-resident.webp` | ✅ matches `[DA]` |
| Contact form | `home/Contact` | none | ✅ |

### FOOTER · global
`brand/logo.png` (white variant) · `brand/footer-mark.png` watermark. ✅ — social link *targets* are wrong (CNT-07) and the design is internally inconsistent between Instagram and Facebook (NEW-04, awaiting ruling).

### LEGAL · `/privacy-policy`, `/terms-of-use` · and `404`
No page assets. Header + footer only. `[DA]` confirms. 404 uses the oversized ring "A" motif — ✅.

---

## 5 · REUSE HEAT MAP

Overused files are how substitutions hide. Flagged, not yet acted on:

| Asset | Uses | Concern |
|---|---|---|
| `clinician-resident.webp` | **5** — home/Services, Testimonials 3, AboutValues 1, ServicesList, ContactInsurance | Highest reuse on the site |
| `lounge-dining.webp` | **4** — home/Services, Gallery, AboutValues 2, ServicesList | |
| `therapy-gym.webp` | **3** — home/Services, Gallery, **AboutValues 3** | AboutValues use is a substitution |
| `care-team.webp` | **3** — WhatSetsUsApart, CareersHero, **AboutValues 4** | AboutValues use is a substitution |
| `resident-son.webp` | 2 — Testimonials 2, ServicesList Indian Program | alt text mismatch |

---

## 6 · OPEN LEAD — resolvable without you

`src/assets/amenities-room.jpg` exists in the project and is **referenced by nothing** `[PRJ][SRC]`.

The Amenities render `[DA]` shows the Accommodations card holding a resident bedroom — bed, wall-mounted TV, dresser, bathroom door — which is exactly how `admissions-room.png` is described. An unused file named `amenities-room.jpg` is a strong candidate for that slot.

I cannot open it: the Lovable API returns binaries as `binary: true` with no content, and this environment's network policy blocks `*.lovable.app` (403 on CONNECT). **The Lovable agent can see it.** Queued for Wave 3: have the agent open both `amenities-room.jpg` and `amenities-courtyard.jpg`, compare against the design description, and wire them if they match — otherwise leave the placeholders. No manual mapping needed from you.

---

## 7 · MISSING ASSET REGISTER — 11 open

Ordered by visual impact.

| # | Asset | Page · Component | Depicts `[DA]` | State |
|---|---|---|---|---|
| 1 | `amenities-hero-woman-reading.png` 2048×768 | Amenities · `AmenitiesHero` | Woman in light-blue sweater reading on a beige sofa, two residents talking behind | `PlaceholderAsset` |
| 2 | `admissions-room.png` | Amenities · Accommodations | Resident bedroom — bed, TV, dresser, bathroom door | `PlaceholderAsset` · **§6 lead** |
| 3 | `admissions-salon.png` | Amenities · Services | On-site beauty salon interior | `PlaceholderAsset` |
| 4 | `admissions-lounge.png` | Amenities · Community | Lounge with grand piano | `PlaceholderAsset` |
| 5 | `service-short-term-rehab.jpg` | Services · `ServicesList` | Therapist assisting an older man with dumbbells | `PlaceholderAsset` |
| 6 | `icon-comfort-care.svg` | Services · `CareApproach` | Outlined nurse/person — **not a heart** | `PlaceholderAsset` |
| 7 | `icon-leaf.svg` | Services · `CareApproach` | Leaf in a solid navy circle | `PlaceholderAsset` |
| 8 | 24/7 panel background | Services · `CareApproach` | Blurred clinical interior | **silent placeholder** |
| 9 | Brand "A" vector | Services · 24/7 badge | Real ring mark | **hand-drawn SVG** |
| 10 | AboutValues photos 3 & 4 | About · `AboutValues` | Recovery-focused support · Respect & dignity | **reused duplicates** |
| 11 | `careers-intro-couple.jpg` | Careers · `CareersIntro` | Older couple embracing outdoors, warm daylight | absent |
| 12 | `pattern-cta-bg.png` | Home/About/Services · `Cta` | Low-opacity diamond pattern | **glyph tiled as substitute** |

Rows 8, 9, 10 and 12 are the dangerous ones — they render as finished work.

**All 12 are BLOCKED on the same thing:** Figma export, which needs the account upgraded from a **View seat** (6 MCP calls/month, exhausted) to **Dev or Full** (200/day). The renders identify every one of them; only the file transfer is blocked.

---

## 5 · FULL PRODUCTION ARCHIVE — WAVES 10–14 · 2026-08-05 · **32/32 INTEGRATED**

Five archives (About, Services, Admissions, Careers, Contact), 32 files, all full-resolution official exports. **Every one integrated. Zero rejected.**

### ✅ RESULT: ZERO PLACEHOLDERS SITE-WIDE
`grep -rn "PlaceholderAsset" src/` returns **only the component definition** — no component renders one. DOM placeholder count = **0 across all 9 routes × all 7 widths**. Every gap opened in the original audit is closed.

| Wave | Page | Files | Gaps closed |
|---|---|---|---|
| 10 | About | 10 | `about-values-3-recovery`, `about-values-4-dignity` · Lucide `HeartPulse`/`Pill` → official icons |
| 11 | Services (hero + care approach) | 7 | `icon-comfort-care.svg`, `icon-leaf.svg`, **`blurred-card-placeholder.png`** |
| 12 | Services (panels) | 4 | `service-short-term-rehab.jpg` · Indian Program alt-text mismatch |
| 13 | Amenities | 4 | **`amenities-hero-woman-reading`** (open since 08-04), `admissions-salon`, `admissions-lounge` |
| 14 | Careers + Contact | 4 | **`careers-intro-couple`** — the last placeholder in the project |

### Content beat filename — three times
The agent inspected artwork before wiring rather than trusting names:

- **`Accommodations 2.png` is not an Accommodations photo.** It is a sunlit dayroom with sofas, dining tables and a **grand piano** → assigned to the **Community** card ("large dayrooms and lounges / musical entertainment"). Filename misleading; content decisive.
- **`Comprehensive Care.png` has the pill baked in**, including rounded corners → the DOM pill span was removed so we don't ship two.
- **`skilled nursing…png` contains only the blurred photograph** — no dark overlay, no circled "A" → both existing DOM layers kept rather than assumed redundant.

### `admissions-room.jpg` superseded
My Wave-3 find (an unused project file) was a bedroom but **had no bathroom door**. The official `admissions-accommodations.png` does, matching the charter spec exactly, and is portrait for the 296×360 slot. Replaced with reason. The old file remains on disk, unreferenced.

### The alpha trap — caught twice more
Three supplied assets are authored at 2–5% alpha (`hero-pattern-full` 5/255, `Comfort Care Compassion` 13/255). Applying the project's conventional low opacity on top renders them invisible — the Wave-9 hero failure. The agent now checks alpha extrema before wiring; both later cases were rendered at opacity 1 and are visible.

### Legacy assets still in use — 10 `.webp`, all legitimate
`family-album`, `resident-son`, `clinician-resident` (Testimonials) · `great-room-piano` ×2, `lobby-wide`, `lounge-dining` ×2, `therapy-gym` ×2, `reception-desk`, `reception-closeup` ×2 (Home Gallery, Amenities Gallery, Contact hero) · `garden-walk` (shared CTA default). **No official export was supplied for any of these slots.** Everything else on the site is now an official `.png`.

### Verification
63/63 responsive cells pass (9 routes × 7 widths, 390→1920). Zero 404s, zero console errors, no CLS, no distortion — natural vs rendered checked per photo, all `object-cover`. Full Wave 1–9 regression intact.

*Noted, not a defect:* one headless run reported `naturalWidth 0` on the third Testimonials image; direct fetch returned HTTP 200, 80,996 bytes, decoding to 1086×1448. Transient headless decode.

## 6 · WAVES 8–9 — VISIBILITY CORRECTIONS · 2026-08-05

Wave 7 wired elements correctly and reported measurements — but three of them were **present in the DOM and invisible on screen**. "Wired" was the wrong pass condition; "renders visible pixels" is the right one. All three found and fixed.

| Element | Failure | Fix |
|---|---|---|
| Hero pattern | `opacity: .06` carried over from the old solid 121×114 tile. The official asset is drawn at **max alpha 5/255 (≈2%)** — 2% × 6% ≈ 0.1%, below display quantisation, literally unrenderable | opacity → **1**, `background-size` `1440px 1200px` → **`cover`**. `Hero.tsx` only |
| Plane glyph | positioned at `-bottom-30 -right-30` — **rendered outside the card bounds**, never on screen | repositioned inside the ring's lower-right, opacity 1, 21×21 |
| Panel watermark | white artwork at opacity .18 on a near-white panel — effectively invisible | opacity → **0.85** |

**Wave 8 also delivered:** `footer-logo-official.png` as both the footer lockup and a **557px bottom-cropped watermark**, footer height exactly 580 · **Facebook removed from the Home footer, LinkedIn + Instagram in its place**, via a configurable `socials` prop so the other six pages were untouched · `guided-care-ring-official.jpg` white-masked to transparent for the blue card · `our-mission-mark-official.png` above the Mission heading · `rail-marker-official.png` on the active rail item.

### ⚠️ HERO PATTERN — the file is the ceiling

Verified by rendered-pixel sampling at 1440, paired against the asset's own alpha map (35,484 motif px vs 158,328 bare px in the header band):

- on-motif mean RGB **218.66, 227.32, 243.55**
- bare background mean RGB **221.60, 230.27, 246.52**
- **delta ≈ 2.95 per channel**

The pattern is measurably present and no longer invisible. But **≈3 RGB levels is near the threshold of perception** on most displays. That is the *maximum* this file can produce: its artwork is authored at **alpha 5/255**, and opacity is already 1 with no filter, blend mode or tint.

If the design intends a more discernible pattern, **the asset must be re-exported at the intended alpha** — it cannot be recovered by CSS without manipulating the artwork, which the brief forbids.

### Known, deliberately left
`Cta.tsx` still imports `hero-pattern-tile.png` — the documented stand-in for the still-missing `pattern-cta-bg.png`. Removing it would blank the CTA background on three pages.

## 7 · DELIVERY LOG — `Logos_and_elements.rar`, 2026-08-05 07:35 · **5 INTEGRATED, 3 SKIPPED**

| Package file | Export | Destination | Outcome |
|---|---|---|---|
| `Home page hero backgraund.png` | **1440 × 1200** RGBA | `home/Hero` background | ✅ **Integrated** — full-bleed no-repeat layer at `top center`, opacity .06. **CSS tiling of the 121×114 tile removed** — pattern rhythm now matches the design instead of being re-tiled |
| `Guided care/elements (1).png` | 21 × 21 RGBA | `WhatSetsUsApart` — plane glyph | ✅ Integrated — exact match to the 21×21 render box |
| `Personalized…(with text).png` | 19 × 24 RGBA | `home/Services` — rail active marker | ✅ Integrated — exact match to the 19×24 render box |
| `Personalized….png` | **312 × 233** RGBA | `home/Services` — panel watermark | ✅ Integrated — **landscape at natural size, rotation removed.** Was a portrait glyph rendered 238×314 at `rotate(-15deg)`; now the official artwork bottom-right, cropped by the card edge, opacity .18 |
| `Where Healing Feels Like Home.png` | 18 × 16 RGBA | `home/Hero` badge icon | ✅ Integrated **at natural size** — render box reduced 20×20 → 18×16 inside the unchanged 40×40 chip, so no upscale |

**SKIPPED — 3, byte-identical to files already rejected twice.** Not re-exported in any delivery: `Our Mission.png` 91×120 (renders at 135), `footer logo.png` 333×272, `Guided care/Pattern (1).jpg` 141×186 (renders at 165×205). Each is smaller than the asset it would replace. **SVG re-export closes all three permanently.**

**Open question for the designer:** the official panel watermark is white artwork. At opacity .18 on the `#E6EFFF` panel it reads as a very faint *lighter* mark, where the previous approximation was a darker ring. Confirm the intended tone/opacity.

## 7a · DELIVERY LOG — `Home_Page.rar` v2, 2026-08-04 22:11 · **7 INTEGRATED, 4 SKIPPED**

Second archive, 15.8 MB, 11 files. Extracted, dimension-checked, and every photograph opened and visually verified against its destination before wiring. Integrated in **Wave 6** — all 9 checks pass.

### ✅ REPLACED — 7 production photographs

| Package file | Export | Destination | Replaced | Uplift |
|---|---|---|---|---|
| `Comfort You Can Trust (2).png` | **1672 × 941** | `home/Hero` — hero photo | `reception-signage.png` | slot 1280×720, AR 1.777 vs 1.778 — exact |
| `Inviting spaces.png` | **1086 × 1448** | `WhatSetsUsApart` card 1 | `great-room-piano.webp` | slot 413×460 |
| `Connected support.png` | **1086 × 1448** | `WhatSetsUsApart` card 3 | `care-team.webp` | slot 413×460 |
| `Planning & Care Coordination.png` | **1086 × 1448** | `home/Services` panel 1 | `clinician-resident.webp` | slot 265×200 |
| `Short-Term Rehabilitation.png` | **1254 × 1254** | `home/Services` panel 2 | `therapy-gym.webp` | slot 329×200 |
| `Social Services.png` | **1672 × 941** | `home/Services` panel 3 | `family-album.webp` | slot 329×200 |
| `Dining & Nutrition.png` | **1086 × 1448** | `home/Services` panel 4 | `lounge-dining.webp` | slot 329×200 |

Wired via `.asset.json` imports. `object-cover`, `object-position`, radius and slot geometry all unchanged — source only. Intrinsic `width`/`height` added to each so nothing shifts on load. Alt text rewritten to describe the new photography. **The old `.webp` assets were retained** — About, Services, Careers and Contact still import them, so no other page's photography moved.

Source images are portrait or square against landscape slots; that is expected — `object-cover` crops exactly as the Figma frame does. No stretching, no letterboxing, no aspect change.

### ⏭️ SKIPPED — 4 files, byte-identical to the rejected first archive

These were **not re-exported** between deliveries — same byte sizes as v1. Every one is *smaller* than the asset it would replace, so integrating them would breach "never replace a better asset with a worse one".

| File | Size | Would replace | Current render size | Verdict |
|---|---|---|---|---|
| `Our Mission.png` | 91 × 120 | `glyph-ring.png` | 135 px tall | **smaller** → skipped |
| `Guided care 1.jpg` | 141 × 186 | `glyph-white.png` | 165 × 205 | **smaller** → skipped |
| `Footer Logo.png` | 333 × 272 | `footer-mark.png` | large, cropped by a 580-tall footer | **smaller** → skipped |
| `Guided care 2.jpg` | 655 B | `plane-glyph.png` 21×21 | — | **corrupt** — extracts to 0 bytes, both deliveries |

All four are brand glyphs. **Re-export as SVG** and they become resolution-independent, ending this class of problem permanently.

## 7b · DELIVERY LOG — `Home_Page.rar` v1, 2026-08-04 · **REJECTED, NOT INTEGRATED**

Archive received, RAR5, 102 KB, 11 files. Extracted and inspected in full. **Not wired into the project — every file is a thumbnail, not a production asset.**

| File in package | Actual size | Destination slot | Slot needs | Upscale required |
|---|---|---|---|---|
| `Comfort You Can Trust.png` | **80 × 62** | `home/Hero` photo | 1280 × 720 | **16×** |
| `Inviting spaces.png` | **80 × 62** | `WhatSetsUsApart` card 1 | 413 × 460 | ~7× |
| `Connected support.png` | **80 × 62** | `WhatSetsUsApart` card 3 | 413 × 460 | ~7× |
| `Guided care 1.jpg` | **141 × 186** | Guided care ring glyph | 165 × 205 | 1.2× |
| `Guided care 2.jpg` | **corrupt** — 655 B, extracts to 0 B | plane glyph | 21 × 21 | — |
| `Our Mission.png` | **91 × 120** | mission ring glyph | ≥135 tall | 1.1× |
| `Planning & Care Coordination.png` | **80 × 62** | services panel 1 photo | 265 × 200 | ~3.3× |
| `Short-Term Rehabilitation.png` | **80 × 62** | services panel 2 photo | 329 × 200 | ~4× |
| `Social Services.png` | **80 × 62** | services panel 3 photo | 329 × 200 | ~4× |
| `Dining & Nutrition.png` | **80 × 62** | services panel 4 photo | 329 × 200 | ~4× |
| `Footer Logo.png` | **333 × 272** | footer watermark | cropped by a 580-tall footer | — |

**Why rejected.** Three independent reasons, any one sufficient:

1. **Every file is smaller than the slot it would fill.** Not one asset in this package improves on what is already wired. The hero would upscale 16×.
2. **The Home page has no missing images.** Every slot listed above already holds a correct full-resolution photo, verified against the approved renders across Waves 1–5, with zero image 404s on the final sweep. Integrating this package would *replace working assets with thumbnails* — a pure regression.
3. **One file is corrupt.** `Guided care 2.jpg` fails extraction: *"Attempted to read more data than was available."*

This is the "no stretching, no incorrect crop, preserve proportions" rule doing its job. Upscaling an 80×62 JPEG-artefacted thumbnail into a 1280×720 hero is precisely the quality destruction the charter exists to prevent.

**Required to proceed — re-export at native resolution, 2× preferred:**

| Slot | 1× | 2× (recommended) |
|---|---|---|
| Home hero | 1280 × 720 | 2560 × 1440 |
| WhatSetsUsApart cards ×3 | 413 × 460 | 826 × 920 |
| Services panel 1 | 265 × 200 | 530 × 400 |
| Services panels 2–4 | 329 × 200 | 658 × 400 |
| Ring / plane glyphs | — | **SVG preferred** |
| Footer watermark | large enough to crop at 580 tall | SVG preferred |

In Figma: select the frame → Export → set scale to 2× → PNG for photography, SVG for glyphs. The 80×62 output indicates the export was taken from a layer thumbnail or a 0.0625× scale rather than the frame itself.

## 8 · CONVENTIONS

**Reference assets via `.asset.json` import**, never a raw URL:
```ts
import gardenWalk from "@/assets/photos/garden-walk.webp.asset.json";
const CTA_IMAGE = gardenWalk.url;
```
**18 hardcoded `/__l5e/assets-v1/<uuid>/…` strings remain** (COD-01) — a re-upload changes the UUID and the image 404s with no build error.

**Naming:** `photos/` descriptive-kebab · `brand/` role-based · page-specific may carry a page prefix. Formats: `.webp` photography · `.png` transparency · `.svg` icons/vectors. Radius 24px cards & images, 16px card-internal photos. Every `<img>` needs alt text that matches what the file shows (CNT-08 is an open violation).

**Never:** generate replacements · use stock · reuse another section's image · draw a substitute logo · recreate the brand mark in CSS · leave a container empty · hide a gap behind blur or gradient. If an asset is absent → `<PlaceholderAsset name="exact-filename.ext" />` and list it here.
