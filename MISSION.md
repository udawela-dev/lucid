# Founder Notebook

Welcome to your Founder Notebook. This is the single source of truth for your startup project. As founder and lead decision-maker, use this file to define your concept, guide OpenCode, and track every important decision.

---

## Founder Decision (Official)

**Date:** 2026-09-17
**Status:** Approved — passes the 5-Point Filter at Category 1 or 2
**Refined by challenge step:** 2026-09-17

> **We are building Lucid, a privacy-first personal search tool for students and beginner programmers.**
>
> The problem: important information is scattered across bookmarks, screenshots, notes, messages, emails, files, and apps. People save things passively and later forget where they saved them, wasting 1–2 hours a week and sometimes missing deadlines.
>
> Our promise: **find a link you saved but lost.** The product starts with the most common loss — links and resources saved across bookmarks, screenshots, and messages — and finds them again from one search box.
>
> Our edge: existing tools only search inside one app each; we search across the places people actually save, and unlike big-company tools, our data stays on the user's device — no ads, no selling personal data.
>
> This project's deliverable is a **landing page** that tells this story and collects waitlist signups (saved with SQLite). The first user is me.

**Scope decisions locked in this round:**

| Decision | Locked choice |
| :--- | :--- |
| Hero promise | "Find a link you saved but lost" — the simplest useful version |
| First kind of saved thing | Links / resources saved as bookmarks, screenshots, or shares |
| Long-term vision (not hero) | Searching "everything" across all apps — future roadmap |
| Pricing | $5–10/mo stays in my head, NOT on the page (billing is out of scope) |
| Privacy | A core selling point: local-first, no ads, no selling data |

**5-Point Filter results:**

| Filter | Score | Why |
| :--- | :--- | :--- |
| User | ✅ | Specific: students & beginner programmers. I am the first user |
| Problem | ✅ | Quantified: 1–2 hrs/wk lost, 30+ min searches, missed deadlines |
| Value | ✅ | Clear now: one concrete case shown well (lost links found) |
| Feasibility | ✅ | Buildable: landing page + SQLite waitlist, within my skill level |
| Clarity | ✅ | Passes 20-second test: "find a link you saved but lost" |

---

## 1. Vision & Problem Discovery

*The foundation: Knowledge → Problem → Solution → Value → Product*

- **Domain / Industry:** Personal productivity / knowledge management for students and beginner programmers
- **Target Audience (Who is this for?):** Students and beginner programmers who juggle projects, notes, assignments, resources, and deadlines across many different apps, websites, emails, and files.
- **The Core Problem (What pain point are you solving?):** Important information is scattered across bookmarks, screenshots, notes, messages, emails, files, and apps. People save things passively and later forget where they saved them. Finding something again can take 30+ minutes, wastes 1–2 hours a week, and sometimes causes missed deadlines or giving up. The real pain is *finding later*, not organizing upfront.
- **Proposed Solution (current scope):** A privacy-first tool that finds **a link you saved but lost.** Links and resources saved across bookmarks, screenshots, and messages, found again from one search box.
- **Long-term vision (not promised on the page yet):** Searching "everything" — notes, files, emails, and more — no matter which app it lives in.
- **Value Proposition (Why choose this over existing alternatives?):** Existing tools only search inside themselves (bookmarks, notes, or files separately). This product searches across the places people actually save. And unlike big-company tools, it keeps your data on your device — no ads, no personal data used for advertising. 

---

## 2. Brand Identity & Design System

*Define the visual and emotional tone before generating code or copy.*

- **Company / Product Name:** Lucid — *"Find anything you've ever saved."*
- **Tagline:** "Find anything you've ever saved."
- **Brand Personality / Tone of Voice (e.g., Playful, Minimalist, Bold, Professional):** Private, calm, intelligent. The site should feel like a quiet, trustworthy library — never loud, never busy.
- **Color Palette (chosen: white + light blue — light theme):**
  - Background: `#FFFFFF`
  - Surface / Card: `#F8FAFC`
  - Primary: `#60A5FA` (hover `#3B82F6`)
  - Secondary: `#1E293B`
  - Accent: `#BFDBFE`
  - Text (Primary / Muted): `#1E293B` / `#64748B`
  - Border: `#CBD5E1`
