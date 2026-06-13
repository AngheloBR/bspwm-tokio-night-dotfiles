#!/usr/bin/env python3
"""
Genera 10 wallpapers Tokyo Night + Material You usando HTML+CSS
Convertidos a PNG con WeasyPrint (1920x1080)
"""

import os
import subprocess
from weasyprint import HTML

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "wallpapers"))
W, H = 1920, 1080

CSS_BASE = """
  @page { size: 1920px 1080px; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { width: 1920px; height: 1080px; overflow: hidden; position: relative; }
"""

# Paleta Tokyo Night
TN = {
    "bg": "#1a1b26", "surface": "#24283b", "surface2": "#2f3549",
    "blue": "#7aa2f7", "cyan": "#7dcfff", "green": "#9ece6a",
    "orange": "#e0af68", "red": "#f7768e", "purple": "#bb9af7",
    "text": "#c0caf5", "subtext": "#565f89", "pink": "#ff9e64",
}

def render(name, body_html, extra_css=""):
    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<style>
{CSS_BASE}
{extra_css}
</style>
</head>
<body>
{body_html}
</body>
</html>"""
    os.makedirs(OUT_DIR, exist_ok=True)
    pdf_path = os.path.join(OUT_DIR, name.replace(".png", ".pdf"))
    png_path = os.path.join(OUT_DIR, name)
    HTML(string=html).write_pdf(pdf_path)
    subprocess.run(["pdftoppm", "-png", "-r", "96", "-singlefile",
                    pdf_path, png_path.replace(".png", "")],
                   capture_output=True, check=True)
    os.remove(pdf_path)
    size_kb = os.path.getsize(png_path) // 1024
    print(f"  ✓ {name} ({size_kb} KB)")


def w1_glass_orbs():
    """Esferas flotantes glassmorphism + mesh gradient"""
    css = f"""
    body {{
      background: linear-gradient(135deg, {TN['bg']} 0%, #13141f 50%, {TN['bg']} 100%);
    }}
    .orb {{
      position: absolute;
      border-radius: 50%;
      filter: blur(60px);
      opacity: 0.4;
    }}
    .o1 {{ width: 600px; height: 600px; top: -100px; left: -100px;
           background: radial-gradient(circle, {TN['blue']}, {TN['purple']}); }}
    .o2 {{ width: 500px; height: 500px; bottom: -150px; right: -100px;
           background: radial-gradient(circle, {TN['cyan']}, {TN['blue']}); }}
    .o3 {{ width: 400px; height: 400px; top: 300px; left: 700px;
           background: radial-gradient(circle, {TN['purple']}, {TN['pink']}); }}
    .card {{
      position: absolute;
      top: 50%; left: 50%; transform: translate(-50%, -50%);
      width: 500px; height: 280px;
      background: rgba(36, 40, 59, 0.35);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(122, 162, 247, 0.15);
      border-radius: 24px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
    }}
    .card h1 {{ color: {TN['blue']}; font-family: sans-serif; font-size: 32px;
                letter-spacing: 4px; font-weight: 300; margin-bottom: 8px; }}
    .card p {{ color: {TN['text']}; font-family: sans-serif; font-size: 14px;
               opacity: 0.6; letter-spacing: 2px; }}
    .line {{ width: 60px; height: 1px; background: {TN['blue']}; margin: 12px 0; opacity: 0.4; }}
    """
    body = """
    <div class="orb o1"></div>
    <div class="orb o2"></div>
    <div class="orb o3"></div>
    <div class="card">
      <h1>TOKYO NIGHT</h1>
      <div class="line"></div>
      <p>STYX</p>
    </div>"""
    render("tokyo-glass-orbs.png", body, css)


def w2_mountains():
    """Montañas CSS clip-path con cielo estrellado"""
    css = f"""
    body {{
      background: linear-gradient(180deg, {TN['bg']} 0%, #13141f 40%, {TN['surface']} 100%);
    }}
    .star {{ position: absolute; width: 2px; height: 2px; background: {TN['text']};
             border-radius: 50%; opacity: 0.5; }}
    .mountain {{
      position: absolute; bottom: 0; width: 100%; height: 700px;
    }}
    .m1 {{
      clip-path: polygon(0% 100%, 5% 50%, 15% 55%, 22% 35%, 30% 45%, 38% 25%, 45% 35%,
                         50% 20%, 55% 30%, 62% 15%, 70% 25%, 78% 30%, 85% 20%,
                         92% 35%, 100% 40%, 100% 100%);
      background: linear-gradient(180deg, {TN['purple']}44, {TN['purple']}22);
    }}
    .m2 {{
      clip-path: polygon(0% 100%, 3% 55%, 12% 60%, 18% 40%, 25% 50%, 32% 30%,
                         40% 45%, 48% 35%, 55% 48%, 62% 25%, 70% 35%,
                         78% 20%, 85% 30%, 92% 25%, 100% 35%, 100% 100%);
      background: linear-gradient(180deg, {TN['blue']}33, {TN['blue']}11);
    }}
    .m3 {{
      clip-path: polygon(0% 100%, 0% 60%, 8% 65%, 15% 45%, 22% 55%,
                         30% 40%, 38% 50%, 45% 30%, 52% 45%, 60% 35%,
                         68% 50%, 75% 28%, 82% 40%, 90% 30%, 100% 45%, 100% 100%);
      background: {TN['surface']};
    }}
    .peak {{
      position: absolute; width: 4px; height: 30px;
      background: linear-gradient(180deg, {TN['cyan']}, transparent);
      filter: blur(2px);
    }}
    .sun {{
      position: absolute; top: 250px; left: 50%; transform: translateX(-50%);
      width: 120px; height: 120px; border-radius: 50%;
      background: radial-gradient(circle, {TN['cyan']}44, transparent);
      filter: blur(20px);
    }}
    """
    stars = "".join(f'<div class="star" style="top:{r*1000}px;left:{r*1900}px"></div>'
                    for r in [0.05, 0.12, 0.18, 0.23, 0.31, 0.37, 0.42, 0.48, 0.55, 0.61, 0.67, 0.73, 0.79, 0.84, 0.91])
    body = f"""
    {stars}
    <div class="sun"></div>
    <div class="mountain m3"></div>
    <div class="mountain m2"></div>
    <div class="mountain m1"></div>
    """
    render("tokyo-mountains.png", body, css)


def w3_neon_grid():
    """Grid cyberpunk con sol central"""
    css = f"""
    body {{
      background: linear-gradient(180deg, {TN['bg']} 0%, #0f0f1a 100%);
    }}
    .grid {{
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background-image:
        linear-gradient(rgba(122,162,247,0.06) 1px, transparent 1px),
        linear-gradient(90deg, rgba(122,162,247,0.06) 1px, transparent 1px);
      background-size: 60px 60px;
    }}
    .horizon {{
      position: absolute; top: 50%; left: 0; width: 100%; height: 400px;
      background: linear-gradient(180deg, transparent, {TN['blue']}08);
    }}
    .sun-glow {{
      position: absolute; top: 380px; left: 50%; transform: translateX(-50%);
      width: 500px; height: 300px;
      background: radial-gradient(ellipse at center, {TN['cyan']}22, {TN['blue']}11, transparent);
      filter: blur(40px);
    }}
    .sun {{
      position: absolute; top: 420px; left: 50%; transform: translateX(-50%);
      width: 100px; height: 100px; border-radius: 50%;
      background: radial-gradient(circle, #fff, {TN['cyan']}, {TN['blue']}66);
      box-shadow: 0 0 80px {TN['cyan']}44, 0 0 200px {TN['blue']}22;
    }}
    .vline {{
      position: absolute; height: 100%;
      width: 1px;
      background: linear-gradient(180deg, transparent, {TN['blue']}15, transparent);
    }}
    """
    vlines = "".join(f'<div class="vline" style="left:{x}px"></div>' for x in range(60, 1920, 120))
    body = f"""
    <div class="grid"></div>
    <div class="horizon"></div>
    <div class="sun-glow"></div>
    <div class="sun"></div>
    {vlines}
    """
    render("tokyo-neon-grid.png", body, css)


def w4_concentric_rings():
    """Anillos concéntricos con glow"""
    css = f"""
    body {{
      background: radial-gradient(ellipse at center, #1a1b32, {TN['bg']});
    }}
    .ring {{
      position: absolute; border-radius: 50%;
      border: 1px solid; left: 50%; top: 50%;
      transform: translate(-50%, -50%);
    }}
    .glow {{
      position: absolute; border-radius: 50%;
      left: 50%; top: 50%; transform: translate(-50%, -50%);
      filter: blur(60px);
    }}
    .center {{
      position: absolute; border-radius: 50%;
      left: 50%; top: 50%; transform: translate(-50%, -50%);
      width: 8px; height: 8px;
      background: {TN['blue']};
      box-shadow: 0 0 40px {TN['blue']}, 0 0 80px {TN['blue']}44;
    }}
    """
    rings_data = [
        (60, TN['blue'], 0.15), (100, TN['cyan'], 0.12), (150, TN['purple'], 0.10),
        (200, TN['blue'], 0.08), (260, TN['cyan'], 0.07), (330, TN['purple'], 0.06),
        (410, TN['blue'], 0.05), (500, TN['cyan'], 0.04), (600, TN['purple'], 0.03),
        (720, TN['blue'], 0.025), (850, TN['cyan'], 0.02), (1000, TN['purple'], 0.015),
    ]
    rings = "".join(f'<div class="ring" style="width:{r*2}px;height:{r*2}px;border-color:{c}{hex(int(a*255))[2:].zfill(2)}"></div>'
                    for r, c, a in rings_data)
    body = f"""
    <div class="glow" style="width:300px;height:300px;background:{TN['blue']}15"></div>
    <div class="glow" style="width:500px;height:500px;background:{TN['purple']}10"></div>
    {rings}
    <div class="center"></div>
    """
    render("tokyo-concentric-rings.png", body, css)


def w5_blobs():
    """Formas orgánicas Material You con blur"""
    css = f"""
    body {{
      background: linear-gradient(135deg, {TN['bg']}, #11111f, {TN['bg']});
    }}
    .blob {{
      position: absolute; border-radius: 50%;
      filter: blur(50px); opacity: 0.35;
    }}
    .b1 {{
      width: 700px; height: 550px; top: -50px; left: -100px;
      background: {TN['blue']};
      border-radius: 60% 40% 70% 30%;
    }}
    .b2 {{
      width: 600px; height: 600px; bottom: -100px; right: -80px;
      background: {TN['purple']};
      border-radius: 50% 50% 30% 70%;
    }}
    .b3 {{
      width: 450px; height: 450px; top: 350px; left: 600px;
      background: {TN['cyan']};
      border-radius: 40% 60% 50% 50%;
    }}
    .b4 {{
      width: 300px; height: 300px; top: 100px; right: 200px;
      background: {TN['pink']};
      border-radius: 70% 30% 50% 50%;
    }}
    .b5 {{
      width: 250px; height: 250px; bottom: 200px; left: 300px;
      background: {TN['green']};
      border-radius: 30% 70% 60% 40%;
    }}
    .label {{
      position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
      color: {TN['text']}; font-family: sans-serif; font-size: 48px;
      font-weight: 100; letter-spacing: 8px; text-shadow: 0 0 40px rgba(0,0,0,0.8);
      opacity: 0.8;
    }}
    .sub {{
      position: absolute; top: 55%; left: 50%; transform: translate(-50%, -50%);
      color: {TN['subtext']}; font-family: sans-serif; font-size: 14px;
      letter-spacing: 6px; margin-top: 20px;
    }}
    """
    body = """
    <div class="blob b1"></div>
    <div class="blob b2"></div>
    <div class="blob b3"></div>
    <div class="blob b4"></div>
    <div class="blob b5"></div>
    <div class="label">TOKYO</div>
    <div class="sub">MATERIAL YOU</div>
    """
    render("tokyo-blobs.png", body, css)


def w6_waves():
    """Olas CSS con gradiente"""
    css = f"""
    body {{
      background: linear-gradient(180deg, {TN['bg']}, #11111f, {TN['surface']});
    }}
    .wave {{
      position: absolute; bottom: 0; width: 100%;
    }}
    .w1 {{
      height: 400px;
      background: linear-gradient(180deg, transparent, {TN['blue']}08);
      mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 400'%3E%3Cpath d='M0,200 C320,40 640,360 960,200 C1280,40 1600,360 1920,200 L1920,400 L0,400 Z' fill='black'/%3E%3C/svg%3E");
      -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 400'%3E%3Cpath d='M0,200 C320,40 640,360 960,200 C1280,40 1600,360 1920,200 L1920,400 L0,400 Z' fill='black'/%3E%3C/svg%3E");
    }}
    .w2 {{
      height: 350px;
      background: linear-gradient(180deg, transparent, {TN['purple']}06);
      mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 350'%3E%3Cpath d='M0,175 C400,350 800,0 1200,175 C1600,350 1800,0 1920,175 L1920,350 L0,350 Z' fill='black'/%3E%3C/svg%3E");
      -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 350'%3E%3Cpath d='M0,175 C400,350 800,0 1200,175 C1600,350 1800,0 1920,175 L1920,350 L0,350 Z' fill='black'/%3E%3C/svg%3E");
    }}
    .w3 {{
      height: 300px;
      background: linear-gradient(180deg, transparent, {TN['cyan']}04);
      mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 300'%3E%3Cpath d='M0,150 C300,0 600,300 900,150 C1200,0 1500,300 1920,150 L1920,300 L0,300 Z' fill='black'/%3E%3C/svg%3E");
      -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 300'%3E%3Cpath d='M0,150 C300,0 600,300 900,150 C1200,0 1500,300 1920,150 L1920,300 L0,300 Z' fill='black'/%3E%3C/svg%3E");
    }}
    .dot {{
      position: absolute; width: 3px; height: 3px;
      border-radius: 50%; opacity: 0.3;
    }}
    """
    dots = "".join(f'<div class="dot" style="top:{r*1000}px;left:{r*1900}px;background:{TN["blue"]}"></div>'
                   for r in [0.03, 0.08, 0.15, 0.22, 0.28, 0.35, 0.42, 0.48, 0.55, 0.62, 0.68, 0.75, 0.82, 0.88, 0.95])
    body = f"""
    {dots}
    <div class="wave w3"></div>
    <div class="wave w2"></div>
    <div class="wave w1"></div>
    """
    render("tokyo-waves.png", body, css)


def w7_dots():
    """Patrón de puntos con glow central"""
    css = f"""
    body {{
      background: {TN['bg']};
    }}
    .dot-grid {{
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background-image: radial-gradient(circle, {TN['subtext']}33 1px, transparent 1px);
      background-size: 40px 40px;
    }}
    .glow-center {{
      position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
      width: 600px; height: 600px; border-radius: 50%;
      background: radial-gradient(circle, {TN['blue']}15, {TN['purple']}08, transparent);
      filter: blur(40px);
    }}
    .ring-dot {{
      position: absolute; border-radius: 50%;
      left: 50%; top: 50%; transform: translate(-50%, -50%);
      background: radial-gradient(circle, {TN['blue']}44, transparent);
    }}
    .vline {{
      position: absolute; width: 1px; height: 100%;
      background: linear-gradient(180deg, transparent, {TN['blue']}08, transparent);
    }}
    .hline {{
      position: absolute; height: 1px; width: 100%;
      background: linear-gradient(90deg, transparent, {TN['blue']}08, transparent);
    }}
    """
    body = """
    <div class="dot-grid"></div>
    <div class="glow-center"></div>
    <div class="vline" style="left:20%"></div>
    <div class="vline" style="left:40%"></div>
    <div class="vline" style="left:60%"></div>
    <div class="vline" style="left:80%"></div>
    <div class="hline" style="top:20%"></div>
    <div class="hline" style="top:40%"></div>
    <div class="hline" style="top:60%"></div>
    <div class="hline" style="top:80%"></div>
    """
    render("tokyo-dots.png", body, css)


def w8_minimal_dawn():
    """Amanecer minimalista con sol"""
    css = f"""
    body {{
      background: linear-gradient(180deg, {TN['bg']} 0%, #171725 40%, #1f1f35 100%);
    }}
    .horizon {{
      position: absolute; top: 55%; left: 0; width: 100%; height: 1px;
      background: linear-gradient(90deg, transparent, {TN['blue']}22, transparent);
    }}
    .sun {{
      position: absolute; top: 45%; left: 50%; transform: translate(-50%, -50%);
      width: 100px; height: 100px; border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, {TN['orange']}, #d06a3a);
      box-shadow:
        0 0 40px {TN['orange']}44,
        0 0 80px {TN['orange']}33,
        0 0 160px {TN['orange']}22,
        0 0 300px {TN['pink']}11;
    }}
    .glow-bg {{
      position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%);
      width: 800px; height: 400px;
      background: radial-gradient(ellipse at center, {TN['orange']}11, transparent);
      filter: blur(60px);
    }}
    .mount {{
      position: absolute; bottom: 0; width: 100%; height: 450px;
      background: linear-gradient(180deg, {TN['surface']}88, {TN['bg']});
      clip-path: polygon(0% 100%, 2% 80%, 5% 82%, 8% 70%, 12% 72%, 15% 60%,
                         18% 65%, 22% 50%, 25% 55%, 28% 45%, 32% 48%, 35% 38%,
                         38% 42%, 42% 35%, 45% 38%, 48% 28%, 52% 32%, 55% 25%,
                         58% 28%, 62% 20%, 65% 25%, 68% 18%, 72% 22%, 75% 15%,
                         78% 18%, 82% 12%, 85% 15%, 88% 10%, 92% 14%, 95% 8%,
                         98% 12%, 100% 15%, 100% 100%);
    }}
    """
    body = """
    <div class="glow-bg"></div>
    <div class="sun"></div>
    <div class="horizon"></div>
    <div class="mount"></div>
    """
    render("tokyo-minimal-dawn.png", body, css)


def w9_polygons():
    """Fragmentos poligonales con glass"""
    css = f"""
    body {{
      background: linear-gradient(135deg, {TN['bg']}, #0e0e1a);
    }}
    .shard {{
      position: absolute;
      opacity: 0.15;
      backdrop-filter: blur(10px);
      border: 1px solid;
    }}
    .s1 {{
      top: 5%; left: 5%; width: 300px; height: 300px;
      background: linear-gradient(135deg, {TN['blue']}22, {TN['purple']}11);
      border-color: {TN['blue']}22;
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      transform: rotate(15deg);
    }}
    .s2 {{
      top: 60%; left: 60%; width: 400px; height: 400px;
      background: linear-gradient(225deg, {TN['purple']}22, {TN['cyan']}11);
      border-color: {TN['purple']}22;
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      transform: rotate(-10deg);
    }}
    .s3 {{
      top: 30%; left: 70%; width: 200px; height: 200px;
      background: linear-gradient(45deg, {TN['cyan']}22, {TN['blue']}11);
      border-color: {TN['cyan']}22;
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      transform: rotate(25deg);
    }}
    .s4 {{
      top: 55%; left: 15%; width: 250px; height: 250px;
      background: linear-gradient(180deg, {TN['pink']}22, {TN['orange']}11);
      border-color: {TN['pink']}22;
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      transform: rotate(-20deg);
    }}
    .s5 {{
      top: 15%; left: 55%; width: 180px; height: 180px;
      background: linear-gradient(90deg, {TN['green']}22, {TN['cyan']}11);
      border-color: {TN['green']}22;
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      transform: rotate(40deg);
    }}
    .center-glow {{
      position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
      width: 300px; height: 300px; border-radius: 50%;
      background: radial-gradient(circle, {TN['blue']}10, transparent);
      filter: blur(30px);
    }}
    """
    body = """
    <div class="shard s1"></div>
    <div class="shard s2"></div>
    <div class="shard s3"></div>
    <div class="shard s4"></div>
    <div class="shard s5"></div>
    <div class="center-glow"></div>
    """
    render("tokyo-polygons.png", body, css)


def w10_line_art():
    """Arte lineal minimalista"""
    css = f"""
    body {{
      background: linear-gradient(160deg, {TN['bg']}, #111122);
    }}
    .canvas {{
      position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
      width: 800px; height: 600px;
    }}
    .curve {{
      position: absolute;
      width: 100%; height: 100%;
    }}
    .c1 {{
      border: 1px solid {TN['blue']}33;
      border-radius: 50%;
      top: 10%; left: 10%; width: 80%; height: 80%;
    }}
    .c2 {{
      border: 1px solid {TN['purple']}22;
      border-radius: 50%;
      top: 20%; left: 15%; width: 70%; height: 60%;
    }}
    .c3 {{
      border: 1px solid {TN['cyan']}22;
      border-radius: 50%;
      top: 5%; left: 25%; width: 50%; height: 90%;
    }}
    .c4 {{
      border: 1px solid {TN['pink']}18;
      border-radius: 50%;
      top: 30%; left: 5%; width: 90%; height: 40%;
    }}
    .dot {{
      position: absolute; width: 4px; height: 4px;
      border-radius: 50%; background: {TN['blue']}; opacity: 0.6;
    }}
    .line-h {{
      position: absolute; height: 1px; width: 200px;
      background: linear-gradient(90deg, transparent, {TN['blue']}44, transparent);
    }}
    .line-v {{
      position: absolute; width: 1px; height: 200px;
      background: linear-gradient(180deg, transparent, {TN['purple']}44, transparent);
    }}
    .label {{
      position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%);
      color: {TN['subtext']}; font-family: sans-serif; font-size: 11px;
      letter-spacing: 6px; opacity: 0.5;
    }}
    """
    body = """
    <div class="canvas">
      <div class="curve c1"></div>
      <div class="curve c2"></div>
      <div class="curve c3"></div>
      <div class="curve c4"></div>
      <div class="dot" style="top:30%;left:50%"></div>
      <div class="dot" style="top:50%;left:30%"></div>
      <div class="dot" style="top:60%;left:70%"></div>
      <div class="dot" style="top:25%;left:65%"></div>
      <div class="dot" style="top:70%;left:40%"></div>
      <div class="line-h" style="top:50%;left:50%"></div>
      <div class="line-v" style="top:50%;left:50%"></div>
    </div>
    <div class="label">MINIMAL</div>
    """
    render("tokyo-line-art.png", body, css)


def generate_all():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"\n  Generando 10 wallpapers HTML+CSS en {OUT_DIR}/\n")
    print(f"  Resolución: {W}x{H}\n")

    w1_glass_orbs()
    w2_mountains()
    w3_neon_grid()
    w4_concentric_rings()
    w5_blobs()
    w6_waves()
    w7_dots()
    w8_minimal_dawn()
    w9_polygons()
    w10_line_art()

    print(f"\n  ¡Listo! 10 wallpapers generados.\n")

if __name__ == "__main__":
    generate_all()
