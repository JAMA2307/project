# ASANA IMPLEMENTATION PLAN — Amara Care Center

| | |
|---|---|
| Prepared | 2026-08-06 |
| Source | `ASANA_QA_LEDGER.md` — Asana project **Amara** `1217105105055924` |
| Status | **PREPARATION ONLY — nothing dispatched.** Lovable credits are at zero |
| Purpose | Sequence 59 QA items into the fewest Lovable turns, grouped by shared code impact rather than by Asana page |

---

## 0 · THE ECONOMICS THIS PLAN IS OPTIMISING FOR

A Lovable turn costs the same whether it fixes one item or fifteen. R7 — a whole-codebase sweep plus 198 harness runs — cost **6.5 credits in a single turn**. The waste is not in the size of a turn; it is in **turns that have to be repeated** because the brief was wrong, incomplete, or blocked halfway through.

So this plan is built on three rules:

1. **Fix shared code once.** A Footer defect reported on Home is one edit and nine verifications, not nine edits.
2. **Never dispatch a batch containing a blocked item.** A turn that stalls waiting for an asset is a wasted turn. Everything blocked is quarantined in §3.
3. **Do not dispatch anything that needs a screenshot nobody has seen.** 35 of 59 items are `NEEDS VISUAL VERIFICATION`. Guessing at them and being wrong costs two turns — the wrong fix and the correction — plus the credibility of the whole pass.

**Consequence: the plan below is deliberately front-loaded.** Batch 1 is everything that is certain today. Batches 2–7 cannot be written in final form until the 60 screenshots are visible, and I have not pretended otherwise by inventing their contents.

---

## 1 · WHAT GATES THIS PLAN

| # | Blocker | Blocks | Needed |
|---|---|---|---|
| **B1** | Egress policy denies `asanausercontent.com` (403 CONNECT) | **35 items** across all 7 pages | Allow the host, or export the 60 PNGs into the repo |
| **B2** | Figma seat quota exhausted (View seat, 6 calls/month) | Legal copy (AUX-01/02), UI-KIT success state (HOME-21), "correct icons" (ABOUT-02/11, CON-02), replacement photography (HOME-03, HOME-09) | Dev/Full seat — 200 calls/day |
| **B3** | Lovable credits at zero | **all implementation** | Credit top-up |
| **B4** | IA decision on Admissions vs Amenities (§5-C1 of the ledger) | ADM-04, and the nav on all 9 routes | Client/agency decision |
| **B5** | Placeholder policy conflict (§5-C2) | HOME-09 | Client ruling — recommend upholding the no-placeholder rule |
| **B6** | Poppins has no official source; Satoshi ships no licence file | **Batch 6a** (fonts) | Agency answer on both, see `TYPOGRAPHY_AND_FORM_STATES.md` T3 and D1 |
| **B7** | Form-state designs live in a Figma UI KIT frame reachable neither via Figma (quota) nor via the Asana screenshot (egress 403) | HOME-21, and all form work | **B1 or B2** — either one unblocks it |

**B1 is the cheap one and it unlocks the most.** Opening one host converts 35 items from guesswork into work.

---

## 2 · BATCHES

### BATCH 1 — SHARED COMPONENTS · **dispatch first, ready now**

The only batch that needs neither a screenshot nor a Figma call. Every item was verified directly against source.

| Asana | Fix | File |
|---|---|---|
| **HOME-12** | Remove the default-open FAQ item: `useState<number \| null>(1)` → `useState<number \| null>(null)` | `sections/Faq.tsx` |
| **HOME-11** | Reveal the header nav on scroll-up. Header is currently `absolute inset-x-0 top-6` with no scroll behaviour — needs a scroll-direction listener, `position: fixed` when revealed, and a translate transition. Must honour `prefers-reduced-motion` and must not break the 1080px content-fit breakpoint or the 52px row height | `Header.tsx` |
| **ABOUT-01a** | Add hover states to buttons | `ui/button.tsx` |
| **CON-03** | Change the checkmark colour. **Do not touch the shape** — `!rounded-[4px]` is on the regression watch | `home/Contact.tsx` |
| **HOME-14** | Set the CTA copy to *"Contact our team / to learn more about / our services"*. Ship **"our"**, not the "out" in the ticket — a fourth typo override alongside `Shedule`/`addres`/`Brookwood` | CTA/contact block |

