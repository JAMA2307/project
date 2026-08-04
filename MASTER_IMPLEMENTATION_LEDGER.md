# MASTER IMPLEMENTATION LEDGER — AMARA

Single cumulative ledger. Supersedes audits v1–v3. **Never fork into v4/v5.** Update in place.

| | |
|---|---|
| Project | Amara Care Center — skilled nursing & rehab, 25 5th Avenue, Haskell NJ 07420, 973-839-6000 |
| Implementation | Lovable `amara-care-site` · `63342c41-9fa9-4f01-81cb-7bab9030a9df` · workspace "AMIR's startup" |
| Commit audited | `daae8f96fed07dc82eb336e99a2c2220f62f311d` |
| Live | https://amara-care-site.lovable.app (published) |
| Figma | `Tm96OSYcEv6kdVzIqHYKeP` — *Amara x Mozart* |
| Stack | TanStack Start · React · TypeScript · Tailwind v4 · shadcn/ui |
| Ledger updated | 2026-08-04 |
| Mode | **AUDIT ONLY** — no code modified, no assets uploaded, no Lovable prompts sent |

---

## 0 · GOVERNING AUTHORITY — standing rule, 2026-08-04

> **When written instructions conflict with the final approved design, the final approved design wins.**
> The latest approved design overrides earlier written instructions unless explicitly told otherwise.

Order of authority: **1.** Final approved design (Figma file / exported design archive) → **2.** Explicit designer override issued *against* the design → **3.** Earlier written specs → **4.** Implementation (never authoritative).

### 0.0 · EXPLICIT OVERRIDES — the design is deliberately NOT followed here

These three are mock typos the designer explicitly ruled on. They are level-2 authority and **outrank the design**. Never "restore" them to match the renders.

| Design render shows | Ship instead | Ruling |
|---|---|---|
| `Shedule a Tour` | **`Schedule a Tour`** | 08-04 14:55 — *"mock's 'Shedule' is a typo"* |
| `Enter email addres` | **`Enter email address`** | 08-03 20:03 mobile QA — supersedes the 08-01 "keep this exact spelling" |
| `Brookwood provides a full spectrum…` | **`Amara provides a full spectrum…`** | 08-04 14:55 — *"NOT 'Brookwood', that is a mock typo"* |

Also deliberate: `oncommunity` → **`on community`** (spaced).

## 0 · EVIDENCE CLASSIFICATION

Per the honesty requirement, every finding carries its source.

| Tag | Meaning | Coverage achieved |
|---|---|---|
| **[DA]** | **Verified from the design archive** — 18 approved full-page renders, desktop + mobile × 9 routes, received 2026-08-04 | **Complete page coverage.** Highest authority |
| **[F]** | Verified from Figma MCP | **Top-level page index ONLY** — 2 pages: `187:1361` *Design*, `369:17180` *UI kit* |
| **[LH]** | Verified from Lovable history | **Complete.** All 4 history pages, 07-29 → 08-04, `has_more: false` |
| **[SRC]** | Verified from source code | 35 of 37 project files |
| **[INF]** | Inferred — needs confirmation | flagged individually |
| **[BLK]** | Blocked | Figma frames, comments, prototype, assets |

### 0.1 · WHAT WAS **NOT** INSPECTED — stated plainly

I did **not** read a single Figma frame, layer, comment, prototype flow, variable, or asset. Two `get_metadata` calls were attempted (15:51 and 19:14); both returned:

> *You've reached the Figma MCP tool call limit for your **View seat** on the **Professional plan**.*

Per Figma's published entitlement table, **View/Collab seats get 6 MCP tool calls per month on every plan tier.** The budget is spent and does not reset until next month.

**Unchecked and unreadable:**

| Target | Node | Status |
|---|---|---|
| Page *Design* | `187:1361` | **BLOCKED** — never opened |
| Page *UI kit* | `369:17180` | **BLOCKED** — never opened |
| Node from your URL | `357:7322` "Group 2141256309 1" | **BLOCKED** |
| All frames, all pages | — | **BLOCKED** |
| **All designer comments** | — | **BLOCKED — zero comments read** |
| Prototype / interactions | — | **BLOCKED** |
| Variables & styles | — | **BLOCKED** |
| Asset export | — | **BLOCKED** |

**Every "expected" value in this ledger comes from [LH] — the designer's own Figma-extracted written specs — not from the file.** No Figma frame, comment, or layer has been inspected. I will not claim otherwise.

**Unblock:** upgrade `oybekovj97@gmail.com` from **View** to **Dev or Full** on the Professional plan owning *Amara x Mozart*. 6/month → 200/day, 15/min. Dev seat suffices.

