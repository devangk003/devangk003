# Devang Kumawat

2026 Information Science grad, Bengaluru. I design the interface and then ship it myself, in the same repo.

Frontend and design systems, AI agents and the evaluation harnesses that make them measurable, and the brand work around both. Three startup internships: Useful Ventures (Crewm8.ai), Brixline, and a work trial at OpenTrade (YC S26).

**[Portfolio and case studies →](https://devangk003.vercel.app)**

## What I've built

**[AstroAgent](https://github.com/devangk003/astroagent)** · a conversational agent built to refuse to make things up
LangGraph, five tools, six layered safety rails. The evaluation is the point: a held-out 30-case set kept disjoint from the guardrail-tuning set, and an LLM-as-judge deliberately pointed at a different model family so it can't rubber-stamp its own output. 93% pass, 0% attack-success-rate.
[Case study](https://devangk003.vercel.app/case-studies/astro-ai-agent) · Python

**[gtm-agent-skills](https://github.com/devangk003/gtm-agent-skills)** · an open-source GTM agent skill graph
32 GTM skills across 6 categories plus a personal DM helper, a dependency DAG, and three CRM adapters. Ran live end to end for $0 in API spend. MIT licensed.
[Case study](https://devangk003.vercel.app/case-studies/crewm8-gtm-ai-system) · Python

**[Cook-Along Mode](https://github.com/devangk003/recipe-app)** · a recipe app for when your hands are covered in oil
Not a redesign. A cook test showed a wet finger doesn't register a tap and water on the glass causes uncontrolled scrolling, so the touchscreen is unavailable exactly when it's needed. The IA splits on hand state, driven by a 14-rule voice grammar. The design system sits behind a 241-line build check of 15 assertions that fails CI on a raw hex or an off-scale radius, rather than sitting in a document.
[Live](https://cookalong-devangk.vercel.app/) · React 19, TypeScript

**[This portfolio](https://devangk003.vercel.app)** · built to be readable by AI search
Hand-written `llms.txt`, server-rendered schema.org JSON-LD so crawlers get it without executing JS, and the sitemap and robots rules generated from one route manifest with five named AI crawlers allowlisted.
Next.js, TypeScript, React Three Fiber

**[KusPus](https://github.com/devangk003/kuspus)** · local speech-to-text for Windows
whisper.cpp on the CPU, paste anywhere. Around 860 ms end to end for 3 seconds of audio on `tiny.en`. Fully offline, no account, no telemetry.
C#

**[HiveCodex](https://github.com/devangk003/hivecodex)** · real-time collaborative coding
Monaco, Socket.IO, MongoDB with GridFS, Docker.
TypeScript

## Stack

**Building with:** TypeScript · React · Next.js · Tailwind · Python · LangGraph · Claude Code · Codex
**Also:** Node.js · PostgreSQL · MongoDB · Docker · Fly.io · Stripe · Three.js / React Three Fiber · Remotion · C++ · C# · Java · SQL
**Design:** Figma · design tokens · Photoshop · Illustrator · InDesign · Affinity
**Measurement:** PostHog · schema.org JSON-LD · technical SEO and AEO

## Elsewhere

[![Portfolio](https://img.shields.io/badge/Portfolio-000000.svg?style=for-the-badge&logo=vercel&logoColor=white)](https://devangk003.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/devangk003)
[![X](https://img.shields.io/badge/X-black.svg?style=for-the-badge&logo=X&logoColor=white)](https://x.com/devang_kumawat)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:devangk1403@gmail.com)

![](https://github-readme-stats.vercel.app/api/top-langs/?username=devangk003&theme=nightowl&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

![snake gif](https://github.com/devangk003/devangk003/blob/output/github-snake-dark.svg)
