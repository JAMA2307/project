# ASANA EXECUTION QUEUE — Amara (REVISION 2)

| | |
|---|---|
| Revised | 2026-08-06 — after the "no guessed visual values" ruling |
| Previous | Rev 1 claimed 39 dispatchable in 38 turns. **That count was too loose.** See §4 |
| Now | **18 dispatchable items · 18 Lovable turns** |
| Status | **HELD.** Nothing dispatches until `ВСЁ ОТПРАВЛЯЙ` |
| Rule | One Asana subtask = one Lovable turn. **No merges remain** — the only merge candidate (Cta mobile) is now blocked |

---

## 0 · THE TEST APPLIED

Every item had to pass all five. One failure blocks it.

1. Target stated in the Asana text **or** visible in a mapped screenshot
2. **No invented numeric or visual value** — no px, no hex, no opacity, no duration, no scroll distance we chose ourselves
3. All affected routes enumerated
4. Acceptance criteria that are objectively checkable
5. Independently verifiable after implementation without asking the agency

**A change is allowed to be structural** (move, remove, re-order, align, stop clipping, use an asset already in the repo) because none of those requires a number we invented. **A change is blocked if it needs a value nobody approved** — a gap size, a hex, a height, a timing, a scroll trigger point.

That single distinction is what took the queue from 39 to 18.

---

## 1 · THE 18 DISPATCHABLE TURNS

### Shared components first

**Q1 · FAQ collapsed on load** — `1217108466019458` (HOME-12)
`sections/Faq.tsx` · routes `/`, `/services`, `/careers`
Defect: `useState<number | null>(1)` opens item 2 on mount. Target: no item open; accordion still toggles.
Accept: zero `[aria-expanded="true"]` on load on all 3 routes · all six answers absent from the DOM · click opens exactly one · **Home FAQ measures 752 at 1440** (closed accordion 444 + 240 padding = 684, so `min-h-[752px]` governs).
No value invented — one boolean.

**Q2 · Header reveals on scroll up** — `1217108466019450` (HOME-11)
`Header.tsx` · routes **all 9**
Defect: header is `absolute inset-x-0 top-6`; no scroll listener exists. Target: scrolling down hides it, any upward scroll reveals it pinned to the top.
Accept: down 400px → off-screen · up 50px → visible and fixed · no layout shift · reduced-motion disables the transition · row still 52, logo 189×52, 1080 breakpoint intact · verified on all 9.
Geometry is unchanged and the transition uses the existing `--ease-premium` / `--dur-hover` tokens, so nothing is invented.
**⚠ Reaches `/amenities`** because the header is global. This is behaviour, not page identity, so it does not touch the IA question — but say the word and I will hold it too.

**Q3 · Testimonials loop infinitely** — `1217108466019425` (HOME-09, *loop half only*)
`sections/Testimonials.tsx` · routes `/`, `/about`, `/services`, `/careers`
Ticket: *"make infinite scroll in this section — the pages rotate."* Target: the track wraps past the last card and before the first.
Accept: continuous in both directions on all 4 routes · cards still 847×440, arrows 56×32 · keyboard focus still advances the track.
**Card-structure half stays blocked** — adding a photo slot to cards that have no photo would render empty boxes. Ticket remains open.

### Home

**Q4 · Contact heading on three lines** — `1217213785962834` (HOME-14)
`home/Contact.tsx` · routes `/`, `/careers`, `/contact`
Defect: `max-w-[380px]` cannot hold "to learn more about" at 44px Playfair, so it wraps to four lines. Figma shows three.
Accept: exactly 3 line boxes at 1440 · no fourth wrap 1280–1920 · copy unchanged ("our") · section still 780 at 1440.
Target is a line count, not a width — the implementation widens until three lines hold and reports the value.

**Q5 · Gallery button label** — `1217213785962837` (HOME-15)
`home/Gallery.tsx` · route `/`
"View Amenities" → **"View More"**. Link and geometry unchanged.

**Q6 · Services rail is not clickable** — `1217108466019422` (HOME-08, *non-clickable half only*)
`home/Services.tsx` · route `/`
Ticket: *"make the buttons in this section non-clickable — the scroll to the card isn't smooth and is basically unnecessary."*
Accept: rail entries have no click handler, no pointer cursor, no scroll-jump · active item still dark with the ∧ marker, others muted · rail 413 and panels 847×500 at 1440 unchanged.
**Pinning half blocked** — "should stick in this state" needs a scroll release point nobody has specified.

**Q7 · Hero CTAs side by side on mobile** — `1217213785962843` (HOME-16)
`home/Hero.tsx` · route `/`
Stacked → one row. Accept: both buttons on one row at 390 and 320 · each ≥44px tall · no overflow at 320 · desktop unchanged.

