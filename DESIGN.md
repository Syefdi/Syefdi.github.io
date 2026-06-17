---
name: Syefdi Portfolio
description: Precise, modern portfolio with terminal-inspired precision and Apple-grade restraint
colors:
  sky-blue: "#0ea5e9"
  sky-light: "#e0f2fe"
  sky-dark: "#0284c7"
  sky-bright: "#38bdf8"
  purple-accent: "#8b5cf6"
  purple-light: "#a78bfa"
  amber-accent: "#f59e0b"
  amber-light: "#fbbf24"
  amber-warm: "#fef3c7"
  amber-deep: "#92400e"
  neutral-bg-light: "#fafafa"
  neutral-surface-light: "#ffffff"
  neutral-text-dark: "#0f172a"
  neutral-text-mid: "#334155"
  neutral-text-dim: "#94a3b8"
  neutral-border-light: "#e2e8f0"
  neutral-bg-dark: "#0f172a"
  neutral-surface-dark: "#1e293b"
  neutral-text-light: "#f1f5f9"
  neutral-text-slate: "#cbd5e1"
  neutral-text-muted: "#64748b"
  neutral-border-dark: "#334155"
typography:
  display:
    fontFamily: "Plus Jakarta Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 5vw, 4rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "normal"
  headline:
    fontFamily: "Plus Jakarta Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "2.25rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "normal"
  title:
    fontFamily: "Plus Jakarta Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "normal"
  body:
    fontFamily: "Plus Jakarta Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
  label:
    fontFamily: "Fira Code, SF Mono, Monaco, Courier, monospace"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.1em"
rounded:
  pill: "9999px"
  card: "12px"
  button: "6px"
  input: "8px"
  none: "0"
spacing:
  xs: "0.25rem"
  sm: "0.5rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  2xl: "2.5rem"
  3xl: "4rem"
  section: "6rem"
components:
  button-primary:
    backgroundColor: "{colors.sky-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.button}"
    padding: "0.5rem 1.25rem"
  button-primary-hover:
    backgroundColor: "{colors.sky-dark}"
    textColor: "#ffffff"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.sky-blue}"
    rounded: "{rounded.button}"
    padding: "0.5rem 1.25rem"
  card:
    backgroundColor: "{colors.neutral-surface-light}"
    rounded: "{rounded.card}"
    padding: "2rem"
  badge-pill:
    backgroundColor: "{colors.sky-light}"
    textColor: "{colors.sky-dark}"
    rounded: "{rounded.pill}"
    padding: "0.25rem 0.75rem"
---

# Design System: Syefdi Portfolio

## 1. Overview

**Creative North Star: "The Terminal Precision Aesthetic"**

This portfolio embodies the intersection of command-line precision and Apple's restrained visual refinement. Every element serves evaluation: the fixed sidebar navigation mirrors macOS app structure, the dual interface (visual + terminal) demonstrates technical versatility, and the restrained sky blue accent against neutral grays signals professionalism without corporate blandness.

The design philosophy follows Apple Human Interface Guidelines: intentional whitespace, subtle interactive feedback (cursor spotlight, smooth lift on hover), and a semantic hierarchy that guides rather than shouts. The terminal mode isn't decoration; it's a fully functional alternate interface with tab autocomplete, command history, and typing animation that feels real. Both interfaces are first-class citizens, reflecting the duality of modern development: visual polish meets command-line confidence.

Dark and light themes are equally refined, not an afterthought. The color palette is committed but not aggressive: sky blue as primary (30-40% surface presence), purple and amber as supporting roles for categorization (project badges, learning tags). The result feels technical and modern without falling into "hacker aesthetic" clichés or over-engineered spectacle.

**Key Characteristics:**
- Precision over decoration: every element earns its place through function
- Dual-interface fluency: visual polish and terminal competency as equal expressions
- Restrained color: sky blue primary, purple and amber accents, nothing more
- Apple-grade interactivity: subtle hover lifts, cursor spotlight, smooth 300ms transitions
- System thinking: consistent spacing scale, semantic token names, reusable component patterns

## 2. Colors: The Technical Sky Palette

The palette centers on sky blue as the single voice of interaction, supported by purple for categorization and amber for learning/progress states. Neutrals are true grays (no warm tint) to maintain technical precision.

