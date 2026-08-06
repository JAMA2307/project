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
