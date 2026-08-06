# ASANA STATUS SYNC REPORT

| | |
|---|---|
| Run | 2026-08-06, 12:20–12:26 UTC |
| Scope | Asana project **Amara** `1217105105055924`, workspace `1210357482925157` — **and no other project** |
| Mode | Verification and status sync only. **No code changed, no Lovable message sent, no Lovable credits spent** |
| Actor | `oybekovj97@gmail.com` · `1216258602373851` |
| Evidence base | current source (read via Lovable `read_file`, free), the mapped screenshot archive, `ASANA_QA_LEDGER.md` §12, `TYPOGRAPHY_AND_FORM_STATES.md` |

---

## 1 · HEADLINE

**59 QA subtasks re-inspected. Zero marked complete.**

That is the accurate result, not a shortfall. Every Lovable wave to date (1–14 and R1–R7) either predates the Asana QA board or addressed a different problem class — Waves 1–14 were asset integration, R1–R7 were responsive geometry. **Not one of the 59 QA items has been implemented**, and each conclusion below is backed by a specific line of current source or a mapped screenshot, never by a prior "PASS".

Two items are genuinely half-done and are recorded as such. Four were reopened. Twelve questions were posted.

---

## 2 · MUTATIONS PERFORMED

### 2.1 · Reopened — 4 subtasks (status E)

All four were `completed: true`. All four share the same two disqualifiers: **their screenshot is absent from the archive**, and **the task was edited after it was closed**. The four absent screenshots are *exactly* the four closed subtasks, so the agency's export appears to exclude closed items.

| GID | Task | Page | Was | Now | Comment GID |
|---|---|---|---|---|---|
| `1217105105133471` | 1 Safari/Chrom | Home | complete | **incomplete** | `1217246106377602` |
| `1217108466019428` | 10 safari/chrome | Home | complete | **incomplete** | `1217234107583248` |
| `1217108466019451` | 1 Safari/Chrome | Services | complete | **incomplete** | `1217231593330481` |
| `1217108466019455` | 2 safari/Chrome | Services | complete | **incomplete** | `1217234107740723` |

Each comment states plainly that this is a **verification gap, not a judgement that the work is wrong**, and names exactly what would let us close it again (the missing screenshot, or a one-line confirmation). Confidence: **high** — the disqualifiers are factual, not interpretive.

### 2.2 · Partially complete — 2 subtasks (status C, left incomplete)

| GID | Task | Verified done | Still open | Comment GID |
|---|---|---|---|---|
| `1217108466019431` | About 1 | **Button hover effects.** `ui/button.tsx` — `dark`/`light` variants carry `hover-lift`, hover background shift, hover shadow, active state; reduced-motion honoured globally | **Duplicate logo.** `about/AboutHero.tsx` still renders `glyph-ring.png` centred at `opacity-[0.10]`, `h-[100px] md:h-[160px]` — the mark circled in the screenshot | `1217239076043987` |
| `1217108466019447` | About 5 | **CTA structure.** `sections/Cta.tsx` now matches the Figma frame — two columns, slate panel with pattern watermark, centred eyebrow/h2/body/white pill, photo right, radius 24, 630×660 at 1440 | **Panel colour.** Uses `bg-primary` #2C2E45; Figma shows ≈ #56677F. Same defect as Admissions 5 | `1217239076201709` |

### 2.3 · Clarification questions — 12 posted (status D)

One question per subtask, each in the subtask it belongs to, each naming the conflicting sources and offering concrete options.

| # | GID | Subtask | The decision requested |
|---|---|---|---|
| 1 | `1217108466019468` | ADM-04 | Admissions vs Amenities IA — 4 options. The Figma frame is titled *"Amenities Page"* but its own nav says *"Admissions"*, so the design contains the mismatch it reports |
| 2 | `1217108466019425` | HOME-09 | Placeholder instruction vs the standing no-placeholder rule — supply 2 testimonial photos, or authorise placeholders. Also flags the duplicated "Oliver M." attribution |
| 3 | `1217213785962849` | HOME-18 | **The Playfair weight table** — which weight for h1/h2/h3/h4. Names the root cause (wght@400 only + hard-coded `font-weight: 400`) |
| 4 | `1217234006576135` | ABOUT-10 | Poppins has no official source; Satoshi ships no licence file |
| 5 | `1217234006576129` | HOME-21 | Form states — exact S1/S2 body copy (hidden under the annotation digits), input preservation on retry, network-vs-validation failure, loading state |
| 6 | `1217234006576180` | CAR-02 | The one screenshot with **no annotation at all** — 4 options for "structure doesn't match" |
| 7 | `1217234006576159` | SERV-06 | Ticket says *"справа"* (right), arrow points **left**, and the Home equivalent asks for left |
| 8 | `1217234006576196` | AUX-01 | Both legal subtasks carry one byte-identical image, it shows **Terms** not Privacy, and it shows our placeholder rather than the Figma copy |
| 9 | `1217108334767499` | HOME-03 | The red X over the reception signage **inside** the photo — 3 options; plus the lattice-vs-chevron hero background |
| 10 | `1217234006576144` | ABOUT-13 | *"no cards"* vs the arrow pointing at the icon badge — 3 options; cross-referenced to About 4 for consistency |
| 11 | `1217108466019476` | HOME-13 | Which footer mark is correct — we already ship `footer-logo-official.png` — 3 options. Newsletter half confirmed and queued |
| 12 | `1217108466019462` | ADM-02 | Carousel target arrangement — 4 options |