**Q8 · Hero badge inside the photo on mobile** — `1217213785962846` (HOME-17)
`home/Hero.tsx` · route `/`
Ticket: *"the panel should be inside the image."* Reuses the **existing desktop** absolute placement, so no new value.
Accept: badge bounds inside the photo bounds at 390 and 320 · no overflow, no clipping, text legible over the image.
⚠ Reverses R2's decision to make the badge absolute only from `lg:` — the overflow R2 was avoiding must not return.

**Q9 · Testimonial card centred on mobile** — `1217213785962852` (HOME-19)
`sections/Testimonials.tsx` · route `/`
Flush-left with the next peeking → centred. Accept: equal margins both sides at 390 and 320 · scroll-snap intact · desktop unchanged.

**Q10 · Gallery text left-aligned on mobile** — `1217213785962855` (HOME-20)
`home/Gallery.tsx` · route `/`
`items-center text-center` applies at every width → left-aligned on mobile. Accept: left at 390/320 · centred from the desktop breakpoint up · tile grid untouched.

### About

**Q11 · Remove the duplicate hero monogram** — `1217108466019431` (ABOUT-01, *second half*)
`about/AboutHero.tsx` · route `/about`
`glyph-ring.png` renders centred at `opacity-[0.10]`, duplicating the header logo. Remove it.
Accept: no monogram in the hero · hero 900 at 1440 · scrim and heading placement unchanged.
Hover half already verified done (comment `1217239076043987`) — this closes the ticket.

**Q12 · Values card internal layout** — `1217213785962840` (ABOUT-08)
`about/AboutValues.tsx` · route `/about`
Defect: icon floats top with dead space below the text; photo inset with padding. Figma frame `About/4 ChromeSafari.png` shows icon top-left, heading and paragraph anchored lower-left, photo flush to the card's right/top/bottom edges.
Accept: matches that frame structurally · card 847×440 at 1440 · no dead space below the paragraph.
**Structural only — no padding or gap values are to be changed to numbers we chose.**

**Q13 · About pill icons must render** — `1217234006576138` (ABOUT-11)
`about/AboutIntro.tsx` · route `/about`
Defect: **both icon slots render empty on mobile** — nothing loads. The official files are already in the repo (`about-icon-skilled-nursing.png.asset.json`, `about-icon-medication-management.png.asset.json`).
Also: the pill overflows past the photo's bottom edge (`About/10`, `About/12`) — contain it.
Accept: both icons `naturalWidth > 0` at 390, 320 and 1440 · pill fully inside the photo bounds.
**Pre-dispatch check required:** read `AboutIntro.tsx` first and confirm those two files are the ones being referenced. If it points at Lucide icons instead, this becomes an asset question and gets blocked.

### Services

**Q14 · Indian Program list consistency** — `1217234006576153` (SERV-04)
`services/ServicesList.tsx` · route `/services`
Defect: this card uses chips; the other three use bulleted lists — visible side by side in the same screenshot.
Accept: same list treatment as the other three · all ten items retained verbatim · panel 847×500 at 1440.

**Q15 · Services CTA to the end; remove the Therapy chip** — `1217234006576162` (SERV-07)
`services/ServicesList.tsx` · route `/services`
Ticket: *"the button should be at the end of the section, and there's no such chip."*
Accept: "Plan Your Visit" moved below the cards · "Therapy" chip removed · no other chip removed without instruction.

**Q16 · 24/7 panel stops clipping its text** — `1217234006576150` (SERV-03, *clipping half only*)
`services/CareApproach.tsx` · route `/services`
Defect: the supporting line is cut at the card's right edge — a real overflow bug.
Accept: no clipped text at any of the 22 viewports · row 460 with columns 306/621/313 at 1440 unchanged.
**Repositioning half blocked** — no measured target for the monogram / 24/7 / Comfort-Care-Compassion placement.

### Careers · Contact

**Q17 · Remove "View full Team"** — `1217234006576183` (CAR-03)
`careers/CareersTeam.tsx` · route `/careers`
Red X on the button; ticket says remove it on desktop and mobile.
Accept: button gone at all viewports · eight monograms 68×68 retained · section spacing closes without a gap.

**Q18 · Contact hero left column vertically centred** — `1217234006576186` (CON-01)
`contact/ContactHero.tsx` · route `/contact`
Defect: the column is top-anchored and the h1 collides with the header row.
Accept: column vertically centred in the hero · no collision with the header at any width · column exactly 413 and photo 630×720 at 1440 (both R6 fixes — must not move).

---

## 2 · DROPPED FROM REV 1 — 21 items, and why

### Blocked by your ruling — 3

| Item | Reason |
|---|---|
| ABOUT-06 (was Q5) | Testimonials gap — no approved value |
| HOME-04 (was Q13) | Hero band terminus — the annotation marks the current state, not a target |
| CAR-01 (was Q36) | Careers scrim — no Figma frame for that hero |

### Admissions / Amenities — 5

