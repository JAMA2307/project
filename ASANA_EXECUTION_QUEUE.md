# ASANA EXECUTION QUEUE — Amara

| | |
|---|---|
| Built | 2026-08-06 |
| Source | 59 QA subtasks, all opened and classified · `ASANA_QA_LEDGER.md` §12 (acceptance criteria) · §13 (mutation audit) |
| Rule | **ONE ASANA SUBTASK = ONE LOVABLE TURN.** Only exact duplicates inside one shared component share a turn, and each Asana item is still verified and closed separately |
| Status | **HELD.** Nothing dispatches until the command `ВСЁ ОТПРАВЛЯЙ` |
| Asana project | Amara `1217105105055924`, workspace `1210357482925157` — no other project touched |

**Base URL for every item:** `https://app.asana.com/1/1210357482925157/task/<GID>`

---

## 0 · SUMMARY

| | Count |
|---|---|
| QA subtasks total | **59** |
| **Dispatchable now** | **39** |
| Turns needed for those 39 | **38** (one duplicate pair shares a turn) |
| Blocked — cannot be dispatched at any price | **20** |
| Already complete before execution | **0** |

**Nothing is merged for convenience.** The single shared turn is Q19, where About-14 and Admissions-8 are the *same* defect in the *same* file (`sections/Cta.tsx` mobile proportions). Both Asana items are verified and closed independently.

### Blocked, by cause

| Cause | Items | GIDs |
|---|---|---|
| Screenshot absent from the export (all 4 reopened) | 4 | HOME-01, HOME-10, SERV-01, SERV-02 |
| Playfair weight table not supplied | 3 | HOME-05, HOME-18, ABOUT-10 |
| Legal body copy not supplied | 2 | AUX-01, AUX-02 |
| CTA panel hex not supplied | 3 | ABOUT-05, ABOUT-07 *(dup)*, ADM-05 |
| Question posted, awaiting answer | 5 | ABOUT-13, SERV-06, ADM-02, ADM-04, CAR-02 |
| Figma asset file needed | 2 | HOME-06 *(card copy + photo)*, CON-02 *(icon)* |
| Target value not derivable | 1 | HOME-02 |
| **Total** | **20** | |

---

## 1 · TIER 1 — SHARED COMPONENTS (highest reach, dispatch first)

---

### Q1 · FAQ must be fully collapsed on load
| | |
|---|---|
| **GID** | `1217108466019458` · HOME-12 · "12 safari/chrome" |
| **Page / component** | Home → `src/components/sections/Faq.tsx` |
| **Routes** | `/`, `/services`, `/careers` |
| **Screenshot** | none (text-only ticket — correctly has no attachment) |
| **Current defect** | `const [open, setOpen] = useState<number \| null>(1)` opens item 2 on mount |
| **Target** | No item open on first render. Accordion still toggles on click; clicking an open item closes it |
| **Responsive** | All viewports |
| **Acceptance** | On `/`, `/services`, `/careers`: zero `[aria-expanded="true"]` on load · all six answers absent from the DOM · clicking a question opens exactly one · **Home FAQ section measures 752px at 1440** |
| **Regression** | The 752 reference value. Closed accordion = 6×64 + 5×12 = 444; 444 + 240 padding = 684, so `min-h-[752px]` governs and the section lands on 752 naturally |
| **Clarification** | none needed |
| **Note** | This one line also closes the last outstanding FAIL from the responsive programme (R7 measured 766 vs 752). No padding is to be shaved |

---

