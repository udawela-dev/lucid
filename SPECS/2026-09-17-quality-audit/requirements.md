# Feature Spec — Quality Audit Fixes (Stage 5, Step 4)

**Date:** 2026-09-17
**Branch:** `feature/quality-audit`
**Stage:** Roadmap Stage 5, Step 4 — 5-Point Quality Audit + fixes

---

## Context

Stage 5 Steps 1–3 are merged into `main`. The landing page is functionally complete
(Navbar, Hero, Problem, Solution, Features cards, Social Proof, CTA stub, Footer).
A quality audit was run against the current page. All 42 automated tests pass, but the
audit found several issues to fix before the site is considered production-quality.

Constitution rules that apply:
- No frameworks, no libraries, no npm packages — plain HTML, CSS, vanilla JS only.
- Design tokens first: `var(--…)` only, never hardcoded hex/radius values.
- Brand personality: private, calm, intelligent.
- Accessibility and calm motion are core values (TECH.md motion budget + modern UI/UX rules).

---

## Audit findings (from the 5-Point Quality Audit)

| Severity | Finding |
| :--- | :--- |
| Critical | Hero content is hidden if JavaScript fails. `.hero-reveal { opacity: 0 }` default means no-JS visitors never see the headline. |
| Important | No `prefers-reduced-motion` support. Users requesting reduced motion still get the hero animation + feature-card hover lift. |
| Important | Only one `:focus` style exists (text input). Buttons and links lack a calm focus-visible style consistent with the design system. |
| Nice-to-have | Anchor navigation (`#problem`, `#cta`, etc.) jumps instantly; `scroll-behavior: smooth` is a subtle professional touch. |

### Items that PASSED the audit (no change needed)
- All 42 automated tests green (navbar-hero + content-sections).
- No duplicate IDs, balanced HTML tags, all sections have `aria-label`, no images missing `alt`.
- No hardcoded hex colors outside `:root`; no emoji; no external libraries.
- Motion budget: 1 keyframe (hero) + 1 scroll listener (navbar) + card hover microinteraction.
- SEO basics present: `<title>`, meta description, viewport.
- Contrast check: white text on primary indigo ≈ 6.3:1 (WCAG AA passes).

---

## Scope (What this feature does)

1. **Critical — no-JS hero fallback:** add a `<noscript>` block in `index.html` that forces the
   hero content visible if JavaScript is disabled, so the page is never blank.
2. **Important — reduced motion:** add a `@media (prefers-reduced-motion: reduce)` block in
   `style.css` that disables the hero animation and feature-card hover transition for users
   who request reduced motion.
3. **Important — focus-visible styles:** add a calm `:focus-visible` rule for buttons and links
   using design tokens (soft ring in primary color), consistent with the design system.
4. **Nice-to-have — smooth scrolling:** add `scroll-behavior: smooth` to the base `html` rule
   for gentle anchor navigation.

## Non-Goals (Out of scope)

- Waitlist form submit behavior (JS + SQLite) — later feature.
- CTA section content finalization — later feature.
- Any new animations or components — this is a fix-only feature.
- Testing in real browsers — validations are static file checks (per project constraints).

## Decisions locked in by the founder (2026-09-17)

| Decision | Choice |
| :--- | :--- |
| Fix scope | All four findings (Critical + Important + smooth scroll) |
| Approach | TDD where code changes: tests first (red), implement (green) |
| Dependencies | Vanilla only — no new libraries |

## Technical approach

- **HTML** (`index.html`): add `<noscript>` fallback style near the top of `<head>` so the hero
  shows even without JS. No other markup changes.
- **CSS** (`style.css`): add
  - `html { scroll-behavior: smooth; }` (respecting reduced-motion, see below),
  - `:focus-visible` rule for `.btn` and links using a token-based ring (e.g. outline in
    `--color-primary` with subtle offset, or `box-shadow` ring like `.input:focus`),
  - `@media (prefers-reduced-motion: reduce)` block that sets
    `html { scroll-behavior: auto; }`, `.hero-reveal` animation off, and feature-card
    transition off.
- **JS** (`script.js`): no changes required (existing pure functions + wiring untouched).
  Existing tests must still pass unchanged.

## Testability

- New test file `build-lab/tests/quality-audit.test.js` (plain Node, no npm):
  1. `index.html` contains `<noscript>`.
  2. `style.css` contains `prefers-reduced-motion`.
  3. `style.css` contains `:focus-visible`.
  4. `style.css` contains `scroll-behavior`.
  5. Regression: all existing navbar-hero + content-sections tests still pass.
  6. Token hygiene: no hardcoded hex outside `:root` (unchanged).
- Motion budget: still 1 keyframe + 1 scroll listener + card hover (fixes only touch
  accessibility/smooth-scroll, no new keyframes or listeners).