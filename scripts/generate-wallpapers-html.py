#!/usr/bin/env python3
"""
TOKYO NIGHT + MATERIAL YOU WALLPAPER COLLECTION — 20 VARIATIONS
HTML+CSS → PNG via WeasyPrint + pdftoppm
1920x1080 Full HD
"""

import os, subprocess, math
from weasyprint import HTML

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "wallpapers"))
W, H = 1920, 1080

BASE = """@page { size: 1920px 1080px; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { width: 1920px; height: 1080px; overflow: hidden; position: relative; }
"""

# Palette
N = "#1a1b26"
I = "#2c2e3f"
DP = "#3d3f4d"
T = "#26c6da"
P = "#ec407a"
PU = "#ab47bc"
TX = "#c0caf5"
S = "#565f89"

def render(name, body, css):
    html = f"<!DOCTYPE html><html><meta charset='utf-8'><style>{BASE}{css}</style><body>{body}</body></html>"
    os.makedirs(OUT, exist_ok=True)
    pdf = os.path.join(OUT, name.replace(".png", ".pdf"))
    png = os.path.join(OUT, name)
    HTML(string=html).write_pdf(pdf)
    subprocess.run(["pdftoppm", "-png", "-r", "96", "-singlefile", pdf, png.replace(".png", "")], check=True, capture_output=True)
    os.remove(pdf)
    print(f"  ✓ {name}  ({os.path.getsize(png)//1024} KB)")

def circle(cx, cy, r, color, opacity=1, blur=0, border=False):
    b = f"border:1px solid {color};" if border else ""
    bl = f"filter:blur({blur}px);" if blur else ""
    return f"<div style='position:absolute;left:{cx}px;top:{cy}px;width:{r*2}px;height:{r*2}px;border-radius:50%;background:{color};opacity:{opacity};{b}{bl}transform:translate(-50%,-50%)'></div>"

def rect(x, y, w, h, color, opacity=1, blur=0, rot=0):
    bl = f"filter:blur({blur}px);" if blur else ""
    r2 = f"transform:rotate({rot}deg);" if rot else ""
    return f"<div style='position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};opacity:{opacity};{bl}{r2}'></div>"

def text(txt, x, y, size=14, color=TX, weight=300, align="left", spacing=2):
    return f"<div style='position:absolute;left:{x}px;top:{y}px;font-family:sans-serif;font-size:{size}px;color:{color};font-weight:{weight};letter-spacing:{spacing}px;text-align:{align}'>{txt}</div>"

