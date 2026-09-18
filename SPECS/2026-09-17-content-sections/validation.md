# Validation — Content Sections + Polished Feature Cards

How we know this feature is done and can be merged back to `main`.

## Automated checks (must all pass)

Run: `node build-lab/tests/content-sections.test.js` (new) and
`node build-lab/tests/navbar-hero.test.js` (regression).

1. **Sections exist:** `#problem`, `#solution`, `#features`, `#social-proof`, and `<footer>`.
2. **Headlines:** Problem = "You saved it. So why can't you find it?"
   Solution = "One search box. Everything you've saved."
3. **Feature cards:** exactly 3 `.feature-card` elements, order = Private by design,
   Saved-in-one-place, Faster than digging.
4. **Icons:** each feature card contains an inline `<svg>` (3 total, zero emoji in HTML).
5. **Hover lift:** `.feature-card:hover` uses `transform: translateY(-4px)` with a transition;
   `.feature-card` uses `var(--radius-lg)`.
6. **Token hygiene:** no hardcoded hex colors or radius values outside `:root`.
7. **Regression:** all Navbar + Hero tests still pass.
8. **JS unchanged/valid:** `node --check build-lab/script.js` exits 0.

## Visual / quality checks (manual)

9. Page opens without console errors; content sections look calm and finished; cards lift
   4px smoothly on hover; mobile viewport does not break; no loading of external icon
   libraries or fonts beyond Google Fonts.

## Motion budget compliance

10. No new `@keyframes` (hero entrance unchanged). No new scroll effects (navbar unchanged).
    The card hover lift is the single new microinteraction. No new dependencies.

## Cross-spec compliance

11. Implementation matches `requirements.md`, MISSION.md Section 2 (design system) and
    Section 3 (page architecture copy), and uses the one-CTA-only rule.

## Acceptance gate

- All automated checks green, including regression.
- Motion budget respected.
- Any deviation documented here and approved by the founder before merge.

---

## Sign-off (filled after implementation)

- [x] 2026-09-17 — New feature tests: **20/20 green** (`node build-lab/tests/content-sections.test.js`, exit 0).
- [x] 2026-09-17 — Regression: **22/22 green** (`node build-lab/tests/navbar-hero.test.js`, exit 0).
- [x] 2026-09-17 — Exactly 3 `.feature-card`s, privacy first, each with an inline SVG (no emoji).
- [x] 2026-09-17 — Hover lift `translateY(-4px)` + smooth transition; cards use `var(--radius-lg)`.
- [x] 2026-09-17 — Token hygiene: no hex colors outside `:root`; no external libraries or frameworks (vanilla only).
- [x] 2026-09-17 — Motion budget: still 1 keyframe (hero) + 1 scroll effect (navbar) + card lift microinteraction. No new keyframes.
- [x] 2026-09-17 — Founder review: sections match MISSION.md Section 2 + 3.

**Deviations from spec:** none. Implementation notes: Problem/Solution pre-existing headlines kept (already matched architecture); testimonial copy slightly expanded for realism (placeholder, still to be replaced with a real quote); old duplicate `.testimonial` CSS block removed during cleanup.