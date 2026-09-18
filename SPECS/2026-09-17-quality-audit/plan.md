# Plan — Quality Audit Fixes

Feature spec: `build-lab/SPECS/2026-09-17-quality-audit/`

## Task Groups

### Group 0 — Scaffolding
- [x] Verify branch `feature/quality-audit` is checked out and clean.
- [x] Full audit run done (findings recorded in requirements.md).

### Group 1 — Tests first (RED)
Write failing tests before feature code. Run with `node build-lab/tests/quality-audit.test.js`.

- [ ] Test: `index.html` contains a `<noscript>` fallback block.
- [ ] Test: `style.css` contains `prefers-reduced-motion` media query.
- [ ] Test: `style.css` contains a `:focus-visible` rule.
- [ ] Test: `style.css` contains `scroll-behavior`.
- [ ] Confirm these 4 FAIL (red) on the current code.

### Group 2 — Implement fixes (GREEN)
- [ ] Add `<noscript>` hero fallback to `index.html` (forces hero visible without JS).
- [ ] Add `html { scroll-behavior: smooth; }` to `style.css` base rules.
- [ ] Add `:focus-visible` styling for `.btn` and links using tokens.
- [ ] Add `@media (prefers-reduced-motion: reduce)` block:
      `scroll-behavior: auto`, hero animation off, card transition off.
- [ ] Keep all existing markup/styles; no new components or animations.

### Group 3 — Quality checks
- [ ] Run `node build-lab/tests/quality-audit.test.js` — all green.
- [ ] Regression: `node build-lab/tests/navbar-hero.test.js` and
      `node build-lab/tests/content-sections.test.js` — all green.
- [ ] `node --check build-lab/script.js` — clean.
- [ ] Token hygiene re-check: no hex outside `:root`.
- [ ] Motion budget re-check: no new keyframes, no new scroll listeners, no new libraries.

### Group 4 — Commit
- [ ] Commit staged changes with clear message.
- [ ] Sign off validation.md; note any deviations.