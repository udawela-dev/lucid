# Feature Spec — Content Sections + Polished Feature Cards

**Date:** 2026-09-17
**Branch:** `feature/content-sections`
**Stage:** Roadmap Stage 5, Step 3 (content sections) + "one polished component + motion budget"

---

## Context

Stage 5 Steps 1–2 are merged into `main` (base shell + tokens, Navbar, Hero with motion).
The page still has placeholder/stub content sections: Problem, Solution, Features (empty),
Social Proof, and Footer. This feature builds those sections into finished, polished content
and adds **one polished UI component: the feature cards** with a subtle hover lift.

Constitution rules that apply (`build-lab/SPECS/TECH.md`, `build-lab/SPECS/MISSION.md`):

- No frameworks, no libraries, no npm packages — plain HTML, CSS, vanilla JS only (vanilla dependencies).
- Design tokens first: components use `var(--…)` only, never hardcoded hex/radius values.
- Motion budget: max **1 hero effect + 1 scroll effect + 1 microinteraction**.
  Decision (founder locked): the **feature-card hover lift is the polished microinteraction**;
  hero entrance stays as-is; navbar scroll effect stays as-is.
- Brand personality: private, calm, intelligent — quiet library, never loud.
- Inline SVG icons only (no emoji, no icon libraries).

---

## Scope (What this feature does)

1. **Problem section** — headline "You saved it. So why can't you find it?" + supporting copy
   from the approved architecture (Section 3 of MISSION.md). Calm, two-part message.
2. **Solution section** — headline "One search box. Everything you've saved." + copy on privacy
   and ease.
3. **Features section** — one polished component: **3 feature cards** (Private by design,
   Saved-in-one-place, Faster than digging — in that order, privacy first), each with an
   **inline SVG icon**, card styling using `--radius-lg` / `--color-surface` / shadow tokens,
   and a **hover lift effect** (`translateY(-4px)` with smooth transition).
4. **Social Proof** — one refined testimonial block (placeholder quote, replace later).
5. **Footer** — polished footer with wordmark, tagline, waitlist link, copyright.

## Non-Goals (Out of scope)

- Waitlist form submit behavior (JS + SQLite) — later feature.
- The CTA section content stays as-is (built in base shell) — only above sections change.
- Scroll-triggered reveals on these sections (would exceed the motion budget).
- Any additional hover effects beyond the feature cards + existing CTA transition.

## Decisions locked in by the founder (2026-09-17)

| Decision | Choice |
| :--- | :--- |
| Scope | All content sections: Problem, Solution, Features, Social Proof, Footer |
| Hero entrance | Keep existing load-in unchanged |
| Motion budget | Card hover lift = the 1 polished microinteraction |
| Card icons | Inline SVG (no emoji, no libraries) |
| Dependencies | Vanilla only — no npm packages or frameworks |

## Technical approach

- **HTML** (`index.html`): replace stub copy inside existing `<section id="problem">`,
  `<section id="solution">`, `<section id="features">`, `<section id="social-proof">`,
  and the `<footer>`. Add exactly three `.feature-card` elements with inline `<svg>` icons.
- **CSS** (`style.css`): add `.feature-card` styling using existing tokens (surface,
  `--radius-lg`, `--shadow-sm`, `--space-*`); add `.feature-card:hover` with
  `transform: translateY(-4px)` and `transition` using `--transition-fast` (or a calm
  `200ms ease`) — the single microinteraction. Style testimonial and footer using tokens.
- **JS** (`script.js`): no changes required (motion is pure CSS; existing wiring untouched).
  Tests must still pass unchanged.

## Testability

- HTML structure asserts: three `.feature-card`s, each containing an inline `<svg>`,
  section ids/headlines present, footer content present.
- CSS asserts: `.feature-card:hover` has `translateY(-4px)`; card uses `--radius-lg`;
  no hardcoded hex outside `:root`; no emoji characters in the HTML.
- Existing Navbar + Hero tests must still pass (regression).