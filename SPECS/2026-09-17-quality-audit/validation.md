# Validation — Quality Audit Fixes

How we know this feature is done and can be merged back to `main`.

## Automated checks (must all pass)

Run: `node build-lab/tests/quality-audit.test.js` (new),
`node build-lab/tests/navbar-hero.test.js` (regression),
`node build-lab/tests/content-sections.test.js` (regression).

1. **No-JS fallback:** `index.html` contains a `<noscript>` block so the hero stays visible
   without JavaScript.
2. **Reduced motion:** `style.css` contains `@media (prefers-reduced-motion: reduce)` that
   disables hero animation and feature-card hover transition, and sets `scroll-behavior: auto`.
3. **Keyboard accessibility:** `style.css` contains a `:focus-visible` rule for buttons/links
   styled with design tokens.
4. **Smooth scrolling:** `style.css` contains `scroll-behavior: smooth` on `html`.
5. **Regression:** all 42 prior tests still pass.
6. **Token hygiene:** no hardcoded hex colors or radius values outside `:root`.

## Visual / quality checks (manual)

7. Page renders normally in a browser with JS on; hero headline visible (no blank hero);
   keyboard Tab shows visible focus rings; clicking nav links scrolls smoothly.

## Motion budget compliance

8. No new keyframes, no new scroll listeners, no new libraries. The
   `prefers-reduced-motion` block only disables existing motion for those users.

## Cross-spec compliance

9. Fixes use tokens from MISSION.md Section 2 (Soft Fog) and satisfy
   MISSION.md Non-Negotiables (20s clarity, one CTA, calm personality).

## Acceptance gate

- All automated checks green, including regression.
- Motion budget respected.
- Any deviation documented here and approved by the founder before merge.