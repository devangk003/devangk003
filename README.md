<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/header-light.svg">
  <img alt="Devang Kumawat. I design the interface and then ship it myself, in the same repo." src="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/header-dark.svg" width="100%">
</picture>

<br>

Frontend, design systems, and the agent underneath. Three startup internships, about eight months total: Useful Ventures (Crewm8.ai), Brixline, and a work trial at OpenTrade (YC S26). 2026 Information Science graduate.

I build the thing, then I go find what's wrong with it. Most of what's below has a number attached because I went and counted.

> [!NOTE]
> Looking for a full-time role. Bengaluru, or remote. &nbsp;·&nbsp; **[devangk003.vercel.app](https://devangk003.vercel.app)** &nbsp;·&nbsp; [devangk1403@gmail.com](mailto:devangk1403@gmail.com)

<br>

## Selected work

<table>
<tr>
<td width="50%" valign="top">

<sub><code>01</code> &nbsp; AGENTS &amp; EVALUATION</sub>

### [AstroAgent](https://github.com/devangk003/astroagent)
An agent built to refuse to make things up

LangGraph, five tools, six safety rails. 93% pass on a 30-case held-out set, kept disjoint from the set I tuned the guardrails on. 0% attack-success-rate.

The judge is a different model family, so it can't rubber-stamp its own output. It scores tone only. I never let it gate pass or fail.

<sub>Python &nbsp;·&nbsp; LangGraph &nbsp;·&nbsp; [Case study &rarr;](https://devangk003.vercel.app/case-studies/astro-ai-agent)</sub>

</td>
<td width="50%" valign="top">

<sub><code>02</code> &nbsp; PRODUCT &amp; UX RESEARCH</sub>

### [Cook-Along Mode](https://github.com/devangk003/recipe-app)
A recipe app for when your hands are covered in oil

I recorded a 50-minute cook. A wet finger doesn't register a tap. Water on the glass scrolls the page on its own. The screen is unusable at the exact moment you need it.

All 15 lookups in that cook were questions. Nobody set a timer. So the IA splits on hand state and runs on a 14-rule voice grammar.

<sub>React 19 &nbsp;·&nbsp; TypeScript &nbsp;·&nbsp; [Live &rarr;](https://cookalong-devangk.vercel.app/)</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<sub><code>03</code> &nbsp; AGENT TOOLING &amp; GTM</sub>

### [gtm-agent-skills](https://github.com/devangk003/gtm-agent-skills)
A go-to-market team, encoded as a skill graph

32 skills across 6 categories, a dependency DAG, three CRM adapters. Ran it live on 30 leads for $0 in API spend.

The DM helper refuses to write a message it can't ground in a real record. That was the point of building it.

<sub>MIT &nbsp;·&nbsp; Python &nbsp;·&nbsp; [Case study &rarr;](https://devangk003.vercel.app/case-studies/crewm8-gtm-ai-system)</sub>

</td>
<td width="50%" valign="top">

<sub><code>04</code> &nbsp; FRONTEND &amp; TECHNICAL SEO</sub>

### [This portfolio](https://devangk003.vercel.app)
Built to be read by AI search, not just by people

Hand-written `llms.txt`. Schema.org JSON-LD rendered server-side, so a crawler gets it without running JS. Sitemap and robots generate from one route manifest.

Then I shipped three case studies on 8 July and forgot to add them to that manifest. No crawler could see them for a month. I caught it diffing the sitemap against the routes.

<sub>Next.js &nbsp;·&nbsp; TypeScript &nbsp;·&nbsp; React Three Fiber</sub>

</td>
</tr>
</table>

<details>
<summary><b>&nbsp;More work</b></summary>

<br>

<table>
<tr><td width="25%" valign="top"><b><a href="https://github.com/devangk003/kuspus">KusPus</a></b><br><sub>C#</sub></td>
<td valign="top">Local speech-to-text for Windows. whisper.cpp on the CPU. About 860 ms end to end for 3 seconds of audio on <code>tiny.en</code>. No cloud, no account, no telemetry.</td></tr>
<tr><td valign="top"><b><a href="https://github.com/devangk003/hivecodex">HiveCodex</a></b><br><sub>TypeScript</sub></td>
<td valign="top">Real-time collaborative coding. Monaco, Socket.IO, MongoDB with GridFS, Docker.</td></tr>
<tr><td valign="top"><b><a href="https://github.com/devangk003/GoFetch">GoFetch</a></b><br><sub>TypeScript</sub></td>
<td valign="top">Natural-language queries over Indian public datasets, on MongoDB vector search. Hackathon-scale prototype, and it reads like one.</td></tr>
<tr><td valign="top"><b><a href="https://github.com/devangk003/SundayInsurance">SundayInsurance</a></b><br><sub>TypeScript</sub></td>
<td valign="top">Vehicle-insurance comparison. React and Express with a Puppeteer quote scraper.</td></tr>
</table>

</details>

<br>

## Stack

|  |  |
|---|---|
| **Building with** | `TypeScript` `React` `Next.js` `Tailwind` `Python` `LangGraph` `Claude Code` `Codex` |
| **Also** | `Node.js` `PostgreSQL` `MongoDB` `Docker` `Fly.io` `Stripe` `Three.js` `Remotion` `C++` `C#` `Java` `SQL` |
| **Design** | `Figma` `design tokens` `Photoshop` `Illustrator` `InDesign` `Affinity` |
| **Measurement** | `PostHog` `schema.org JSON-LD` `technical SEO` `AEO` |

<br>

<table>
<tr>
<td width="58%" valign="top">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/langs-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/langs-light.svg">
  <img alt="Languages by bytes: TypeScript 66.1%, Python 12.5%, C# 11.5%, JavaScript 4.7%, HTML 2.0%, CSS 1.8%, Other 1.3%." src="https://raw.githubusercontent.com/devangk003/devangk003/main/assets/langs-dark.svg" width="100%">
</picture>

</td>
<td valign="top">

**Elsewhere**

[![Portfolio](https://img.shields.io/badge/Portfolio-24292f?style=for-the-badge&logo=vercel&logoColor=white)](https://devangk003.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-24292f?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/devangk003)
[![X](https://img.shields.io/badge/X-24292f?style=for-the-badge&logo=x&logoColor=white)](https://x.com/devang_kumawat)
[![Email](https://img.shields.io/badge/Email-24292f?style=for-the-badge&logo=gmail&logoColor=white)](mailto:devangk1403@gmail.com)

</td>
</tr>
</table>
