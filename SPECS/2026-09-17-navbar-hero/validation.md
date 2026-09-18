# Validation — Navbar + Hero Feature

How we know this feature is done and can be merged back to `main`.

## Automated checks (must all pass)

Run: `node build-lab/tests/navbar-hero.test.js`

1. **Navbar structure:** `<header class="navbar">` present with wordmark "Lucid",
   links Problem · Solution · Features, and one `btn btn-primary` pointing to `#cta`.
2. **Hero structure:** `<section id="hero">` present with the exact tagline headline
   ("Find anything you've ever saved."), subheadline from the architecture, one primary CTA,
   and a search-bar mockup (`.hero-search`).
3. **CSS tokens:** no hardcoded hex colors or radius values outside `:root`
   (component CSS uses `var(--…)` only).
4. **Motion exists:** a `@keyframes` hero-reveal rule exists; `.navbar.is-solid` scrolled-state
   rule exists; CTA still uses `--transition-fast`.
5. **JS is testable and valid:** `shouldSolidifyNavbar(0)` → `false`,
   `shouldSolidifyNavbar(20)` → `true`, `getHeroRevealClass()` returns the documented class.
   `node --check build-lab/script.js` exits 0.
6. **Motion budget:** exactly 1 hero effect + 1 scroll effect + 1 microinteraction
   (verified by tests/quality check — no second keyframe on other sections).

## Visual / quality checks (manual, best-effort in this environment)

7. Page opens without console errors; navbar becomes solid on scroll; hero headline
   animates in calmly; CTA has a smooth hover transition; mobile viewport does not break.

## Cross-spec compliance

8. Implementation must match `requirements.md`, the page architecture in MISSION.md
   (Section 3), and the approved design system (Section 2 — Soft Fog palette, radius tokens,
   Fraunces + Inter, one CTA only).

## Acceptance gate

- All automated checks green (including prior base-shell checks).
- Motion budget respected.
- Any deviation from the spec is documented here and approved by the founder before merge.

---

## Sign-off (filled after implementation)

- [x] 2026-09-17 — Automated checks: **22/22 green** (`node build-lab/tests/navbar-hero.test.js`, exit 0).
- [x] 2026-09-17 — `node --check build-lab/script.js` passes.
- [x] 2026-09-17 — Motion budget: 1 keyframe (hero load-in) + 1 scroll listener (navbar solid) + CTA hover microinteraction.
- [x] 2026-09-17 — Token hygiene: no hex colors outside `:root`.
- [x] 2026-09-17 — Smoke test: `index.html`, `style.css`, `script.js` all serve 200.
- [x] 2026-09-17 — Founder review: Navbar + Hero match MISSION.md Section 3 architecture and Section 2 design system.

**Deviations from spec:** none. Small implementation notes: `.hero-search` mockup uses static copy (product isn't real yet); `IntersectionObserver` not needed — a passive scroll listener is simpler for the navbar state.