# ═══════════════════════════════════════════════════════════════
# 1 — MINIMALIST GEOMETRIC NIGHT
# ═══════════════════════════════════════════════════════════════
def w01():
    css = f"""
    body {{ background: linear-gradient(135deg, {N}, #13131f); }}
    .g1 {{ position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
           width:1000px;height:1000px;background:radial-gradient(circle at 30% 40%, {PU}08, {T}06, transparent);
           filter:blur(60px); }}
    """
    body = f'<div class="g1"></div>'
    for cx, cy, r, c, o in [
        (200, 200, 180, PU, 0.12), (400, 600, 120, T, 0.15), (700, 300, 100, P, 0.10),
        (1200, 700, 200, T, 0.08), (1500, 200, 140, PU, 0.12), (1000, 800, 90, P, 0.10),
        (1700, 800, 160, T, 0.06), (300, 900, 80, PU, 0.10), (1400, 500, 110, P, 0.08),
        (600, 950, 70, T, 0.12),
    ]:
        body += circle(cx, cy, r, c, o)
    body += text("26°C", 80, 80, 48, T, 100, "left", 4)
    body += text("TOKYO NIGHT", 80, 140, 13, S, 300, "left", 6)
    render("01-minimal-geometric.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 2 — GLASSMORPHISM MATERIAL YOU
# ═══════════════════════════════════════════════════════════════
def w02():
    css = f"""
    body {{ background: linear-gradient(160deg, {N}, #11101a, {DP}); }}
    .g {{
      position:absolute; width:420px; height:200px; border-radius:20px;
      background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.06);
      backdrop-filter:blur(20px); box-shadow:0 8px 32px rgba(0,0,0,0.3);
    }}
    .a {{ position:absolute; width:250px; height:250px; border-radius:50%; filter:blur(70px); opacity:0.25; }}
    """
    body = f"""
    <div class='a' style='top:-50px;left:-50px;background:{PU}'></div>
    <div class='a' style='bottom:-80px;right:-60px;background:{T}'></div>
    <div class='a' style='top:400px;left:800px;background:{P}'></div>
    <div class='g' style='top:120px;left:200px'></div>
    <div class='g' style='top:200px;left:500px;height:160px'></div>
    <div class='g' style='top:350px;left:350px;width:350px;height:180px'></div>
    <div class='g' style='top:600px;left:600px;width:380px;height:150px'></div>
    <div class='g' style='top:550px;left:200px;width:300px;height:170px'></div>
    """
    body += text("STYX", 1200, 850, 64, PU, 100, "left", 8)
    body += text("TOKYO NIGHT", 1200, 920, 13, S, 300, "left", 6)
    render("02-glassmorphism.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 3 — ABSTRACT NIGHT LANDSCAPE
# ═══════════════════════════════════════════════════════════════
def w03():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #0f0f1f, {DP}22); }}
    .m {{
      position:absolute; bottom:0; width:100%;
      clip-path:polygon(0% 100%, 2% 65%, 5% 68%, 8% 50%, 12% 55%, 15% 40%,
                        18% 45%, 22% 30%, 25% 35%, 28% 20%, 32% 28%, 35% 15%,
                        38% 22%, 42% 10%, 45% 18%, 48% 8%, 52% 15%, 55% 5%,
                        58% 12%, 62% 3%, 65% 10%, 68% 2%, 72% 8%, 75% 15%,
                        78% 5%, 82% 12%, 85% 8%, 88% 18%, 92% 12%, 95% 22%,
                        98% 15%, 100% 25%, 100% 100%);
    }}
    .s {{ position:absolute; width:2px; height:2px; border-radius:50%; }}
    """
    body = ""
    for i in range(40):
        body += f"<div class='s' style='top:{30+i*25}px;left:{20+i*48}px;background:{TX};opacity:{0.1+(i%5)*0.05}'></div>"
    body += f"<div class='m' style='height:650px;background:linear-gradient(180deg,{PU}33,{N})'></div>"
    body += f"<div class='m' style='height:550px;background:linear-gradient(180deg,{I}44,{N})'></div>"
    body += f"<div class='m' style='height:450px;background:linear-gradient(180deg,{N},{N})'></div>"
    body += text("TOKYO · 03:47", 80, 80, 18, TX, 100, "left", 4)
    body += text("NIGHT LANDSCAPE", 80, 110, 11, S, 300, "left", 6)
    render("03-night-landscape.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 4 — DEVELOPER CODE AESTHETIC
# ═══════════════════════════════════════════════════════════════
def w04():
    css = f"""
    body {{ background: {N}; }}
    .line {{ position:absolute; height:20px; border-radius:3px; opacity:0.1; }}
    """
    body = f"""
    <div style='position:absolute;left:60px;top:60px;font-family:monospace;font-size:14px;line-height:1.8;color:{TX};opacity:0.15;'>
    function __init__() &#123;<br>
    &nbsp;&nbsp;const night = "tokyo";<br>
    &nbsp;&nbsp;const accent = "material";<br>
    &nbsp;&nbsp;return night.concat(accent).toUpper();<br>
    &#125;<br><br>
    for (let i = 0; i &lt; 256; i++) &#123;<br>
    &nbsp;&nbsp;draw(i, i * 0.618);<br>
    &#125;
    </div>
    <div style='position:absolute;left:960px;top:60px;font-family:monospace;font-size:14px;line-height:1.8;color:{TX};opacity:0.06;'>
    {chr(10).join('  "0x{:04x}": "tokyo-night",'.format(i) for i in range(0, 256, 8))}
    </div>
    """
    for i in range(5):
        body += f"<div style='position:absolute;left:{200+i*350}px;top:{400+i*80}px;font-family:monospace;font-size:48px;color:{[PU,T,P][i%3]};opacity:0.25;'>&#123;&#125;</div>"
    body += text("$ echo night", 80, 920, 16, T, 300, "left", 3)
    body += text("TOKYO NIGHT // DEVELOPER", 80, 950, 10, S, 300, "left", 5)
    render("04-developer-code.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 5 — ORGANIC FLUID GRADIENT
# ═══════════════════════════════════════════════════════════════
def w05():
    css = f"""
    body {{ background: {N}; }}
    .b {{ position:absolute; border-radius:50%; filter:blur(80px); opacity:0.3; }}
    """
    body = f"""
    <div class='b' style='width:900px;height:700px;top:-200px;left:-200px;background:{PU}'></div>
    <div class='b' style='width:800px;height:800px;bottom:-300px;right:-200px;background:{T}'></div>
    <div class='b' style='width:600px;height:600px;top:200px;left:600px;background:{P}'></div>
    <div class='b' style='width:400px;height:400px;top:600px;left:200px;background:{PU}'></div>
    <div class='b' style='width:500px;height:500px;top:100px;right:200px;background:{T}'></div>
    <div class='b' style='width:350px;height:350px;bottom:100px;left:900px;background:{P}'></div>
    """
    render("05-fluid-gradient.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 6 — RETRO CYBERPUNK GRID
# ═══════════════════════════════════════════════════════════════
def w06():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #0a0a12); }}
    .grid {{
      position:absolute;top:0;left:0;width:100%;height:100%;
      background-image:
        linear-gradient(rgba(171,71,188,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(171,71,188,0.04) 1px, transparent 1px);
      background-size:40px 40px;
      transform:perspective(800px) rotateX(50deg);
      transform-origin:50% 100%;
    }}
    .sg {{ position:absolute; bottom:0; width:100%; height:500px;
           background:linear-gradient(0deg, {N}, transparent); }}
    .sun {{ position:absolute;bottom:350px;left:50%;transform:translateX(-50%);
            width:120px;height:120px;border-radius:50%;
            background:radial-gradient(circle, {T}, {PU}66);
            box-shadow:0 0 80px {T}44,0 0 200px {PU}22; }}
    .h {{ position:absolute;bottom:400px;left:0;width:100%;height:2px;
          background:linear-gradient(90deg,transparent,{T}44,{PU}44,transparent); }}
    """
    body = f"""
    <div class='grid'></div><div class='sg'></div><div class='sun'></div><div class='h'></div>
    """
    body += text("NIGHT", 80, 80, 56, T, 100, "left", 10)
    body += text("CYBERPUNK", 80, 145, 12, S, 300, "left", 8)
    body += text("2026", 1760, 1010, 12, S, 100, "right", 6)
    render("06-retro-grid.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 7 — MATERIAL YOU BUBBLES
# ═══════════════════════════════════════════════════════════════
def w07():
    css = f"""
    body {{ background: linear-gradient(135deg, {N}, #12121e); }}
    .g {{ position:absolute; width:600px; height:600px;
          background:radial-gradient(circle at 30% 40%, {T}08, transparent);
          filter:blur(50px); border-radius:50%; }}
    .b {{
      position:absolute; border-radius:50%;
      background:rgba(255,255,255,0.03);
      border:1px solid rgba(255,255,255,0.06);
      box-shadow:inset 0 -20px 40px rgba(0,0,0,0.2), 0 10px 30px rgba(0,0,0,0.3);
    }}
    """
    body = f"<div class='g' style='left:50%;top:50%;transform:translate(-50%,-50%)'></div>"
    for cx, cy, r in [
        (300, 300, 180), (600, 700, 140), (1400, 300, 200),
        (1200, 700, 120), (900, 500, 160), (1600, 800, 100),
        (400, 200, 80), (1000, 900, 90), (200, 800, 60),
    ]:
        colors = [T, P, PU]
        c = colors[(cx+cy)//200 % 3]
        body += f"<div class='b' style='left:{cx-r}px;top:{cy-r}px;width:{r*2}px;height:{r*2}px;border-color:{c}22'></div>"
    body += text("zen · 静寂", 1530, 940, 18, TX, 100, "right", 4)
    body += text("MATERIAL YOU", 1530, 975, 10, S, 300, "right", 6)
    render("07-bubbles.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 8 — DYNAMIC FLOWING LINES
# ═══════════════════════════════════════════════════════════════
def w08():
    css = f"""
    body {{ background: linear-gradient(160deg, {N}, #11101a); }}
    .s {{ position:absolute; width:600px; height:600px; border-radius:50%; filter:blur(100px); opacity:0.15; }}
    """
    body = f"""
    <div class='s' style='top:-100px;left:-100px;background:{PU}'></div>
    <div class='s' style='bottom:-100px;right:-100px;background:{T}'></div>
    <div class='s' style='top:400px;left:800px;background:{P}'></div>
    """
    for i in range(40):
        y1 = 100 + i * 25
        x1 = 200 + 40 * math.sin(i * 0.3)
        x2 = 1700 - 50 * math.sin(i * 0.4)
        colors = [T, PU, P]
        c = colors[i % 3]
        body += f"<div style='position:absolute;top:{y1}px;left:{x1}px;width:{x2-x1}px;height:1px;background:linear-gradient(90deg,{c},{c}00);opacity:0.15'></div>"
    body += text("flow", 80, 80, 48, T, 100, "left", 6)
    body += text("DYNAMIC LINES", 80, 135, 11, S, 300, "left", 6)
    render("08-flowing-lines.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 9 — BOKEH NIGHT LIGHTS
# ═══════════════════════════════════════════════════════════════
def w09():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #0d0d18); }}
    .b {{
      position:absolute; border-radius:50%;
      filter:blur(15px);
    }}
    .v {{ position:absolute;top:0;left:0;width:100%;height:100%;
          background:radial-gradient(ellipse at 50% 60%, transparent 40%, {N}88 90%); }}
    """
    body = "<div class='v'></div>"
    for cx, cy, r, c, o in [
        (400, 300, 80, T, 0.3), (700, 500, 60, PU, 0.25), (1100, 200, 100, P, 0.2),
        (1500, 600, 70, T, 0.3), (300, 700, 50, PU, 0.2), (900, 800, 90, P, 0.15),
        (1300, 400, 65, T, 0.25), (600, 200, 45, P, 0.2), (1700, 300, 55, PU, 0.2),
        (500, 900, 40, T, 0.15), (1000, 100, 35, PU, 0.2), (1600, 800, 75, P, 0.15),
        (200, 500, 30, T, 0.2), (800, 400, 50, P, 0.2), (1400, 700, 45, T, 0.15),
        (1800, 500, 60, PU, 0.15),
    ]:
        body += f"<div class='b' style='left:{cx-r}px;top:{cy-r}px;width:{r*2}px;height:{r*2}px;background:radial-gradient(circle,{c},transparent);opacity:{o}'></div>"
    body += text("NIGHT LIGHTS", 80, 80, 28, TX, 100, "left", 6)
    body += text("TOKYO BOKEH", 80, 118, 11, S, 300, "left", 6)
    render("09-bokeh-lights.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 10 — GEOMETRIC MANDALA TECH
# ═══════════════════════════════════════════════════════════════
def w10():
    css = f"""
    body {{ background: radial-gradient(ellipse at center, #13131e, {N}); }}
    .r {{ position:absolute; border-radius:50%; left:50%; top:50%; transform:translate(-50%,-50%); }}
    """
    body = ""
    for i in range(40):
        r = 30 + i * 22
        c = [PU, T, P][i % 3]
        o = 0.12 - i * 0.003
        w = 1 if i % 3 == 0 else 0.5
        body += f"<div class='r' style='width:{r*2}px;height:{r*2}px;border:{w}px solid {c};opacity:{max(o,0.02)}'></div>"
        if i % 4 == 0:
            body += f"<div class='r' style='width:{r*2}px;height:{r*2}px;border:{w*2}px dashed {c};opacity:{max(o*0.5,0.015)};border-radius:0;transform:translate(-50%,-50%) rotate({i*15}deg)'></div>"
    body += text("TOKYO NIGHT", 80, 80, 16, TX, 100, "left", 6)
    body += text("GEOMETRIC", 80, 110, 10, S, 300, "left", 6)
    render("10-mandala-tech.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 11 — MINIMALIST GEOMETRIC NIGHT (Variant A)
# ═══════════════════════════════════════════════════════════════
def w11():
    css = f"""
    body {{ background: linear-gradient(160deg, #13131f, {N}); }}
    .g {{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
          width:1000px; height:1000px; background:radial-gradient(circle at 60% 50%, {T}08, transparent);
          filter:blur(60px); }}
    """
    body = '<div class="g"></div>'
    for i in range(18):
        cx = 100 + (i % 6) * 300 + (i // 6) * 50
        cy = 200 + (i // 6) * 300
        r = 60 + (i % 3) * 30
        c = [T, P, PU][i % 3]
        body += circle(cx, cy, r, c, 0.15)
    body += text("26°C · TOKYO", 1380, 920, 18, T, 100, "right", 4)
    body += text("MINIMAL VARIANT A", 1380, 950, 10, S, 300, "right", 6)
    render("11-minimal-geometric-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 12 — GLASSMORPHISM (Variant A)
# ═══════════════════════════════════════════════════════════════
def w12():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #12101e); }}
    .g {{
      position:absolute; border-radius:16px;
      background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.04);
      backdrop-filter:blur(15px); box-shadow:0 4px 20px rgba(0,0,0,0.2);
    }}
    .a {{ position:absolute; width:300px; height:300px; border-radius:50%; filter:blur(60px); opacity:0.2; }}
    """
    body = f"""
    <div class='a' style='top:100px;left:100px;background:{P}'></div>
    <div class='a' style='bottom:100px;right:100px;background:{T}'></div>
    <div class='g' style='top:80px;left:80px;width:1760px;height:120px'></div>
    <div class='g' style='top:250px;left:80px;width:800px;height:700px'></div>
    <div class='g' style='top:250px;left:920px;width:920px;height:340px'></div>
    <div class='g' style='top:630px;left:920px;width:440px;height:320px'></div>
    <div class='g' style='top:630px;left:1390px;width:450px;height:320px'></div>
    """
    body += text("STYX", 1080, 340, 64, PU, 100, "left", 8)
    body += text("GLASS VARIANT A", 1080, 410, 12, S, 300, "left", 6)
    render("12-glassmorphism-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 13 — ABSTRACT NIGHT LANDSCAPE (Variant A) — Urban skyline
# ═══════════════════════════════════════════════════════════════
def w13():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #0e0e1a); }}
    .b {{ position:absolute; bottom:0; }}
    .s {{ height:1px; width:{'100%'}; background:linear-gradient(90deg,transparent,{T}44,transparent);
          position:absolute; bottom:350px; left:0; }}
    """
    body = f"<div class='s'></div>"
    buildings = [(0, 450, I), (60, 520, DP), (120, 380, I), (180, 600, DP), (260, 350, I),
                 (340, 500, DP), (420, 420, I), (490, 550, DP), (560, 380, I), (630, 480, DP),
                 (710, 600, I), (790, 400, DP), (860, 520, I), (940, 350, DP), (1000, 450, I),
                 (1080, 580, DP), (1160, 420, I), (1230, 500, DP), (1310, 380, I), (1380, 550, DP),
                 (1460, 440, I), (1530, 480, DP), (1590, 360, I), (1650, 520, DP), (1720, 400, I),
                 (1800, 460, DP), (1860, 350, I)]
    for x, h, c in buildings:
        body += f"<div class='b' style='left:{x}px;width:40px;height:{h}px;background:{c}'></div>"
        y_win = 20
        while y_win < h - 20:
            body += f"<div class='b' style='left:{x+8}px;width:24px;height:2px;background:{PU}33;bottom:{y_win}px'></div>"
            y_win += 25
    body += f"<div style='position:absolute;bottom:0;left:0;width:100%;height:400px;background:linear-gradient(0deg,{N},transparent)'></div>"
    body += text("TOKYO STREET", 80, 80, 24, TX, 100, "left", 5)
    body += text("URBAN VARIANT", 80, 115, 10, S, 300, "left", 6)
    render("13-night-landscape-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 14 — DEVELOPER CODE AESTHETIC (Variant A) — JSON
# ═══════════════════════════════════════════════════════════════
def w14():
    css = f"""
    body {{ background: {N}; }}
    .m {{ position:absolute; width:1px; height:100%;
          background:linear-gradient(180deg,transparent,{T}06,transparent); }}
    """
    body = ""
    for x in range(100, 1900, 120):
        body += f"<div class='m' style='left:{x}px'></div>"
    body += f"""
    <div style='position:absolute;left:120px;top:80px;font-family:monospace;font-size:13px;line-height:1.6;color:{TX};opacity:0.18;'>
    &nbsp;1 &#123; "theme": "tokyo_night",<br>
    &nbsp;2 &nbsp;&nbsp;"colors": &#123;<br>
    &nbsp;3 &nbsp;&nbsp;&nbsp;&nbsp;"primary": "<span style='color:{T}'>#26c6da</span>",<br>
    &nbsp;4 &nbsp;&nbsp;&nbsp;&nbsp;"accent": "<span style='color:{PU}'>#ab47bc</span>",<br>
    &nbsp;5 &nbsp;&nbsp;&nbsp;&nbsp;"highlight": "<span style='color:{P}'>#ec407a</span>",<br>
    &nbsp;6 &nbsp;&nbsp;&nbsp;&nbsp;"bg": "#1a1b26"<br>
    &nbsp;7 &nbsp;&nbsp;&#125;,<br>
    &nbsp;8 &nbsp;&nbsp;"fonts": [<br>
    &nbsp;9 &nbsp;&nbsp;&nbsp;&nbsp;"JetBrains Mono",<br>
    &nbsp;10 &nbsp;&nbsp;&nbsp;&nbsp;"SF Pro Display"<br>
    &nbsp;11 &nbsp;&nbsp;]<br>
    &nbsp;12 &#125;
    </div>
    """
    for i in range(30):
        body += f"<div style='position:absolute;left:{120+i*70}px;top:{200+i*25}px;font-family:monospace;font-size:8px;color:{T};opacity:0.03;'>01011000 01111001 01101100 01101111 01101110</div>"
    body += text("$ cat theme.json", 80, 920, 14, PU, 300, "left", 3)
    body += text("DEVELOPER VARIANT A · JSON", 80, 950, 9, S, 300, "left", 5)
    render("14-developer-code-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 15 — ORGANIC FLUID GRADIENT (Variant A)
# ═══════════════════════════════════════════════════════════════
def w15():
    css = f"""
    body {{ background: {N}; }}
    .b {{ position:absolute; border-radius:50%; filter:blur(90px); opacity:0.35; }}
    """
    body = f"""
    <div class='b' style='width:1000px;height:600px;top:-200px;left:-100px;background:{P}'></div>
    <div class='b' style='width:800px;height:800px;top:200px;left:400px;background:{PU}'></div>
    <div class='b' style='width:900px;height:500px;bottom:-100px;right:-200px;background:{T}'></div>
    <div class='b' style='width:400px;height:400px;top:700px;left:200px;background:{P}'></div>
    """
    render("15-fluid-gradient-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 16 — RETRO CYBERPUNK GRID (Variant A) — Diagonal perspective
# ═══════════════════════════════════════════════════════════════
def w16():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #080810); }}
    .grid {{
      position:absolute;top:0;left:0;width:100%;height:100%;
      background-image:
        linear-gradient(rgba(38,198,218,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(171,71,188,0.03) 1px, transparent 1px);
      background-size:60px 60px;
      transform:perspective(600px) rotateX(60deg) rotateZ(-10deg);
      transform-origin:50% 100%;
    }}
    .sg {{ position:absolute; bottom:0; width:100%; height:400px;
           background:linear-gradient(0deg, {N}, transparent); }}
    .s {{ position:absolute;bottom:300px;left:50%;transform:translateX(-50%);
          width:200px;height:200px;border-radius:50%;
          background:radial-gradient(circle, {T}, transparent);
          opacity:0.3;filter:blur(30px); }}
    """
    body = f"<div class='grid'></div><div class='sg'></div><div class='s'></div>"
    body += text("NIGHT", 80, 80, 56, T, 100, "left", 10)
    body += text("SYNTHWAVE", 80, 145, 12, S, 300, "left", 8)
    render("16-retro-grid-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 17 — MATERIAL YOU BUBBLES (Variant A)
# ═══════════════════════════════════════════════════════════════
def w17():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #12121e); }}
    .b {{
      position:absolute; border-radius:50%;
      background:rgba(255,255,255,0.02);
      border:1px solid rgba(255,255,255,0.04);
      box-shadow:inset 0 -30px 60px rgba(0,0,0,0.15), 0 15px 40px rgba(0,0,0,0.2);
    }}
    """
    body = ""
    for cx, cy, r, c in [
        (560, 540, 320, T), (1360, 540, 280, P),
        (400, 200, 100, PU), (1520, 200, 120, T),
        (200, 800, 80, P), (1720, 800, 90, PU),
        (960, 200, 60, T), (960, 880, 60, P),
    ]:
        body += f"<div class='b' style='left:{cx-r}px;top:{cy-r}px;width:{r*2}px;height:{r*2}px;border-color:{c}22'></div>"
        body += f"<div style='position:absolute;left:{cx-r//2}px;top:{cy-r//2}px;width:{r}px;height:{r}px;border-radius:50%;background:radial-gradient(circle at 30% 30%, rgba(255,255,255,0.06), transparent)'></div>"
    body += text("bubbles · 泡", 1480, 930, 18, TX, 100, "right", 4)
    body += text("VARIANT A · OVERLAP", 1480, 960, 10, S, 300, "right", 6)
    render("17-bubbles-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 18 — DYNAMIC FLOWING LINES (Variant A) — Vertical
# ═══════════════════════════════════════════════════════════════
def w18():
    css = f"""
    body {{ background: linear-gradient(180deg, {N}, #11101a); }}
    .g {{ position:absolute; width:500px; height:500px; border-radius:50%; filter:blur(80px); opacity:0.12; }}
    """
    body = f"""
    <div class='g' style='top:300px;left:-100px;background:{T}'></div>
    <div class='g' style='top:200px;right:-100px;background:{P}'></div>
    """
    for i in range(50):
        x = 80 + i * 36
        h = 400 + 300 * math.sin(i * 0.2)
        y = 200 + 100 * math.sin(i * 0.5)
        c = [T, PU, P][i % 3]
        body += f"<div style='position:absolute;left:{x}px;top:{y}px;width:1px;height:{h}px;background:linear-gradient(180deg,{c}00,{c},{c}00);opacity:0.12'></div>"
    body += text("vertical flow", 80, 80, 32, T, 100, "left", 5)
    body += text("BRUSHSTROKE VARIANT", 80, 120, 10, S, 300, "left", 6)
    render("18-flowing-lines-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 19 — BOKEH NIGHT LIGHTS (Variant A) — Center concentration
# ═══════════════════════════════════════════════════════════════
def w19():
    css = f"""
    body {{ background: linear-gradient(180deg, #0a0a14, {N}); }}
    .b {{ position:absolute; border-radius:50%; filter:blur(12px); }}
    .v {{ position:absolute;top:0;left:0;width:100%;height:100%;
          background:radial-gradient(ellipse at 50% 50%, transparent 30%, #0a0a1488 100%); }}
    """
    body = "<div class='v'></div>"
    for i in range(50):
        cx = 960 + 400 * math.cos(i * 0.5)
        cy = 540 + 300 * math.sin(i * 0.7)
        r = 20 + 30 * math.sin(i * 1.3) + 20
        c = [T, P, PU][i % 3]
        o = 0.15 + 0.15 * math.sin(i * 0.9)
        body += f"<div class='b' style='left:{cx-r}px;top:{cy-r}px;width:{r*2}px;height:{r*2}px;background:radial-gradient(circle,{c},transparent);opacity:{o}'></div>"
    body += text("BOKEH · ボケ", 80, 80, 24, TX, 100, "left", 5)
    body += text("VIGNETTE VARIANT", 80, 115, 10, S, 300, "left", 6)
    render("19-bokeh-lights-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
# 20 — GEOMETRIC MANDALA TECH (Variant A) — Corner placement
# ═══════════════════════════════════════════════════════════════
def w20():
    css = f"""
    body {{ background: radial-gradient(ellipse at 70% 50%, #12121e, {N}); }}
    .r {{ position:absolute; border-radius:50%; }}
    .sq {{ position:absolute; }}
    """
    body = ""
    cx, cy = 1400, 300
    for i in range(30):
        r = 20 + i * 18
        c = [PU, T, P][i % 3]
        o = 0.15 - i * 0.005
        w = 1 if i % 2 == 0 else 0.5
        body += f"<div class='r' style='left:{cx-r}px;top:{cy-r}px;width:{r*2}px;height:{r*2}px;border:{w}px solid {c};opacity:{max(o,0.02)}'></div>"
        body += f"<div class='sq' style='left:{cx-r}px;top:{cy-r}px;width:{r*2}px;height:{r*2}px;border:{w}px dashed {c};opacity:{max(o*0.5,0.01)};transform:rotate({i*12}deg);transform-origin:{cx}px {cy}px'></div>"
    # secondary cluster bottom-left
    cx2, cy2 = 400, 800
    for i in range(20):
        r = 15 + i * 14
        c = [T, PU, P][i % 3]
        o = 0.10 - i * 0.005
        body += f"<div class='r' style='left:{cx2-r}px;top:{cy2-r}px;width:{r*2}px;height:{r*2}px;border:0.5px solid {c};opacity:{max(o,0.015)}'></div>"
    body += text("TOKYO NIGHT", 80, 80, 16, TX, 100, "left", 6)
    body += text("MANDALA VARIANT A", 80, 110, 10, S, 300, "left", 6)
    render("20-mandala-tech-a.png", body, css)


# ═══════════════════════════════════════════════════════════════
def generate_all():
    os.makedirs(OUT, exist_ok=True)
    print(f"\n  TOKYO NIGHT + MATERIAL YOU — 20 WALLPAPERS\n")
    print(f"  Resolución: {W}x{H}  |  Output: {OUT}/\n")
    for i, fn in enumerate([
        w01, w02, w03, w04, w05, w06, w07, w08, w09, w10,
        w11, w12, w13, w14, w15, w16, w17, w18, w19, w20,
    ], 1):
        print(f"  [{i:02d}/20]", end="")
        fn()
    print(f"\n  ✓ 20 wallpapers generados\n")

if __name__ == "__main__":
    generate_all()