### 0.2 · AUTHORITATIVE SOURCES RECOVERED [LH]

Found by mining project history, not supplied:

1. **Foundation brief** (08-01 07:35) — tokens, 3 font families, full type scale incl. mobile, layout grid.
2. **Global components brief** (08-01 07:38) — Button/Header/Footer measurements.
3. **FIGMA SYNCHRONIZATION PASS** (08-03 12:39) — *"AUTHORITATIVE numbers from the Figma node tree. Where the implementation differs, the implementation is wrong."* Section heights, per-section bounding rects, 14 verification checks.
4. **Testimonials rebuild spec** (08-03 12:52) — pixel-measured from the design export.
5. **Structure & copy spec** (08-04 14:55 / 15:03) — About vs Services order, team roster, mock typos.
6. **Interaction spec** (08-04 15:19) — scroll reveal mechanics, hover system.
7. **Section rebuild specs** (08-04 15:26 Amenities hero / 15:29 Admissions carousel).

---

## 1 · DESIGN SYSTEM — VERIFIED CORRECT

`src/styles.css` matches the foundation brief exactly. **Do not touch these.** [LH][SRC]

**Colours** `#2C2E45` primary · `#4B5066` muted-foreground · `#56677F` accent · `#E6F0FF` secondary-bg · `#0F0F0F` heading · `#441802` label-brown ✓
**Radius** 16px buttons · 24px cards/images ✓
**Type scale** h1/h2 44/52 @-1% · h3 40/48 @-1% · h4 24/32 · body 18/24 · body-large 20/32 · button 18/20 @-0.18px · label 16/22 · eyebrow 14/20 lowercase +2% ✓
**Mobile scale** h1/h2 32/40 · h3 28/36 · body 16/22 ✓
**Layout** container 1280 @ 80px padding (1440 viewport) · 16px mobile · breakpoint 768 ✓
**Fonts** Playfair Display 400, Poppins 500 (Google), Satoshi 400/500/700 (Fontshare) — **all three present** in `__root.tsx` links. The Aug-1 instruction *"verify Satoshi actually loads… tell me explicitly rather than silently falling back"* is **satisfied**. ✓
**Buttons** L 48px @14/28 · S 44px @12/28 ✓
**Interaction layer** `--ease-premium cubic-bezier(.22,1,.36,1)` · 260ms · `hover-lift` / `hover-card` / `hover-underline` · `:focus-visible` · `prefers-reduced-motion` ✓

**Every typography defect below is a component overriding a correct scale — the system is not at fault.**

---

## 2 · PRIORITY ORDER

1 Visual mismatch · 2 Missing assets · 3 Typography · 4 Spacing · 5 Responsive · 6 Animation · 7 Hover · 8 Navigation · 9 Content integrity · 10 Code quality

---

## 3 · VISUAL GEOMETRY — `VIS`

All expected values [LH] from the 08-03 12:39 / 12:52 specs. Status **VERIFIED**, QA `n/a`, no blockers, no asset dependency unless noted.

| ID | Page | Component | Current [SRC] | Expected [LH] | Root cause |
|---|---|---|---|---|---|
| **VIS-01** | Home, About, Services, Careers | `Testimonials.tsx:120` | card **1080×400**, padding `p-5`=20, photo **360×360** | card **847×440**, padding **24**, photo **389×392** r16 | 12:52 rebuild spec not applied |
| **VIS-02** | Services | `ServicesHero.tsx:44,14` | photo **385×430**, left col **522** | photo **630×720**, left col **413** | built before sync pass |
| **VIS-03** | Amenities | `AmenitiesCarousel.tsx:151` | card **940×420**, photo **356** | card **846×450**, photo **~296×360** | 15:29 rebuild used prose, not the measured 846 |
| **VIS-04** | Services | `CareApproach.tsx:31` | row `h-[580px]`, cols `300fr/600fr/320fr`, stack `h-[282px]` | row **460**, cols **306/621/313**, stack **306×220** | 14:55 "increase size" applied without the measured target |
| **VIS-05** | Services, Careers | `AboutTeam.tsx:21,49` | monogram **95×95**, gap **17** | monogram **68×68**, gap **20** | — |
| **VIS-06** | Home | `WhatSetsUsApart.tsx:31,41` | cards **413×505**, intro `max-w-[660px]` | cards **413×460**, intro **774** | width correct, height/measure not |
| **VIS-07** | Home | `home/Services.tsx:213` | photos **259×201** all panels, r **24→32** | **265×200** panel 1, **329×200** panels 2-4, r **16** | no per-index variation |
| **VIS-08** | About | `AboutIntro.tsx:52,41` | photos **630×420**, `gap-4`=16 | **630×380**, gap **20** | — |
| **VIS-09** | all | `Header.tsx:43,48` | row `h-[64px]`, logo `md:h-[64px]` | header **52**, logo **189×52** | `top-6`=24 offset ✓ correct |
| **VIS-10** | Home, About, Careers | `Faq.tsx:64` | `grid-cols-[440fr_820fr]` | left **~490**, right **680–770** | — |
| **VIS-11** | Home, About, Services | `Cta.tsx:60` | `md:min-h-[560px]` | image **630×660** | — |
| **VIS-12** | Home | `Mission.tsx:44` | `max-w-[1120px]`, lh **52** | `max-width` **900**, lh **56**, exactly 3 lines | 1120 measure destroys the 3-line wrap |