ADM-01, ADM-03, ADM-06, ADM-07 and the ADM-08 half of the shared Cta turn. Held until the IA question is answered (`1217243625850198`).

### Typography — 2

ABOUT-12 (mission paragraph family and size) and the ABOUT-02 label-weight half. Held for the Playfair weight table (`1217234108090689`) and the Poppins/Satoshi decision (`1217239076714225`).

### Newly blocked on the same test — 11

These passed Rev 1 but fail criterion 2. Listing them because dropping them silently would be the exact failure this protocol exists to prevent.

| Item | Rev 1 turn | Value we would have invented |
|---|---|---|
| HOME-13 footer newsletter response | Q3 | The confirmation's appearance. The ticket reports broken *function*, but implementing it creates an undesigned UI element. **If you class this as functional rather than visual, say so and it returns to the queue** |
| HOME-21 form machinery | Q4 | Nothing visual — but it is invisible plumbing for S1/S2, which are blocked. **Deferred deliberately to share the S1/S2 turn and save a credit** |
| HOME-09 card structure | Q6 | Empty photo boxes on cards with no photo |
| HOME-07 Mission 5-stage reveal | Q11 | Scroll distances and per-stage opacities — the frames show end states, not the interpolation |
| HOME-03 heading colour + hero photo | Q12 | The colour half changes a **global** `--heading` token from one page ticket, and contradicts §1 of our own design system (`#0F0F0F`). The photo half is contaminated — the red X sits on the very photo we would adopt |
| HOME-08 pinning | Q10 | The scroll release point |
| ABOUT-14 + ADM-08 Cta mobile | Q19 | "Sizes seem swapped" gives no target proportions |
| ABOUT-04 values scroll-stack | Q20 | Scroll distances, plus the card-2 background hex |
| ABOUT-03 mission variant swap | Q22 | The scroll trigger point for the swap |
| ABOUT-09 mobile hero | Q25 | Hero height. *(The button-alignment half alone was too thin to justify a turn while the main complaint stays unaddressed)* |
| ABOUT-02 paragraph shift | Q26 | How far right |
| SERV-05 mobile hero | Q28 | Header→H1 gap, and the H1 size reduction is typography-blocked |
| CON-03 checkmarks | Q38 | The tick hex — cannot be sampled reliably from the screenshot |
| AUX-03 404 rebuild | Q39 | Background hex, "404" size, watermark size and opacity. Copy and structure are fully known; the values are not |

**AUX-03 is the most frustrating of these.** Structure and copy are completely specified by the two Figma frames. It is held on four colour and size values. One reply with those unblocks a whole page.

---

## 3 · BLOCKED REGISTER — 41 of 59

| Cause | Count |
|---|---|
| Value not approved (the new test) | 14 |
| Awaiting a posted question | 5 |
| Screenshot absent from the export (4 reopened) | 4 |
| Admissions/Amenities IA | 5 |
| Playfair weights / Poppins / Satoshi | 5 |
| Legal body copy | 2 |
| Figma asset file needed | 2 |
| Ruled blocked by you | 3 |
| No derivable target at all (HOME-02) | 1 |
| **Total** | **41** |

18 + 41 = 59 ✓

---

## 4 · WHY REV 1 WAS WRONG

Rev 1 counted an item dispatchable if I could describe the target in a sentence. That is a lower bar than being able to *build* it without choosing a number.

Three items I had already flagged as carrying "a flagged interpretation" — and eleven more had the same defect without my flagging it, because each individual guess looked small: a gap, a hex, a scroll trigger. Small guesses are exactly how a QA backlog gets re-opened after implementation, and each would have cost a turn to make and a turn to correct.

The 18 that survive share one property: **every one is either a removal, a re-order, an alignment, a boolean, an overflow fix, or the use of an asset already in the repo.** None requires a value the agency has not approved.

---

## 5 · WHAT UNBLOCKS THE MOST, PER REPLY

1. **Playfair weight table** (`1217234108090689`) → 5 items
2. **Admissions/Amenities IA** (`1217243625850198`) → 5 items, plus the page's identity
3. **The four missing screenshots** → 4 reopened items, possibly closable on sight
4. **404 colours and sizes** → a whole page in one turn
5. **CTA panel hex** (`1217239076201709`) → 3 items across 3 routes
6. **Testimonial photos** (`1217231593814836`) → completes HOME-09

---

## 6 · VERIFICATION LOOP (unchanged)

Per turn: read the changed files → confirm the change is present and nothing outside scope moved → check the rendered result against the mapped screenshot at the viewports the ticket names → re-measure the affected 1440 reference values → check console errors, image 404s, page overflow → for a shared component verify **every** route → only then close the Asana subtask with a verification comment. A Lovable report is never accepted as proof.

---

## 7 · STANDING ENGINEERING STANDARD — binding on every turn