**Why HOME-12 leads:** it also closes the single outstanding FAIL from the responsive programme. R7 measured the Home FAQ at 766px against a 752px spec and could not account for the surplus. The open answer is worth exactly 82px; 240 padding + 444 closed accordion = 684, so `min-h-[752px]` then governs and the section lands on **752 naturally** — no padding shaved, no section compressed. One line, two problems.

- **Routes affected:** all 9 (Header, Button) · `/`, `/services`, `/careers` (FAQ) · `/`, `/careers`, `/contact` (form)
- **Attachments required:** none
- **Acceptance:** FAQ renders fully collapsed on mount on all 3 routes; header hides on scroll-down and reveals on scroll-up on all 9, with no layout shift, reduced-motion honoured; button hover visible in light and dark variants; checkbox colour changed and shape unchanged; CTA copy exact.
- **Regression:** full 9×22 harness; re-measure the R7 reference table — **FAQ must now read 752**; header still 52 tall with 189×52 logo; zero sub-44px tap targets; no `overflow-x`.
- **Expected Lovable turns:** **1**
- **Risk:** the scroll-reveal header is the only non-trivial piece — it can fight the absolute-positioned hero overlays. Specify that the header must not become `sticky` inside a transformed ancestor.

---

### BATCH 2 — HOME · *gated on B1*

18 remaining Home items. Actionable-from-text now: HOME-03 (heading colour → bluish), HOME-05 + HOME-18 (type weights), HOME-08 (pin end-state + disable in-section buttons), HOME-06 (card hover animation — **re-reported by the agency on 2026-08-06 after the first report, the only item in the project with a follow-up comment**).
Needs screenshots: HOME-02, 04, 07, 15, 16, 17, 19, 20. Needs Figma: HOME-09 photography, HOME-21 UI-KIT success state.

- **Shared spillover:** HOME-13 (footer newsletter feedback + wrong logo) → Batch 6. HOME-01 (brand marks) → Batch 6.
- **Expected turns:** **2** (interaction/animation work separated from static layout — they fail differently and mixing them makes a failed turn expensive)
- **Risk:** HOME-08 and HOME-06 are both scroll/hover motion on the same page; ScrollTrigger refresh behaviour must be re-verified after either.

### BATCH 3 — ABOUT · *gated on B1*

14 items, the largest per-page group and the one with the most structural damage: ABOUT-04 (values scroll-stack must rise and cover), ABOUT-05 (Get Started section *"looks nothing like Figma"* — a rebuild), ABOUT-08 (card layout broken), ABOUT-09 (**mobile hero too small — the 08-05 "ABOUT HERO — QA FAILED" report, still open; R3 fixed only the desktop fault**).

- **Expected turns:** **2**
- **Risk:** ABOUT-04 touches the framer-motion scroll-stack that R3 gated behind `useStackEnabled` (min-width 768 **and** min-height 800). Changing the stack must not reintroduce a pinned region taller than the viewport.

### BATCH 4 — SERVICES · *gated on B1*

7 items. SERV-01 and SERV-02 are marked complete in Asana but were **modified after closure on 2026-08-06** and are not accepted as fixed. SERV-05 alone carries four distinct mobile defects.

- **Expected turns:** **1**
- **Risk:** SERV-02 names two wrong logos and a missing backdrop blur — the logo half belongs to Batch 6, so split the ticket rather than duplicating the asset work.

### BATCH 5 — ADMISSIONS / AMENITIES · *gated on B1 **and** B4*

8 items. **Do not dispatch until the IA question is answered** — ADM-04 may change the route, the nav label, or the page title, and every other Admissions item is written against whatever that page ends up being. ADM-03 does give caption copy verbatim (*"Serene / Courtyard Retreat"*).

- **Expected turns:** **1**
- **Risk:** highest of any batch. Dispatching before B4 is resolved risks doing the work twice.

### BATCH 6 — BRAND, LOGOS, ICONS, TYPOGRAPHY · *partly gated on B2 and B6*

**Revised 2026-08-06 after the official font delivery.** The typography half of this batch is now precisely specified rather than exploratory — see `TYPOGRAPHY_AND_FORM_STATES.md`. It splits into **6a (fonts)** and **6b (brand assets)**, which have different gates and should not be dispatched together.

#### 6a · Self-host the official fonts — closes HOME-05, HOME-18, ABOUT-10, SERV-01