### VIS-13 · Section heights — 13 violations of the fixed-height rule

Spec [LH]: *"vertical rhythm comes from these fixed section heights, NOT from py-\*. Replace big py paddings with min-h + flex centering. There must be NO extra white gaps between sections."* Priority **Critical** — governs whole-page rhythm.

| Section | Expected | Current | |
|---|---|---|---|
| Home hero | **1200** | no `min-h`, `pt-[172px] pb-[72px]` | ✗ |
| Home Mission | **900** | no `min-h`, `py-[168px]` | ✗ |
| Home Our Services | **~900** | no `min-h`, `py-[100px]` | ✗ |
| What-sets-us-apart | **900** | `min-h-[980px]` | ✗ |
| Home Contact | **780** | `min-h-[700px]` | ✗ |
| About "about" | **840** | no `min-h` | ✗ |
| About Mission | **900** | `min-h-[560px]` | ✗ |
| About Values | **900** | `h-[320vh]` | ✗ |
| Team | **912** | no `min-h` | ✗ |
| CTA | **820** | no `min-h`, `py-[140px]` | ✗ |
| Services care approach | **968** | no `min-h` | ✗ |
| Amenities hero | **900** | `min-h-[880px]` | ✗ |
| Amenities carousel | **1046** | no `min-h` | ✗ |

**Correct — do not touch:** Testimonials 828 · Gallery 994 · FAQ 752 · Footer 580 · About/Services/Careers/Contact heroes 900 · Careers intro 590 · open positions 928 · contact admissions 860 · insurance 902.

### VIS-PASS · Verified correct, protect against regression
Home Gallery mosaic 1280×458 / cols 394-453-394 / tiles 394×219 + 453×458 · Amenities gallery 512×710 centre + 255×406 sides at `top-204` · Contact hero 630×720 · Contact admissions row 428 + left card 380 · Insurance photo 500×410 · Careers job rows 1280×148 · Home hero photo 1280×720 r24 + badge inset 24 · h1 max-w 640 / para 498 / button gap 16 · Services rail 413, panels 847×500, padding 40, gap 32 · Container 1280 @ 80.

---

## 4 · ASSETS — `AST`

### 4.1 · Silent failures — render as finished work, appear in no existing list

| ID | Page | Component | Issue | Priority |
|---|---|---|---|---|
| **AST-01** | About | `AboutValues.tsx` cards 3–4 | Spec [LH]: *"Keep the two knowingly-missing slots (**About values 3-4 photos**, Amenities Community card) as-is."* Slots were filled with `therapy-gym.webp` + `care-team.webp` — both reused from home/Services, WhatSetsUsApart, CareersHero, Gallery. Violates "never reuse another section's image." | **Critical** |
| **AST-02** | Services | `Logo.tsx:38` `AMark` | Hand-drawn SVG circle+triangle rendered in the 24/7 card. Spec [LH]: *"must be the real logo asset — **never the drawn SVG**."* | **Critical** |
| **AST-03** | Services | `CareApproach.tsx:5` | `blurred-card-placeholder.png` is the 24/7 background, `alt=""`, bypasses `<PlaceholderAsset>` | **Critical** |
| **AST-04** | Home, About, Services | `Cta.tsx:39` | `pattern-cta-bg.png` silently worked around by tiling `glyph-white.png` @72px | **Major** |

### 4.2 · ASSET INVENTORY