### Q2 · Header reveals on scroll up
| | |
|---|---|
| **GID** | `1217108466019450` · HOME-11 · "11 safari/chrome" |
| **Page / component** | Home (global) → `src/components/Header.tsx` |
| **Routes** | **all 9** |
| **Screenshot** | none (text-only) |
| **Current defect** | Header is `absolute inset-x-0 top-6`. **No scroll listener of any kind exists** — this is new behaviour, not a repair |
| **Target** | Scrolling down past the header's own height hides it; any upward scroll reveals it, pinned to the viewport top |
| **Layout** | Row height stays **52px**; logo **189×52**; nav gap keeps `clamp(1.5rem, 0.5rem+1.667vw, 2.5rem)`; the 1080px content-fit breakpoint is unchanged |
| **Responsive** | All viewports. The mobile menu overlay must be unaffected |
| **Prohibited** | Do not change nav labels, routes, the CTA, the 1080 breakpoint, or the header's transparent background over heroes. Do not make the header `sticky` inside a transformed ancestor |
| **Acceptance** | Scroll down 400px → header off-screen · scroll up 50px → header visible, fixed to top · no layout shift when it appears · `prefers-reduced-motion` disables the transition · verified on all 9 routes · zero sub-44px tap targets retained |
| **Regression** | Hero overlays on `/about`, `/careers`, `/contact`, `/amenities`; the mobile menu; header 52 on all 9 |
| **Clarification** | none needed |

---

### Q3 · Footer newsletter must respond on submit
| | |
|---|---|
| **GID** | `1217108466019476` · HOME-13 · "13 safari/chromr" — *first half only* |
| **Page / component** | Home (global) → `src/components/Footer.tsx` |
| **Routes** | **all 9** |
| **Screenshot** | `Home/13 safarichromr.png` — red circle around the input + Submit with an address typed in |
| **Current defect** | `handleSubmit` calls `event.preventDefault()` and **nothing else**. No success, no error, no pending state |
| **Target** | Submitting a valid address shows a confirmation in place of, or beneath, the field. Invalid input shows an inline error. The button shows a pending state while submitting and cannot be double-fired |
| **Visual** | Stay inside the existing pill: `rounded-full`, `bg-brand-white/10`, `ring-1 ring-brand-white/20`. Confirmation text in `text-brand-white`, error legible on the dark footer |
| **Responsive** | The pill stacks below 400px — feedback must not break that |
| **Prohibited** | **Do not touch the watermark** — that is the second half of this ticket and is awaiting an answer (comment `1217231594623979`). Do not change footer links, socials or the copyright line |
| **Acceptance** | Valid address → visible confirmation · invalid → inline error · pending state present · no double-submit · verified on all 9 routes · footer still 580 at 1440 · watermark unchanged |
| **Regression** | Footer height 580 · `auto-fit` columns · watermark no overflow · Home socials = LinkedIn + Instagram |
| **Clarification** | Second half (which watermark) **blocked** — this Asana item stays open until both halves land |

---

### Q4 · Contact-form machinery — async, pending, inline errors
| | |
|---|---|
| **GID** | `1217234006576129` · HOME-21 · "21 Mobile" — *design-independent half* |
| **Page / component** | Home (global) → `src/components/home/Contact.tsx` |
| **Routes** | `/`, `/careers`, `/contact` |
| **Screenshot** | `Home/21 Mobile.png` — the UI KIT frame (read at 8× magnification, `ASANA_QA_LEDGER.md` §12.7) |
| **Current defect** | `onSubmit` is fully synchronous. No pending state, no double-submit guard, and only `parsed.error.issues[0]` reaches the user — as a transient toast. Five invalid fields report one. There is therefore **no code path that can reach a failure state at all** |
| **Target** | Submission becomes async with a pending state; every invalid field gets an inline message and `aria-invalid`; the submit button is disabled while pending; state changes announce via an ARIA live region and move focus |
| **Typography** | Fields stay Satoshi 18/24; error text Satoshi 16/22 in `--destructive` |
| **Prohibited** | **Do not build the S1/S2 visual states yet** — their body copy is still unread (question `1217239076858549`). Do not change the checkbox shape `!rounded-[4px]` — CON-03 authorises a colour change only. Do not alter field order or labels |
| **Acceptance** | Submit is async with a pending state · double-click submits once · all invalid fields show inline errors simultaneously · `aria-invalid` set · live region announces · focus managed · verified on all 3 routes · **Home contact section still 780 at 1440** |
| **Regression** | `min-h-[780px]` at 1440 · square checkbox · form field heights 50 / textarea 104 / submit 52 |
| **Clarification** | S1/S2 copy, retry behaviour, failure type and loading state — **Q22-a…d posted**. This Asana item stays open until the visual states land |