Issued 2026-08-06. Production project, zero tolerance for rework. This governs every dispatch from here on.

### 7.1 · Pre-dispatch, before a single prompt is written

Rev 2 required a source read before dispatch for **Q13 only**. That is now mandatory for **all 18**:

1. Read the target file in full.
2. Read every file it imports that the change touches.
3. Identify the existing reusable component or token that already does the job — **never regenerate what exists**.
4. Confirm the defect is still present exactly as the ticket describes. If the code has moved on, re-verify before spending anything.
5. Write the prompt only after all four are done.

A prompt written without this is a guess wearing a specification.

### 7.2 · Every prompt must carry these constraints verbatim

- **Minimum edit.** Change only the lines required. Do not rewrite a file for a small change. Do not reformat.
- **Do not touch what works.** Named explicitly per turn: the 1440 reference values, the regression-watch list in `MASTER_IMPLEMENTATION_LEDGER.md` §15, and every fix from Waves 1–14 and R1–R7.
- **No unrequested change** to spacing, typography, colour, responsiveness, animation or layout. If the ticket did not ask for it, it does not move.
- **No component substitution**, no simplification, no removed functionality, no "improvement".
- **Only files directly related to the task.** Unrelated files are a failed turn.

### 7.3 · Required self-review, returned with every turn

Lovable must confirm, item by item, before reporting done:

`UI · responsiveness · animations · imports · console errors · runtime errors · TypeScript errors · broken layouts · existing functionality · visual consistency`

Any failure is fixed inside the same turn, not reported as a caveat.

### 7.4 · Our own verification is unchanged and still binding

Their self-review does not replace §6. We independently read the diff, check the rendered result against the mapped screenshot at the ticket's viewports, re-measure the affected 1440 values, and verify every route for a shared component — before the Asana subtask is closed.

### 7.5 · Why the blocked list is the point, not friction

"Correct on the first attempt" and "never guess" are the same requirement viewed from two ends. An item with an unapproved value cannot be built correctly on the first attempt — only guessed at, then corrected, at the cost of two turns and the credibility of the pass.

The 41 blocked items are what makes first-attempt-correct achievable for the 18. Each is blocked on a specific, answerable question, and every one of those questions is already posted in Asana.

---

## 8 · EXECUTION LOG — dispatch begun 2026-08-06 on `ВСЁ ОТПРАВЛЯЙ`

One subtask per Lovable turn, each preceded by the §7.1 source read and followed by the §6 independent verification.

| # | Ticket | GID | Outcome | Asana comment | Subtask state |
|---|---|---|---|---|---|
| Q1 | HOME-12 FAQ open on mount | `1217108466019416` | **Shipped & verified.** `useState(1)` → `null`. Section lands on 752 exactly — the R8 discrepancy resolved | posted | closed |
| Q2 | HOME-11 header scroll | `1217108466019413` | **Shipped & verified** over 3 turns. Two real bugs caught in our own verification, not theirs | posted | closed |
| Q3 | HOME-09 testimonial arrows | `1217108466019425` | **Shipped & verified.** Wrap-around cycling, arrows never disabled | posted | **left open** — photo/attribution half blocked |
| Q4 | HOME-14 heading lines | `1217213785962834` | **Shipped & verified.** 3 lines at ≥1280. Residual 4-line band 1024–1280 documented | posted | closed |
| Q5 | HOME-15 button label | `1217213785962837` | **Shipped & verified.** "View Amenities" → "View More" | posted | closed |
| Q6 | SERV rail not clickable | `1217108466019422` | **Shipped & verified.** Rail is now a passive indicator; `<nav>` demoted to `<div>` | `1217268161803922` | **left open** — pinning half blocked |
| Q7 | HOME-16 hero CTAs side by side | `1217213785962843` | **BLOCKED — reclassified.** Does not fit. See below | `1217265347900491` | open |
| Q8 | HOME-17 hero badge inside photo | `1217213785962846` | **BLOCKED — reclassified.** Panel would cover 74% of the photo. See below | `1217272191854590` | open |
| Q9 | HOME-19 testimonial card centred | `1217213785962852` | **Shipped & verified.** `[scroll-padding-left:16px]` — one class. Card now 16px from each edge at 390 and 320 | `1217270135177609` | **CLOSED** |
| Q10 | HOME-20 gallery text left on mobile | `1217213785962855` | **Shipped & verified.** Left below 640, centred from 640 — the component's own existing breakpoint | `1217265816310193` | **CLOSED** |
| Q11 | ABOUT-01 duplicate hero logo | `1217108466019431` | **Shipped & verified.** Hero glyph + import deleted; both scrims, photo and geometry intact | `1217272201128339` | **CLOSED** (both halves) |
| Q12 | ABOUT-08 values card layout | `1217213785962840` | **BLOCKED — reclassified.** Design reference unreadable; component rebuilt after the ticket | `1217272203924879` | open |
| Q13 | ABOUT-11 pill icons | `1217234006576138` | **BLOCKED — but diagnosed.** Icons load fine; they are white on #E5EEFF, contrast **1.17:1** | `1217272204703918` | open |

