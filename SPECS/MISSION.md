# Mission

## What is this project?

This is your startup project. You are building a real, public-facing website for a product or service you believe in.

By the end, you will have:
- A clear problem you are solving and a specific audience you are helping
- A visual brand identity (colors, fonts, style)
- A live landing page that communicates your value to real visitors

---

## Fill This In (Your Startup's Mission)

**Startup Name:**
> **Lucid** — "Find anything you've ever saved."

**The Problem:**
> Important information is scattered across bookmarks, screenshots, notes, messages, emails, files, and apps. People save things passively and later forget where they saved them. Finding something again can take 30+ minutes, wastes 1–2 hours a week, and sometimes causes missed deadlines or giving up. The real pain is *finding later*, not organizing upfront.

**Target Audience:**
> Students and beginner programmers who juggle projects, notes, assignments, resources, and deadlines across many different apps, websites, emails, and files.

**Your Solution:**
> A privacy-first tool that finds **a link you saved but lost** — links and resources saved across bookmarks, screenshots, and messages, found again from one search box. Data stays on your device. (Long-term vision: searching everything across all apps.)

**Value Proposition (one sentence):**
> *"We help students and beginner programmers who can't find links they've saved across bookmarks, screenshots, and messages by providing one private search box that finds any of them instantly, helping them stop wasting hours digging through scattered places."*

---

## Design System

- **Brand personality:** Private, calm, intelligent — like a quiet, trustworthy library.
- **Palette ("Soft Fog"):** Background `#F8FAFC` · Surface `#FFFFFF` · Primary `#4F46E5` · Secondary `#1E293B` · Accent `#0EA5E9` · Text `#0F172A` / Muted `#64748B`
- **Typography:** Fraunces (headings) + Inter (body) — free on Google Fonts.
- **Buttons:** Primary = solid indigo, white text, `10px` radius, soft shadow, hover `#4338CA`. Secondary = ghost (transparent, `1px` slate border).
- **Radius tokens:** `--radius-sm 8px` · `--radius-md 10px` · `--radius-lg 16px`

---

## Non-Negotiables

- The product must be explainable in 20 seconds or less.
- The landing page must have one clear Call to Action (CTA) — not two, not three.
- Every design decision must trace back to your brand personality words.
- OpenCode is your junior engineer. You are the founder. You make the decisions.

---

## Page Architecture (approved)

Narrative flow: **Navbar → Hero → Problem → Solution → Features → Social Proof → CTA → Footer**

| Section | Headline | Content |
| :--- | :--- | :--- |
| Navbar | — | Wordmark **Lucid** · links (Problem, Solution, Features) · one "Join the waitlist" button |
| 1. Hero | "Find anything you've ever saved." | Sub: "Bookmarks, screenshots, and links you shared with yourself — Lucid finds what you lost, no matter which app it's buried in." CTA: **Join the waitlist** · visual: search bar mockup that finds one forgotten link |
| 2. Problem | "You saved it. So why can't you find it?" | Saved links scattered across five apps · "A 30-second search becomes 30 minutes. Sometimes you give up and search it all over again." |
| 3. Solution | "One search box. Everything you've saved." | "Type what you remember — a topic, a word, a name — Lucid searches across the places you actually save." + data stays on your device line |
| 4. Features | "Made simple on purpose." | 3 cards, privacy first: Private by design · Saved-in-one-place · Faster than digging |
| 5. Social Proof | "Built for people who save more than they find." | One placeholder testimonial (replace with real one later) |
| 6. CTA | "Never lose another link." | Waitlist email input + "Join the waitlist" (SQLite) · trust line: "Private by design" |

**One CTA only:** "Join the waitlist." No pricing on the page.

---

## Out of Scope

- No user login systems or dashboards for this project.
- No payment processing.
- No backend APIs or databases — this is a frontend landing page.
- No React, Vue, or other JavaScript frameworks.
