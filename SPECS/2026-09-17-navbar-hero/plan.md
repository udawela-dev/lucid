# Plan — Navbar + Hero Feature

Feature spec: `build-lab/SPECS/2026-09-17-navbar-hero/`

## Task Groups

### Group 0 — Scaffolding (before any code)
- [ ] Verify branch `feature/navbar-hero` is checked out and clean.
- [ ] Create `build-lab/tests/` directory for the Node test scripts.

### Group 1 — Tests first (RED)
Write failing tests before any feature code. Run with `node build-lab/tests/navbar-hero.test.js`.

- [ ] Test: `index.html` contains `<header class="navbar">` with brand wordmark "Lucid",
      three nav links (Problem, Solution, Features), and a `btn btn-primary` linking to `#cta`.
- [ ] Test: `index.html` contains `<section id="hero">` with the exact tagline headline,
      subheadline text, a primary CTA to `#cta`, and a search-bar mockup element (e.g. `.hero-search`).
- [ ] Test: `style.css` defines a `@keyframes` rule for the hero reveal (calm fade/slide),
      a `.navbar` scrolled state rule (e.g. `.navbar.is-solid`), and uses only design tokens
      (no hardcoded hex outside `:root`).
- [ ] Test: `script.js` exports/shows pure functions `shouldSolidifyNavbar(scrollY)` and
      `getHeroRevealClass()` returning the documented values; `node --check` passes on syntax.
- [ ] Confirm all tests FAIL (red) for the as-yet-unimplemented behaviors.

### Group 2 — Implement Navbar (GREEN)
- [ ] Enhance navbar markup if needed (links, aria-labels, `is-solid` hook).
- [ ] Add `.navbar` scrolled-state CSS using tokens (calm background + subtle shadow).
- [ ] Implement `shouldSolidifyNavbar(scrollY)` in `script.js` (pure function, `scrollY > 8`).

### Group 3 — Implement Hero (GREEN)
- [ ] Add hero search-bar mockup markup with realistic "found a link" microcopy.
- [ ] Add `@keyframes` hero reveal + apply via `getHeroRevealClass()` (load-in effect).
- [ ] Style `.hero-search` and hero layout with tokens; keep calm spacing per design system.

### Group 4 — Motion budget + wiring (GREEN)
- [ ] Wire `initLucid()` — scroll listener toggles navbar solid state; hero load-in applied.
- [ ] CTA hover microinteraction confirmed (existing `--transition-fast` + hover token).
- [ ] Confirm exactly: 1 hero effect + 1 scroll effect + 1 microinteraction (no more).

### Group 5 — Quality checks + verification
- [ ] Run `node build-lab/tests/navbar-hero.test.js` — all green.
- [ ] Run `node --check build-lab/script.js` — clean.
- [ ] Manual visual check if a server is running (AGENTS.md URL rules).
- [ ] No console errors, no layout breakage at mobile width.

### Group 6 — Commit
- [ ] Commit staged changes with a clear message.
- [ ] Note any differences between implementation and specs for founder approval.