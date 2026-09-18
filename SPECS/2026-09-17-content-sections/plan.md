# Plan — Content Sections + Polished Feature Cards

Feature spec: `build-lab/SPECS/2026-09-17-content-sections/`

## Task Groups

### Group 0 — Scaffolding (before any code)
- [x] Verify branch `feature/content-sections` is checked out and clean (merged from `main`).
- [ ] Read current `index.html`, `style.css`, `script.js` to confirm baseline.

### Group 1 — Tests first (RED)
Write failing tests before feature code. Run with `node build-lab/tests/content-sections.test.js`.

- [ ] Test: sections `#problem`, `#solution`, `#features`, `#social-proof`, and `<footer>` exist.
- [ ] Test: Problem headline ("You saved it. So why can't you find it?") and Solution headline
      ("One search box. Everything you've saved.") are present.
- [ ] Test: exactly **3** `.feature-card` elements exist, in privacy-first order
      (Private by design, Saved-in-one-place, Faster than digging).
- [ ] Test: each `.feature-card` contains an inline `<svg>` icon (count match: 3 svgs).
- [ ] Test: CSS has `.feature-card:hover` with `translateY(-4px)` and a transition;
      `.feature-card` uses `var(--radius-lg)`.
- [ ] Test: no hardcoded hex colors outside `:root` (unchanged rule).
- [ ] Test: no emoji characters in `index.html` (calm tone).
- [ ] Regression: existing `navbar-hero.test.js` still passes.
- [ ] Confirm new tests FAIL (red) for unimplemented behaviors (feature cards, hover lift).

### Group 2 — Implement Problem + Solution (GREEN)
- [ ] Replace stub copy in `#problem` and `#solution` with the approved architecture copy.
- [ ] Style both sections calmly with tokens (spacing, `.section-title`, `.section-subtitle`,
      maybe a subtle surface card if it aids readability — keep calm).

### Group 3 — Implement Features (the polished component) (GREEN)
- [ ] Add exactly 3 `.feature-card` elements with inline SVG icons and approved titles/copy.
- [ ] Add `.feature-card` styles: surface bg, `--radius-lg`, `--shadow-sm`, padding via `--space-*`.
- [ ] Add `.feature-card:hover`: `transform: translateY(-4px)` + smooth transition (the 1 microinteraction).
- [ ] Ensure privacy card is first.

### Group 4 — Implement Social Proof + Footer (GREEN)
- [ ] Refine testimonial: quote, cite, styling using tokens (surface card, `--radius-lg`).
- [ ] Refine footer: wordmark, tagline, waitlist link, copyright; tokens only.

### Group 5 — Quality checks
- [ ] Run `node build-lab/tests/content-sections.test.js` — all green.
- [ ] Run regression `node build-lab/tests/navbar-hero.test.js` — all green.
- [ ] `node --check build-lab/script.js` — clean.
- [ ] Motion budget respec: 1 hero effect (unchanged) + 1 scroll effect (unchanged) +
      card lift microinteraction (this feature) — no new keyframes, no extra libraries.
- [ ] Manual visual check if server runs; mobile width does not break.

### Group 6 — Commit
- [ ] Commit staged changes with clear message.
- [ ] Sign off validation.md; note any deviations for founder approval.