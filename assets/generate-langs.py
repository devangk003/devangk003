"""Generate the self-hosted language card, light and dark.

Data comes from the GitHub API, summed over non-fork repos. One exclusion:
ai-resume-ats/public/pdf.worker.min.mjs is a vendored 1,035,022-byte pdf.js
worker, which is 84% of all the JavaScript on the account and not authored
code. Counting it reports the wrong primary language, which is exactly the
failure the third-party card had.
"""
import json
import os
import subprocess

OUT = r"C:\Users\kumaw\AppData\Local\Temp\claude\E--RozgaariAandolan\c8ad8bf9-a59f-4af4-970c-701e161aeb1d\scratchpad\devangk003\assets"
VENDORED = {"JavaScript": 1_035_022}   # ai-resume-ats/public/pdf.worker.min.mjs
TOP_N = 6

# GitHub's own language colours, kept because they are recognisable.
COLOR = {
    "TypeScript": "#3178c6", "Python": "#3572A5", "C#": "#178600",
    "JavaScript": "#f1e05a", "HTML": "#e34c26", "CSS": "#663399",
    "Other": "#6e7681",
}

THEME = {
    "dark":  dict(bg="#0d1117", stroke="none", title="#8b949e", name="#e6edf3",
                  pct="#8b949e", foot="#6e7681", track="#21262d", sheen="0.16"),
    "light": dict(bg="#ffffff", stroke="#d0d7de", title="#59636e", name="#1f2328",
                  pct="#59636e", foot="#818b98", track="#eaeef2", sheen="0.55"),
}

W, H = 640, 286
PAD = 28
BAR_Y, BAR_H = 62, 14
GAP = 3


def gather():
    repos = json.loads(subprocess.run(
        ["gh", "api", "users/devangk003/repos?per_page=100&type=owner"],
        capture_output=True, text=True).stdout)
    total, n = {}, 0
    for r in repos:
        if r.get("fork"):
            continue
        n += 1
        langs = json.loads(subprocess.run(
            ["gh", "api", f"repos/devangk003/{r['name']}/languages"],
            capture_output=True, text=True).stdout or "{}")
        for k, v in langs.items():
            total[k] = total.get(k, 0) + v
    for k, v in VENDORED.items():
        total[k] = total.get(k, 0) - v
    return {k: v for k, v in total.items() if v > 0}, n


def build(theme, rows, footnote):
    t = THEME[theme]
    bar_w = W - 2 * PAD
    usable = bar_w - GAP * (len(rows) - 1)

    segs, x = [], PAD
    for i, (name, pct) in enumerate(rows):
        w = usable * pct / 100
        segs.append(f'<rect x="{x:.1f}" y="{BAR_Y}" width="{w:.1f}" height="{BAR_H}" '
                    f'rx="{BAR_H/2}" fill="{COLOR.get(name, COLOR["Other"])}"/>')
        x += w + GAP

    # Legend: 4 rows in column one, the remainder in column two.
    col1, col2 = rows[:4], rows[4:]
    legend = []
    for ci, col in enumerate((col1, col2)):
        lx = PAD if ci == 0 else 336
        rx = 300 if ci == 0 else W - PAD
        for ri, (name, pct) in enumerate(col):
            y = 116 + ri * 34
            d = ri + ci * 4
            legend.append(
                f'<g>'
                f'<circle cx="{lx + 5}" cy="{y - 5}" r="5" fill="{COLOR.get(name, COLOR["Other"])}"/>'
                f'<text class="nm" x="{lx + 20}" y="{y}" fill="{t["name"]}">{name}</text>'
                f'<text class="pc" x="{rx}" y="{y}" fill="{t["pct"]}" text-anchor="end">{pct:.1f}%</text>'
                f'</g>')

    border = (f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" '
              f'stroke="{t["stroke"]}"/>') if t["stroke"] != "none" else ""

    aria = "Languages by bytes: " + ", ".join(f"{n} {p:.1f} percent" for n, p in rows)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">
  <style>
    .ti {{ font: 500 11px ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace; letter-spacing: 1.4px; }}
    .nm {{ font: 500 14px Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .pc {{ font: 400 13px ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace; font-variant-numeric: tabular-nums; }}
    .fn {{ font: 400 10.5px ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace; }}

    /* Motion here is additive only. Nothing on this card is revealed by an
       animation, because CSS animations do not advance in every context that
       renders an SVG through an img tag, and an entrance that hides its own
       content is one failed render away from a blank card.

       So the sheen is the only moving part. At frame 0 it sits off the left
       edge, which means the static render is the complete card. */
    .sheen {{ animation: sweep 7s cubic-bezier(.4,0,.2,1) 2s infinite; }}
    @keyframes sweep {{
      0%   {{ transform: translateX(-260px); }}
      55%  {{ transform: translateX({W + 60}px); }}
      100% {{ transform: translateX({W + 60}px); }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      .sheen {{ animation: none; }}
    }}
  </style>

  <rect width="{W}" height="{H}" rx="10" fill="{t["bg"]}"/>
  {border}

  <text class="ti" x="{PAD}" y="36" fill="{t["title"]}">LANGUAGES</text>

  <defs>
    <clipPath id="clip"><rect x="{PAD}" y="{BAR_Y - 2}" width="{W - 2*PAD}" height="{BAR_H + 4}" rx="{BAR_H/2}"/></clipPath>
    <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="{t["sheen"]}"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect x="{PAD}" y="{BAR_Y}" width="{W - 2*PAD}" height="{BAR_H}" rx="{BAR_H/2}" fill="{t["track"]}"/>
  <g clip-path="url(#clip)">
    {"".join(segs)}
    <rect class="sheen" x="0" y="{BAR_Y - 2}" width="200" height="{BAR_H + 4}" fill="url(#sheen)"/>
  </g>

  {"".join(legend)}

  <text class="fn" x="{PAD}" y="{H - 22}" fill="{t["foot"]}">{footnote}</text>
</svg>
'''


totals, repo_count = gather()
grand = sum(totals.values())
ranked = sorted(totals.items(), key=lambda kv: -kv[1])
rows = [(k, v / grand * 100) for k, v in ranked[:TOP_N]]
other = sum(v for _, v in ranked[TOP_N:]) / grand * 100
if other > 0:
    rows.append(("Other", other))

foot = f"Bytes across {repo_count} public repos. Excludes a vendored 1.0 MB pdf.js worker."

os.makedirs(OUT, exist_ok=True)
for theme in ("dark", "light"):
    p = os.path.join(OUT, f"langs-{theme}.svg")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(build(theme, rows, foot))
    print(f"wrote {p}")

print(f"\n{repo_count} repos, {grand:,} bytes after exclusion")
for n, p in rows:
    print(f"  {n:<12} {p:5.2f}%")
print(f"  sum        {sum(p for _, p in rows):6.2f}%")