| Filename | Page | Section | Component | Figma source | Project path | Status | Verified |
|---|---|---|---|---|---|---|---|
| `amenities-hero-woman-reading.png` 2048×768 | Amenities | Hero | `AmenitiesHero:16` | **BLOCKED** | — | `PlaceholderAsset`, `HERO_IMAGE=null` | ✗ |
| `admissions-room.png` | Amenities | Carousel | `AmenitiesCarousel` | **BLOCKED** | — | `PlaceholderAsset` | ✗ |
| `admissions-salon.png` | Amenities | Carousel | `AmenitiesCarousel` | **BLOCKED** | — | `PlaceholderAsset` | ✗ |
| `admissions-lounge.png` | Amenities | Carousel | `AmenitiesCarousel` | **BLOCKED** | — | `PlaceholderAsset` — *spec-acknowledged missing* | ✗ |
| `icon-comfort-care.svg` | Services | Overview | `CareApproach:78` | **BLOCKED** | — | `PlaceholderAsset` — nurse outline, **not a heart** | ✗ |
| `icon-leaf.svg` | Services | Overview | `CareApproach:105` | **BLOCKED** | — | `PlaceholderAsset` — leaf in solid navy circle | ✗ |
| `service-short-term-rehab.jpg` | Services | Our Services | `ServicesList` | **BLOCKED** | — | `PlaceholderAsset` — therapist + dumbbells | ✗ |
| `pattern-cta-bg.png` | 3 pages | CTA | `Cta:39` | **BLOCKED** | — | **silent substitute** (AST-04) | ✗ |
| 24/7 background | Services | Overview | `CareApproach:5` | **BLOCKED** | `blurred-card-placeholder.png` | **silent placeholder** (AST-03) | ✗ |
| Brand "A" vector | Services | 24/7 badge | `Logo:38` | **BLOCKED** | drawn SVG | **drawn substitute** (AST-02) | ✗ |
| values photo 3 | About | What We Value | `AboutValues` | **BLOCKED** | `therapy-gym.webp` | **reused duplicate** (AST-01) | ✗ |
| values photo 4 | About | What We Value | `AboutValues` | **BLOCKED** | `care-team.webp` | **reused duplicate** (AST-01) | ✗ |

**AST-LEAD-01** — `src/assets/amenities-room.jpg` exists and is **unused**. Designer describes `admissions-room.png` as *"resident bedroom — bed, TV, dresser, bathroom door."* Plausibly already delivered in `Amara_imges.zip` (08-01). **Cannot verify:** Lovable's API returns binaries as `binary:true` without content, and the published site is unreachable — this environment's network policy returns **403 on CONNECT** for `*.lovable.app`. One look from you closes this and removes a blocker. **INFERRED — not acted on.**

---

## 5 · TYPOGRAPHY — `TYP`

Expected [LH]: h1 **and** h2 both Playfair 400 **44/52** @ **-0.44px**.