---

### Q5 · Testimonials — heading-to-track gap
| | |
|---|---|
| **GID** | `1217154780337210` · ABOUT-06 · "6 Chrome/Safari" |
| **Page / component** | About → `src/components/sections/Testimonials.tsx` |
| **Routes** | `/`, `/about`, `/services`, `/careers` |
| **Screenshot** | `About/6 ChromeSafari.png` — underline beneath "About Our Care" and a vertical stroke marking the gap |
| **Current defect** | The card track sits close under the section heading |
| **Target** | Increase the vertical gap between the heading block and the track |
| **⚠ Interpretation flagged** | The ticket says *"more spacing"* without a value and no Figma frame was supplied for this section. **Proposed target: raise the gap to 64px at 1440, scaling fluidly to 40px at 390.** This is a derived value, not a measured one — flag it in the prompt and have Lovable report the before/after so it can be adjusted in one cheap follow-up |
| **Responsive** | Fluid between the two endpoints |
| **Acceptance** | Gap increased and measured on all 4 routes · cards still 847×440, photo 389×392, arrows 56×32 · no overflow at any of the 22 viewports |
| **Regression** | All four routes carrying Testimonials |

---

### Q6 · Testimonials — card structure and infinite loop
| | |
|---|---|
| **GID** | `1217108466019425` · HOME-09 · "9 safari/chrome" — *structure half* |
| **Page / component** | Home → `src/components/sections/Testimonials.tsx` |
| **Routes** | `/`, `/about`, `/services`, `/careers` |
| **Screenshot** | `Home/9 safarichrome.png` — bracket around card 1, the only one with a photo |
| **Current defect** | Card 1 has a photo; cards 2 and 3 have none. The carousel does not loop |
| **Target** | Every card uses card 1's structure — photo 389×392 + quote + attribution + date. The track loops infinitely in both directions |
| **Prohibited** | **Do not insert placeholder images** for the two empty slots — that is the open question on this ticket (comment `1217231593814836`) and it conflicts with a standing rule. Build the slot; leave it empty until the photos arrive. Do not invent a third testimonial |
| **Acceptance** | Photo slot present on every card · loop verified past the last and before the first card · cards 847×440 · arrows 56×32 · keyboard focus still advances the track · verified on all 4 routes |
| **Clarification** | Photos **blocked**; this Asana item stays open until they arrive |

---

### Q7 · Header/Footer nav label — *held*
Not queued. `ADM-04` (`1217108466019468`) is blocked on the Admissions-vs-Amenities decision (comment `1217243625850198`). It changes the header on all 9 routes and the footer Company column, so it must not be guessed.

---

## 2 · TIER 2 — HOME

