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
