# ASANA QA LEDGER — Amara Care Center

| | |
|---|---|
| Collected | 2026-08-06 |
| Workspace | `1210357482925157` — **display name "Eloqwnt"** (see §0.1) |
| Project | **Amara** · `1217105105055924` · [open](https://app.asana.com/1/1210357482925157/project/1217105105055924) |
| Team | Eloqwnt · `1210357482925159` · project is **private** (`public: false`) |
| Project owner | `shokhrukh.orolov@gmail.com` · `1214031295224067` — sole author of every task and comment |
| Sections | **DEV** `1217105105055925` · **QA** `1217105105055927` |
| Created / last modified | 2026-08-03 07:21 · 2026-08-05 07:20 |
| Companion ledgers | `MASTER_IMPLEMENTATION_LEDGER.md` · `ASSET_MAP.md` · `ASANA_IMPLEMENTATION_PLAN.md` |

---

## 0 · COLLECTION SUMMARY

| Metric | Value |
|---|---|
| Top-level tasks inspected | **14 / 14** (7 DEV + 7 QA) |
| Subtasks inspected | **59 / 59** |
| Comments inspected | **1** — the only comment in the entire project (HOME-06) |
| Attachments enumerated | **60** |
| Attachments visually inspected | **0** — see §0.2, blocked |
| Custom fields | **none defined on this project** |
| Assignees | **none** — every task is unassigned |
| Due dates | **none** |
| Priorities | **none** — no priority field exists |
| Dependencies | **none** |
| Tags | **none** |
| Archived / hidden items | none found; `archived: false` |
| Completed subtasks | **4 of 59** — HOME-01, HOME-10, SERV-01, SERV-02 |

### 0.1 · Two naming discrepancies, recorded not corrected

1. **Workspace is named "Eloqwnt", not "Work".** The GID matches the supplied URL exactly (`1210357482925157`), and the account is a member of exactly this one workspace, so this **is** the right project. I am recording the discrepancy rather than claiming to have confirmed a workspace named "Work".
2. **There is no "Amenities" task in either section.** The board's **"Admissions"** task is the QA for the `/amenities` route — its subtasks describe the Amenities hero, carousel and gallery. Related: ADM-04 flags the nav/page naming as a defect. See §5-C1.

### 0.2 · Attachments — BLOCKED, and what that costs

All 60 attachments are enumerated with GIDs and signed download URLs (§6). **Zero could be opened.** The session's egress policy blocks every Asana host:

```
CONNECT asanausercontent.com:443  →  HTTP/1.1 403 Forbidden
CONNECT app.asana.com:443         →  blocked
CONNECT asana.com:443             →  blocked
```

Proxy diagnostic (`$HTTPS_PROXY/__agentproxy/status`) logs each attempt as:
```json
{"kind":"connect_rejected",
 "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
 "host":"asanausercontent.com:443"}
```
`WebFetch` on the same URL also returns **HTTP 403**. The proxy README is explicit that a 403 is an organisation egress-policy denial and must be reported, not routed around.

**Consequence, stated plainly:** every QA item below is reconstructed from its **written description only**. The descriptions are specific — most name the section, the defect and the required end state — but the annotated screenshot is the primary artefact and I have not seen a single one. Items whose text alone does not determine the fix are marked **NEEDS VISUAL VERIFICATION** and must not be implemented until the image is available.

**To unblock:** allow `asanausercontent.com` in the session egress policy, or export the 60 images and place them in the repo. Nothing else is required — the text collection is complete.

### 0.3 · Read-only compliance

Nothing in Asana was created, edited, moved, completed, commented on, reassigned, re-dated, uploaded or deleted. Every call used was a read (`get_project`, `get_tasks`, `get_task`, `get_me`, `get_projects`, `search_objects`). No Lovable agent message was sent during this phase; the only Lovable calls were `list_files` / `read_file`, which are reads and consume no credits.

---

## 1 · DEV SECTION — implementation status board

Seven cards, one per page. **All seven are empty**: no description (except one), no comment, no attachment, no assignee, no subtask, and all are `completed: false`.

| Task ID | Title | Status | Content |
|---|---|---|---|
| `1217105105055928` | Home | incomplete | empty |
| `1217105105055930` | About | incomplete | empty |
| `1217105105055932` | Services | incomplete | empty |
| `1217105105055934` | Admissions | incomplete | empty |
| `1217105105055936` | Careers | incomplete | empty |
| `1217105105055938` | Contact us | incomplete | empty |
| `1217105105055940` | Auxilliary pages | incomplete | *"В эти страницы входит: 404, privacy policy, Terms"* |

**Reading.** DEV carries **no implementation status information at all.** These are page placeholders. Per the collection brief — *"Do not mark a DEV page complete merely because its card exists"* — the correct inference is the opposite of completion: DEV tells us nothing, so page state must be judged from QA plus our own verification. **No DEV card should be treated as a signal in either direction.**

**Missing coverage:** DEV has no card for Amenities as a distinct page, and none for Privacy / Terms / 404 individually (folded into "Auxilliary pages").

---

## 2 · QA SECTION — the backlog

Seven parent cards, 59 subtasks. Parent cards carry no attachments and only two descriptions.

Test devices, from the Home parent card (`1217105105055942`) — **the only place the test matrix is recorded, and it applies to the whole board**:
> *Devices — Macbook 13" + Desktop Windows, iPhone 16 Pro*

That maps to roughly **1440×900 / 1470×956 (MacBook 13")**, an unspecified Windows desktop, and **393×852 (iPhone 16 Pro)**. Every "mobile" subtask below should be read as iPhone 16 Pro, not 320px.

Legend — **Sev**: CRITICAL / MAJOR / MINOR / BLOCKED · **State**: OPEN / ALREADY FIXED / PARTIALLY FIXED / DUPLICATE / STALE / NEEDS VISUAL VERIFICATION (NVV) · **Shared**: the shared component the fix belongs in, if any.

---

### 2.1 · HOME — parent `1217105105055942` · 21 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105055942) · route `/`

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **HOME-01** | `1217105105133471` · "1 Safari/Chrom" · **completed in Asana** · mod 08-06 | *"Brand elements are different, doesn't look like Figma."* | Brand marks / logo | MAJOR | NVV — closed by agency; verify before assuming resolved | **Logo/brand** |
| **HOME-02** | `1217108334767496` · "2 Safari/Chrome" | *"Spacing differs a lot from Figma."* | unidentified section | MAJOR | NVV — section not named in text | Spacing scale |
| **HOME-03** | `1217108334767499` · "3 Safari/Chrome" | *"This image needs to go on the hero; also the black text should be bluish, as in Figma."* | `home/Hero.tsx` | MAJOR | OPEN — colour change actionable; the image is identifiable only from the screenshot | — |
| **HOME-04** | `1217108334767502` · "4 Safari/Chrome" | *"Reduce the end of the border here."* | unidentified | MINOR | NVV | — |
| **HOME-05** | `1217108334767505` · "5 Safari/Chrome" | *"Increase the text and the heading — in Figma they're a bit heavier."* | typography | MAJOR | OPEN | **Type scale** |
| **HOME-06** | `1217108334767508` · "6 Safari/Chrome" · **has the project's only comment** | Description: *"There should be a hover animation on the card. First the image shows; then on hover it becomes a card in the centre and text appears. I've added the text in Figma. For the image, take another thematically similar one from the same Figma."* · **Comment 2026-08-06 07:34, `1217213785962832`: "These animations aren't here."** | card hover interaction | CRITICAL | **OPEN — re-reported today after the first report; agency confirms still missing** | — |
| **HOME-07** | `1217108334767511` · "7 Safari/Chrome" | *"Animation in this part."* | unidentified | MAJOR | NVV | — |
| **HOME-08** | `1217108466019422` · "8 safari/chrome" | *"It should stick in this state — right now only the shrunken headings are visible. Also make the buttons in this section non-clickable: the scroll-to-card isn't smooth and is basically unnecessary."* | scroll-pinned stack | CRITICAL | OPEN — two distinct changes: pin end-state, and disable in-section buttons | — |
| **HOME-09** | `1217108466019425` · "9 safari/chrome" | *"The card structure differs a lot from the design. Where images are missing you can put placeholders for now. Also make this section an infinite scroll — the pages loop."* | card carousel | CRITICAL | OPEN — **placeholder clause conflicts with a standing client rule, see §5-C2** | — |
| **HOME-10** | `1217108466019428` · "10 safari/chrome" · **completed in Asana** · mod 08-06 | *"These parts broke overall — section inside a section, images too big."* | nested section | CRITICAL | NVV — closed by agency; verify | — |
| **HOME-11** | `1217108466019450` · "11 safari/chrome" · **no attachment** | *"On scroll up, make the menu appear / come down."* | `Header.tsx` | MAJOR | **OPEN — verified in source: header is `absolute inset-x-0 top-6`, not sticky. No scroll behaviour of any kind exists. This is new work.** | **Header — all 9 routes** |
| **HOME-12** | `1217108466019458` · "12 safari/chrome" · **no attachment** | *"FAQ — one of the questions is open automatically. Remove that. In the design that's just showing how an answer looks when you click a question."* | `sections/Faq.tsx` | MAJOR | **OPEN — verified in source: `useState<number \| null>(1)` opens item 2 on mount. See §4 — this also resolves an open FAIL in the responsive pass.** | **FAQ — Home, Services, Careers** |
| **HOME-13** | `1217108466019476` · "13 safari/chromr" | *"The response after filling in and submitting your email doesn't work here; also the logo is wrong."* | footer newsletter | MAJOR | OPEN — two defects: no submit feedback, wrong logo asset | **Footer — all 9 routes** |
| **HOME-14** | `1217213785962834` · "14 safari/desktop" | Set the text to exactly: **"Contact out team / to learn more about / our services"** (3 lines) | CTA/contact block | MAJOR | OPEN — **"out" is almost certainly a typo for "our"; see §5-C3** | — |
| **HOME-15** | `1217213785962837` · "15 safary/desktop" | *"Add a View More here."* | unidentified list/grid | MAJOR | NVV — target section not named | — |
| **HOME-16** | `1217213785962843` · "16 Mobile" | *"The buttons should sit to the side."* | mobile layout | MAJOR | NVV | — |
| **HOME-17** | `1217213785962846` · "17 Mobile" | *"The small panel should be inside the image."* | mobile badge/overlay | MAJOR | NVV | — |
| **HOME-18** | `1217213785962849` · "18 Mobile" | *"Some headings use the wrong weight — bold vs regular etc."* | typography | MAJOR | OPEN | **Type scale** |
| **HOME-19** | `1217213785962852` · "19 Mobile" | *"All good except the card position — centre it on screen."* | mobile card | MINOR | NVV — which card is not named | — |
| **HOME-20** | `1217213785962855` · "20 Mobile" | *"The text should be on the left."* | mobile text align | MINOR | NVV | — |
| **HOME-21** | `1217234006576129` · "21 Mobile" | *"In the UI KIT section they added [states] for when messages are sent — use the one marked 1."* | contact form success state | MAJOR | OPEN — needs the Figma UI-KIT frame; **Figma access is blocked** | **Contact form — Home, Careers, Contact** |

---

### 2.2 · ABOUT — parent `1217105105055944` · 14 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105055944) · route `/about`

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **ABOUT-01** | `1217108466019431` · mod 08-06 | *"Need hover effects on the buttons. The logo is duplicated for some reason."* | Button, Logo | MAJOR | OPEN — duplicate-logo is a real structural defect | **Button + Logo** |
| **ABOUT-02** | `1217108466019434` | *"Move the paragraph to the right as in Figma. Add the correct icons. Add regular-weight text."* | `AboutIntro.tsx` | MAJOR | OPEN — "correct icons" implies official icon files not yet placed | Icons, Type scale |
| **ABOUT-03** | `1217108466019437` · **2 attachments** | *"In this part they should change as the text scrolls. The logo is wrong."* | `AboutMission.tsx` / scroll reveal | MAJOR | OPEN | **Logo/brand** |
| **ABOUT-04** | `1217108466019442` · **2 attachments** | *"The cards should rise and cover the previous one on scroll, and the card colour doesn't separate from the background the way it does on the site."* | `AboutValues.tsx` scroll-stack | CRITICAL | OPEN — motion + colour | — |
| **ABOUT-05** | `1217108466019447` | *"Get Started section — this section looks nothing like Figma."* | Get Started / CTA | CRITICAL | OPEN — full rebuild of the section | possibly **Cta** |
| **ABOUT-06** | `1217154780337210` | *"More spacing needed here."* | unidentified | MINOR | NVV | Spacing scale |
| **ABOUT-07** | `1217154780337213` | *"Change this block and put what's in Figma."* | unidentified | MAJOR | NVV — block not named | — |
| **ABOUT-08** | `1217213785962840` · mod 08-06 | *"The card layout structure is broken here, please fix."* | card grid | CRITICAL | OPEN | — |
| **ABOUT-09** | `1217234006576132` · mobile · mod 08-06 | *"The hero block (section 1) is very small — increase the space. The button doesn't line up with the text, and the text placement is off."* | `AboutHero.tsx` **mobile** | CRITICAL | **OPEN — this is the "ABOUT HERO — QA FAILED" report whose screenshots never reached me on 08-05. It is a MOBILE defect. R3 fixed the desktop hero (`aspect-ratio` resolving width from height); mobile was never in scope. Not a duplicate of R3, and not a regression.** | — |
| **ABOUT-10** | `1217234006576135` · mobile | *"The font family, weight and sizes look wrong."* | typography | MAJOR | OPEN | **Type scale** |
| **ABOUT-11** | `1217234006576138` · mobile | *"The Figma icons are missing."* | icons | MAJOR | OPEN — official icon files | **Icons** |
| **ABOUT-12** | `1217234006576141` · mobile | *"The description font is wrong — reduce it slightly; make the transition smooth/different."* | typography + motion | MAJOR | OPEN | **Type scale** |
| **ABOUT-13** | `1217234006576144` · mobile | *"These segments shouldn't have cards."* | mobile card removal | MAJOR | NVV — which segments is not named | — |
| **ABOUT-14** | `1217234006576147` · mobile | *"The sizes look swapped here."* | mobile sizing | MAJOR | NVV | — |

---

### 2.3 · SERVICES — parent `1217105105055946` · 7 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105055946) · route `/services`

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **SERV-01** | `1217108466019451` · **completed in Asana** · mod 08-06 | *"The structure here is completely different. Also the text at bottom-left should be heavier."* | `ServicesHero.tsx` | CRITICAL | NVV — closed by agency; verify | Type scale |
| **SERV-02** | `1217108466019455` · **completed in Asana** · mod 08-06 | *"Right panel — wrong logo, and there's no blur behind it on the lighter background. Middle — the image can stay but the card should be lighter. Top-left — the images are different. Bottom-left — wrong logo."* | `CareApproach.tsx` | CRITICAL | NVV — closed by agency; **four separate defects, two of them wrong-logo** | **Logo/brand** |
| **SERV-03** | `1217234006576150` · mod 08-06 | *"Fix the positions. Apply the changes on mobile too so it matches Figma."* | layout | MAJOR | NVV | — |
| **SERV-04** | `1217234006576153` | *"Why does this block differ from the others? Fix it."* | block consistency | MAJOR | NVV | — |
| **SERV-05** | `1217234006576156` · mobile | *"No space between the hero and the section above. Text sizes differ a lot — reduce so they fit. Button size is wrong, move it left. 'Scroll to explore' is in the wrong place."* | `ServicesHero.tsx` mobile | CRITICAL | OPEN — four distinct defects | Type scale |
| **SERV-06** | `1217234006576159` · mobile | *"They should be on the right."* | mobile alignment | MINOR | NVV | — |
| **SERV-07** | `1217234006576162` · mobile | *"The button should be at the end of the section, and there's no such panel."* | mobile layout | MAJOR | OPEN — a panel present in the design is missing entirely | — |

---

### 2.4 · ADMISSIONS — parent `1217105105055948` · 8 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105055948) · route **`/amenities`** (see §0.1)

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **ADM-01** | `1217108466019459` · mod 08-06 | *"The text on the left isn't centred — here's the Figma."* | `AmenitiesHero.tsx` | MAJOR | OPEN | — |
| **ADM-02** | `1217108466019462` | *"Do this a bit differently — the card that's supposed to come next appeared in the middle."* | `AmenitiesCarousel.tsx` | MAJOR | NVV | — |
| **ADM-03** | `1217108466019465` · mod 08-06 | *"It should have been 1 and 3, with text underneath like 'Serene / Courtyard Retreat'."* | `AmenitiesGallery.tsx` | MAJOR | OPEN — **the caption copy is given verbatim; the "1 and 3" ordering needs the screenshot** | — |
| **ADM-04** | `1217108466019468` | *"Right now I'm in Admissions and it shows Amenities."* | `Header.tsx` nav / page identity | CRITICAL | **OPEN — verified in source: `{ label: "Admissions", to: "/amenities" }` with a code comment saying the mismatch is deliberate per the design. See §5-C1 — this is a direct design-vs-agency conflict.** | **Header — all 9 routes** |
| **ADM-05** | `1217108466019473` · mod 08-06 | *"Wrong colour."* | unidentified | MAJOR | NVV — neither the element nor the target colour is named | possibly design tokens |
| **ADM-06** | `1217234006576167` · mobile | *"The button shouldn't be left [ambiguous]. And 'Scroll to explore' should go down, as in Figma."* | `AmenitiesHero.tsx` mobile | MAJOR | NVV — first clause ambiguous in the original | — |
| **ADM-07** | `1217234006576170` · mobile | *"Image up and down."* | mobile image | MINOR | NVV | — |
| **ADM-08** | `1217234006576173` · mobile | *"The sizes differ."* | mobile sizing | MAJOR | NVV | — |

---

### 2.5 · CAREERS — parent `1217105105055950` · 3 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105055950) · route `/careers`

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **CAR-01** | `1217234006576177` | *"The hero is darker than in Figma."* | `CareersHero.tsx` scrim | MAJOR | OPEN — the hero carries two inline gradient scrims (recorded in the R6 audit); the scrim opacity is the likely cause | — |
| **CAR-02** | `1217234006576180` | *"The structure doesn't match."* | unidentified section | MAJOR | NVV | — |
| **CAR-03** | `1217234006576183` | *"Remove the button here — on mobile too."* | button removal | MINOR | NVV — which button is not named, but the action is unambiguous | — |

---

### 2.6 · CONTACT US — parent `1217105105133465` · 3 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105133465) · route `/contact`

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **CON-01** | `1217234006576186` | *"Move the text on the left down to the middle."* | `ContactHero.tsx` | MAJOR | OPEN — vertical alignment of the left column | — |
| **CON-02** | `1217234006576189` | *"Change the icon here."* | icon swap | MINOR | NVV — needs the official icon file | **Icons** |
| **CON-03** | `1217234006576192` | *"Change the colour of the checkmarks."* | checkbox / bullet ticks | MINOR | OPEN — **caution: the square checkbox `!rounded-[4px]` is on the regression watch; change colour only, not shape** | **Contact form** |

---

### 2.7 · AUXILLIARY PAGES — parent `1217105105133467` · 3 subtasks
[parent](https://app.asana.com/1/1210357482925157/project/1217105105055924/task/1217105105133467) · routes `/privacy-policy`, `/terms-of-use`, 404
Parent description: *"These pages include: 404, privacy policy, Terms"*

| ID | Task | Requested correction (translated) | Component | Sev | State | Shared |
|---|---|---|---|---|---|---|
| **AUX-01** | `1217234006576196` | *"Add the text from Figma here."* | `LegalPage.tsx` — Privacy Policy | CRITICAL | **BLOCKED — the body copy lives only in Figma, and Figma access is exhausted. Content cannot be invented.** | **LegalPage** |
| **AUX-02** | `1217234006576199` | *"Add the text from Figma here."* | `LegalPage.tsx` — Terms of Use | CRITICAL | **BLOCKED — same. Note: this task's attachment `1217234006576200` resolves to the same underlying file as AUX-01's (`…/1217234006576197/6ea504e1…`) — the agency attached one image to both.** | **LegalPage** |
| **AUX-03** | `1217234006576202` | *"The 404 page doesn't look like Figma — add the missing elements."* | `NotFoundPage.tsx` | MAJOR | NVV — "missing elements" are only identifiable from the design | — |

---

## 3 · SHARED-COMPONENT GROUPING

Per the deduplication rule: one implementation issue, many affected routes, many verification checks.

| # | Shared issue | Asana items | Fix location | Affected routes | Verification checks |
|---|---|---|---|---|---|
| **SH-1** | **Header — reveal nav on scroll up** | HOME-11 | `Header.tsx` | all 9 | 9 |
| **SH-2** | **Header — "Admissions" nav points at `/amenities`** | ADM-04 | `Header.tsx` (+ routing/IA decision) | all 9 | 9 |
| **SH-3** | **FAQ — no item open on mount** | HOME-12 | `sections/Faq.tsx` | `/`, `/services`, `/careers` | 3 |
| **SH-4** | **Footer — newsletter submit gives no feedback; wrong logo** | HOME-13 | `Footer.tsx` | all 9 | 9 |
| **SH-5** | **Logo / brand marks — wrong mark in several places** | HOME-01, HOME-13, ABOUT-01 (duplicate), ABOUT-03, SERV-02 (×2) | `Logo.tsx`, `Footer.tsx`, `assets/brand/*` | `/`, `/about`, `/services` + wherever Logo renders | 6+ |
| **SH-6** | **Typography — weights and sizes off the design** | HOME-05, HOME-18, ABOUT-02, ABOUT-10, ABOUT-12, SERV-01, SERV-05 | `styles.css` type scale | all 9 | 9 |
| **SH-7** | **Official icons missing / wrong** | ABOUT-02, ABOUT-11, CON-02 | `assets/brand/*` + call sites | `/about`, `/contact` | 2 |
| **SH-8** | **Contact form — success state + checkmark colour** | HOME-21, CON-03 | `home/Contact.tsx` | `/`, `/careers`, `/contact` | 3 |
| **SH-9** | **Button hover states** | ABOUT-01 | `ui/button.tsx` | all 9 | 9 |
| **SH-10** | **Spacing scale** | HOME-02, ABOUT-06 | `styles.css` / section padding | ≥2, likely global | TBD |
| **SH-11** | **Legal page body copy** | AUX-01, AUX-02 | `LegalPage.tsx` | `/privacy-policy`, `/terms-of-use` | 2 |

**Deduplication effect:** 26 page-level Asana items collapse into **11 shared implementation issues**. Without grouping these would have been written as ~26 independent fixes across ~26 files.

---

## 4 · RECONCILIATION WITH THE EXISTING PROGRAMME

### 4.1 · HOME-12 resolves the one open FAIL in the responsive pass — arithmetic confirmed

Wave R7 measured the Home FAQ section at **766px against a spec of 752px** and could not explain the surplus. HOME-12 explains it exactly.

`sections/Faq.tsx` line: `const [open, setOpen] = useState<number | null>(1);`

| | Height |
|---|---|
| 6 question rows × `min-h-[64px]` | 384 |
| 5 gaps × `gap-3` (12px) | 60 |
| **Accordion, all closed** | **444** |
| Open answer on item 2 (3 lines × 22px lh + `pb-4`) | +82 |
| **Accordion as it renders today** | **526** ← exactly the 526 R7 measured |
| `py-[120px]` × 2 | 240 |
| **Section as it renders today** | **766** ← exactly the 766 R7 measured |
| **Section with all items closed** | 240 + 444 = 684 → `min-h-[752px]` governs → **752** ✅ |

**One fix closes both.** Collapsing the FAQ on mount satisfies the agency's instruction *and* lands the section on its 752 reference value naturally — no padding shaved, no section compressed. This is precisely the root cause R8 was dispatched to find; it was in Asana the whole time.

### 4.2 · Item-by-item reconciliation against previous waves

| Asana item | Verdict against our record |
|---|---|
| HOME-11 (header scroll) | **Still open — never in scope.** Source confirms `absolute … top-6`, no scroll listener. New feature, not a regression. |
| HOME-12 (FAQ) | **Still open.** Confirmed in source. Resolves R7's FAIL (§4.1). |
| ADM-04 (Admissions→Amenities) | **Conflict, not a bug report we can act on unilaterally.** Our §15 Regression Watch protects this exact mapping as design-correct. §5-C1. |
| ABOUT-09 (mobile hero) | **Still open, and correctly never actioned.** This is the 08-05 "ABOUT HERO — QA FAILED" whose screenshots never attached; I refused to rebuild blind. R3 then proved the *desktop* fault was `aspect-ratio` resolving width from height and fixed it with **no global value changed** — vindicating the refusal. ABOUT-09 is a **mobile** defect and is genuinely outstanding. |
| HOME-09 (placeholders) | **Conflicts with a standing client rule.** §5-C2. |
| HOME-14 ("Contact out team") | **Typo in the instruction.** §5-C3. |
| CON-03 (checkmark colour) | Open, but the checkbox **shape** (`!rounded-[4px]`) is on the regression watch — change colour only. |
| SERV-02, HOME-01, ABOUT-03 (wrong logos) | Consistent with our open **AST 1–10** asset gap and **NEW-04**. Root cause is the same: assets that need Figma access we do not have. |
| AUX-01 / AUX-02 (legal copy) | **Blocked on Figma**, same blocker as AST 1–10. |
| HOME-21 (form success state) | Needs the Figma **UI KIT** frame. **Blocked on Figma.** |
| All 4 Asana-completed items (HOME-01, HOME-10, SERV-01, SERV-02) | **Not accepted as fixed.** They were closed by the agency, but three were modified again on 2026-08-06 — after closure — and I cannot see the screenshots. Marked NVV. |
| Waves R1–R7 findings | **No Asana item contradicts any of them.** No wave fix is challenged by QA. |

### 4.3 · What QA does *not* cover

- **No item disputes any 1440 reference value.** The entire board is composition, motion, assets and mobile — not desktop geometry. The R1–R7 desktop work stands unchallenged.
- **No item mentions browser zoom.** The 150%-zoom dead-space complaint that drove the whole responsive programme appears nowhere in Asana.
- **No item mentions tablet.** The device list is MacBook 13", a Windows desktop, and iPhone 16 Pro. 768–1280 is untested by the agency.
- **No QA card exists for Amenities as a page distinct from Admissions**, nor for Privacy / Terms / 404 as separate cards beyond the three AUX subtasks.

---

## 5 · CONFLICTS REQUIRING A DECISION

Both sides preserved, per the no-silent-discard rule.

### C1 · "Admissions" nav → `/amenities` — **design vs. agency**
- **Implementation** (`Header.tsx`): `{ label: "Admissions", to: "/amenities" }`, with the comment *"Label intentionally 'Admissions' per the source design, pointing at /amenities."* Protected in our §15 Regression Watch.
- **Asana ADM-04** (2026-08-03): *"Right now I'm in Admissions and it shows Amenities."*
- **Complication:** the Asana board itself calls the `/amenities` QA card **"Admissions"** — so the agency uses the two names interchangeably, which is evidence the naming is unsettled on their side too.
- **Authority order** puts the latest agency decision (#1) above the Figma design (#2), so ADM-04 nominally wins. **But the resolution is not derivable**: it could be rename the route, rename the nav label, retitle the page, or build a separate Admissions page. There is no `/admissions` route today.
- **Needs:** a client/agency decision on information architecture. Do not guess.

### C2 · Placeholders — **agency instruction vs. standing client rule**
- **Asana HOME-09** (2026-08-03): *"where images are missing you can put placeholders for now."*
- **Standing client rule**, issued directly and repeatedly: *"Never use placeholder images. Never use stock replacements. If an asset is missing: STOP, report it, wait."*
- The client's instruction to me is the more recent and more specific authority, and the project currently renders **zero** `PlaceholderAsset` — a state achieved deliberately over Waves 6–14.
- **Recommendation:** do not reintroduce placeholders. Identify the missing images from the HOME-09 screenshot, request the real files, and leave the section as-is meanwhile. **Flagging rather than deciding** — the client can overrule.

### C3 · HOME-14 copy — **"Contact out team"**
- Asana specifies verbatim: *"Contact out team / to learn more about / our services"*.
- **"out" is almost certainly "our".** This matches the three typo overrides already in §0.0 of the master ledger (`Shedule`→`Schedule`, `addres`→`address`, `Brookwood`→`Amara`).
- **Recommendation:** ship **"Contact our team"** and record it as a fourth override. Reversible in one word if the agency actually meant otherwise.

### C4 · Four Asana-completed items modified after closure
HOME-01, HOME-10, SERV-01, SERV-02 are `completed: true`, yet three carry `modified_at` of **2026-08-06** — after they were closed. Either the agency reopened the underlying issue in the description or edited it post-closure. **Do not treat completion as acceptance** until the screenshots are visible.

### C5 · Workspace name
Supplied as "Work"; Asana reports **"Eloqwnt"**. GID matches exactly, so the project is right. Recorded, not corrected.

---

## 6 · ATTACHMENT REGISTER — 60 files, all enumerated, none opened

Every attachment GID is recorded so the images can be matched one-to-one when access is granted. All are `image.png`.

| Item | Attachment GID(s) |
|---|---|
| HOME-01 | `1217108334767495` |
| HOME-02 | `1217108334767498` |
| HOME-03 | `1217108334767501` |
| HOME-04 | `1217108334767504` |
| HOME-05 | `1217108334767507` |
| HOME-06 | `1217108334767510` (description) · `1217213785962831` (**comment**, 08-06) |
| HOME-07 | `1217108466019421` |
| HOME-08 | `1217108466019424` |
| HOME-09 | `1217108466019427` |
| HOME-10 | `1217108466019430` |
| HOME-11 | **none** |
| HOME-12 | **none** |
| HOME-13 | `1217108466019478` |
| HOME-14 | `1217213785962836` |
| HOME-15 | `1217213785962839` |
| HOME-16 | `1217213785962845` |
| HOME-17 | `1217213785962848` |
| HOME-18 | `1217213785962851` |
| HOME-19 | `1217213785962854` |
| HOME-20 | `1217213785962857` |
| HOME-21 | `1217234006576131` |
| ABOUT-01 | `1217154578583622` |
| ABOUT-02 | `1217154780337209` |
| ABOUT-03 | `1217108466019439` · `1217108466019441` |
| ABOUT-04 | `1217108466019444` · `1217108466019446` |
| ABOUT-05 | `1217108466019449` |
| ABOUT-06 | `1217154780337212` |
| ABOUT-07 | `1217154780337215` |
| ABOUT-08 | `1217213785962842` |
| ABOUT-09 | `1217234006576134` |
| ABOUT-10 | `1217234006576137` |
| ABOUT-11 | `1217234006576140` |
| ABOUT-12 | `1217234006576143` |
| ABOUT-13 | `1217234006576146` |
| ABOUT-14 | `1217234006576149` |
| SERV-01 | `1217108466019454` |
| SERV-02 | `1217108466019457` |
| SERV-03 | `1217234006576152` |
| SERV-04 | `1217234006576155` |
| SERV-05 | `1217234006576158` |
| SERV-06 | `1217234006576161` |
| SERV-07 | `1217234006576164` |
| ADM-01 | `1217108466019461` |
| ADM-02 | `1217108466019464` |
| ADM-03 | `1217108466019472` |
| ADM-04 | `1217108466019470` |
| ADM-05 | `1217234006576166` |
| ADM-06 | `1217234006576169` |
| ADM-07 | `1217234006576172` |
| ADM-08 | `1217234006576175` |
| CAR-01 | `1217234006576179` |
| CAR-02 | `1217234006576182` |
| CAR-03 | `1217234006576185` |
| CON-01 | `1217234006576188` |
| CON-02 | `1217234006576191` |
| CON-03 | `1217234006576194` |
| AUX-01 | `1217234006576198` |
| AUX-02 | `1217234006576200` — **same underlying file as AUX-01** |
| AUX-03 | `1217234006576204` |

Signed download URLs are archived at `scratchpad/asana/manifest.txt`. They carry expiry timestamps and will need refreshing via `get_attachments` when egress is opened.

**Screenshot-interpretation fields are deliberately left empty.** Per the honesty rule, I will not describe an image I could not open — no page/section/Figma-vs-live/viewport/annotation determination has been made for any of the 60.

---

## 7 · TOTALS

| Severity | Count |
|---|---|
| CRITICAL | **11** — HOME-06, 08, 09, 10 · ABOUT-04, 05, 08, 09 · SERV-01, 02, 05 · ADM-04 · AUX-01, 02 *(14 incl. blocked)* |
| MAJOR | **34** |
| MINOR | **8** |
| BLOCKED (client/Figma content) | **3** — AUX-01, AUX-02, HOME-21 |
| **Total QA items** | **59** |

| State | Count |
|---|---|
| OPEN — actionable from text now | **20** |
| NEEDS VISUAL VERIFICATION | **35** |
| Closed by agency, unverified | **4** |
| Blocked on Figma/client | **3** |
| Confirmed against source code | **3** — HOME-11, HOME-12, ADM-04 |
| Duplicates | **0** distinct items (one duplicated *attachment*: AUX-01/AUX-02) |
| Stale / superseded | **0** — every item is the newest word on its subject; only HOME-06 has a follow-up, which *reinforces* rather than supersedes |
| Conflicts | **5** — §5 C1–C5 |

| Page | Items |
|---|---|
| Home | 21 |
| About | 14 |
| Admissions (`/amenities`) | 8 |
| Services | 7 |
| Careers | 3 |
| Contact | 3 |
| Auxiliary (Privacy / Terms / 404) | 3 |

---

## 8 · RE-READ 2026-08-06 (post font delivery) — NO NEW ASANA ITEMS

The agency reported an updated backlog. **The board is unchanged from the collection recorded above.**

| Check | Earlier collection | Re-read | |
|---|---|---|---|
| Subtask counts | 21 / 14 / 7 / 8 / 3 / 3 / 3 = **59** | 21 / 14 / 7 / 8 / 3 / 3 / 3 = **59** | identical |
| Home parent `modified_at` | `2026-08-06T07:53:56.742Z` | same | identical |
| About / Services / Admissions | `08:08:54.876` / `08:23:18.747` / `09:00:51.466` | same | identical |
| Careers / Contact / Auxiliary | `09:24:05.162` / `09:34:43.923` / `09:37:16.006` | same | identical |
| Home subtask GID list | 21 GIDs | same 21 GIDs, same order | identical |
| Project `modified_at` | `2026-08-05T07:20:49.287Z` | same | identical |

The newest modification anywhere on the board is **09:37:34 UTC**, which predates the original collection run. **The agency's update is the material already captured in §2** — including the form-state item.

### 8.1 · The form-state designs are HOME-21, and they are blocked

The only form-state reference in the entire project is **HOME-21** (`1217234006576129`): *"In the UI KIT section they added [states] for when messages are sent — take the one marked 1."* It points at a **Figma UI KIT frame**, with screenshot `1217234006576131`.

Both are unreachable — Figma by seat quota, the screenshot by the `403 CONNECT` egress denial on `asanausercontent.com`. **The eight requested states (default, focus, filled, error, disabled, loading, success, hover) cannot be documented as designed.** The current implementation is documented instead, state by state, in `TYPOGRAPHY_AND_FORM_STATES.md` §4.2, as the baseline the designs will be diffed against.

### 8.2 · One item can now be closed — HOME-14 is ALREADY FIXED

HOME-14 asks for the copy *"Contact **out** team / to learn more about / our services"*. `home/Contact.tsx` already renders, verbatim:

```
Contact our team
to learn more about
our services
```

The copy matches on all three lines, with "our" already correct in place of the ticket's "out" typo. **Reclassified OPEN → ALREADY FIXED**, pending screenshot confirmation that the ticket refers to this section and not another. Conflict **C3** is resolved by the existing implementation and needs no override after all.

### 8.3 · Four Asana items now have a named root cause — see `TYPOGRAPHY_AND_FORM_STATES.md` §3

**HOME-05, HOME-18, ABOUT-10 and SERV-01** all report headings at the wrong weight. They are one defect, not four:

> Playfair Display is loaded as `wght@400` **only**, so every heavier heading is a browser-synthesised fake bold — *and* all four heading utilities hard-code `font-weight: 400`, so no heading can render heavier even once the files are present.

These four items merge into shared issue **SH-6**, whose fix is now precisely specified rather than exploratory. **SERV-05 and ABOUT-12** ("sizes differ", "description font wrong") remain separate — they are size complaints, not weight, and still need the screenshots.

### 8.4 · New shared issue — SH-12 · self-host the official fonts

| | |
|---|---|
| Trigger | Agency delivered the official Playfair Display and Satoshi sources, 2026-08-06 |
| Sources | preserved at `design-sources/fonts/` — 26 files, 3.2 MB, all 22 binaries validated |
| Absorbs | HOME-05, HOME-18, ABOUT-10, SERV-01 (via SH-6) |
| Affected routes | **all 9** |
| Blocked on | **T3** — Poppins has no official source; **D1** — Satoshi ships no licence file |

Two questions must be answered by the agency before this can be built, and both are recorded in `TYPOGRAPHY_AND_FORM_STATES.md`:
1. **Poppins** drives `text-label` and is fetched from Google Fonts, but is not in the official delivery. Keep it, or re-map labels to Satoshi?
2. **Satoshi's licence file is absent** from the zip. Self-hosted webfont use must be confirmed as permitted before deployment. Playfair's OFL is included and unambiguous.

### 8.5 · Totals after this re-read

| | Before | After |
|---|---|---|
| QA items | 59 | **59** — no change |
| Already fixed | 0 | **1** (HOME-14) |
| Open | 20 | **19** |
| Shared issues | 11 | **12** (SH-12 added) |
| Conflicts | 5 | **4** — C3 resolved by existing code |
| Items with a named root cause | 3 | **7** (+HOME-05, 18, ABOUT-10, SERV-01) |

---

## 10 · RE-READ UNDER THE AGENCY'S PROTOCOL · 2026-08-06

The agency specified the reading order: open each page task in QA → open every subtask → treat each subtask as an individual correction → read its description, comments and attachments → record genuine ambiguities as exact questions here, without posting them to Asana.

**Protocol applied. Result: the board is unchanged for a third consecutive read.**

| Page task | Subtasks | All opened individually | Descriptions | Comments | Attachments |
|---|---|---|---|---|---|
| Home `1217105105055942` | 21 | ✅ | 21/21 | 1 found (HOME-06) | 22 enumerated, **0 readable** |
| About `1217105105055944` | 14 | ✅ | 14/14 | none | 16 enumerated, **0 readable** |
| Services `1217105105055946` | 7 | ✅ | 7/7 | none | 7 enumerated, **0 readable** |
| Admissions `1217105105055948` | 8 | ✅ | 8/8 | none | 8 enumerated, **0 readable** |
| Careers `1217105105055950` | 3 | ✅ | 3/3 | none | 3 enumerated, **0 readable** |
| Contact us `1217105105133465` | 3 | ✅ | 3/3 | none | 3 enumerated, **0 readable** |
| Auxilliary `1217105105133467` | 3 | ✅ | 3/3 | none | 3 enumerated, **0 readable** |
| **Total** | **59** | **59/59** | **59/59** | **1** | **60 / 0** |

Every parent `modified_at` is byte-identical to the two previous reads; `num_subtasks` unchanged on all seven. Contact and newsletter subtasks were re-opened individually in case the new form-state material had been attached there — `CON-03` still `09:34:24.259Z`, `HOME-13` still `2026-08-03T12:28:50.308Z`, `HOME-21` still `07:54:09.684Z`. **No new subtask, no new comment, no new attachment anywhere.**

**Figma re-tested, still blocked.** `whoami` confirms the account holds a **View** seat on the "Project" plan (it also holds a Full seat on an unrelated "Geek Brains" plan, which does not grant access to this file). A live `get_metadata` call on `Tm96OSYcEv6kdVzIqHYKeP` returned, verbatim:

> *"You've reached the Figma MCP tool call limit for your View seat on the Professional plan. Upgrade your seat or plan for more tool calls."*

Nothing complete was marked, nothing was moved, nothing was posted.

### 10.1 · AMBIGUITY REGISTER — exact questions, held for the agency

Recorded here, **not posted to Asana**, per instruction. Each is a question whose answer changes what gets built; none can be resolved from the text alone. Ordered by how much work they gate.

| # | Item | The exact question |
|---|---|---|
| **Q1** | ADM-04 | The nav reads "Admissions" and routes to `/amenities`, which the code marks as deliberate per the design — but this board also calls the `/amenities` QA card "Admissions". Which is correct: **(a)** rename the route to `/admissions`, **(b)** relabel the nav to "Amenities", **(c)** retitle the page content to "Admissions" and keep the route, or **(d)** build a separate Admissions page? There is no `/admissions` route today. |
| **Q2** | HOME-09 | The ticket says *"where images are missing you can put placeholders for now."* The standing client rule is *"never use placeholder images."* The site currently renders zero placeholders. **Confirm: leave the sections as they are and supply the real images, or authorise placeholders?** |
| **Q3** | T3 (typography) | `text-label` is driven by **Poppins**, fetched from Google Fonts, but the official font delivery contains only Playfair Display and Satoshi. **Is Poppins intended — in which case please supply the source — or should labels be re-mapped to Satoshi?** |
| **Q4** | D1 (typography) | The Satoshi zip contains ten `.otf` files and no licence. **Please confirm the Satoshi licence permits self-hosted webfont use**, and supply the licence file. Playfair's OFL 1.1 is included and unambiguous. |
| **Q5** | HOME-05 / HOME-18 / ABOUT-10 / SERV-01 | All four report headings at the wrong weight, but none names a target. **Which Playfair weight should each heading level use — h1, h2, h3, h4?** The delivered family supports 400/500/600/700/800/900. |
| **Q6** | HOME-02 | *"Spacing differs a lot from Figma"* — **which section, and which spacing** (section padding, gap between cards, or gap between text blocks)? |
| **Q7** | HOME-04 | *"Reduce the end of the border here."* — **which element, and to what value?** "End of the border" does not map to a known property. |
| **Q8** | HOME-15 | *"Add a View More here."* — **which section**, and does it paginate, expand in place, or link to another page? |
| **Q9** | HOME-19 | *"All good except the card position — centre it on screen."* — **which card**, on which section? |
| **Q10** | ABOUT-07 | *"Change this block and put what's in Figma."* — **which block**, and which Figma frame replaces it? |
| **Q11** | ABOUT-13 | *"These segments shouldn't have cards."* — **which segments**, and what replaces the cards? |
| **Q12** | ABOUT-14 | *"The sizes look swapped here."* — **which two elements** have exchanged sizes? |
| **Q13** | ADM-05 | *"Wrong colour."* — **which element, and which target colour?** Neither is named. |
| **Q14** | ADM-06 | *"Кнопку надо не лево"* is grammatically ambiguous in the original. **Should the button move to the left, or away from the left?** |
| **Q15** | ADM-03 | *"It should have been 1 and 3."* — **1 and 3 of what** — gallery slots, image order, or column count? The caption copy ("Serene / Courtyard Retreat") is clear; the ordering is not. |
| **Q16** | CAR-02 | *"The structure doesn't match."* — **which section of `/careers`**, and in what respect? |
| **Q17** | CAR-03 | *"Remove the button here — on mobile too."* — **which button?** The action is unambiguous, the target is not. |
| **Q18** | SERV-04 | *"Why does this block differ from the others?"* — **which block**, and which "others" is it meant to match? |
| **Q19** | SERV-06 | *"They should be on the right."* — **which elements?** |
| **Q20** | AUX-03 | *"The 404 doesn't look like Figma — add the missing elements."* — **which elements are missing?** |
| **Q21** | HOME-14 | The copy requested is already live verbatim (§8.2). **Does this ticket refer to the Home contact section, or to a different section showing the same copy?** |
| **Q22** | FORM-S0…S2 | See §11 — the entire visual specification of the four form states. |

**Q6–Q20 would all be answered by the screenshots.** They are not really fifteen questions; they are one blocked resource. Only **Q1–Q5, Q21 and Q22** need a human decision even with the images in hand.

---

## 11 · CONTACT-FORM STATES FROM THE FIGMA UI KIT — requirements register

The agency has added official contact-form states to the Figma UI KIT and asked for them to be recorded precisely.

### 11.1 · What is now known — from the agency's written brief

This is new information and it **decodes a previously ambiguous ticket.** Asana **HOME-21** reads *"In the UI KIT section they added [states] for when messages are sent — take the one marked 1."* Until now "the one marked 1" was unidentified. It is now resolved:

| ID | State | Trigger — stated by the agency |
|---|---|---|
| **FORM-S0** | Default form | initial render |
| **FORM-SF** | Focus / filled | *"if shown"* — the agency is not certain this state exists in the kit |
| **FORM-S1** | **Successful submission** | *"Use State 1 only after the form has been submitted successfully"* |
| **FORM-S2** | **Failed submission / message not sent** | *"Use State 2 when submission fails"* |

Both **desktop and mobile** versions exist and must both be documented.

**FORM-S2 is entirely new.** No Asana ticket mentions a failure state — the board only ever referred to messages being sent. This requirement exists solely in the agency's brief, so it is registered here rather than against an Asana ID.

### 11.2 · What cannot be recorded — the visual specification

The agency asked for eleven attributes per state. **None can be filled in.** The UI KIT is a Figma frame, and both routes to it are closed:

| Route | Status |
|---|---|
| Figma MCP | **View seat, monthly call limit reached.** Re-tested 2026-08-06; error quoted verbatim in §10 |
| Asana screenshot `1217234006576131` | **`403 CONNECT` on `asanausercontent.com`** — session egress policy |

The specification matrix below is therefore a **template with every visual cell unfilled**. Writing plausible values into it would be fabrication, and would be indistinguishable from real measurements once committed.

| Attribute | FORM-S0 default | FORM-SF focus/filled | FORM-S1 success | FORM-S2 failure |
|---|---|---|---|---|
| Heading copy | ⛔ | ⛔ | ⛔ | ⛔ |
| Body copy | ⛔ | ⛔ | ⛔ | ⛔ |
| Button copy | ⛔ | ⛔ | ⛔ | ⛔ |
| Dimensions (desktop) | ⛔ | ⛔ | ⛔ | ⛔ |
| Dimensions (mobile) | ⛔ | ⛔ | ⛔ | ⛔ |
| Spacing | ⛔ | ⛔ | ⛔ | ⛔ |
| Typography | ⛔ | ⛔ | ⛔ | ⛔ |
| Colours | ⛔ | ⛔ | ⛔ | ⛔ |
| Card background | ⛔ | ⛔ | ⛔ | ⛔ |
| Transition from the form | ⛔ | ⛔ | ⛔ | ⛔ |
| Retry / reset behaviour | ⛔ | ⛔ | ⛔ | ⛔ |
| Responsive differences | ⛔ | ⛔ | ⛔ | ⛔ |

⛔ = requires the UI KIT frame. **Either unblock fills the whole matrix.**

### 11.3 · Exact questions for the agency — Q22 expanded

Only needed if the UI KIT itself does not answer them:

1. Does **FORM-SF** exist in the kit as a distinct state, or is focus/filled only implied? The brief says *"if shown"*.
2. On **FORM-S1**, does the card **replace** the form entirely, or does a confirmation panel appear above or below a still-present form?
3. Is there a way back from **FORM-S1** — a "Send another message" affordance — or is the success state terminal until reload?
4. On **FORM-S2**, are the user's entered values **preserved** so they can retry, or is the form cleared?
5. Does **FORM-S2** distinguish *network/server failure* from *validation failure*? The current build treats only validation, and does so via a toast.
6. Is there a **loading / submitting** state between the form and S1/S2? None is listed among the four, but every real submission has one.
7. Do S1 and S2 keep the card at the **same height** as the form, or does the section reflow? This determines whether the surrounding layout shifts — and the Home contact section carries a `min-h-[780px]` reference value at 1440.

### 11.4 · Engineering requirements that hold regardless of the visuals

Derived from the **stated behaviour**, not from the unseen design — recorded so this work is not re-derived later. Clearly separated from §11.2, which is blocked.

- **Submission must become asynchronous.** `onSubmit` in `home/Contact.tsx` is fully synchronous today; there is no way to reach a failure state without a real request.
- **A pending state is required** between submit and S1/S2, with a **double-submit guard** — the current button can be pressed repeatedly.
- **Failure must be recoverable.** S2 implies a retry path; entered values should survive unless the design says otherwise (Q4 above).
- **Validation errors need an inline surface.** Today only `parsed.error.issues[0]` is shown, as a transient toast — five invalid fields report one. Independent of S1/S2, and needed before either is meaningful.
- **State changes must be announced.** S1 and S2 change content without navigation, so they need an ARIA live region and focus moved to the new heading.
- **The transition must honour `prefers-reduced-motion`**, which the project already enforces globally.
- **The 1440 reference value must survive.** The Home contact section is signed off at `min-h-[780px]`. If S1/S2 are shorter or taller than the form, the section must not jump — this is a regression check, not a nice-to-have.
- **Three routes are affected**, not one: the form component renders on `/`, `/careers` and `/contact`. One implementation, three verifications.
- **The checkbox is on the regression watch** — `!rounded-[4px]` square. CON-03 authorises a colour change only.

---

## 12 · SCREENSHOT ARCHIVE MAPPED · 2026-08-06

The agency supplied `Скрины Asana.rar` — 55 PNGs in 7 page folders plus `README.txt`. **This unblocks the 35 items previously marked NEEDS VISUAL VERIFICATION.** Archive preserved at `design-sources/asana-qa-screenshots/`.

### 12.1 · Mapping rule applied

Per the README: folder = page, numeric filename prefix = subtask position, `(1)` suffix = additional image for the same subtask, `ChromeSafari`/`SafariChrome` = desktop, `mobile` = mobile. Mapped by **folder + numeric prefix + existing subtask order/GID**, never by visual similarity.

| Metric | Count |
|---|---|
| Files in archive | **55** + README |
| Distinct images opened | **54** |
| Byte-identical duplicate confirmed by md5, not re-opened | **1** (`Auxilliary pages/2` = `Auxilliary pages/1`) |
| Additional upscaled crops derived (UI KIT) | 6 |
| Files mapped to a subtask GID | **55 / 55** |
| Subtasks now carrying a screenshot | **55 of 59** |

### 12.2 · Coverage — and the pattern in what is missing

| Page | Subtasks | Files | Numbers present | Missing |
|---|---|---|---|---|
| Home | 21 | 17 | 2–9, 13–21 | **1, 10, 11, 12** |
| About | 14 | 16 | 1–14 (3 and 4 have two each) | none |
| Services | 7 | 5 | 3–7 | **1, 2** |
| Admissions | 8 | 8 | 1–8 | none |
| Careers | 3 | 3 | 1–3 | none |
| Contact us | 3 | 3 | 1–3 | none |
| Auxilliary | 3 | 3 | 1–3 | none |

**HOME-11 and HOME-12 are not gaps** — neither has an attachment in Asana either (both are text-only tickets). Verified against the attachment register in §6.

**The four genuinely absent screenshots — HOME-01, HOME-10, SERV-01, SERV-02 — are exactly the four subtasks marked `completed` in Asana.** That is not a coincidence: the agency's export appears to exclude closed items. Combined with §5-C4 (three of those four were *edited after closure*), these four remain **unverifiable** and must not be treated as fixed.

A fifth attachment is also absent: **HOME-06's comment image** (`1217213785962831`, the 2026-08-06 *"these animations aren't here"* follow-up). Asana holds 2 attachments for HOME-06; the archive supplies 1. 55 archive files + 5 absent = 60, reconciling exactly with the Asana attachment count.

### 12.3 · Ambiguities found in the archive — recorded, not guessed

| # | Issue |
|---|---|
| **A1** | `Auxilliary pages/1 Privacy and Policy.png` and `2 Term and Appliance.png` are **byte-identical** (md5 `fc12ea16…`), and the image shows the **Terms of Use** page (sections *Acceptance of Terms*, *Use of the Site*, *Contact*) — not Privacy Policy. This independently confirms the Asana-side finding that both subtasks point at one asset. **No Privacy Policy screenshot exists.** |
| **A2** | `Services/6 mobile` — the ticket says elements should be *"справа"* (on the right); the annotation arrow appears to point **left**, and the parallel Home ticket (HOME-20) explicitly asks for **left**. Unresolved. |
| **A3** | `About/13 mobile` — *"these segments shouldn't have cards"*, but the red arrow points at the dark **icon badge**, not the card container. Two readings. |
| **A4** | `Admissions/2` — *"the card that should come next appeared in the middle"*; three cards are visible with the middle one struck through. The target arrangement is not derivable without the Figma carousel frame. |
| **A5** | `Home/3` — a red **X sits over the AMARA reception signage inside the photo**. The instruction asks for this photo *on* the hero, so the X's meaning is unclear (a photo's contents cannot be edited). |
| **A6** | `Careers/2` — **no annotation at all** and no Figma reference. *"The structure doesn't match"* cannot be resolved. **Q16 stands.** |

### 12.4 · Questions the archive ANSWERED

Seven of the twenty-two open questions are now closed by direct visual evidence.

| Was | Now resolved |
|---|---|
| **Q13** ADM-05 *"wrong colour"* — element and target both unnamed | **The `Cta` panel background.** Live renders dark navy `--primary` #2C2E45; the Figma CTA frames (`About/5`, `About/7`) show a **lighter slate blue-grey ≈ #56677F**. Affects About, Services, Amenities |
| **Q15** ADM-03 *"should have been 1 and 3"* | **The gallery side-image counters.** They currently read **05** (left) and **02** (right); with the centre at 02 the neighbours must read **01 and 03**. Side images also need a caption beneath, as the centre has |
| **Q17** CAR-03 *"remove the button"* | **"View Full Team"** at the foot of `CareersTeam` — desktop and mobile |
| **Q20** AUX-03 *"add the missing elements"* | Full 404 target captured from two Figma frames — see §12.5 |
| **Q14** ADM-06 (grammatically ambiguous) | Resolved by cross-page pattern: `Admissions/6`, `Services/5` and `About/9` **all** show a full-width mobile CTA the agency wants changed. Target = **auto-width, left-aligned** |
| **Q8** HOME-15 *"add a View More"* | **The Gallery button** — relabel **"View Amenities" → "View More"** |
| **Q9** HOME-19 *"centre the card"* | **The testimonial card on mobile**, currently flush-left with the next card peeking |

**Q1 (Admissions vs Amenities) is now sharper but still needs a human decision.** `Admissions/4` shows the URL bar reading `/amenities` underlined *and* the nav item "Admissions" underlined. But `Admissions/1` is a Figma frame **titled "Amenities Page | Desktop" whose own nav bar also reads "Admissions"** — so the design contains the same mismatch it is now reporting as a bug. Four sources, two names: route `/amenities`, nav label "Admissions", Figma frame title "Amenities Page", H1 "Life at Amara Care Center". **The authority rule cannot resolve a contradiction inside the design.**

### 12.5 · VISUAL ACCEPTANCE CRITERIA

Desktop = D, mobile = M. Annotations (red/orange/yellow strokes, X marks, numbers), Figma selection borders, comment avatars, browser chrome, iOS status bars and Lovable badges are **excluded** — none is a website element.

#### Home
| ID | View | Acceptance criterion |
|---|---|---|
| HOME-02 | D | Hero vertical rhythm matches Figma at two marked gaps: **header→H1** and **buttons→hero photo**. |
| HOME-03 | D | Hero photo = the **AMARA reception-desk** shot (M already uses it; D uses a different ceiling/room photo). Heading colour moves off `#0F0F0F` to the **bluish `#2C2E45`**. Figma hero background is a diamond lattice; live is A-chevron tiles. *(A5 open.)* |
| HOME-04 | D | The `--blue-100` hero background band **ends higher** — excess blue currently sits between the photo's bottom and the white section. |
| HOME-05 | D | Intro paragraph and the `what sets us apart` eyebrow render **larger and heavier** (Satoshi; 500 is available). |
| HOME-06 | D | All three WSUA cards default to **photo + white pill label**. On hover the card becomes **blue with a paragraph at top, large A monogram watermark, pill retained**. The middle card must stop rendering the hover state permanently and needs a thematically-matched Figma photo. Cards stay 413×460. |
| HOME-07 | D | Mission reveal follows the **5-frame storyboard**: monogram ring fades up across frames 1–3, then heading + paragraph reveal in 4–5. |
| HOME-08 | D | The services section **pins with the rail *and* the active panel visible** (today only shrunken headings show). Rail entries become **non-interactive** — no click, no scroll-jump. |
| HOME-09 | D | **Every** testimonial card carries a photo (only card 1 does). Carousel **loops infinitely**. Cards 847×440, photo 389×392, arrows 56×32. *Confirms CNT-03: cards 2 and 3 are both "Oliver M."* |
| HOME-13 | D | Newsletter submit produces a **visible response**. The **large faint footer watermark is the wrong mark** (red X) and must be replaced. |
| HOME-14 | D | Heading renders on **exactly three lines** — `Contact our team / to learn more about / our services`. Live wraps to four because `max-w-[380px]` pushes "about" down. **See §12.6 — this reverses an earlier call.** |
| HOME-15 | D | Gallery button reads **"View More"**. |
| HOME-16 | M | The two hero CTAs sit **side by side**, not stacked. |
| HOME-17 | M | The "Where Healing Feels Like Home" badge **overlays inside the hero photo**, not below it. *(Reverses the R2 decision that made the badge absolute only from `lg:` — the fix must avoid overflow.)* |
| HOME-18 | M | Section headings render at the **Figma weight** — blocked by T1/T2 until heavier Playfair is loaded. |
| HOME-19 | M | Active testimonial card is **centred** in the viewport. |
| HOME-20 | M | Gallery eyebrow, heading and paragraph are **left-aligned**, not centred. |
| HOME-21 | D+M | The four form states — **see §12.7**. |

#### About
| ID | View | Acceptance criterion |
|---|---|---|
| ABOUT-01 | D | "Get Started" and "Meet Our Team" gain **hover states**. The **large faint A monogram in the hero centre is a duplicate of the header logo and is removed** (red X). |
| ABOUT-02 | D | Heading + paragraph block **shifts right** per Figma. Both pill icons replaced with the official assets (already in the repo). Pill label weight → **regular**. |
| ABOUT-03 | D | Mission paragraph **alternates between two variants on scroll**: ① *"At Amara Care Center, our mission is to provide compassionate, personalized care in an environment focused on healing and comfort."* ② *"Through attentive support and coordinated rehabilitation services, we are committed to helping residents feel supported, respected, and cared for every step of the way."* Paragraph renders **sans-serif** per Figma — live uses Playfair. Monogram = correct official mark, **visible** (currently near-invisible). |
| ABOUT-04 | D | Values cards **rise and cover the previous** on scroll. **Card 2 "Comfort & Wellbeing" currently has no background at all** and vanishes into the page blue — every card needs a background distinct from the page. Cards 847×440. |
| ABOUT-05 | D | CTA rebuilt to the Figma frame: **left slate panel + right photo, equal height, radius 24**; panel content centred — eyebrow `contact us`, h2 `Plan Your Visit`, body *"Contact our team to learn more about our services or schedule a tour of our community."*, white pill button. CTA image 630×660. **Ship "Schedule a Tour" — the Figma shows the "Shedule" typo (§0.0 override holds).** |
| ABOUT-06 | D | **Increase the gap** between the testimonials heading and the card track. |
| ABOUT-07 | D | **DUPLICATE of ABOUT-05** — same Figma CTA frame. Merge; do not implement twice. |
| ABOUT-08 | D | Values card internals: **icon top-left, heading + paragraph anchored lower-left, photo flush right**. Live floats the icon with dead space beneath the text and insets the photo. |
| ABOUT-09 | M | Hero **taller**; "Meet Our Team" becomes **auto-width, left-aligned to the heading** (currently full-width); heading placement per Figma. |
| ABOUT-10 | M | Intro block family/weight/size per Figma. **Also: the pill overflows past the photo's bottom edge.** |
| ABOUT-11 | M | **Both pill icon slots render empty** — the official icons must actually load. |
| ABOUT-12 | M | Mission paragraph → **sans-serif, reduced size** (live renders oversized Playfair). Smooth the transition. |
| ABOUT-13 | M | Values segments drop the card treatment. *(A3 — "cards" vs the icon badge is ambiguous.)* |
| ABOUT-14 | M | CTA panel/photo proportions per Figma — the dark panel carries **dead space below the button**. **Same defect as ADM-08 → one fix in `Cta`.** |

#### Services
| ID | View | Acceptance criterion |
|---|---|---|
| SERV-03 | D+M | CareApproach: monogram, "24/7" heading, supporting line and the Comfort/Care/Compassion lockup **repositioned per Figma**. **The 24/7 supporting text is currently clipped at the card's right edge.** Row 460 / 306·621·313 preserved. |
| SERV-04 | D | The **Indian Program** card uses chips while the other three use **bulleted lists** — make it consistent. *(Answers Q18.)* |
| SERV-05 | M | Add **top spacing between header and H1** (currently zero); **reduce H1** so it stops running to four lines; CTA **auto-width, left-aligned**; **"Scroll to Explore" repositioned**. |
| SERV-06 | M | Services-overview eyebrow/h2/paragraph re-aligned. *(A2 — ticket says right, arrow reads left.)* |
| SERV-07 | M | "Plan Your Visit" moves to the **end of the section**; the **"Therapy" chip is removed** — not present in the design. |

#### Admissions (`/amenities`)
| ID | View | Acceptance criterion |
|---|---|---|
| ADM-01 | D | Hero left column **vertically centred**; "Scroll to Explore" bottom-left; photo 660×600 right. |
| ADM-02 | D | Carousel arrangement corrected. *(A4 — target not derivable.)* Third card currently clips mid-word. |
| ADM-03 | D | Gallery side counters read **01 and 03** around the centre 02 (today: 05 and 02); **side images gain captions**. Centre 512×710, sides 255×406 at `top-204`. |
| ADM-04 | — | Route/label mismatch — **blocked on Q1**. |
| ADM-05 | D | `Cta` panel background → the **lighter slate blue-grey** of the Figma frames, not `--primary`. Applies to About, Services, Amenities. |
| ADM-06 | M | "Explore Amara Amenities" → **auto-width, left-aligned**; "Scroll to Explore" moves **down** to the hero foot. |
| ADM-07 | M | Carousel card places the **photo above** the text content. |
| ADM-08 | M | Same as ABOUT-14 — shared `Cta` fix. |

#### Careers / Contact / Auxiliary
| ID | View | Acceptance criterion |
|---|---|---|
| CAR-01 | D | **Lighten the hero scrim** — the photo goes nearly black at the bottom. Text contrast must hold. Hero 900. |
| CAR-02 | D | *(A6 — no annotation, no reference. **Q16 stands.**)* |
| CAR-03 | D+M | **Remove the "View Full Team" button.** Monograms 68×68. |
| CON-01 | D | Hero left column **vertically centred** — it is top-anchored and the heading collides with the header row. Column 413, photo 630×720. |
| CON-02 | D | Replace the icon inside the **"Supported Transition"** pill on the admissions photo. |
| CON-03 | D | Insurance checkmarks → **white filled circle with a slate-blue tick** per Figma; panel is a **medium slate blue**, photo 500×410, two-column list, "Verify Your Coverage" top-right. *MA carriers appear in the design — CNT-02 remains "matches design".* |
| AUX-01/02 | D | **Still blocked.** The screenshot shows the live placeholder (*"Content coming soon — full text will be provided by Amara Care Center"*), **not the Figma copy.** Confirms single centred column, no ToC. |
| AUX-03 | D+M | 404 rebuilt to the two Figma frames: **full-bleed slate blue-grey background**; header with light logo, nav and **white "Get Started" pill**; large white Playfair **"404"**; "Page was not found"; body *"The page you're looking for couldn't be found. / Let's get you back on track."*; **white "Back to Home Page" pill**; **large faint A monogram watermarks bleeding off the left and right edges** (mobile: one bottom-centre). |

### 12.6 · CORRECTION — HOME-14 is not "already fixed"

In §8.2 I reclassified HOME-14 **OPEN → ALREADY FIXED** because the copy in `home/Contact.tsx` matches the ticket verbatim. **The screenshots show that was wrong.**

The words are correct. The **line breaks** are not. The Figma left column (`Home/21`, upscaled) renders exactly three lines; the live site (`Home/14`) renders four, because `max-w-[380px]` on the `h2` is too narrow for *"to learn more about"* at 44px Playfair, so "about" drops to its own line — the `<br>` tags are present but a second, unwanted wrap occurs after them.

**HOME-14 → OPEN.** Fix: widen the heading's max-width so the second line holds. Conflict **C3** was correctly retired — the copy needed no typo override — but the ticket itself is live.

### 12.7 · FORM STATES — the UI KIT, now read

`Home/21 Mobile.png` **is the UI KIT frame**. It was previously unreadable; the archive supplies it. At 342×610 native, six regions were cropped and upscaled 8× to read the content. **The red "1" and "2" digits obscure part of each card**, so some body copy remains partially illegible — marked ⚠ below.

**Layout.** Desktop shows two full-width frames (State 1 above, State 2 below), each with the standard two-column contact section: left = eyebrow, 3-line heading, address and phone; right = the state card. Mobile shows three frames side by side: default form, State 1, State 2.

| Attribute | FORM-S0 default | FORM-SF focus | FORM-S1 success | FORM-S2 failure |
|---|---|---|---|---|
| Heading | "Plan Your Visit" (serif) | — | **"Thank you!"** (serif, dark) | **"Message not sent."** (serif, dark) |
| Body | — | — | 2 lines, small, grey ⚠ *"…sent successfully… back to you shortly"* | 2 lines, small, grey ⚠ |
| Icon | none | — | **envelope/mail outline**, rounded-square, centred above the heading | not visible behind the "2" ⚠ |
| Button copy | "Submit" | — | **"Got it"** | **"Try again"** |
| Button width | full-width (M) | — | **full-width on M**, auto-width centred on D | **full-width on M**, auto-width centred on D |
| Card background | light grey (≈ `--surface-muted` #F4F4F6), rounded ≈24 | same | **same card, same tone** | **same card, same tone** |
| Content alignment | left | — | **centred** | **centred** |
| Field treatment | borderless, card-toned | **white fill + dark navy rounded border** | — | — |
| Transition | — | — | card **replaces the form in place** (heading/address column unchanged) | same |
| Retry | — | — | "Got it" | **"Try again"** |

**FORM-SF is confirmed to exist** — the agency's *"if shown"* is resolved. In the mobile default frame the **Name\*** field renders with a distinctly darker border and lighter fill than the other three, which are borderless. Today the live build gives *every* field a white fill and only adds a border on focus.

**Two further mismatches visible in the same frame:**
- **Contact icons are rounded squares in the design**; live uses `rounded-full` circles (`bg-blue-200`).
- **The address and phone sit low in the left column**, roughly aligned with the card's lower area; live places them directly beneath the heading via `mt-10 md:mt-14`.

**Still unanswered** (the digits obscure the text, and no loading frame exists in the kit): exact body copy for both states; whether S2 preserves the user's input; whether S2 distinguishes network from validation failure; and whether a loading state exists between submit and S1/S2. These carry forward as **Q22-a…d**.

---

## 9 · PAGE INDEX

| Page | Items |
|---|---|
| About | 14 |
| Admissions (`/amenities`) | 8 |
| Services | 7 |
| Careers | 3 |
| Contact | 3 |
| Auxiliary (Privacy / Terms / 404) | 3 |
