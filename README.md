<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/header-light.svg">
  <img alt="Devang Kumawat. I design the interface and then ship it myself, in the same repo." src="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/header-dark.svg" width="100%">
</picture>

Frontend, design systems, and the agent underneath. Three startup internships, about eight months total: Useful Ventures (Crewm8.ai), Brixline, and a work trial at OpenTrade (YC S26). 2026 Information Science graduate, Bengaluru.

I build the thing, then I go find what's wrong with it. Most of what's below has a number attached because I went and counted.

**[devangk003.vercel.app →](https://devangk003.vercel.app)**

---

## Selected work

<table>
<tr>
<td width="50%" valign="top">

### [AstroAgent](https://github.com/devangk003/astroagent)
**An agent built to refuse to make things up**

LangGraph, five tools, six safety rails. 93% pass on a 30-case held-out set, kept disjoint from the set I tuned the guardrails on. 0% attack-success-rate.

The judge is a different model family, so it can't rubber-stamp its own output. It scores tone only. I never let it gate pass or fail.

<sub>Python · LangGraph · [Case study](https://devangk003.vercel.app/case-studies/astro-ai-agent)</sub>

</td>
<td width="50%" valign="top">

### [Cook-Along Mode](https://github.com/devangk003/recipe-app)
**A recipe app for when your hands are covered in oil**

I recorded a 50-minute cook. A wet finger doesn't register a tap. Water on the glass scrolls the page on its own. So the screen is unusable at the exact moment you need it.

All 15 lookups in that cook were questions. Nobody set a timer. The IA splits on hand state and runs on a 14-rule voice grammar.

<sub>React 19 · TypeScript · [Live](https://cookalong-devangk.vercel.app/)</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [gtm-agent-skills](https://github.com/devangk003/gtm-agent-skills)
**A go-to-market team, encoded as a skill graph**

32 skills across 6 categories, a dependency DAG, three CRM adapters. Ran it live on 30 leads for $0 in API spend.

The DM helper refuses to write a message it can't ground in a real record. That was the point of building it.

<sub>MIT · Python · [Case study](https://devangk003.vercel.app/case-studies/crewm8-gtm-ai-system)</sub>

</td>
<td width="50%" valign="top">

### [This portfolio](https://devangk003.vercel.app)
**Built to be read by AI search, not just by people**

Hand-written `llms.txt`. Schema.org JSON-LD rendered server-side, so a crawler gets it without running JS. Sitemap and robots generate from one route manifest.

Then I shipped three case studies on 8 July and forgot to add them to that manifest. No crawler could see them for a month. I caught it diffing the sitemap against the routes.

<sub>Next.js · TypeScript · React Three Fiber</sub>

</td>
</tr>
</table>

<details>
<summary><b>More</b></summary>

<br>

**[KusPus](https://github.com/devangk003/kuspus)** · local speech-to-text for Windows
whisper.cpp on the CPU. About 860 ms end to end for 3 seconds of audio on `tiny.en`. No cloud, no account, no telemetry. `C#`

**[HiveCodex](https://github.com/devangk003/hivecodex)** · real-time collaborative coding
Monaco, Socket.IO, MongoDB with GridFS, Docker. `TypeScript`

**[GoFetch](https://github.com/devangk003/GoFetch)** · natural-language queries over Indian public datasets
MongoDB vector search. Hackathon-scale prototype, and it reads like one. `TypeScript`

**[SundayInsurance](https://github.com/devangk003/SundayInsurance)** · vehicle-insurance comparison
React and Express with a Puppeteer quote scraper. `TypeScript`

</details>

---

## Stack

| | |
|---|---|
| **Building with** | TypeScript · React · Next.js · Tailwind · Python · LangGraph · Claude Code · Codex |
| **Also** | Node.js · PostgreSQL · MongoDB · Docker · Fly.io · Stripe · Three.js / React Three Fiber · Remotion · C++ · C# · Java · SQL |
| **Design** | Figma · design tokens · Photoshop · Illustrator · InDesign · Affinity |
| **Measurement** | PostHog · schema.org JSON-LD · technical SEO and AEO |

---

<table>
<tr>
<td valign="top">

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=devangk003&theme=github_dark&hide_border=true&bg_color=00000000&include_all_commits=false&count_private=false&layout=compact&langs_count=8" alt="Most used languages" width="100%">

</td>
<td valign="top">

**Elsewhere**

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=vercel&logoColor=white)](https://devangk003.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/devangk003)
[![X](https://img.shields.io/badge/X-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/devang_kumawat)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:devangk1403@gmail.com)

<sub>Looking for a full-time role. Bengaluru, or remote.</sub>

</td>
</tr>
</table>