| # | GID | Title | Defect → Target | Files | Acceptance |
|---|---|---|---|---|---|
| **Q8** | `1217213785962834` | HOME-14 "14 safari/desktop" | Heading wraps to **4** lines; Figma shows **3**. `max-w-[380px]` cannot hold "to learn more about" at 44px Playfair → widen so the three `<br>`-defined lines hold exactly | `home/Contact.tsx` | Exactly 3 lines at 1440 · no 4th wrap between 1280–1920 · copy unchanged ("our", not "out") · section still 780 |
| **Q9** | `1217213785962837` | HOME-15 "15 safary/desktop" | Gallery button reads "View Amenities" → **"View More"** | `home/Gallery.tsx` | Label exact · link still `/amenities` · button geometry unchanged |
| **Q10** | `1217108466019422` | HOME-08 "8 safari/chrome" | Services section unpins too early (only shrunken rail headings visible) and rail entries scroll-jump on click → pin with **rail + active panel both visible**; rail entries **non-interactive** | `home/Services.tsx` | Pinned state matches the screenshot · rail items have no click handler and no pointer cursor · active item dark with ∧, others muted · rail 413 and panels 847×500 at 1440 · unpins cleanly at 1100 and below |
| **Q11** | `1217108334767511` | HOME-07 "7 Safari/Chrome" | Mission reveal does not follow the storyboard → 5-stage sequence: monogram ring fades 0→1 across frames 1–3, then heading and paragraph reveal in 4–5, scroll-driven | `home/Mission.tsx`, `ScrollRevealText.tsx` | All 5 stages observable while scrolling · reduced-motion shows the end state immediately · mission paragraph still 4 lines at 1440 · `ScrollTrigger.refresh()` still debounced on resize |
| **Q12** | `1217108334767499` | HOME-03 "3 Safari/Chrome" | ① h1 renders `#0F0F0F`; Figma is bluish `#2C2E45` ② desktop hero photo differs from the AMARA reception-desk shot mobile already uses | `styles.css` (`--heading`), `home/Hero.tsx` | Heading token `#2C2E45` · desktop hero = reception-desk photo, matching mobile · hero photo 1280×720 at 1440 · **do not touch the pattern layer** (`opacity-100`, `backgroundSize: cover` — hard-won, see ledger) |
| **Q13** | `1217108334767502` | HOME-04 "4 SafariChrome" | The `--blue-100` hero band extends well past the hero photo before the white section starts → band terminates at the photo's bottom edge. **⚠ Interpretation** — the annotation marks the current boundary, not a target offset; have Lovable report the before/after in px | `home/Hero.tsx` | No blue visible below the hero photo · hero section still 1200 at 1440 · no overflow |
| **Q14** | `1217213785962843` | HOME-16 "16 Mobile" | Hero CTAs stack full-width on mobile → **side by side in a row** | `home/Hero.tsx` | Two buttons on one row at 390 and 320 · both ≥44px tall · no overflow at 320 · desktop unchanged |
| **Q15** | `1217213785962846` | HOME-17 "17 Mobile" | "Where Healing Feels Like Home" badge sits **below** the photo on mobile → overlays **inside** the photo, as on desktop | `home/Hero.tsx` | Badge inside the photo bounds at 390 and 320 · no overflow, no clipping, text legible over the image · **reverses the R2 decision** that made the badge absolute only from `lg:` — the overflow it was avoiding must not return |
| **Q16** | `1217213785962852` | HOME-19 "19 Mobile" | Testimonial card is flush-left with the next peeking → **centred** in the viewport | `sections/Testimonials.tsx` | Equal margins both sides at 390 and 320 · scroll-snap still works · desktop unchanged |
| **Q17** | `1217213785962855` | HOME-20 "20 Mobile" | Gallery eyebrow, heading and paragraph are centred (`items-center text-center` at every width) → **left-aligned on mobile** | `home/Gallery.tsx` | Left-aligned at 390 and 320 · centred from the desktop breakpoint up · tile grid untouched |

---

## 3 · TIER 3 — ABOUT