- **Typography (chosen: "calm brain, clean voice"):**
  - Heading Font: Fraunces (serif, weight 600) — intelligent, editorial, calm
  - Body Font: Inter (sans-serif, weight 400) — clean, readable, modern
  - Both free on Google Fonts.
- **Button Styles:**
  - Primary: solid light blue `#60A5FA`, white text, radius `10px`, padding `0.75rem 1.5rem`, soft subtle shadow, hover `#3B82F6`, `150ms` smooth transition
  - Secondary: ghost — transparent, `1px` slate border, slate text, very light fill on hover
- **Border Radius Rules (design tokens):**
  - `--radius-sm` = `8px` — small elements (inputs, chips)
  - `--radius-md` = `10px` — buttons
  - `--radius-lg` = `16px` — cards
  - These become CSS variables in `style.css`; never hardcode radius values. 

---

## 3. Page Architecture

*Approved landing page outline for Lucid. Narrative flow: Navbar → Hero (with search demo) → Problem → Solution → How it works → Cross-source search → Privacy → Example results → Before vs Lucid → Who it's for → Features → Social Proof → Founder note → FAQ → CTA → Footer. (13 sections — the full recommended feature set.)*

### Navbar
- Brand with search-mark logo icon + wordmark: **Lucid**
- Links: Problem · Solution · Features · How it works · FAQ
- Right side: one solid button — **"Join the waitlist"** (links to `#cta`)

### 1. Hero
- **Headline (= tagline):** "Find anything you've ever saved."
- Subheadline: "Bookmarks, screenshots, and links you shared with yourself — Lucid finds what you lost, no matter which app it's buried in."
- CTA: the page's **one** primary action — solid blue **"Join the waitlist"** button.
- Visual: a clean search bar demo showing `"Python async tutorial"` → one forgotten link found, with source tags (Bookmarks · Screenshots · Messages).

### 2. Problem
- **Headline:** "You saved it. So why can't you find it?"
- "I know I saved it somewhere... — a bookmark here, a screenshot there, a link you messaged yourself."
- "So a 30-second search turns into 30 minutes of clicking through history, folders, and chats."

### 3. Solution
- **Headline:** "One search box. Everything you've saved."
- "Type what you remember — a topic, a word, a name — Lucid searches across the places you actually save."
- "Your data stays on your device. No ads. No selling your history."

### 4. How it works
- **Headline:** How Lucid works · 4 steps: Save → Forget → Search → Find
- 4-step process showing the user journey from saving links to finding them again.

### 5. Cross-source search
- **Headline:** "One search. Every place you save."
- 3 source cards: Bookmark · Screenshots · Messages — links found across all of them from one box.

### 6. Privacy-first
- **Headline:** "Private by design. No exceptions."
- Checklist panel: your data stays on your device · no ads, ever · your personal data is never sold.

### 7. Example results
- **Headline:** "See what you'll find"
- Realistic result cards showing title, source (Bookmarks/Screenshots/Messages), saved date, and link.

### 8. Before vs Lucid
- **Headline:** "Before vs Lucid"
- Two columns: searching 5 apps one by one vs one search box that checks everywhere at once.

### 9. Who it's for
- **Headline:** For **students** and **beginner programmers**
- Audience list: assignments/research, tutorials and code snippets, documentation and references, project resources.

### 10. Features *(3 calm cards — privacy leads)*
- **Headline:** Made simple on purpose.
- **Private by design** *(card 1):* everything stays on your device — no accounts built on your data.
- **Saved-in-one-place** *(card 2):* links from bookmarks, screenshots, and messages, searchable from one box.
- **Faster than digging** *(card 3):* finds what you remember in seconds, not 30 minutes of clicking around.

### 11. Social Proof
- **Headline:** "Built for people who save more than they find."
- Placeholder quote *(replace with a real testimonial later):* "I used to lose tutorials and references every week. Lucid found one I'd hunted for an hour."