Root cause, now named: **Playfair Display is loaded at `wght@400` only**, so every heavier heading is a browser-synthesised fake bold — **and** `text-h1/h2/h3/h4` each hard-code `font-weight: 400`, so no heading can render heavier even once the files exist. Both must change together; either alone is a no-op.

| Step | Detail |
|---|---|
| 1 | Convert `design-sources/fonts/` to WOFF2, Latin subset. **Mandatory** — the raw TTF/OTF are 4–5× larger than the CDN files they replace |
| 2 | Ship the **variable** Playfair (`wght 400–900`, ~60–70 KB as WOFF2) — one file covers all six weights and beats shipping six statics |
| 3 | Satoshi as statics: 300/400/500/700/900 + italics as needed. **No 600 exists — forbid `font-semibold` on `--font-sans`** |
| 4 | Add real `@font-face` rules. There are none in the codebase today |
| 5 | Remove the Google Fonts and Fontshare `<link>`s from `__root.tsx`; drop the four now-dead `preconnect`s |
| 6 | Un-hardcode `font-weight` in the four heading utilities and the base `h1–h6` rule |
| 7 | Point buttons at `text-button` instead of the inline `font-sans text-[18px] font-medium` in `ui/button.tsx` (T6) |
| 8 | Fix the no-op `clamp()` on `text-label` (T8) |

- **Gate B6 — needs an agency answer first:** (i) **Poppins** drives `text-label` but is not in the official delivery — keep or re-map to Satoshi? (ii) **Satoshi ships no licence file** — confirm self-hosted webfont use is permitted. Playfair's OFL is included and clear.
- **Do not dispatch 6a before B6 is answered.** Building it twice costs more than waiting.
- **Regression — this is the highest-risk batch in the programme.** The `clamp()` scale interpolates 390→1440 and drives **every section height**. Changing a weight changes glyph widths, which changes wrapping, which changes heights. After 6a, re-measure the **entire** R7 reference table, not a sample — and confirm the Home FAQ still reads 752 after Batch 1.
- **Side benefit:** self-hosting removes T7, the silent fallback to `system-ui` when a font CDN is slow or blocked. That failure mode is invisible in code review and looks exactly like "typography is inconsistent".
- **Expected turns:** **1** for the font layer, **1** for the scale/consumer cleanup.

#### 6b · Brand assets — *gated on B2 (Figma seat)*

Wrong or duplicated logos (HOME-01, HOME-13, ABOUT-01b, ABOUT-03, SERV-02 ×2) and missing official icons (ABOUT-02, ABOUT-11, CON-02).

- **Expected turns:** **1**

### BATCH 6-OLD — superseded, retained for reference · *gated on B2*

The cross-cutting asset batch, pulled out of every page batch above so the same asset is never fixed twice.

| Group | Items |
|---|---|
| Wrong / duplicated logo | HOME-01, HOME-13, ABOUT-01b, ABOUT-03, SERV-02 (×2) |
| Missing official icons | ABOUT-02, ABOUT-11, CON-02 |
| Type weights and sizes | HOME-05, HOME-18, ABOUT-02, ABOUT-10, ABOUT-12, SERV-01, SERV-05 |
| Footer newsletter feedback | HOME-13 |

- **Expected turns:** **2** (assets, then the type scale — the type scale is global and must be re-verified against every 1440 reference value)
- **Risk:** the type scale is `clamp()`-interpolated 390→1440. Any endpoint change moves **every** section height. Re-run the full reference table afterwards, not a sample.

### BATCH 7 — CAREERS, CONTACT, LEGAL, 404 · *partly gated on B1 and B2*

CAR-01 (hero scrim too dark) and CON-01 (left column vertical alignment) are actionable from text. CAR-02, CAR-03, CON-02, AUX-03 need screenshots. **AUX-01 and AUX-02 are hard-blocked on B2** — the legal body copy exists only in Figma and cannot be invented.

- **Expected turns:** **1**, plus **1** more for the legal copy once B2 clears
- **Risk:** low, except that the legal pages currently have real structure but placeholder-length copy; dropping in the real text will change the page height and must be re-verified at 2560 and 768.

### BATCH 7b — CONTACT-FORM STATES · *gated on B7*

Added 2026-08-06. The agency has published four official form states in the Figma UI KIT — **FORM-S0** default, **FORM-SF** focus/filled (*"if shown"*), **FORM-S1** successful submission, **FORM-S2** failed submission. Full register in `ASANA_QA_LEDGER.md` §11.

