# Bold Style Website — Requirements

**Feature:** Redeclare the Lucid brand with a bold, award-caliber website style inspired by Awwwards 2026 trends.

**User type:** Design-aware visitors who expect modern, immersive web experiences.

## 1. Visual Design Language (Awwwards-Aligned)

- **Brand personality**: Confident, innovative, immersive — the site should feel like a digital experience, not a brochure.
- **Color palette**: Reject safe, generic schemes. Use a distinctive, intentional palette with high-contrast typography. Deep dark modes with luminous accents are dominant in 2026 award galleries.
- **Typography**: 
  - Bold, confident typography often anchors the visual system.
  - Oversized headlines and expressive type pairings set immediate tone.
  - Large, strong types dominate — typography becomes a design element itself.
  - Some websites have animated typography that moves while scrolling; others use layered text compositions generating rhythm and energy.
  - Fraunces (variable optical size) for headlines, Inter for body — but with `font-optical-sizing: auto` actively tuned.
- **Layout**:
  - Generous negative space; layouts are asymmetric; grids are broken strategically.
  - No fixed galleries; discover patterns closer to social-media infinite scroll.
  - One-column foundation (mobile first), then progressive enhancement.

## 2. Motion & Interaction (Awwwards Aligned)

- **Motion design expresses the brand's personality now** — every animation, transition, hover effect, and scroll movement has emotional meaning.
- **Motion types**:
  - Slow + graceful → luxury sensation.
  - Crisp, aggressive → invention and speed sensation.
- **Scroll-driven narratives** — the primary input device is scroll position; 3D camera movement is the storytelling medium.
- **Signature moment** — one unforgettable interaction (not 20 effects). Typical: pinned scroll sequence, considered page transition, one signature moment.
- **Motion should mean something** — directed animation that guides the eye and paces the story.
- **Loading experience** — branded reveal that sets tone (2-second max), not a 6-second progress bar penalty.
- **Respect reduced motion** — gate decorative animation behind user preference.
- **Interactivity staples**:
  - Scroll-triggered animations revealing content at the right pace.
  - Cursor effects, parallax elements, custom hover states.
  - Micro-interactions for depth and engagement (but not gimmicky).
- **3D & WebGL** (optional but favored):
  - WebGL + Three.js + GSAP ScrollTrigger for timeline control.
  - Custom post-processing passes for visual tone.
  - Progressive enhancement: functional HTML fallback for low-power devices.
  - GPU performance budgets matter — 60fps sustained on mid-range hardware.
- **Sound design** (optional but trending):
  - Micro-sounds for interactions and feedback.
  - Ambient audio to reinforce brand identity.
  - Sound cues for navigation and transitions.
  - Must balance creativity with usability.

## 3. Performance & Technical (Awwwards Aligned)

- **Performance is a judging criterion**, not just a technical nice-to-have — Core Web Vitals directly affect usability scores.
- **Performance targets**:
  - LCP < 1.5s (award winners), industry average 2.5–4s.
  - CLS < 0.05 (award winners), industry average 0.1–0.25.
  - INP < 100ms (award winners), industry average 200–500ms.
  - Total page weight < 3MB (award winners), industry average 5–10MB.
  - Animation FPS 60fps sustained (award winners), industry average 30–45fps.
- **One signature moment** — not 20 effects; one unforgettable one.
- **Performance under pressure** — complex visuals that load fast and run smooth on mid-range devices, not just MacBook Pros.
- **Mobile parity** — mobile experience is considered, not just responsive. Touch interactions replace hover states intentionally.
- **One-column foundation** (mobile first), then progressive enhancement.
- **No performance neglect** — beautiful sites that take 5+ seconds to load fail the usability criterion (30% of Awwwards score).
- **No inconsistent design systems** — every page must feel part of the same system.

## 4. Content & Usability (Awwwards Aligned)