### 12. Founder note
- **Headline:** "The first user is me."
- Personal note: why Lucid exists and that the founder loses links constantly too.

### 13. FAQ
- Accordion (details/summary): data privacy · what Lucid searches · availability · pricing.

### 14. CTA / Final Ask
- **Headline:** "Never lose another link."
- "Lucid is coming. Join the waitlist and be first to know."
- Name (optional) + email input + **"Join the waitlist"** button (saves to SQLite).
- Trust line about privacy.

### Footer
- **Bold wordmark:** **Lucid** · tagline · **bold** waitlist link · privacy note · contact/GitHub links · copyright. 

---

## 4. Decision Log

*Follow the cycle: Think → Ask → Evaluate → Decide → Build*

| Date | Topic / Area | Options Considered | Final Decision & Rationale | Status |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-17 | Core problem | Lost info vs sports aggregation vs universal organization | "Find everything you've saved" — it unifies all three pains, and I experience it daily myself | Done |
| 2026-09-17 | Target user | Students & beginner programmers vs all developers vs students in general | Students & beginner programmers — closest to my own life as first user | Done |
| 2026-09-17 | Core promise | "Search everything you've saved" vs "Never lose a link" vs "Whole digital life in one place" | "Search everything you've ever saved" — one search box, simplest to understand | Done |
| 2026-09-17 | Privacy | Local-first vs free-with-my-data | Local-first on my device — privacy is important to me, and I'd pay $5–10/mo for it | Done |
| 2026-09-17 | Scope refinement | Hero promise: "everything" vs "links saved but lost" | Narrowed to "find a link you saved but lost" — the simplest case the page can actually show; "everything" becomes long-term vision | Done |
| 2026-09-17 | Pricing on page | Show $5–10/mo vs keep offline | Kept OFF the page — billing is out of scope this project; price stays in my head | Done |
| 2026-09-17 | Brand personality | Playful vs Bold vs Private-calm-intelligent | Private, calm, intelligent — matches a privacy-focused product | Done |
| 2026-09-17 | Color palette | Night Study vs Soft Fog vs Library Green | Soft Fog — trust, calm, clean; privacy shown through copy and feel | Done |
| 2026-09-17 | Product name & tagline | Lucid vs Recall vs Stash | Lucid — "Find anything you've ever saved." Professional, calm, matches the promise; recall had privacy-brand risk | Done |
| 2026-09-17 | Hero headline | Original vs repeated tagline | Kept hero headline = tagline — visitors need the message twice to understand it | Done |
| 2026-09-17 | Feature ordering | Privacy first vs saved-in-one-place first | Privacy card first — privacy is the core differentiator, not storage | Done |
| 2026-09-17 | Page structure | Hero/Problem/Solution/Features/Social Proof/CTA | Approved 8-part outline (Navbar–Footer) with ONE primary CTA: Join the waitlist | Done |
| 2026-09-18 | Page structure | Hero/Problem/Solution/Features/Social Proof/CTA | Approved 8-part outline (Navbar–Footer) with ONE primary CTA: Join the waitlist | Done |
| 2026-09-18 | Waitlist feature | Static form vs Python+SQLite backend vs JS fetch | Python stdlib server with SQLite + fetch handler, inline success/duplicate messages, reconciled privacy copy | Done |
| 2026-09-18 | New sections added | How it works / Who it's for / Example results | Added three new sections per recommended feature set; all tests still pass | Done |
| 2026-09-18 | Footer redesign | Original footer vs bold-enhanced footer | Updated footer with bold text for brand emphasis; matches light theme | Done |
| 2026-09-18 | Theme | Dark "Midnight Professional" vs white + light blue | White background `#FFFFFF` with light blue `#60A5FA`/`#BFDBFE` accents — user chose light, professional look; replaces Soft Fog indigo and dark theme | Done |
| 2026-09-18 | Logo | Old indigo/cyan SVG vs light-blue search mark | New search-mark logo (circle + crosshair) with light-blue gradient, matching theme; favicon updated too | Done |
| 2026-09-18 | Full page structure | 8-part outline vs recommended 13-section feature set | Rebuilt index.html around the full 13-section set (cross-source, privacy, before-vs-lucid, founder note, FAQ added); all 50 tests still pass | Done |
| 2026-09-18 | Static serving bug | 404 on style.css/script.js vs serve all static files | Fixed server.py do_GET to serve any static file; page now renders styled | Done |
| 2026-09-18 | Waitlist fields | Email only vs Name + email | Added optional name field to form, JS fetch, and server INSERT; DB migrated with ALTER TABLE | Done |
| 2026-09-18 | Sign-in page | Not needed vs create signin.html | Created signin.html + POST /api/signin endpoint (email + password to SQLite) per user approval | Done |
| 2026-09-18 | Full 13-section page | 8-part vs recommended 13-section set | Rebuilt index.html around the full 13-section set (cross-source, privacy, before-vs-lucid, founder note, FAQ added); all 50 tests pass | Done |
| 2026-09-18 | Founder dashboard | No dashboard vs private watch area | Added /dashboard (login-protected) listing waitlist signups (name/email/date) with refresh, email-everyone button, and sign out; sessions stored in SQLite with HttpOnly cookie | Done |
| 2026-09-18 | Join notifications | No email vs notify founder on each join | Added SMTP notifications (email_config.py) — founder gets an email with the joiner's name/email on every new signup; gracefully skipped until credentials are set | Done |
| 2026-09-18 | Account creation | First sign-in auto-creates vs explicit sign-up page | Added dedicated /signup page + /api/signup endpoint (name, email, password) with duplicate-account guard; sign-in still auto-creates the founder account when the table is empty | Done |
| 2026-09-18 | Hero + section visuals | Plain mockups vs professional SVG images | Added assets/hero-app.svg (browser mockup), assets/sources.svg (cross-source diagram), assets/privacy.svg (shield) — inspired by the "Copywriter" WebWave template style, in the light-blue theme; external files keep no-hex rule in HTML | Done |
| 2026-09-18 | Welcome emails | No email vs welcome to new joiners | New waitlist joiners AND new account creators get an automatic "Welcome to Lucid" email; founder gets a "New Lucid waitlist signup" notification on every join | Done |
| 2026-09-18 | Waitlist delete | No removal vs delete button | Watch area now has a Delete button per row (signed-in only, confirm before removing) — POST /api/waitlist/delete by email | Done |
| 2026-09-18 | Outbox | Silent email failure vs visible outbox | Every generated email is saved to an `outbox` table and shown on the dashboard (recipient, subject, status, time) — no more silent "not configured" dead ends | Done |
| 2026-09-18 | Email setup UX | Edit config file vs on-site form | New /email-setup page (signed-in only): type Gmail + app password + notification address, press one button; server saves email_config.py and test-sends a real email immediately | Done |
| 2026-09-18 | Dashboard banner | None vs clear off-state | Dashboard shows a banner when no sender is configured, linking to the Connect page and the /email-help step-by-step guide | Done |
| 2026-09-18 | Email failure handling | Hang forever vs safe timeout | SMTP calls now time out after 10s and the server is threaded (ThreadingHTTPServer) so a slow email can never freeze the site | Done |
| 2026-09-18 | Server restart | Temp folder script vs in-repo script | Added start-server.py inside build-lab/ so the site can be restarted with one command if the box stops it | Done |

