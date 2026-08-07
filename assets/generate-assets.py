"""Generate the profile README artwork: header, tech strip, section and link icons.

Design tokens, chosen for this brief rather than reached for:

  ink      #0B1020   deep indigo-black. Deliberately NOT GitHub's #0d1117, so the
                     header reads as his surface rather than as GitHub chrome.
  rose     #EC6A88   design
  teal     #4FD1C5   engineering
  gold     #F6C177   distribution

The triad is the signature: three parallel tracks, one per domain, each carrying
segments that stand for the versioned artifacts left behind. It encodes the
positioning structurally instead of decorating it.

Type: one very large, tightly tracked heavy sans against small wide-tracked
monospace. The contrast between those two is the typographic idea.

Motion rule, learned the hard way: every animation is additive. Nothing is
revealed by an animation, because CSS animation does not advance in every
context that renders an SVG through an image tag, and an entrance that hides
its own content renders as a blank card. Frame zero is always the full artwork.
"""
import html
import os
import re


def esc(v):
    """Escape text destined for XML. & in a label silently breaks the whole file."""
    return html.escape(str(v), quote=True)

SP = r"C:\Users\kumaw\AppData\Local\Temp\claude\E--RozgaariAandolan\c8ad8bf9-a59f-4af4-970c-701e161aeb1d\scratchpad"
OUT = os.path.join(SP, "devangk003", "assets")
ICONS = os.path.join(SP, "icons")

T = {
    "dark": dict(bg="#0B1020", ink="#EEF1F8", mut="#8792AD", dim="#5A6480",
                 rose="#EC6A88", teal="#4FD1C5", gold="#F6C177",
                 panel="#131A30", line="#222B47", stroke="none"),
    "light": dict(bg="#FBFBFD", ink="#0B1020", mut="#5A6480", dim="#8792AD",
                  rose="#D6436A", teal="#0E9384", gold="#B77D18",
                  panel="#F3F4F9", line="#E3E6F0", stroke="#DFE3EE"),
}

FONT_D = 'Inter, "Helvetica Neue", -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif'
FONT_M = 'ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace'


def icon_path(name):
    """Pull the path data out of a simple-icons file."""
    s = open(os.path.join(ICONS, f"{name}.svg"), encoding="utf-8").read()
    return re.search(r'<path d="([^"]+)"', s).group(1)


# ----------------------------------------------------------------- header
# Three panels rather than three rules, so the header speaks the same chip
# language as the stack strip: same radius, same panel fill, same mono label.
TRACKS = [
    ("DESIGN", "rose", ["Design systems v1 to v3.", "Brand books and launch campaigns."]),
    ("ENGINEERING", "teal", ["Frontend, agents, and the", "evaluation harnesses under them."]),
    ("DISTRIBUTION", "gold", ["270k views on a channel", "I ran solo, at 18."]),
]