- **Real content** — genuine photography, original copy, brand-appropriate tone. No stock imagery.
- **Navigation clarity** — first-time visitor finds what they need in under 3 seconds.
- **Load performance** — sub-3-second load target.
- **Responsive design** — judged on mobile first. A desktop masterpiece that breaks on iPhone loses immediately.
- **Accessibility**:
  - Color contrast per WCAG AA.
  - Keyboard navigation.
  - Screen reader support.
  - Reduced motion preference gating.
- **Content quality**:
  - Real copy, real case studies, real imagery.
  - No Lorem ipsum energy.
  - Brand-appropriate tone.
- **Usability features**:
  - Navigation clarity — under 3 seconds to find what's needed.
  - Focus states visible and designed, not just browser default.
  - Reduced motion preference honored.
  - Custom cursor doesn't hide the real one.

## 5. Technology Stack (Awwwards Aligned)

- **Three.js** — dominant 3D library behind recent Awwwards/FWA winners. Enables custom 3D environments, particle systems, shader effects, generative visuals.
- **WebGPU** — successor to WebGL, supported in Chrome, Edge, Safari. Better performance for complex 3D scenes, compute-heavy effects, real-time rendering.
- **GSAP (GreenSock Animation Platform) with ScrollTrigger** — industry standard for scroll-driven animations and transitions. Award winners use scroll as a storytelling mechanism.
- **Modern frameworks** (optional but common): Next.js, Nuxt, Astro for performance.
- **No template foundations** — judges recognize WordPress themes, Webflow templates, AI-generated layouts immediately. Custom code is the baseline, not the differentiator.

## 6. Judging Criteria Alignment (Awwwards)

| Criterion | Weight | Focus Areas |
|-----------|--------|-------------|
| **Design** | 40% | Visual hierarchy, typography, color palette, micro-details (hover states, transitions, spacing rhythm, cursor behaviors), consistency across pages |
| **Usability** | 30% | Navigation clarity (under 3s), load performance (sub-3s LCP), responsive design (mobile first), accessibility (color contrast, keyboard nav, screen reader support), Core Web Vitals (LCP, CLS, INP) |
| **Creativity** | 20% | Custom interaction patterns, 3D/immersive elements, sound design, concept-driven design (not derivative), originality of execution |
| **Content** | 10% | Quality and relevance of work shown, real copy, original imagery, brand-appropriate tone |

**Key success factors judges emphasize**:
- One sentence concept that makes art direction inevitable (not trend-chasing).
- Design the signature moment and protect the rest of the site's performance budget around it.
- Build with a performance budget, not an afterthought. Measure on a real mid-range phone weekly.
- Reserve a dedicated polish week for 60fps, mobile parity, reduced motion, focus states, and TTFB.
- Submit a flawless, live production build early in the voting window.
- **Never**: Poor usability/performance (over-invest in visual creativity while neglecting load times/mobile), derivative concepts, no memorable moment, broken mobile, performance neglect, inconsistent design systems.

## 6. Required Pages/Sections

1. **Hero** — scroll-driven reveal, bold typography, signature moment.
2. **About/Concept** — one clear concept sentence; brand story.
2. **Work/Projects** — case study format with original copy/imagery.
3. **Feature/Highlight section** — one standout interaction (the signature moment).
4. **Contact/Footer** — functional, styled consistently.

## 7. Prohibited (will cause point deductions)

- Template foundations (WordPress themes, Webflow templates, AI-generated layouts recognized immediately).
- Mobile afterthoughts (desktop-first with bolted-on responsive breakpoints).
- Performance neglect (5+ second load times).
- Inconsistent design systems (homepage polished, inner pages different).
- No memorable moment (technically competent but forgettable).
- Poor usability/performance neglect (the #1 reasons submissions fail).
- Random effects (everything floats/parallaxes/reveals so nothing matters).
- Jank (WebGL hero dropping to 20fps reads as broken).
- Broken mobile (desktop masterpiece with collapsed phone layout).
- Random effects with no hierarchy.
- Derivative concepts (borrowing the trend of the moment).

---