| # | GID | Title | Defect → Target | Files | Acceptance |
|---|---|---|---|---|---|
| **Q18** | `1217108466019431` | ABOUT-01 "1 Chrome/Safari" | `glyph-ring.png` renders centred in the hero at `opacity-[0.10]`, duplicating the header logo → **remove it** | `about/AboutHero.tsx` | No monogram in the hero · hero 900 at 1440 · scrim and heading placement unchanged · *(hover half already verified done — see comment `1217239076043987`)* |
| **Q19** | `1217234006576147` **+** `1217234006576173` | ABOUT-14 + ADM-08 — **shared turn** | `Cta` on mobile: panel `min-h-[440px]` vs photo `h-[320px]`, with dead space below the button → proportions per Figma, dead space removed | `sections/Cta.tsx` | Panel and photo heights corrected on `/about`, `/services`, `/amenities` at 390 and 320 · no dead space below the button · **CTA image still 630×660 at 1440** · **do not change the panel colour** — that is blocked on the hex |
| **Q20** | `1217108466019442` | ABOUT-04 "4 Chrome/Safari" | ① Values cards do not rise and cover on scroll ② **card 2 "Comfort & Wellbeing" has no background at all** and vanishes into the page blue | `about/AboutValues.tsx` | Each card rises and covers the previous while scrolling · every card has a background distinct from the page · cards 847×440 at 1440 · **the `useStackEnabled` gate (min-width 768 AND min-height 800) must survive**, and the pinned region must never exceed the viewport |
| **Q21** | `1217213785962840` | ABOUT-08 "8 chromesafari" | Card internals broken — icon floats top, dead space below the text, photo inset with excess padding → icon top-left, heading and paragraph anchored lower-left, photo flush right per the Figma frame | `about/AboutValues.tsx` | Matches `About/4 ChromeSafari.png` layout · card 847×440 · no dead space |
| **Q22** | `1217108466019437` | ABOUT-03 "3 Chrome/Safari" | Mission shows one static paragraph in **Playfair**; Figma shows **two variants that swap on scroll**, set in Satoshi | `about/AboutMission.tsx` | Both variants present verbatim (§12.5) and swapping on scroll · paragraph in Satoshi, not Playfair · reduced-motion shows variant 1 statically · **monogram replacement is blocked** — leave the current mark and keep this item open |
| **Q23** | `1217234006576138` | ABOUT-11 "11 mobile" | **Both pill icon slots render empty** on mobile — the icons do not load at all | `about/AboutIntro.tsx` | `about-icon-skilled-nursing` and `about-icon-medication-management` render at 390 and 320 · `naturalWidth > 0` for both · **also fix the pill overflowing past the photo's bottom edge**, seen in `About/10` and `About/12` |
| **Q24** | `1217234006576141` | ABOUT-12 "12 mobile" | Mission paragraph renders oversized Playfair on mobile; Figma is smaller and sans → Satoshi, reduced size, smoother transition | `about/AboutMission.tsx` | Sans-serif on mobile · size reduced · transition smoothed · reduced-motion honoured |
| **Q25** | `1217234006576132` | ABOUT-09 "9 mobile" | ① Hero too short ② "Meet Our Team" is `w-full` on mobile → auto-width, left-aligned to the heading | `about/AboutHero.tsx` | Button auto-width and left-aligned at 390/320 · heading placement per Figma · **hero height target is not supplied** — increase and report the measurement so it can be tuned in one follow-up · desktop 900 unchanged |
| **Q26** | `1217108466019434` | ABOUT-02 "2 Chrom/safari" | Pill icons wrong and label weight wrong → official icons, regular weight. *(The "shift the paragraph right" half has no measured target and stays open)* | `about/AboutIntro.tsx` | Both official icons render · label weight regular · **do not shift the column** until a target is supplied |

---

## 4 · TIER 4 — SERVICES

