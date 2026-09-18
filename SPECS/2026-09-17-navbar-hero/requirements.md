# Feature Spec — Navbar + Hero (Lucid Landing Page)

**Date:** 2026-09-17
**Branch:** `feature/navbar-hero`
**Stage:** Roadmap Stage 5, Step 2 (Navbar and Hero section, with motion budget)

---

## Context

Roadmap Stage 5, Step 1 (base shell + design tokens in `index.html` and `style.css`) is complete.
This feature builds the **Navbar** and **Hero** sections with the professional polish and motion
that the page architecture (MISSION.md Section 3) describes. Content sections (Problem, Solution,
Features, Social Proof, CTA, Footer) remain stubs and are covered by later feature specs.

Constitution rules that apply (from `build-lab/SPECS/TECH.md` and `MISSION.md`):

- No frameworks, no libraries, no npm packages — plain HTML, CSS, vanilla JS only.
- Design tokens first: components use `var(--…)` only, never hardcoded hex colors or radius values.
- Motion budget: maximum **1 hero effect + 1 scroll effect + 1 microinteraction**.
- One CTA only: "Join the waitlist" (same action everywhere — no competing CTAs).
- Brand personality: private, calm, intelligent.

---

## Scope (What this feature does)

1. **Navbar** — brand wordmark "Lucid", links (Problem · Solution · Features), one
   "Join the waitlist" button linking to `#cta`. Becomes solid/blurred when the page
   is scrolled (the 1 scroll effect).
2. **Hero** — headline (tagline): "Find anything you've ever saved." Subheadline as per
   architecture. One primary CTA button. A search-bar mockup visual (what you type reveals
   one "found" link). Headline loads in with a calm fade/slide (the 1 hero effect).
3. **CTA button microinteraction** — the 1 hover microinteraction (already partly defined in
   tokens: `--transition-fast`, hover color `--color-primary-hover`).

## Non-Goals (Out of scope for this feature)

- Content sections (Problem, Solution, Features, Social Proof, CTA form, Footer).
- The waitlist form behavior (JavaScript submit + SQLite) — later feature.
- Scroll-triggered reveals for other sections — later feature.
- Any second hero effect or second scroll effect (motion budget is exactly 1 + 1 + 1).

## Decisions locked in by the founder (2026-09-17)

| Decision | Choice |
| :--- | :--- |
| Feature scope | Navbar + Hero only |
| Motion package | Load-in hero + solid-on-scroll navbar + CTA hover microinteraction |
| Testing | Plain Node test scripts (no npm packages), red/green TDD |
| Git | Repo initialized; work on `feature/navbar-hero` branch |

## Technical approach

- **HTML** (`index.html`): Navbar `<header class="navbar">` and `<section id="hero">` are already
  present as stubs — enhance them (hero search-bar mockup markup, aria-labels).
- **CSS** (`style.css`): add `@keyframes` for the hero load-in, `.navbar` scrolled state,
  and hero search-mockup styling. Uses existing design tokens only.
- **JS** (`script.js`): pure, testable functions:
  - `shouldSolidifyNavbar(scrollY)` → returns `true` when `scrollY > 8` (navbar becomes solid).
  - `getHeroRevealClass()` → the class name applied to the hero for the load-in animation.
  - `initLucid()` → wires up the scroll listener and hero load-in via `requestAnimationFrame`/
    `IntersectionObserver` (whichever is simpler), plus the CTA hover state is pure CSS.
  - Business logic stays separate from DOM wiring so it can be unit-tested in Node.

## Testability

`script.js` keeps pure decision functions that return values (no DOM access), so plain Node
`assert` scripts can `require`/`eval` them and run red/green checks without a browser.
HTML/CSS are verified by reading the files and asserting required structure, tokens, and
keyframe/state rules.