### 2.4 · Status comment — 1

`1217231594950310` on **DEV → Home** (`1217105105055928`): why no DEV page can be signed off, naming the five shared blockers.

### 2.5 · Not done

No task deleted, renamed, reassigned, re-dated, moved between sections, or had its description or attachments altered. No duplicate task created. No project structure change. **No other Asana project touched.**

---

## 3 · WHY NOTHING WAS MARKED COMPLETE

Verified directly in current source — each of these is the defect the ticket describes, still present:

| Ticket | Source evidence |
|---|---|
| HOME-11 header scroll | `Header.tsx` is `absolute inset-x-0 top-6`. **No scroll listener of any kind.** New work |
| HOME-12 FAQ open | `sections/Faq.tsx` → `useState<number \| null>(1)` — item 2 opens on mount |
| HOME-13 newsletter | `Footer.tsx` → `handleSubmit` calls `preventDefault()` and **nothing else** |
| HOME-14 heading lines | `home/Contact.tsx` → `max-w-[380px]` still forces a 4th line |
| HOME-15 button label | `home/Gallery.tsx` → still `View Amenities` |
| HOME-20 mobile align | `home/Gallery.tsx` → `items-center text-center` at every width |
| ADM-04 nav/route | `Header.tsx` → `{ label: "Admissions", to: "/amenities" }` |
| ADM-05 CTA colour | `sections/Cta.tsx` → `bg-primary` |
| ABOUT-14 / ADM-08 | `sections/Cta.tsx` → panel `min-h-[440px]`, photo `h-[320px]` on mobile — panel taller, dead space below the button |
| ABOUT-01 glyph | `about/AboutHero.tsx` → `glyph-ring.png` still rendered |
| ABOUT-09 mobile CTA | `about/AboutHero.tsx` → `w-full sm:w-auto` — full width on mobile |
| CAR-03 button | `careers/CareersTeam.tsx` → `View full Team` still present |

The remaining items are visual corrections in components that no wave has touched since the QA was raised.

---

## 4 · DEV PAGES — all 7 remain incomplete

Under the shared-component rule, a page is complete only when its own QA items **and** every shared item affecting it are verified.

| DEV task | GID | Blocking |
|---|---|---|
| Home | `1217105105055928` | 21 QA items open · all 5 shared blockers |
| About | `1217105105055930` | 14 open (2 partial) · Header, Footer, typography, CTA |
| Services | `1217105105055932` | 7 open (2 reopened) · Header, Footer, FAQ, typography, CTA |
| Admissions | `1217105105055934` | 8 open · **plus the unresolved IA decision (Q1)** — this page's identity is undecided |
| Careers | `1217105105055936` | 3 open · Header, Footer, FAQ, typography |
| Contact us | `1217105105133465` | 3 open · Header, Footer, typography, form states |
| Auxilliary pages | `1217105105133467` | 3 open · **legal copy hard-blocked**; 404 rebuild pending |

### Shared blockers, by reach

| Blocker | Routes | Gates |
|---|---|---|
| **Typography** — Playfair at `wght@400` only + hard-coded `font-weight: 400` | **9** | HOME-05, HOME-18, ABOUT-10, ABOUT-12, SERV-01, SERV-05 |
| **Header** — no scroll behaviour; nav/route mismatch | **9** | HOME-11, ADM-04 |
| **Footer** — dead newsletter submit; queried watermark | **9** | HOME-13 |
| **CTA** — wrong panel colour; mobile proportions | **3** | ABOUT-05, ABOUT-07, ABOUT-14, ADM-05, ADM-08 |
| **FAQ** — item open on mount | **3** | HOME-12 |
| **Contact form** — no async, no pending, no inline errors, no S1/S2 | **3** | HOME-21, CON-03 |
| **Lovable credits at zero** | **all** | every implementation item |

---

## 5 · TOTALS

| | |
|---|---|
| QA subtasks inspected | **59 / 59** |
| Marked complete | **0** |
| Reopened | **4** |
| Partially complete (left open, commented) | **2** |
| Remaining open | **59** (all) |
| Clarification comments posted | **12** |
| Status comments posted | **1** |
| Verification/partial comments posted | **6** (4 reopen + 2 partial) |
| **Total Asana comments** | **13** |
| Task completion states changed | **4** (all `true → false`) |
| DEV pages marked complete | **0 / 7** |
| Lovable messages sent | **0** |
| Lovable credits used | **0** |
| Other Asana projects modified | **0** |

---

## 6 · WHAT WOULD MOVE THE BOARD FASTEST

Ranked by items unblocked per answer:

1. **The Playfair weight table** (HOME-18) → unblocks 6 items across 4 pages and the whole of Batch 6a.
2. **The Admissions/Amenities decision** (ADM-04) → unblocks all 8 Admissions items, which are otherwise unbuildable because the page's identity is undecided.
3. **The four missing screenshots** (HOME-01, HOME-10, SERV-01, SERV-02) → lets 4 reopened items be closed, possibly immediately.
4. **The CTA hex** (ABOUT-05 / ADM-05) → closes a shared defect on 3 routes.
5. **Lovable credits** → without them nothing ships regardless of the answers above.