| # | GID | Title | Defect → Target | Files | Acceptance |
|---|---|---|---|---|---|
| **Q27** | `1217234006576153` | SERV-04 "4 safari chrome" | The Indian Program card lists items as **chips**; the other three use **bulleted lists** → make it consistent | `services/ServicesList.tsx` | Indian Program uses the same list treatment as the other three · all 10 items retained verbatim · panel 847×500 at 1440 |
| **Q28** | `1217234006576156` | SERV-05 "5 mobile" | Four defects: no gap between header and H1; H1 too large (runs to 4 lines); CTA full-width; "Scroll to Explore" misplaced | `services/ServicesHero.tsx` | Top spacing added · H1 fits in ≤3 lines at 390 · CTA auto-width, left-aligned · "Scroll to Explore" at the hero foot · all four verified at 390 and 320 |
| **Q29** | `1217234006576162` | SERV-07 "7 mobile" | "Plan Your Visit" sits directly after the intro; the "Therapy" chip is not in the design | `services/ServicesList.tsx` | Button moved to the **end** of the section · "Therapy" chip removed on mobile · other category chips reviewed for the same treatment |
| **Q30** | `1217234006576150` | SERV-03 "3 safari chrome" | **The 24/7 panel clips its own supporting text at the card's right edge** — a real overflow bug | `services/CareApproach.tsx` | 24/7 text no longer clipped at any viewport · row 460 with columns 306/621/313 at 1440 · **element repositioning is blocked** (no measured target) and this item stays open for that half |

---

## 5 · TIER 5 — ADMISSIONS (`/amenities`)

| # | GID | Title | Defect → Target | Files | Acceptance |
|---|---|---|---|---|---|
| **Q31** | `1217108466019459` | ADM-01 "1 safarichrome" | Hero left column is not vertically centred; the Figma frame shows it centred | `amenities/AmenitiesHero.tsx` | Left column vertically centred · "Scroll to Explore" bottom-left · photo 660×600 and grid `560px 660px` gap 60 at 1440 · h1 one line at 1440 |
| **Q32** | `1217108466019465` | ADM-03 "3 Safarichrome" | Gallery side counters read **05** and **02**; with the centre at 02 they must read **01** and **03**. Side images also need captions | `amenities/AmenitiesGallery.tsx` | Counters sequential around the centre · side captions present · centre 512×710, sides 255×406 at `top-204` |
| **Q33** | `1217234006576167` | ADM-06 "6 mobile" | CTA full-width; "Scroll to Explore" too high | `amenities/AmenitiesHero.tsx` | Button auto-width, left-aligned at 390/320 · "Scroll to Explore" at the hero foot |
| **Q34** | `1217234006576170` | ADM-07 "7 mobile" | Card renders text then photo → **photo above the text** | `amenities/AmenitiesCarousel.tsx` | Photo first at 390/320 · desktop 846×450 with 296×360 photo unchanged |

---

## 6 · TIER 6 — CAREERS · CONTACT · AUXILIARY

| # | GID | Title | Defect → Target | Files | Acceptance |
|---|---|---|---|---|---|
| **Q35** | `1217234006576183` | CAR-03 "3 ChromeSafari" | "View full Team" button present → **remove it**, desktop and mobile | `careers/CareersTeam.tsx` | Button gone at all viewports · 8 monograms 68×68 retained · section spacing closes cleanly |
| **Q36** | `1217234006576177` | CAR-01 "1 ChromeSafari" | Hero scrim so dark the photo is nearly black at the bottom | `careers/CareersHero.tsx` | Scrim lightened, photo legible at the bottom · heading/paragraph/button keep ≥4.5:1 contrast · hero 900 at 1440 · **⚠ no Figma frame supplied for this hero** — report the before/after opacity so it can be tuned |
| **Q37** | `1217234006576186` | CON-01 "1 SafariChrome" | Hero left column is top-anchored and the h1 collides with the header row | `contact/ContactHero.tsx` | Left column vertically centred · no collision with the header · column exactly 413 and photo 630×720 at 1440 (both are R6 fixes — must not move) |
| **Q38** | `1217234006576192` | CON-03 "3 safarichrome" | Insurance checkmarks the wrong colour; the Figma shows a white filled circle with a slate-blue tick on a medium slate panel | `contact/ContactInsurance.tsx` | Checkmarks match the Figma frame · photo still 500×410 at 1440 (R6 fix) · two-column list preserved · **do not change the checkbox in the contact form** — different component, different ticket |
| **Q39** | `1217234006576202` | AUX-03 "3 404" | 404 lacks nearly every element in the design | `NotFoundPage.tsx` | Full-bleed slate blue-grey background · header with light logo, nav and white "Get Started" pill · large white Playfair "404" · "Page was not found" · body *"The page you're looking for couldn't be found. / Let's get you back on track."* · white "Back to Home Page" pill · **A monogram watermarks bleeding off the left and right edges** (mobile: one bottom-centre) · no overflow at 320 · works at short viewport heights |