| ID | Page | Component | Current | Expected |
|---|---|---|---|---|
| **TYP-01** | Services | `ServicesHero` h1 | 40/48 | 44/52 |
| **TYP-02** | Amenities | `AmenitiesHero` h1 | 52/60 | 44/52 |
| **TYP-03** | Services, Careers | `AboutTeam` h2 | 38/46 | 44/52 |
| **TYP-04** | Home, Careers, Contact | `home/Contact` h2 | 40/48 | 44/52 |
| **TYP-05** | 4 pages | `Testimonials` h2 | 46/54, `max-w-[430px]` | 44/52, **max-w ~520**, forced 2 lines |
| **TYP-06** | Home, About, Careers | `Faq` h2 | 48/56 | 44/52 |
| **TYP-07** | Services | `ServicesList` h2 | 52/60 | 44/52 |
| **TYP-08** | Amenities | `AmenitiesCarousel` h2 | 32→40 | 44/52 |
| **TYP-09** | Services | `ServicesList` h3 | 30→36 | 40/48 |
| **TYP-10** | Services | `CareApproach` "24/7" | 64→**76/82** | **~64/70** |
| **TYP-11** | About | `AboutMission:47` | **`font-sans`** 20→24/34 | **Playfair 30–32/40** — wrong family |
| **TYP-12** | Home | `Mission` | 44/**52** | 44/**56** — see VIS-12 |

**TYP-11 is the most visible** — a serif mission statement rendering as body sans.

---

## 6 · SPACING — `SPC`

Expected [LH]: **20px gap everywhere** unless stated; card padding **24 small / 40 large**.

| ID | Component | Current | Expected |
|---|---|---|---|
| **SPC-01** | `AboutIntro` photo grid | `gap-4` 16 | 20 |
| **SPC-02** | `CareApproach` grid | `gap-4` 16 | 20 |
| **SPC-03** | `AboutTeam` grid | `gap-[17px]` | 20 |
| **SPC-04** | `Testimonials` card | `md:p-5` 20 | 24 |
| **SPC-05** | `AboutValues` card | `md:p-8` 32 | 24 |

Correct: services panel gap 32 ✓, panel padding 40 ✓.

---

## 7 · RESPONSIVE — `RSP`

| ID | Page | Component | Defect |
|---|---|---|---|
| **RSP-01** | Amenities | `AmenitiesHero:22` | `md:whitespace-nowrap` at 52px Playfair inside `md:w-[560px]`; `md:`=768px. Overflows **768–1000px**. Your instruction said one line *on desktop* |
| **RSP-02** | Amenities | `AmenitiesGallery` | Desktop stage `md:block` with `left-[calc(50%±611/356px)]` + `h-[860px]` needs **≥1222px**, activates at 768px |
| **RSP-03** | About | `AboutValues` | Mobile container fixed at `440+3×48=584px`; cards are auto-height below `md` → overlap/clip |
| **RSP-04** | About | `AboutMission:44` | Absolute paragraphs in fixed `h-[192px] md:h-[160px]` → clipping at intermediate widths |

RSP-01 and RSP-02 will fail spec **check 14** (`scrollWidth === 390` on every page). Mobile type scale itself is correct ✓.

---

## 8 · ANIMATION — `ANM`

| ID | Component | Current [SRC] | Expected [LH] |
|---|---|---|---|
| **ANM-01** | `ScrollRevealText` | `opacity` 0.22→1, GSAP ScrollTrigger, `scrub:0.6`, `start:"top 88%"`, `end:"bottom 30%"`, `stagger.each:0.45`, `duration:1.4`, `power1.out`, `force3D` | Muted → **`#2D314B` colour interpolation**, word-by-word, scrub-linked. **No-pink rule honoured ✓** |
| **ANM-02** | site-wide | framer-motion **and** GSAP both loaded | one library |
| **ANM-03** | `AboutValues` | scroll-driven stack, `PEEK 48`, `cubicBezier(.16,1,.3,1)`, cards rise 720→0 | interaction approved 08-49 ✓ — geometry wrong (VIS-13, SPC-05) |
| **ANM-04** | `AboutMission` | binary stage crossfade at `scrollYProgress>0.5`, 0.35s | **BLOCKED** — no Figma prototype access |

**Not auditable [BLK]:** prototype flows, designer-specified durations/easings/delays/pinning, decorative logo movement, section entrance animations, scroll-to-explore behaviour. Nothing in the recovered history specifies these beyond ANM-01.

---

## 9 · HOVER — `HOV`

| ID | Component | Current | Expected [LH] |
|---|---|---|---|
| **HOV-01** | `AmenitiesCarousel.RoundArrow` | `h-11 w-11` **44×44 circle** | **56×32**, 8px gap |
| **HOV-02** | `Testimonials.ArrowButton` | no `hover-lift` | premium hover on all interactive elements |
| **HOV-03** | `AmenitiesGallery` thumbs | ad-hoc `hover:opacity-90` | hover system |
| **HOV-04** | `button.tsx:7` | `hover-lift` in **base** cva → `link`/`ghost` text lifts | lift on buttons/cards only |

> **Correction, logged to prevent re-breaking:** audit v2 called the 32×56 arrows "ovals, should be circular." **That was wrong.** The measured spec says **arrows 56×32**. `Testimonials.ArrowButton` and `CarouselArrow` are **correct**; `RoundArrow` is the deviation.

---

## 10 · NAVIGATION — `NAV`

| ID | Component | Defect |
|---|---|---|
| **NAV-01** | `AboutHero:44` → `/about#team`, `CareersTeam:29` → `/about` | `id="team"` lives on `AboutTeam`, moved to **`/services`** by the 15:03 restructure. Both buttons dead. **Regression** |
| **NAV-02** | `Hero.tsx:38,41`, `home/Services.tsx` | `<a href="/services">` / `<a href="/contact">` → full reload |

Header label "Admissions" → `/amenities` is **intentional** [LH]: *"That mismatch is in the source design… Keep the label as designed."* Not a defect.

---

## 11 · CONTENT INTEGRITY — `CNT`

| ID | Page | Component | Defect | Priority |
|---|---|---|---|---|
| **CNT-01** | Careers | `routes/careers.tsx:11-30` | Three fabricated staff testimonials — "Maria, RN", "Daniel, PT", "Alicia" — under the code's own `// PLACEHOLDER: unverified marketing copy`. Live on a healthcare site | **Critical** |
| ~~CNT-02~~ | Contact | `ContactInsurance.tsx:8-22` | **CLOSED — MATCHES DESIGN.** [DA] Contact render specifies this exact list: Tufts, Harvard Pilgrim, Commercial BCBS of Mass, Cigna, Humana, Senior Whole Health, UHC, CCA, Neighborhood Health Plan, Network Health, Medicare, Medicaid, Private Pay. Implementation faithful. *Business note for the client, not a code defect: these are Massachusetts-market carriers on a New Jersey facility.* **Do not change.** | — |
| **CNT-03** | 3 pages | `Testimonials.tsx:34-40` | Card 3 repeats `— Oliver W. / March 2026` from card 1. [DA] Services render shows card 1 Oliver W. / card 2 Daniel R. Card 3 unverified in renders | **Major** |
| ~~CNT-04~~ | Home, About, Careers | `Faq.tsx:22-25` | **CLOSED — MATCHES DESIGN.** [DA] Home, Services and Careers renders all show "Do you accept Medicare or private insurance?" expanded with the general services paragraph. Only the Brookwood→Amara substitution was required, and it is done. **Do not change.** | — |
| ~~CNT-05~~ | Services, Careers | `AboutTeam:4`, `CareersTeam:8` | **CLOSED — MATCHES DESIGN.** [DA] About and Careers renders both read **"Motty Waxler"**. The 14:55 written spec's "Metty" was a typo in the message. **Do not change.** | — |
| **CNT-06** | Careers | `OpenPositions.tsx:25` | **DOWNGRADED.** [DA] Privacy Policy and Terms renders print `info@amaracarecenter.com` — the domain is design-sanctioned. `ENOTFOUND` is client infrastructure, not an implementation defect. Do not invent a substitute domain | Minor |
| **CNT-07** | all | `Footer.tsx` | Social → `linkedin.com` / `facebook.com` homepages | **Major** |
| **CNT-08** | Services | `ServicesList` indian-program | `resident-son.webp` with `alt="Freshly prepared meal served in the dining room"` | **Major** |
| **CNT-09** | Services, Careers | `AboutTeam:6` | `"QA - Staff Development"` vs spec `"QA- Staff Development"` | Minor |

**Resolved — not defects:** newsletter placeholder `"Enter email address"` ✓ (08-03 20:03 overrode the Aug-1 "keep the typo"); Footer social = LinkedIn + **Facebook** ✓ (08-04 spec overrode Aug-1 "Instagram").

---

## 11b · STRUCTURE & NEW FINDINGS FROM THE DESIGN ARCHIVE — `STR` / `NEW`

Added 2026-08-04 after merging the 18 approved renders. All **[DA]**.

### STR-01 · About and Services section composition is inverted — **Critical · READY**

**RESOLVED by the 2026-08-04 authority ruling: the final approved design wins.** Earlier written specs (14:55 and 15:03) are superseded.

| Page | **Design [DA] — implement this** | Written spec (superseded) | Code today |
|---|---|---|---|
| `/about` | Hero → About Us → Our Mission → What We Value → **Meet the Team** → Testimonials → CTA → Footer · **no FAQ** | Testimonials → FAQ → CTA, no Team | follows the superseded spec |
| `/services` | Hero → Care Approach → Our Services → Testimonials → **FAQ** → CTA → Footer · **no Meet the Team** | Team → Testimonials → CTA, no FAQ | follows the superseded spec |

Root cause: the 14:55/15:03 restructure was applied against the design. Dependencies: **fixes NAV-01** — once Team returns to `/about`, `AboutHero`'s `/about#team` link and `CareersTeam`'s `/about` link resolve correctly and must NOT be repointed to `/services`.

### NEW-01 · Home has no "Plan Your Visit" CTA section — **Major · READY**
[DA] Home render: Gallery → FAQ → contact form → Footer. `routes/index.tsx` renders an extra `<Cta />` before `<Contact />`. Remove it from Home only — About, Services and Amenities all keep theirs.

### NEW-02 · CareersIntro is missing its photo — **Major · READY**
[DA] Careers render shows a photo (older couple embracing, outdoors) to the left of the "why Amara / Join a team that puts people first and inspires meaningful careers" text. `CareersIntro.tsx` renders text only. Asset likely already in `src/assets/photos` — verify against the render before wiring.

### NEW-03 · CareersTeam roster and grid are wrong — **Major · READY**
[DA] Careers render shows the **full 8-person roster in a 3-column grid**, identical to About. `CareersTeam.tsx` renders 4 people in `md:grid-cols-2`. Heading "Caring Professionals You Can Trust" is correct.

### NEW-04 · Footer socials — design is internally inconsistent — **Minor · BLOCKED**
[DA] Home, Privacy Policy, Terms renders show **Linkedin / Instagram**. About, Amenities, Careers, Contact renders show **Linkedin / Facebook**. The authority rule cannot resolve a conflict *inside* the design. Code currently ships Facebook. **Holding for a ruling — no change.** (CNT-07 still applies either way: both links point at platform homepages, not Amara profiles.)

## 12 · CODE QUALITY — `COD` *(lowest priority)*

**COD-01** 18 hardcoded `/__l5e/assets-v1/<uuid>/…` strings (`WhatSetsUsApart`×2, `home/Services`×4, `AboutValues`×4, `Gallery`×5, `ServicesList`×3, `CareersHero`, `ContactHero`, `ContactInsurance`, `ContactAdmissions`) vs `.asset.json` imports elsewhere — re-upload changes the UUID, silent 404, no build error
**COD-02** 11 raw colour literals bypassing tokens — `home/Contact` `hsl(217,44%,82%)`×2 + `hsl(240,6%,96%)`; `AboutTeam` `#F2F7FF`,`#C5D5EF`; `OpenPositions` `#E5E7EB`,`#F2F7FF`,`#A8BEE0`,`#4B5066`×2; `ContactInsurance` `#8FA8CE`; `CareApproach` `#7C8A63`. Note `#4B5066`/`#8FA8CE` **are** tokens written as literals
**COD-03** `ServicesList` watermark `opacity-25` vs `home/Services` `0.18` — spec said *"opacity even lower"*
**COD-04** two rail widths — `home/Services` 413 ✓ / `ServicesList` 320 ✗
**COD-05** `md:translate-y-[88px]` magic offset
**COD-06** `AGlyph` dead code
**COD-07** `home/Contact` mounted on 3 pages; spec'd for Home
**COD-08** `AmenitiesCarousel` nests `max-w-[1280px]` inside `Container`'s 1280
**COD-09** `Footer` `<h2>` for link columns; `Mission`/`AboutMission` `<h3>` for section headings
**COD-10** `text-border` on white for inactive rail items — likely fails WCAG AA
**COD-11** `/amenities` route missing `og:type` / `twitter:card`

---

## 13 · OPEN QUESTIONS — genuinely unobtainable

Everything else was recovered from history. These four cannot be:

1. **CNT-02** — Amara's real NJ insurance carriers. Not in Figma (it's data), not in history, `amaracarecenter.com` dead.
2. **CNT-01** — delete the fabricated testimonials, or supply real staff quotes?
3. **CNT-05** — **Metty** or **Motty** Waxler? A real person.
4. **CNT-06 / CNT-07** — real careers email domain and the two real social profile URLs.

---

## 14 · IMPLEMENTATION QUEUE

Frozen on **ВСЁ СКИДЫВАЙ**. Waves 1–7 and 10 need **no Figma access**.

| Wave | Contents | Blocked? |
|---|---|---|
| **1 · Visual geometry** | VIS-13 heights (`py-*`→`min-h`+centering) → VIS-01 → VIS-02 → VIS-03 → VIS-04 → VIS-05 → VIS-06 → VIS-07 → VIS-08 → VIS-09 → VIS-10 → VIS-11 → VIS-12 | No |
| **2 · Typography** | TYP-01…TYP-12 — delete overrides, restore the scale | No |
| **3 · Spacing** | SPC-01…SPC-05 | No |
| **4 · Responsive** | RSP-01…RSP-04, then check 14 at 390 on all 7 pages | No |
| **5 · Animation & hover** | ANM-01 colour interpolation, ANM-02 consolidate; HOV-01…HOV-04 | ANM-04 blocked |
| **1b · Structure** | **STR-01** move Team → `/about`, FAQ → `/services` · **NEW-01** drop `<Cta>` from Home · **NEW-02** CareersIntro photo · **NEW-03** CareersTeam 8-up 3-col | No |
| **6 · Navigation** | NAV-01 — **after STR-01 the `/about#team` links resolve correctly; do NOT repoint to `/services`** · NAV-02 `<Link>` | No |
| **7 · Content** | CNT-01 ✔ in Wave 1 · CNT-03 · CNT-07 · CNT-08 · CNT-09. CNT-02/04/05 closed, CNT-06 downgraded | NEW-04 needs a ruling |
| **8 · Assets** | 12 inventory rows; remove AST-01…AST-04 | 🔒 **Figma seat** |
| **9 · Code quality** | COD-01…COD-11 | No |
| **10 · Verification** | All 14 spec checks @1440 + 390; desktop/tablet/mobile on all 11 routes | Partial |

---

## 14b · WAVE LOG

### WAVE 1 — `daae8f96` → `93fe1cf1` · 2026-08-04 20:07 · **15/16 PASS**

Scope: typography scale restoration · section heights · component geometry · spacing · CNT-01.

**IMPLEMENTED · QA PASSED** — TYP-01…TYP-11 (all component overrides deleted, scale restored; AboutMission now Playfair 32/40) · VIS-01 Testimonials 847×440 / photo 389×392 / h2 2 lines · VIS-02 ServicesHero 630×720 · VIS-03 AmenitiesCarousel 846×450 / photo 296×360 · VIS-04 CareApproach row 460 · VIS-05 monogram 68×68 gap 20 · VIS-06 WSUA 413×460 · VIS-07 panel photos · VIS-08 AboutIntro 630×380 · VIS-09 header 52 / logo 189×52 · VIS-10 FAQ columns · VIS-11 Cta 630×660 · VIS-13 section heights (no unstyled gaps) · SPC-01…SPC-05 · **CNT-01 invented employee testimonials deleted, Careers restored to the standard family testimonials**.

**QA FAILED → carried to Wave 2** — VIS-12 / TYP-12 Home mission line count. Agent correctly refused to fudge it: *"3 lines at max-w 900 is geometrically impossible — that 211-character sentence wraps to 5 lines; 3 lines would need ≈1450px of measure."* The written "3 lines" was wrong. **[DA] The approved Home render shows 4 lines.** Design wins; corrected in Wave 2.

### WAVE 2 — dispatched 2026-08-04 20:15 · IN PROGRESS
Scope: **STR-01** About/Services composition inverted to match the design · **NEW-01** remove `<Cta>` from Home · **NEW-03** CareersTeam 8-up 3-column · **NEW-02** CareersIntro photo (existing asset or named placeholder — no substitution) · **NAV-01** `id="team"` on About, links verified not repointed · **NAV-02** three `<a href>` → `<Link>` · VIS-12 mission to 4 lines.

### DEFERRED BY CLIENT INSTRUCTION — 2026-08-04
Responsive/viewport work (**RSP-01…RSP-04**) is parked until Task #1 (visual implementation) is complete and verified. Regression guards at 390 still run each wave; no new responsive investigation.

## 15 · REGRESSION WATCH — verified correct, do not break

Contact form: square checkbox `!rounded-[4px]` · Name field focus-only outline · no icon in any form field · newsletter spelling · "Schedule a Tour" · "on community" spaced · "Amara…" not "Brookwood" · Admissions carousel title break + centred arrows · Amenities hero one-line heading, 4-line paragraph, "Explore Amara Amenities" · values stack interaction · no-pink reveal · `prefers-reduced-motion` + `:focus-visible` · all VIS-PASS geometry · the full design system in §1 · Header "Admissions"→`/amenities` label.

---

## 16 · STATUS

| | |
|---|---|
| Issues logged | **76** — VIS 13 · AST 4+12 · TYP 12 · SPC 5 · RSP 4 · ANM 4 · HOV 4 · NAV 2 · CNT 9 · STR/NEW 5 · COD 11 |
| Closed as MATCHES DESIGN | **3** — CNT-02, CNT-04, CNT-05. Would have broken a correct site |
| Downgraded | **1** — CNT-06 |
| Critical | **10** (was 12) |
| Code modified | Wave 1 dispatched to Lovable 2026-08-04 19:58 |
| Assets uploaded | **none** |
| Lovable prompts sent | **1** — Wave 1 (typography + section heights + component geometry + spacing + CNT-01) |
| Source coverage | 35/37 files — outstanding: `ui/checkbox.tsx`, `LegalPage.tsx`, `NotFoundPage.tsx`, `routes/$.tsx`, `privacy-policy.tsx`, `terms-of-use.tsx` |
| History coverage | **complete** — 4/4 pages |
| **Figma coverage** | **page index only. Zero frames, zero comments, zero layers, zero assets.** |

**Blockers:** ① Figma View-seat quota (6/month, exhausted) — gates Wave 8 and all comment/prototype/frame verification. ② Four designer photos promised 08-04 15:26 & 15:29, never sent. ③ §13 content answers. ④ Environment network policy blocks `*.lovable.app` (403 CONNECT) — in-browser QA must run through Lovable, not here.