---

## 5. Notes & Prompts for OpenCode

*Use this section to draft prompt briefs, review feedback, and keep track of pending tasks.*

### Build Brief — Stage 5, Step 1: Base shell + design tokens

**Context:** Lucid is a privacy-first personal search tool for students and beginner programmers. Single-page landing site in `build-lab/`, plain HTML/CSS/vanilla JS. Branding and page architecture are locked in; HTML is a starter shell and `style.css` has placeholder tokens. This step is the foundation every later section builds on.

**Goal:** Fill `style.css` with the real Lucid tokens (Soft Fog palette, Fraunces + Inter, radius tokens); add one shared CTA button style (primary + secondary) as reusable classes; set up the page shell in `index.html` with semantic `main` + section placeholders per the approved architecture + Navbar/Footer stubs; load Google Fonts; apply base reset to new tokens.

**Constraints:** No frameworks/libraries/npm packages; no JavaScript yet (HTML/CSS only); one CTA only ("Join the waitlist"); no pricing; calm private intelligent tone; only design-token variables in component CSS (never hardcode colors/radius); keep three-file structure; all design values trace to Section 2.

**Design:** Palette Soft Fog — Background `#F8FAFC` · Surface `#FFFFFF` · Primary `#4F46E5` · Secondary `#1E293B` · Accent `#0EA5E9` · Text `#0F172A` / Muted `#64748B`. Typography: Fraunces (600) headings + Inter (400) body via Google Fonts. Radius: `--radius-sm 8px` / `--radius-md 10px` / `--radius-lg 16px`. Primary button: solid `#4F46E5`, white text, `10px` radius, padding `0.75rem 1.5rem`, soft subtle shadow, hover `#4338CA`, `150ms` transition. Secondary button: ghost (transparent, `1px` slate border, slate text, light fill on hover). Page order: Navbar → Hero → Problem → Solution → Features → Social Proof → CTA → Footer.