def header(theme):
    t = T[theme]
    W, H = 1200, 412
    PAD, GAP = 64, 20
    PW = (W - 2 * PAD - 2 * GAP) // 3
    PY_, PH = 236, 108

    panels, css = [], []
    for i, (label, key, lines) in enumerate(TRACKS):
        col = t[key]
        x = PAD + i * (PW + GAP)
        body = [
            f'<rect x="0" y="0" width="{PW}" height="{PH}" rx="12" fill="{t["panel"]}"/>',
            f'<rect x="0" y="0" width="{PW}" height="{PH}" rx="12" fill="none" stroke="{t["line"]}"/>',
            f'<rect x="22" y="24" width="12" height="12" rx="3.5" fill="{col}"/>',
            f'<text class="lb" x="44" y="34" fill="{col}">{esc(label)}</text>',
        ]
        for j, ln in enumerate(lines):
            body.append(f'<text class="pd" x="22" y="{64 + j * 22}" fill="{t["mut"]}">{esc(ln)}</text>')
        # a slow bloom on the mark, additive, visible at every frame
        body.append(f'<circle class="pulse p{i}" cx="28" cy="30" r="16" fill="{col}"/>')
        css.append(f'.p{i} {{ animation-delay: {i * 1.3:.1f}s; }}')
        panels.append(f'<g transform="translate({x} {PY_})">{"".join(body)}</g>')

    border = (f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" '
              f'stroke="{t["stroke"]}"/>') if t["stroke"] != "none" else ""

    aria = ("Devang Kumawat. I take a surface nobody owns and ship it end to end. "
            + " ".join(f"{l}: {' '.join(d)}" for l, _, d in TRACKS))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(aria)}">
  <defs>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["rose"]}" stop-opacity="0.16"/>
      <stop offset="0.5" stop-color="{t["teal"]}" stop-opacity="0.10"/>
      <stop offset="1" stop-color="{t["gold"]}" stop-opacity="0.14"/>
    </linearGradient>
  </defs>
  <style>
    .nm {{ font: 800 78px {FONT_D}; letter-spacing: -2.6px; }}
    .tg {{ font: 400 21px {FONT_D}; }}
    .lb {{ font: 600 11px {FONT_M}; letter-spacing: 2px; }}
    .pd {{ font: 400 14.5px {FONT_D}; }}
    .mt {{ font: 400 12px {FONT_M}; letter-spacing: 0.4px; }}

    .pulse {{ opacity: 0; animation: bloom 6s ease-in-out infinite; }}
    @keyframes bloom {{
      0%, 70%, 100% {{ opacity: 0; transform: scale(0.5); }}
      18%           {{ opacity: 0.22; transform: scale(1); }}
    }}
    {" ".join(css)}
    @media (prefers-reduced-motion: reduce) {{ .pulse {{ animation: none; }} }}
  </style>

  <rect width="{W}" height="{H}" rx="14" fill="{t["bg"]}"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#glow)"/>
  {border}

  <text class="nm" x="{PAD}" y="136" fill="{t["ink"]}">Devang Kumawat</text>
  <text class="tg" x="{PAD}" y="184" fill="{t["mut"]}">I take a surface nobody owns and ship it end to end.</text>
  {"".join(panels)}
  <text class="mt" x="{PAD}" y="{H - 30}" fill="{t["dim"]}">2026 Information Science graduate &#183; Bengaluru, India</text>
</svg>
'''


# -------------------------------------------------------------- tech strip
GROUPS = [
    ("BUILD", [("typescript", "TypeScript", "#3178C6"), ("react", "React", "#61DAFB"),
               ("nextdotjs", "Next.js", None), ("tailwindcss", "Tailwind", "#06B6D4"),
               ("python", "Python", "#3776AB"), ("claude", "Claude Code", "#D97757")]),
    ("INFRA & DATA", [("nodedotjs", "Node.js", "#5FA04E"), ("docker", "Docker", "#2496ED"),
                      ("vercel", "Vercel", None), ("postgresql", "PostgreSQL", "#4169E1"),
                      ("mongodb", "MongoDB", "#47A248"), ("stripe", "Stripe", "#635BFF")]),
    ("DESIGN & MEASURE", [("figma", "Figma", "#F24E1E"), ("adobephotoshop", "Photoshop", "#31A8FF"),
                          ("adobeillustrator", "Illustrator", "#FF9A00"),
                          ("threedotjs", "Three.js", None), ("posthog", "PostHog", "#F54E00"),
                          ("git", "Git", "#F05032")]),
]


def strip(theme):
    t = T[theme]
    W = 1200
    ROW_H, PAD = 86, 40
    H = PAD * 2 + ROW_H * len(GROUPS) - 18
    mono_fill = t["ink"]

    body = []
    for gi, (gname, items) in enumerate(GROUPS):
        y = PAD + gi * ROW_H
        body.append(f'<text class="gl" x="{PAD}" y="{y + 30}" fill="{t["dim"]}">{esc(gname)}</text>')
        x = PAD + 150
        for key, label, col in items:
            fill = col or mono_fill
            body.append(
                f'<g transform="translate({x} {y + 8})">'
                f'<rect x="0" y="0" width="152" height="44" rx="10" fill="{t["panel"]}"/>'
                f'<g transform="translate(14 12) scale(0.83)" fill="{fill}">'
                f'<path d="{icon_path(key)}"/></g>'
                f'<text class="il" x="48" y="27" fill="{t["ink"]}">{esc(label)}</text>'
                f'</g>')
            x += 160

    border = (f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" '
              f'stroke="{t["stroke"]}"/>') if t["stroke"] != "none" else ""

    aria = esc("Stack. " + ". ".join(f"{g}: " + ", ".join(l for _, l, _ in it) for g, it in GROUPS))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">
  <style>
    .gl {{ font: 500 11px {FONT_M}; letter-spacing: 2px; }}
    .il {{ font: 500 13.5px {FONT_D}; }}
  </style>
  <rect width="{W}" height="{H}" rx="14" fill="{t["bg"]}"/>
  {border}
  {"".join(body)}
</svg>
'''


