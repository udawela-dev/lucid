# Bold Style Website — Validation

**How to evaluate the new spec against Awwwards 2026 criteria.**

## 1. Visual Design Checklist (40% of score)

- [ ] **Palette** is distinctive and intentional — not a safe gradient. Deep dark mode with luminous accents, or bold color choices that reject generic schemes.
- [ ] **Typography** is bold and confident:
    - Headlines are oversized (60–80px) with expressive pairings.
    - `font-optical-sizing: auto` is actively tuned via Fraunces `opsz` axis.
    - Body type is readable with generous scale.
    - No need not match, but the system has visual coherence.
- [ ] **Layout** uses asymmetric compositions, broken grids, generous negative space.
- [ ] **One signature moment** exists — one unforgettable interaction (pinned scroll, signature transition, one standout interaction). Not 20 effects.
- [ ] **Micro‑details** are present: hover states, transitions, spacing rhythm, cursor behaviors.
- [ ] **Consistency** holds across every page, not just the homepage.

## 2. Usability Checklist (30% of score)

- [ ] **Navigation clarity** — first-time visitor finds what they need in under 3 seconds.
- [ ] **Load performance** — LCP < 1.5s (award target), measured on a mid‑range phone.
- [ ] **Responsive design** — judged on mobile first. The site does NOT break on iPhone.
- [ ] **Accessibility**:
    - Color contrast per WCAG AA.
    - Keyboard navigation visible and functional.
    - Screen reader support (semantic markup).
    - `prefers-reduced-motion` gating on decorative animation.
- [ ] **Core Web Vitals**:
    - LCP < 1.5s (award target).
    - CLS < 0.05 (award target).
    - INP < 100ms (award target).
- [ ] **Total page weight** < 3MB (award target), measured on a mid‑range phone.
- [ ] **60fps sustained** animation on mid‑range devices.

## 3. Creativity Checklist (20% of score)

- [ ] **Concept** is one sentence that makes the art direction inevitable (not trend-chasing).
- [ ] **Signature moment** is present — one unforgettable interaction people screenshot.
- [ ] **Custom interaction patterns** — not derivative; original execution.
- [ ] **3D / WebGL / WebGPU** elements (if used) serve the concept and hold 60fps.
- [ ] **Sound design** (if used) reinforces brand identity and is not gratuitous.
- [ ] **Concept is original**, not the trend of the moment.

## 4. Content Checklist (10% of score)

- [ ] **Real copy** — no Lorem ipsum; genuine brand‑appropriate tone.
- [ ] **Original imagery** — no stock photography used as placeholder.
- [ ] **Brand‑appropriate tone** throughout.

## 5. Pass/Fail Threshold

- **Must pass**: Usability (30%) — if LCP > 3s or mobile breaks, the submission fails regardless of Design/Creativity scores.
- **Must pass**: Mobile parity — if the site breaks on iPhone, it fails immediately.
- **Total score**: Honorable Mention requires 6.5+ across all criteria; Site of the Day is the single highest‑scoring site.

---