**8 closed · 2 shipped-but-open · 4 reclassified as blocked · 0 in flight.**

### 8.6 · Q12 — three independent reasons, any one sufficient

1. **The ticket specifies nothing.** ABOUT-08 reads in full: *"The card layout structure is broken here, please fix."*
2. **The design reference cannot be measured.** The attached Figma frame is **849 × 302 px for a whole page**; an 847px card occupies ~238px in it, a 3.6× reduction. Error ≈ ±10% ≈ ±85px on the card. The arrangement is legible; no dimension is.
3. **The component was rebuilt after the ticket was raised.** ABOUT-08 is from 03-Aug; R3 rewrote `AboutValues` on 05-Aug. The attached "live" screenshot no longer shows the current build — the text column is now `justify-center`, so the icon and text are centred as a group rather than pinned top and bottom.

Confirmed from the 1:1 live capture: card **847** wide, photo **265** — matching `sm:w-[265px]`. Those two numbers are real; nothing else is.

Also raised in the same comment: `AboutValues` renders **four Lucide icons** (`HandHeart`, `Home`, `Activity`, `Users`) where the standing rule forbids generic icons if official files exist. Asked whether official artwork exists for the four values.

### 8.7 · Q13 — the ticket's premise was wrong, and we proved it

ABOUT-11 reads *"The Figma icons are missing."* They are not.

- Both pills reference the **official** assets (`about-icon-skilled-nursing`, `about-icon-medication-management`) — the queue's mandatory pre-dispatch check passed; no Lucide substitution.
- The asset JSON resolves to a real 346-byte PNG.
- Pixel analysis of the agency's own screenshot 12 finds the glyph **present** — a white cluster (rgb 254,255,255) inside a badge of rgb(229,238,255). Rendering the badge as ASCII shows the glyph outline plainly.

**White on #E5EEFF = 1.17:1 contrast.** WCAG needs 3:1 for a graphic. The icons load and are invisible.