**Validation:** `index.html` opens clean and calm; no raw hex colors in component CSS (only `var(--…)`); `:root` matches Soft Fog exactly; Fraunces + Inter apply; one conversion action only — "Join the waitlist" (may appear as links to the same waitlist, but there are no other CTAs like "Buy now" or "Learn more"); no console errors; design values trace to `MISSION.md`.

---

- [x] Define core problem statement and audience
- [x] Select core promise: "Find a link you saved but lost"
- [x] Decide privacy approach: local-first, no ads
- [x] Scope refinement: narrowed to the simplest useful version
- [x] Choose company/product name (Lucid)
- [x] Select tagline ("Find anything you've ever saved.")
- [x] Select color palette (Soft Fog)
- [x] Select typography (Fraunces + Inter)
- [x] Define button styles and border radius rules
- [x] Approve landing page outline (Page Architecture section)
- [x] Draft website copy for hero section
- [ ] Build responsive hero and navigation components (original spec)
- [ ] Implement feature showcase sections (original spec)
- [x] Add interactive elements and conversion forms (waitlist implemented)
- [x] Add new sections: How it works, Who it's for, Example results
- [x] Add remaining sections: Cross-source search, Privacy-first, Before vs Lucid, Founder note, FAQ (full 13-section page)
- [x] Footer redesign with bold text
- [x] Fixed static file serving (style.css/script.css 200)
- [x] Added optional name field to waitlist (form + server + DB migration)
- [x] Sign-up page for anyone (name, email, password) with duplicate guard
- [x] Founder dashboard: sign-in/sign-out, waitlist table, refresh, count
- [x] Delete button for waitlist rows (signed-in only)
- [x] Outbox: every generated email saved and visible on the dashboard
- [x] Outbox delete button (signed-in only)
- [x] Connect-your-email page (/email-setup) with instant test email
- [x] SMTP timeout + threaded server (site can never freeze on email)
- [ ] Final visual polish and responsive testing (original spec polish complete)
- [ ] ———
- [ ] Pivot to bold/award-caliber design spec (SPECS/2026-09-18-bold-style) — new brand platform, motion system, and feature set under exploration
- [ ] Define bold brand platform (personality, palette beyond Soft Fog, typography upgrade)
- [ ] Plan motion system (scroll-driven 3D narrative or directed micro-interactions)
- [ ] Prototype performance budget (LCP < 1.5s, CLS < 0.05, INP < 100ms on mid‑range phone)
- [ ] Select technology stack (Three.js / GSAP / WebGPU consideration)
- [ ] Plan required pages (Hero, Concept, Work/Showcase, Feature/Highlight, Contact)
- [ ] Explore Awwwards 2026 criteria alignment (Design 40%, Usability 30%, Creativity 20%, Content 10%)