---

## 7 · BLOCKED — 20 items, not queued

| GID | Item | Blocker | Question posted |
|---|---|---|---|
| `1217105105133471` | HOME-01 | Screenshot absent from export; edited after closure | `1217246106377602` |
| `1217108466019428` | HOME-10 | Same | `1217234107583248` |
| `1217108466019451` | SERV-01 | Same | `1217231593330481` |
| `1217108466019455` | SERV-02 | Same | `1217234107740723` |
| `1217108334767496` | HOME-02 | Hero gap targets not derivable — annotation marks the current state, not a target | — |
| `1217108334767505` | HOME-05 | Playfair weight table | via `1217234108090689` |
| `1217213785962849` | HOME-18 | Playfair weight table | `1217234108090689` |
| `1217234006576135` | ABOUT-10 | Poppins source + Satoshi licence | `1217239076714225` |
| `1217108334767508` | HOME-06 | WSUA card copy and the middle card's photo live in Figma | — |
| `1217108466019447` | ABOUT-05 | CTA panel hex | `1217239076201709` |
| `1217154780337213` | ABOUT-07 | **Duplicate of ABOUT-05** — closes with it, but its own route is verified separately | via ABOUT-05 |
| `1217108466019473` | ADM-05 | Same CTA hex | via ABOUT-05 |
| `1217234006576144` | ABOUT-13 | "cards" vs icon badge | `1217243630734808` |
| `1217234006576159` | SERV-06 | Text says right, arrow reads left | `1217250865276284` |
| `1217108466019462` | ADM-02 | Carousel target arrangement | `1217239077596681` |
| `1217108466019468` | ADM-04 | Admissions vs Amenities IA — gates the whole page's identity | `1217243625850198` |
| `1217234006576180` | CAR-02 | Screenshot has no annotation | `1217243626461861` |
| `1217234006576189` | CON-02 | Correct "Supported Transition" icon file | — |
| `1217234006576196` | AUX-01 | Privacy Policy body copy | `1217231594199034` |
| `1217234006576199` | AUX-02 | Terms of Use body copy | via AUX-01 |

**Four items appear in both the queue and this list** — HOME-13, HOME-21, ABOUT-02, ABOUT-03, SERV-03, ABOUT-09, ABOUT-12 have a dispatchable half and a blocked half. Their Asana subtask stays **open** until both halves land, even after the dispatchable half is verified.

---

## 8 · POST-EXECUTION VERIFICATION LOOP

For every turn, without exception:

1. Read the changed files from Lovable (`read_file` — free, no credit).
2. Confirm the change is present in source **and** that nothing outside the stated scope moved.
3. Check the rendered result against the mapped screenshot at the exact viewports the ticket names.
4. Re-measure the affected 1440 reference values.
5. Check console errors, image 404s, page-level horizontal overflow.
6. For a shared component, verify **every** route it appears on.
7. Only then mark the Asana subtask complete and post a verification comment naming what changed, the file, the routes, and the viewports checked.
8. Update this queue and `ASANA_QA_LEDGER.md`.

**A Lovable report is never accepted as proof.** If verification fails: do not close the item, do not advance, do not dispatch a parallel run — write a corrective prompt for the same task and re-verify.

## 9 · DEV PAGES

None can be evaluated until its page-specific items **and** every shared item reaching it are verified. On current evidence all 7 stay open; the gating table is in `ASANA_STATUS_SYNC_REPORT.md` §4.