### Primary
- **Sky Blue** (#0ea5e9 / oklch(68% 0.17 230)): Primary accent used for links, active nav states, role headings, timeline markers, and hover states. Carries 30-40% of interactive surface. Its brightness signals clarity and approachability without playfulness.
- **Sky Light** (#e0f2fe): Tinted background for badges, status pills, and accent-light hover states. Provides visual hierarchy without adding new hues.
- **Sky Dark** (#0284c7): Hover and pressed states for primary buttons and links. Darkens the primary by one step for tactile feedback.
- **Sky Bright** (#38bdf8): Dark mode primary accent. Lightens from base sky blue for sufficient contrast against dark backgrounds.

### Secondary
- **Purple Accent** (#8b5cf6 / #a78bfa in dark): Project badge color for "Dev" role category. Secondary voice for skill differentiation, never used for primary interaction.
- **Amber Accent** (#f59e0b / #fbbf24 in dark): Project badge for "Build" role and learning tag backgrounds. Signals work-in-progress or educational context.

### Neutral
- **Light Mode Backgrounds**: #fafafa (body), #ffffff (cards/sidebar), #e2e8f0 (borders)
- **Light Mode Text**: #0f172a (primary), #334155 (secondary), #94a3b8 (dim/metadata)
- **Dark Mode Backgrounds**: #0f172a (body), #1e293b (cards/sidebar), #334155 (borders)
- **Dark Mode Text**: #f1f5f9 (primary), #cbd5e1 (secondary), #64748b (dim/metadata)

### Named Rules
**The One Voice Rule.** Sky blue is the only interactive color. Purple and amber exist for categorization, never for buttons or links. Their restraint preserves the primary's signal.

**The True Gray Rule.** Neutrals have no warm or cool tint. Technical work requires neutral judgment; tinted grays introduce unintended mood.

## 3. Typography

**Display Font:** Plus Jakarta Sans (with -apple-system, BlinkMacSystemFont fallback)  
**Body Font:** Plus Jakarta Sans (same stack)  
**Mono Font:** Fira Code (with SF Mono, Monaco, Courier fallback)

**Character:** A single humanist sans (Plus Jakarta Sans) carries the entire typographic hierarchy from hero headlines to body text, ensuring visual consistency without the distraction of contrasting font pairings. Fira Code enters only for metadata, timestamps, code snippets, and terminal UI, signaling technical context without overwhelming the page.

### Hierarchy
- **Display** (800 weight, clamp(2.5rem, 5vw, 4rem), 1.1 line-height): Hero greeting only ("Hi, I'm Syefdi"). Large, confident, but capped to avoid shouting.
- **Headline** (700 weight, 2.25rem, 1.2 line-height): Section titles ("Experience", "Projects"). Clear hierarchy without excessive scale.
- **Title** (700 weight, 1.5rem, 1.3 line-height): Card headings (project names, company names, certifications). Strong enough to scan, restrained enough to nest.
- **Body** (400 weight, 1.05rem, 1.7 line-height): Paragraph text throughout. Slightly larger than browser default (1rem) for comfortable reading. Max line length observed at ~65-75ch via content-wrapper (900px max-width).
- **Label** (500 weight, 0.75rem, 0.1em letter-spacing, uppercase): Section labels ("ABOUT", "SKILLS"), metadata (dates, status), and badge text. Fira Code for technical feel. Always uppercase with tracked spacing.

### Named Rules
**The Single Family Rule.** One humanist sans for all display and body text. Contrast comes from weight and size, not typeface switching. Mono font (Fira Code) enters only for technical signals: timestamps, commands, code, metadata.

**The No Cramp Rule.** Display headings use -0.02em max letter-spacing. Anything tighter causes character collision. Humanist sans at large sizes needs breathing room.

## 4. Elevation

This system uses subtle lift-on-hover rather than heavy ambient shadows. Surfaces are flat at rest; elevation appears as response to interaction.

### Shadow Vocabulary
- **Shadow SM** (`0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)`): Cards and containers at rest. Barely perceptible, just enough to separate from background.
- **Shadow MD** (`0 4px 16px rgba(0,0,0,0.08)`): Hover state for cards and interactive elements. Noticeable lift without drama.
- **Shadow LG** (`0 10px 40px rgba(0,0,0,0.10)`): Deep hover for project cards and major interactive surfaces. Reserved for elements that demand attention on interaction.
- **Dark Mode Shadows**: Same structure but higher opacity (0.3 / 0.4 / 0.5 for SM / MD / LG). Dark backgrounds require stronger shadows for perceptible depth.

### Named Rules
**The Flat Default Rule.** All surfaces are flat at rest (shadow-sm or none). Shadows strengthen only as response to hover or focus. Ambient elevation is minimal; interactive elevation is clear.

**The Lift-on-Hover Rule.** Hover states combine `transform: translateY(-2px to -4px)` with shadow upgrade (SM → MD, MD → LG). The physical lift reinforces clickability without needing color change.

## 5. Components

### Buttons
- **Shape:** Gently curved (6px radius)
- **Primary:** Sky blue background (#0ea5e9), white text, 0.5rem vertical × 1.25rem horizontal padding. Fira Code font at 0.8rem for technical feel. Border: 1px solid sky blue.
- **Hover:** Background darkens to sky-dark (#0284c7), button lifts with `translateY(-1px)` and shadow deepens. Transition: 200ms ease.
- **Ghost:** Transparent background, sky blue text and border. On hover, fills with sky blue background and white text (full inversion). Same 200ms transition.

### Badges & Pills
- **Pill Shape:** Fully rounded (border-radius: 9999px)
- **Project Badge (QA):** Sky light background (#e0f2fe), sky dark text (#0284c7). 6px radius (slightly softer than full pill). 0.3rem × 0.75rem padding. Fira Code uppercase at 0.75rem.
- **Project Badge (Dev):** Purple light background, purple text. Same structure.
- **Project Badge (Build):** Amber warm background, amber deep text. Same structure.
- **Learning Tag:** Amber warm background (#fef3c7), amber deep text (#92400e), full pill radius, 1px border in lighter amber (#fde68a). Fira Code 0.8rem.
- **Status Pill (Availability):** Sky light background, full pill radius, contains green pulsing dot (6px diameter, `@keyframes pulse` at 2s). Fira Code 0.75rem for text.

### Cards
- **Corner Style:** 12px radius (card standard)
- **Background:** Neutral surface (white in light, #1e293b in dark)
- **Border:** 1px solid neutral border (#e2e8f0 light, #334155 dark)
- **Shadow Strategy:** Starts at shadow-sm, upgrades to shadow-md on hover
- **Hover:** `transform: translateY(-4px)` + shadow-md + border color shifts to sky blue. Transition: 300ms ease for all properties.
- **Internal Padding:** 2rem standard for project cards and education cards, 1.5rem for certification cards

### Timeline (Experience)
- **Vertical Line:** 2px width, sky blue, positioned absolutely at left edge
- **Timeline Dots:** 10px circles, sky blue fill, 2px border in bg-primary color (creates ring effect), positioned on the line
- **Content Padding:** 2rem left to clear the line and dots
- **Bullet Points:** Custom `▹` chevron character in sky blue, positioned absolutely 1.5rem from left

### Navigation (Sidebar)
- **Nav Links:** Text-secondary at rest, sky blue on hover/active. Each link has an animated line prefix that extends from 20px to 40px on hover (2px height, transitions from border color to sky blue). Font: 0.95rem, weight 500. Transition: 300ms for color and line width.
- **Active State:** Link text turns sky blue, prefix line reaches 40px and turns sky blue.
- **Mobile:** Hamburger menu (three stacked 20px lines, 2px height, 4px gap), opens full-screen overlay with same nav links styled identically.

### Inputs (Terminal)
- **Style:** Dark background in both themes (mimics terminal surface), monospace font (Fira Code), sky blue prompt symbol (`>`), white/light text for input.
- **Focus:** Border glows with sky blue, no background change (terminal stays dark).
- **Cursor:** Blinking 2px vertical line in sky blue, positioned after input text.

## 6. Do's and Don'ts

Concrete guardrails to enforce the portfolio's strategic positioning and prevent design drift.

### Do:
- **Do** use sky blue (#0ea5e9) as the single interactive color. Purple and amber exist only for categorization badges.
- **Do** apply lift-on-hover (translateY -2px to -4px) combined with shadow upgrade for all interactive cards and buttons. Physical elevation reinforces clickability.
- **Do** use Fira Code exclusively for metadata, timestamps, commands, status labels, and badges. Plus Jakarta Sans handles all other text.
- **Do** keep borders at 1px maximum. The only exception is focus rings (2px for visibility).
- **Do** maintain 12px card radius and 6px button radius consistently. The 2:1 ratio is deliberate.
- **Do** respect the spacing scale (0.5rem / 1rem / 1.5rem / 2rem / 2.5rem steps). Arbitrary pixel values break rhythm.
- **Do** ensure both light and dark themes receive equal attention. Dark mode isn't an afterthought; it's a first-class interface.

### Don't:
- **Don't** use gradient text, gradient backgrounds, or glassmorphism as default patterns. The cursor spotlight effect is the only atmospheric element; everything else stays flat and precise.
- **Don't** add playful illustrations, cartoon avatars, or decorative graphics. This is a technical professional showcase, not a creative agency portfolio.
- **Don't** mimic LinkedIn's generic corporate templates (stock photo hero, buzzword bios, sameness). This portfolio demonstrates system thinking through its own design.
- **Don't** add 3D WebGL scenes, particle systems, or scroll-jacking animations. Technical skill is demonstrated through the system built (dual interface, clean separation of concerns, accessibility), not through visual pyrotechnics.
- **Don't** use multiple accent colors for interactive elements. Purple and amber categorize; sky blue interacts. Mixing roles creates visual noise.
- **Don't** apply shadows heavier than shadow-lg. The system is restrained, not dramatic. Heavy shadows read as 2014-era skeuomorphism.
- **Don't** nest cards inside cards. Single-level containment only.
- **Don't** use arbitrary z-index values (999, 9999). The system has a semantic scale: sidebar (100), scroll progress (9999), mobile overlay (101).
- **Don't** make the display heading larger than clamp(2.5rem, 5vw, 4rem). Above that scale, the page shouts rather than welcomes.
- **Don't** ignore WCAG 2.1 AA contrast requirements. Sufficient contrast isn't compliance theater; it's a marker of thoughtful craft.
