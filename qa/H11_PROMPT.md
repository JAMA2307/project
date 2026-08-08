# H11 — LOVABLE DISPATCH PROMPT (ready, not sent)

TASK: H11 · Asana HOME-17 `1217213785962846` — mobile hero badge and photo geometry.
FILE: `src/components/home/Hero.tsx` — THIS FILE ONLY.

## SCOPE

Mobile (393) only. Desktop and tablet must not move.

## CURRENT DEFECTS at 393

1. Photo uses `aspect-[4/5]` = 0.800, rendering **451.25** tall. Target is **428**, i.e.
   ratio **361 / 428 = 0.843**. The photo is 23px too tall.
2. Badge uses `inset-x-3`, so it stretches full-bleed to **337** wide. Target is **273**.
3. Insets are **12 / 12**. Target is **16 / 16**.
4. Badge is anchored to both side edges. It must be a **bottom-left** card of intrinsic
   width, not a stretched bar.

## TARGET at 393 — measured, do not adjust

- photo **361 × 428**
- badge **273 × 126**, inset **left 16**, **bottom 16**
- badge fill `#E6F0FF` = the existing `bg-secondary-bg` token — do not hard-code the hex

## REQUIRED

- Replace the mobile `aspect-[4/5]` with the 361/428 ratio. Keep `sm:aspect-[3/2]` and
  `md:aspect-[16/9]` exactly as they are.
- Replace `inset-x-3 bottom-3` with a bottom-left anchor at 16/16 and a 273px width at
  mobile widths.
- Keep every `lg:` class unchanged — `lg:inset-x-auto lg:bottom-6 lg:right-6
  lg:max-w-[340px] lg:rounded-[8px] lg:px-6 lg:py-4`. Desktop stays bottom-**right**.
- Badge content, icon, copy, `text-label`, and the `bg-accent` icon chip are unchanged.
- Do not touch the h1, the paragraph, the CTA row, the pattern background, or the section
  padding — those are H01/H02/H03/H10 and all verified.

## DO NOT

- change any file other than `Hero.tsx` — **including generated files such as
  `src/routeTree.gen.ts`**
- hard-code `#E6F0FF`
- alter the desktop badge width (its 345 × 160 target is a separate, later item)

## ACCEPTANCE at 393

- photo **361 × 428**
- badge **273 × 126**, offsets exactly 16 from the photo's left and bottom edges
- badge sits **inside** the photo bounds
- `document.scrollWidth <= window.innerWidth`
- no console errors

## ACCEPTANCE at 1440

- unchanged in every respect — badge still bottom-right, photo still 16/9

## REPORT BACK

Give the measured photo box and badge box at 393, the measured badge offsets, and confirm
no file other than `Hero.tsx` changed. Do not report success without those numbers.