This resolves what **HOME-21** meant: *"take the one marked 1"* = **State 1, successful submission**. It also introduces **FORM-S2**, a failure state that has **no Asana ticket at all** — it exists only in the agency brief.

**Do not dispatch while B7 stands.** Every visual attribute the agency asked for — heading and body copy, button copy, dimensions, spacing, typography, colours, card background, transition, retry/reset, responsive differences, desktop and mobile — sits in the UI KIT frame, and neither route to it is open (Figma seat quota; Asana egress 403). Building from guesswork would cost the turn twice.

**Two-turn shape once unblocked:**

| Turn | Content |
|---|---|
| **7b-i** | Make submission asynchronous, add the pending state and double-submit guard, add an inline validation surface (today only `issues[0]` reaches a toast), add the ARIA live region and focus management. **No visual state work** — this is the machinery S1/S2 need to exist at all, and none of it depends on the design |
| **7b-ii** | Build FORM-S0/SF/S1/S2 to the UI KIT, desktop and mobile |

**7b-i is design-independent and could be promoted into Batch 1** if the form machinery is wanted before the UI KIT opens. It is listed separately because it changes behaviour the agency has not yet seen, and shipping it alone would leave the form in a state neither the old design nor the new one describes.

- **Routes:** `/`, `/careers`, `/contact` — one component, three verifications
- **Regression:** the Home contact section is signed off at `min-h-[780px]` at 1440. If S1/S2 differ in height from the form, the section must not jump. Also: the checkbox stays square (`!rounded-[4px]`) — CON-03 authorises a colour change only
- **Expected turns:** **2**

### BATCH 8 — FINAL REGRESSION

Full 9-route × 22-viewport harness, the R7 1440 reference table re-measured end to end, browser-zoom QA at 8 steps, overlap detection, asset integrity, `oncommunity` absent, About-has-Team/Services-has-FAQ/Home-has-no-CTA composition intact.

- **Expected turns:** **1**

---

## 3 · QUARANTINE — do not put these in any batch yet

| Item | Why | Releases when |
|---|---|---|
| AUX-01, AUX-02 | Legal body copy exists only in Figma | B2 |
| HOME-21 | Needs the Figma UI-KIT "message sent" frame, variant 1 | B2 |
| HOME-09 | Instruction says use placeholders; standing client rule forbids them | B5 ruling |
| ADM-01…08 | Page identity unresolved | B4 |
| 35 NVV items | No screenshot | B1 |

---

## 4 · TURN BUDGET

| Batch | Turns | Gate |
|---|---|---|
| 1 · Shared components | **1** | none — **ready now** |
| 2 · Home | 2 | B1 |
| 3 · About | 2 | B1 |
| 4 · Services | 1 | B1 |
| 5 · Admissions | 1 | B1 + B4 |
| **6a · Self-host fonts + type scale** | **2** | **B6** |
| 6b · Brand assets | 1 | B2 |
| 7 · Careers, Contact, Legal, 404 | 2 | B1 + B2 |
| **7b · Contact-form states** | **2** | **B7** |
| 8 · Final regression | 1 | all |
| **Total** | **15** | |

*(Revised 12 → 13 → 15: Batch 6 split into 6a fonts / 6b brand assets, which have different gates; Batch 7b added for the four official form states, of which turn 7b-i is design-independent.)*

**Minimum to clear the entire Asana backlog: 12 Lovable turns**, against 59 QA items — roughly **5 items per turn**. Dispatching page-by-page as the board is organised would cost ~20 turns and would fix the shared components repeatedly.

At R7's observed rate (6.5 credits for the largest turn yet), 12 turns is on the order of **50–70 credits**, most of it in Batches 2, 3 and 6.

**Sequencing note:** Batch 1 should go out the moment credits return, before any screenshot arrives. It is fully specified, it is verified against source, it fixes the highest-frequency shared defects, and it closes the last open FAIL from the responsive programme.

---

## 5 · WHAT THIS PLAN DELIBERATELY DOES NOT CLAIM

- No screenshot has been interpreted. 35 items are placeholders in this plan with honest gates, not invented briefs.
- No Asana item has been marked fixed on the strength of a previous wave. The four items the agency itself closed are treated as unverified, because three were edited after closure and I cannot see them.
- The four blocked groups are named with the exact permission or decision each needs. None of them is a code problem.