Two possible fixes, visibly different — dark badge with the white icon (matching the Home hero's identical 40px `bg-accent` badge, which is legible), or a pale badge with dark icon files we do not have. Asked which; refused to invert the artwork in CSS, since that modifies an official mark.

**Correction recorded:** our own §12 note claimed the pill overflows the photo's bottom edge on mobile. Re-checking, that was the phone's browser toolbar overlapping the page. The pill sits correctly inside the photo. Posted the correction rather than dropping it.

Q9 and Q10 are the **first two of the 59 QA subtasks marked complete** in this engagement. Both had a single, fully specified outcome and no blocked half.

### 8.4 · DEF-01 confirmed a third time, from a live browser

The Q10 turn was asked to report the container's content-left edge as a reference point for the alignment assertion. It returned **33.52px at 390** and **29.26px at 320** — against the 33.5 and 29.3 predicted from the clamp, and the 33.2 measured off the QA screenshot. Three independent sources agree. DEF-01 is not a reading error.

### 8.5 · Footer logo resized twice outside this queue — flagged, not actioned

Between the Q5 and Q6 turns the client sent Lovable two direct requests, both worded "reduce the footer logo by roughly 25–30%". The first took `Logo` from its 52px default to `h-[38px]`; the second took it to `h-[28px]`. Net **52 → 28, a 46% reduction**.

The second turn's baseline was ambiguous and the agent said so in its own reasoning before guessing — *"we don't have exact measurement… we don't have Figma."* If "25–30%" meant off the original, 38px was already correct and 28px overshoots by ~26%. Current source confirms `<Logo variant="dark" className="h-[28px]" />`.

Raised with the client; **not reverted** — the baseline is theirs to state. Note this is *not* the element in HOME-13, which concerns the large faint watermark (`footer-logo-official.png`) at the bottom centre, not this wordmark.

### 8.1 · Q7 and Q8 — why Rev 2 was still one bar too low

Both passed the Rev 2 test ("is there an approved visual target?") on the strength of the annotated screenshot. The pre-dispatch read plus measurement showed the screenshot states the *intent* but not the *values*, and in both cases the intent cannot be executed at the stated values.

**Q7.** Measured off the QA screenshot itself, which is a 390px viewport (confirmed three ways: side margin 33.2 vs 33.5 predicted, button height, photo aspect exactly 3:2):

| | |
|---|---|
| "Explore Our Services" at the live 18px | 158.5px |
| "Plan Your Visit" at the live 18px | 108.1px |
| `px-7` per button | 56px |
| `gap-4` | 16px |
| **Row requires** | **398.6px** |
| Available at 390 today | 323px |
| Available at 390 with the gutter corrected | 358px |
| At the design system's own 16px mobile button size | still ~366px |

Short by ~40px at best. Side-by-side needs a decision on label text, font size, padding, or wrapping — all design values. Four options posted.

**Q8.** Photo is 323 × 215 at 390. Panel content computes to ~160px tall × up to 275px wide. Inside the photo at the desktop's 24px inset it covers ~74% of the photo's height and ~85% of its width. Also noted: `bg-secondary-bg` equals the hero background, so the panel currently reads as loose text, and the desktop `lg:max-w-[340px]` exceeds the entire 323px mobile content width. Four options posted.

**The lesson, recorded plainly.** An annotated screenshot proves a defect exists. It does not prove the fix is specified. Rev 2 conflated the two. The revised test: *can the target be built without choosing a number the design has not given?*

### 8.2 · Two genuine defects found during the Q7 pre-dispatch read

Neither was fixed — both are outside the tickets in hand and both need sign-off.

**DEF-01 · `container-gutter` clamp intercept has the wrong sign.** `styles.css`:

```
padding-inline: clamp(1rem, 0.6095rem + 6.0952vw, 5rem)
```

For the documented 16px @ 390 → 80px @ 1440 the intercept must be **−0.4857rem**. It is **+0.6095rem**.

| Viewport | Renders | Intended |
|---|---|---|
| 320 | 29.3 | 16 |
| 390 | **33.5** | **16** |
| 768 | 56.6 | 39.0 |
| 1024 | 72.2 | 55.6 |
| 1152 | 80 (clamps early) | 62.4 |
| 1440 | 80 ✓ | 80 ✓ |

Correct at 1440, which is why every desktop pass missed it. Confirmed against the screenshot: content measures 323.7px at 390 instead of 358. Affects all 9 routes below 1152px; reported on HOME-02 (`1217265139981647`), which asked "spacing differs a lot from Figma" and had never been pinned to a cause. **Not fixed unilaterally** — R1–R7 were QA'd against the current, too-wide gutters, so this needs its own scheduled change and its own full re-check.

**DEF-02 · the `dark`/`light` button variants bypass the `text-button` token.** `ui/button.tsx` hard-codes `text-[18px] leading-[20px] tracking-[-0.18px]`, so the design system's own fluid button scale (`clamp(1rem …)` = 16px at 390 → 18px at 1440) never applies. Buttons render 18px at every width. Surfaced by Q7; not yet raised as its own ticket because HOME-18 (heading weights) is the live typography question and this belongs with it.

### 8.3 · Figma access is live again — and we have no file link

`whoami` now authenticates as oybekovj97@gmail.com across two plans ("Geek Brains", "Project"). Every Figma tool requires a `fileKey`, and there is **no Figma URL anywhere in our records** — the design measurements in `MASTER_IMPLEMENTATION_LEDGER.md` were reconstructed from Lovable history precisely because Figma was unreachable at the time.

One file link would unblock Q7, Q8, HOME-19/20, the Playfair weight table (6 items across 4 pages), the CTA hex, and the Admissions IA frame. Requested in the Q7 and Q8 comments. **This is now the single highest-value outstanding request** — ahead of the four missing screenshots.

---

# QUEUE REVISION 4 — rebuilt on the official Figma rasters · 2026-08-07

Rev 3's test stands: *can this be built without choosing a number the design has not given?* The rasters changed the answer for a lot of items, in both directions.

## R4 · DISPATCHABLE — 13 turns

Ordered shared-component-first, then by risk. One logical correction per turn.

| # | Ticket(s) | Component | Target — all measured, none invented |
|---|---|---|---|
| **01** | ABOUT-05 `1217108466019447` · ADM-05 `1217108466019473` | `sections/Cta.tsx` | Panel **#56677F** = existing `--blue-500`/`accent` token. Watermark delta ≤4 units (design: 2). **3 routes, 2 GIDs, one implementation.** |
| 02 | SERV-06 `1217234006576159` | `services/CareApproach.tsx` | "services overview" block **left-aligned** on mobile, centred from 1024 |
| 03 | CAR-03 `1217234006576183` | `careers/CareersTeam.tsx` | Remove "View full Team" — absent from both approved frames |
| 04 | ABOUT-13 `1217234006576144` | `about/AboutValues.tsx` | Remove dark circular icon badge **at mobile widths only** — present on desktop |
| 05 | SERV-04 `1217234006576153` | `services/ServicesList.tsx` | Indian Program → same bulleted list as the other three cards |
| 06 | ADM mobile card order `1217108466019462` | `amenities/AmenitiesCarousel.tsx` | Mobile order **image → heading → body → list → Book a Call** |
| 07 | HOME-16 `1217213785962843` | `home/Hero.tsx` + `ui/button.tsx` | 393: dark **188**, gap **16**, light **157**, h **44**. Label = `text-button` token |
| 08 | HOME-17 `1217213785962846` | `home/Hero.tsx` | Photo **361 × 428**; badge **273 × 126**, insets 16/16, fill #E6F0FF, bottom-**left** |
| 09 | CON-01 `1217234006576186` | `contact/ContactHero.tsx` | Left column block y **383…593** against photo y 100…819 |
| 10 | ADM-02 `1217108466019462` | `amenities/AmenitiesCarousel.tsx` | Active card **centred in the viewport** — margins 299/299, not the 80 gutter |
| 11 | Careers hero scrim (CAR-01 half) | `careers/CareersHero.tsx` | Rendered luminance to match: bottom-left **143**, mid-left **99**, right **75** |
| 12 | Services mobile hero order | `services/ServicesHero.tsx` | "Scroll to Explore" **below** the image |
| 13 | 404 rebuild `1217234006576196` | `NotFoundPage.tsx` | Full geometry, both breakpoints — §14 |

### Needs one more measurement first — then dispatchable

| Ticket | Missing |
|---|---|
| CAR-02 | Intro section height vs our `min-h-[590px]`; mobile order. Layout itself measured: photo **360 × 350**, gap **290**, text **630** |
| ABOUT-14 · ADM-08 | Mobile CTA panel/image heights from the raster. Direction confirmed: panel **shorter** than image; we currently have it inverted (440 vs 320) |
| ABOUT-08 | Desktop values-card internals. Photo confirmed **inset**, not flush — our thumbnail reading was wrong |
| HOME-18 | Playfair weight calibration against the h1–h4 crops. Method proven on the button labels. **Needs no agency answer** |

## R4 · BLOCKED — and why

| Blocker | Items | Needs |
|---|---|---|
| **ADM-04 IA** | all Admissions naming | Agency decision. Raster deepens the conflict — nav says "Admissions" on a page designed as Amenities |
| **Legal copy verification** | Privacy, Terms | Transcribed in full, but read off an image. Our own May 28 → **May 26** date error proves the risk. Agency must send text or verify |
| **Form S1/S2 copy** | HOME-21, CON-03 | Copy hidden under the annotation digits |
| **Testimonial identity** | HOME-09 | Design shows "Oliver W." twice on three pages, "Olivia T." on mobile Home. Ambiguity is in the design |
| **Token changes** | gutter, `--blue-300`, `--blue-50` | Global atomic per the agency's own instruction — measure, change once, verify every route |
| **Footer logo** | — | Figma says **232 × 64**; we ship h 28 after two reduction requests. Client decision |
| **ABOUT-11 badge** | icons invisible at 1.17:1 | Dark badge, or dark icon files? |
| **Amenities card content** | — | Desktop and mobile frames pair different lists with the same heading |
| **Privacy nav duplicate** | — | 10 nav entries, 9 sections |

## R4 · CLOSED — confirmed correct against the rasters, no turn to be spent

HOME-12 · HOME-14 (confirmed twice, from two different pages) · HOME-15 · HOME-19 · HOME-20 · ABOUT-01 · plus verified-correct geometry: desktop header logo 188×52, Amenities card 846×450 with gap 20 and arrows below, Contact hero photo 630×720, Careers hero 900.

## R4 · EXECUTION LOG

| # | Ticket(s) | Outcome |
|---|---|---|
| **01** | ABOUT-05 `1217108466019447` · ADM-05 `1217108466019473` | **Shipped, verified, both CLOSED.** Panel → `bg-accent`; overlay → `bg-accent/[0.98]`. Computed `rgb(87,104,127)` on all 3 routes · 630×660 · contrast 5.44:1 · mobile 440/320 untouched. Comments `1217269743142533`, `1217269767268478` |
| 02 | SERV-06 `1217234006576159` | **Shipped, verified, CLOSED.** Left below 1024, centred from 1024. 393: container edge and all three text elements at **33.70**. 1023 left / 1024 centred. 1440 unchanged — offsets 330/330, collage 306/621/313, row 460. Comment `1217269745205600` |
| 03 | CAR-03 `1217234006576183` | **Shipped, verified, CLOSED.** Button + 2 orphaned imports removed. 0 matches at 5 widths · 8 cards · 900 height · /about unaffected. Comment `1217270407553377` |
| 04 | ABOUT-13 `1217234006576144` | **Shipped, verified, CLOSED.** Badge `hidden … sm:flex`, wrapper `mt-0 sm:mt-6`. Mobile gap exactly **24** · 639 none / 640 flex · desktop badge intact 48×48 navy, icon 20×20 white, card 440, stack preserved. Comment `1217270616549985` |
| 05 | SERV-04 `1217234006576153` | **BLOCKED — content conflict.** See §R4-05. Comment `1217270618523911` |

### R4-01 · we corrected the implementer, not the other way round

The turn reported the pattern overlay as **"visually inert"** — that its opacity no longer modulates the watermark because the panel's `background-image` stacks above a `-z-10` child — and offered to restructure the layer.

That is wrong, and the arithmetic settles it. With `bg-accent` = `rgb(87,104,127)` and a **white** pattern showing through at 2% (overlay `0.98`):

```
R: 87  + 0.02 × 168 = 90.4  → 5A
G: 104 + 0.02 × 151 = 107.0 → 6B
B: 127 + 0.02 × 128 = 129.6 → 82
```

**#5A6B82** — the measured dominant tone, to the unit. The overlay is doing exactly what it was set to do; the knob is live. Accepting the report would have authorised a needless restructure of a component shared by three routes.

### R4-01 · residual, and a fourth token defect

Rendered surface **#5A6B82** vs target **#56677F** — 4 units, imperceptible, two causes:

1. **`--blue-500` is stored as `214 19% 42%`, which converts to `#57687F`** — 1 unit off #56677F before anything else. **This is a fourth token defect**, alongside `--blue-300`, `--blue-50` and the gutter.
2. The pattern contributes +3 against Figma's +2.

Neither is fixable inside a colour ticket: (1) is a shared token — the pending global atomic change; (2) is a 1-unit tuning not worth a build cycle. Both reported to the agency rather than buried.

### Queue correction

R4-02's component was listed as `services/ServicesList.tsx`. The pre-dispatch read shows the "services overview" block lives in **`services/CareApproach.tsx`**. Corrected above. Caught by the mandatory read, which is what it is for.

### R4-02 · the ticket's own contradiction, resolved by the raster

SERV-06 read *"справа"* (right), but its arrow pointed **left** and the equivalent Home block was asked to go left. We flagged the contradiction rather than guessing. The mobile frame settles it: eyebrow ink at x 17, heading at x 18, both on the 16px gutter. **Left.**

Desktop measured centred — eyebrow 719.0, heading 720.0, body 719.0 against a 720 centre — so the shape is identical to HOME-20, and the switch was tied to this component's own 1024 collage breakpoint rather than a new one. The 1023/1024 pair proves it lands there.

### R4-03 · pre-dispatch read found a second-order deletion

`CareersTeam.tsx` uses `Link` and `Button` **only** inside the "View full Team" block. Removing the block orphans both imports, so the brief names them explicitly and requires the implementer to verify no other use before deleting.

Also caught: the Figma frame renders **"Director of Houskeeping"** — a typo in the design. Our source has the correct "Housekeeping". The brief explicitly forbids "correcting" our spelling to match the raster. The authority order makes Figma the visual reference, not a licence to copy its spelling mistakes into production.

### R4-05 · blocked — the raster would delete four services

SERV-04 asks for **list treatment** consistency: the Indian Program card uses chips where the other three use bullets. Confirmed, and the styling fix is trivial.

But the Figma mobile frame does not just change the treatment, it **changes the content**:

| | Site | Figma mobile |
|---|---|---|
| Indian Program | **10** discrete items | **3** combined bullets |
| Dropped entirely | — | Indian Cooks · Indian Snacks · Indian Newspapers · Indian Environment |
| Body copy ends | "…language, and daily experiences." | "…language, and **meals**." |
| Comprehensive Clinical Support | **6** items | **3** items |
| Its body copy | "may receive a range of clinical care services" | "receive expert clinical support to aid stroke, orthopedic, or cardio recovery" |

**Desktop cannot arbitrate.** The desktop frame uses the rail-plus-active-panel layout, so only the Short-Term Rehabilitation panel is drawn — the Indian Program panel is absent from the export. The mobile frame is the sole evidence and may simply be a shortened mobile treatment.

Deleting four offerings from a care home's cultural programme is a **service claim**, not styling. Blocked with three options; (a) keep all ten and convert to bullets is recommended, since it satisfies the ticket exactly and loses nothing.

### FIFTH design-content defect — another company's name in the approved file

The Figma FAQ answer to *"Do you accept Medicare or private insurance?"* reads:

> **"Brookwood** provides a full spectrum of senior care services, including rehabilitation, skilled nursing, **memory care**, and wellness programs…"

**Brookwood is not Amara.** Template copy from another project, sitting in the approved design.

Our build already reads "Amara Care Center" — corrected earlier — so the live site is clean. But anyone rebuilding this section from the raster would put a competitor's name onto the site. Raised on the Services DEV task (`1217269774939145`).

Two further problems in the same answer, one of which **is live**:
- It never mentions Medicare or insurance — it answers a different question than the one asked.
- It claims **"memory care"** as a service. On a healthcare site that is a factual claim about what the provider offers, and it needs confirming or removing.

Not drafted or corrected by us: clinical and commercial claims are the client's to state.

**Design-content defects now at five:** duplicated testimonial author · Amenities card lists disagreeing between frames · Privacy nav 10-entries-9-sections · ADM-04 naming · Brookwood in the FAQ.
