# Bold Style Website — Plan

**Order of operations**: start-to-finish, building a new spec from the ground up.

## Step 1 — Redefine the Brand Platform

- **Name**: Lucid (retained, but repositioned).
- **Tagline**: Refine "Find anything you've ever saved." to be more award-caliber — perhaps "Navigate the unseen." or "Find what you've lost, rediscovered."
- **Personality**: Confident, innovative, immersive — not "quiet library." The site should feel like a digital experience, not a brochure.
- **Portfolio/Case-study style** — treat the site like a award-caliber studio showcase, not a product showcase.

## Step 2 — Visual Design System (Awwwards‑Aligned)

- **Palette**: Deep dark mode foundation (#0a0a0f or similar), luminous accents (#0ea5e9, #f8fafc used sparingly as highlights). Avoid safe gradients; use intentional, distinctive color.
- **Typography**:
  - Fraunces variable font with `font-optical-sizing: auto` actively tuned.
  - Headlines: 60–80px range, letter‑tracked, expressive pairings.
  - Body: Inter or similar, but with generous line-height and scale.
  - Type becomes the primary visual element — large, strong types dominate.
- **Texture & Depth**:
  - Subtle SVG noise data‑URL layered behind sections (`::before`, opacity ~2%).
  - Optional: light glassmorphism/frosted glass effect on panels, but mature/moderated.
- **Visual hierarchy**:
  - Broken grids, asymmetric compositions.
  - Generous negative space used intentionally.
  - One signature moment with elevated production (the one unforgettable interaction).

## Step 3 — Motion & Interaction (Awwwards‑Aligned)

- **Scroll‑driven 3D narrative** (if committing to 3D):
  - Master timeline controlled by normalized scroll position (0 to 1).
  - Camera keyframes, material transitions, content reveals mapped to progress thresholds.
  - GSAP ScrollTrigger to decouple scroll position from animation playback.
  - Camera animation systems driving narrative progression through choreographed environments.
  - Each scroll increment advances the camera along a predefined path, revealing new content zones, triggering particle effects, or rotating the camera.
  - Easing curves and scroll‑velocity thresholds control pacing (fast scrolling → abbreviated transitions; slow scrolling → hidden details/Easter eggs).
- **If NOT using 3D**:
  - Directed motion: pinned scroll sequence, considered page transition, one signature moment.
  - Motion should mean something — guide the eye and pace the story.
  - Subtle micro‑interactions for depth, but within a strict motion budget.
- **Loading experience** — branded reveal (2‑second max), not a 6‑second progress bar.
- **Respect `prefers-reduced-motion`** — gate all decorative animation.

## Step 4 — Performance (Awwwards‑Aligned)

- **Performance budget** measured on a mid‑range phone weekly:
  - LCP < 1.5s (award target), industry average 2.5–4s.
  - CLS < 0.05 (award target), industry average 0.1–0.25.
  - INP < 100ms (award target), industry average 200–500ms.
  - Total page weight < 3MB (award target), industry average 5–10MB.
  - Animation FPS 60fps sustained (award target), industry average 30–45fps.
- **One signature moment** — the one interaction people screenshot — and protect the rest of the site's performance budget around it.
- **Mobile parity** — cap device pixel ratio, pause off‑screen WebGL, honor reduced‑motion.
- **Performance‑first mindset**: ship less JS, dynamic‑import heavy WebGL modules, stream the first view. Aim for sub‑3s LCP even with motion.

## Step 4 — Technology Stack

- **Three.js** (or **WebGPU** for next‑gen) for any 3D/immersive elements.
- **GSAP with ScrollTrigger** for scroll‑driven animations/transitions.
- **Modern framework** (Next.js / Nuxt / Astro) for performance if using 3D/heavy JS.
- **No template foundations** — custom code is the baseline.
- **Progressive enhancement**: functional HTML fallback for devices without GPU acceleration.

## Step 5 — Required Pages/Sections

1. **Hero** — scroll‑driven reveal, bold typography, signature moment. May include a 3D intro environment.
2. **Concept/About** — one clear concept sentence; brand story told concisely.
3. **Work/Showcase** — case‑study style entries with original copy and imagery.
4. **Feature/Highlight** — the signature moment (one unforgettable interaction).
5. **Contact/Footer** — functional, styled consistently with the bold aesthetic.

## Step 6 — Development Workflow

- **Weekly performance check** on a mid‑range phone (LCP, CLS, INP).
- **Dedicated polish week** before submission: 60fps verification, mobile parity, reduced‑motion gating, focus‑state audit, TTFB measurement.
- **Submit flawless live build early** in the 5‑day voting window; never deploy changes mid‑vote.
- **Code quality**: clean, commented, modular. Recognize WordPress/Webflow/AI templates immediately — this submission must be custom code.

## Step 7 — Submission & voting

- Live site approved → sent automatically to minimum 18 jurors.
- Scored independently across Design (40%), Usability (30%), Creativity (20%), Content (10%).
- Three extreme scores dropped automatically.
- Voting window ≈ 5 days.
- SOTD winner → sent to Developer jury; score > 7 earns Developer Award (technical excellence, accessibility, code quality).

---