# ------------------------------------------------------------ small icons
AVATAR = open(os.path.join(SP, "avatar64.b64")).read().strip()


def chip(name, key, col, label, url_theme):
    """A single link chip: brand icon plus label."""
    t = T[url_theme]
    W, H = 168, 40
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label)}">
  <style>.l {{ font: 600 13px {FONT_D}; }}</style>
  <rect width="{W}" height="{H}" rx="10" fill="{t["panel"]}" stroke="{t["line"]}"/>
  {f'<image x="12" y="8" width="24" height="24" href="data:image/png;base64,{AVATAR}"/>' if key == "__avatar__" else f'<g transform="translate(14 11) scale(0.75)" fill="{col}"><path d="{icon_path(key)}"/></g>'}
  <text class="l" x="44" y="25" fill="{t["ink"]}">{esc(label)}</text>
</svg>
'''


def section_icon(kind, theme):
    """Section heading marks. Geometric, drawn to mean something, not clip art."""
    t = T[theme]
    c = {"work": t["rose"], "stack": t["teal"], "links": t["gold"]}[kind]
    if kind == "work":       # four panes, the work grid
        g = (f'<rect x="3" y="3" width="8" height="8" rx="2" fill="{c}"/>'
             f'<rect x="13" y="3" width="8" height="8" rx="2" fill="{c}" opacity=".55"/>'
             f'<rect x="3" y="13" width="8" height="8" rx="2" fill="{c}" opacity=".55"/>'
             f'<rect x="13" y="13" width="8" height="8" rx="2" fill="{c}" opacity=".3"/>')
    elif kind == "stack":    # three layers
        g = (f'<rect x="3" y="4" width="18" height="4" rx="2" fill="{c}"/>'
             f'<rect x="3" y="10" width="18" height="4" rx="2" fill="{c}" opacity=".6"/>'
             f'<rect x="3" y="16" width="18" height="4" rx="2" fill="{c}" opacity=".35"/>')
    else:                    # a node reaching out
        g = (f'<circle cx="7" cy="12" r="4" fill="{c}"/>'
             f'<circle cx="18" cy="6" r="3" fill="{c}" opacity=".6"/>'
             f'<circle cx="18" cy="18" r="3" fill="{c}" opacity=".6"/>'
             f'<path d="M10 11 L15.5 7 M10 13 L15.5 17" stroke="{c}" stroke-width="1.6" opacity=".5"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
            f'role="img" aria-label=""><g>{g}</g></svg>\n')


os.makedirs(OUT, exist_ok=True)
written = []

for theme in ("dark", "light"):
    for name, svg in (("header", header(theme)), ("stack", strip(theme))):
        p = os.path.join(OUT, f"{name}-{theme}.svg")
        open(p, "w", encoding="utf-8").write(svg)
        written.append(p)


# Section marks are saturated enough to read on either canvas, so one set serves
# both themes and the README needs no picture element for a 24px glyph.
for kind in ("work", "stack", "links"):
    p = os.path.join(OUT, f"ico-{kind}.svg")
    open(p, "w", encoding="utf-8").write(section_icon(kind, "dark"))
    written.append(p)

LINKS = [("portfolio", "__avatar__", None, "Portfolio"), ("linkedin", "linkedin", "#0A66C2", "LinkedIn"),
         ("x", "x", None, "X"), ("email", "gmail", "#EA4335", "Email")]
for theme in ("dark", "light"):
    for slug, key, col, label in LINKS:
        c = col or T[theme]["ink"]
        p = os.path.join(OUT, f"link-{slug}-{theme}.svg")
        open(p, "w", encoding="utf-8").write(chip(slug, key, c, label, theme))
        written.append(p)

for p in written:
    print(f"  {os.path.basename(p):<26} {os.path.getsize(p):>6} bytes")
print(f"\n{len(written)} files")
