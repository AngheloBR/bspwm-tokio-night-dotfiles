#!/usr/bin/env python3
"""
Wallpapers Generator - Tokyo Night + Material You
Genera 10 wallpapers únicos en 1920x1080
"""

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random
import os

W, H = 1920, 1080
OUT_DIR = os.path.join(os.path.dirname(__file__) or ".", "..", "wallpapers")

# Tokyo Night palette
TN = {
    "bg": (26, 27, 38),
    "surface": (36, 40, 59),
    "surface2": (47, 53, 73),
    "blue": (122, 162, 247),
    "cyan": (125, 207, 255),
    "green": (158, 206, 106),
    "orange": (224, 175, 104),
    "red": (247, 118, 142),
    "purple": (187, 154, 247),
    "text": (192, 202, 245),
    "subtext": (86, 95, 137),
    "pink": (255, 158, 100),
}

def lerp_color(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))

def gradient_h(img, c1, c2):
    draw = ImageDraw.Draw(img)
    for x in range(W):
        t = x / W
        c = lerp_color(c1, c2, t)
        draw.line([(x, 0), (x, H)], fill=c)

def gradient_v(img, c1, c2):
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = lerp_color(c1, c2, t)
        draw.line([(0, y), (W, y)], fill=c)

def gradient_diag(img, c1, c2):
    draw = ImageDraw.Draw(img)
    for i in range(W + H):
        t = i / (W + H)
        c = lerp_color(c1, c2, t)
        for x in range(max(0, i - H), min(W, i)):
            y = i - x
            draw.point((x, y), fill=c)

def soft_glow(draw, cx, cy, r, color, steps=8):
    for s in range(steps, 0, -1):
        t = s / steps
        rr = int(r * (1 + 0.5 * (1 - t)))
        alpha = int(40 * t)
        c = (*color[:3], alpha)
        draw.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)

def draw_circle(draw, cx, cy, r, color, width=None):
    if width:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=width)
    else:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def wallpaper_01_aurora():
    """Aurora - curvas de luz gradiente"""
    img = Image.new("RGBA", (W, H), TN["bg"])
    draw = ImageDraw.Draw(img)

    gradient_v(img, TN["bg"], (18, 19, 30))

    curves = [
        (TN["blue"], 600, 300, 800, 700),
        (TN["purple"], 900, 200, 1000, 800),
        (TN["cyan"], 300, 400, 1200, 600),
        (TN["pink"], 1300, 250, 700, 750),
    ]

    for color, x1, y1, x2, y2 in curves:
        for offset in range(-30, 31, 3):
            t = abs(offset) / 30
            alpha = int(30 * (1 - t * 0.5))
            pts = []
            for x in range(0, W, 3):
                y = y1 + (y2 - y1) * (x / W) + offset * math.sin(x * 0.008) + 20 * math.sin(x * 0.003)
                pts.append((x, y + 10 * math.sin(x * 0.005 + offset)))
            if len(pts) > 1:
                draw.line(pts, fill=(*color, alpha), width=2)

    return img


def wallpaper_02_mountains():
    """Montañas geométricas - triángulos superpuestos"""
    img = Image.new("RGBA", (W, H))
    gradient_v(img, TN["bg"], (30, 34, 50))
    draw = ImageDraw.Draw(img)

    layers = [
        (TN["purple"], 0.8, 0.6),
        (TN["blue"], 0.7, 0.7),
        (TN["cyan"], 0.6, 0.8),
        (TN["surface2"], 0.5, 0.9),
    ]

    for color, min_h, max_h in layers:
        pts = [(0, H)]
        peaks = []
        x = 0
        while x <= W:
            h = int(H * (min_h + random.random() * (max_h - min_h)))
            peaks.append((x, h))
            x += random.randint(80, 200)
        peaks[-1] = (W, peaks[-1][1])

        for px, py in peaks:
            pts.append((px, py))

        draw.polygon(pts, fill=(*color, 180), outline=(*color, 200))

        for px, py in peaks:
            if random.random() > 0.5:
                snow_h = py - random.randint(10, 30)
                draw.polygon([(px - 15, py), (px, snow_h), (px + 15, py)], fill=(200, 210, 230, 100))

    return img


def wallpaper_03_neongrid():
    """Neon Grid - cuadrícula cyberpunk con glow"""
    img = Image.new("RGBA", (W, H), TN["bg"])
    draw = ImageDraw.Draw(img)

    gradient_v(img, TN["bg"], (20, 22, 40))

    gap = 80
    for x in range(0, W + gap, gap):
        alpha = int(40 + 20 * math.sin(x * 0.01))
        draw.line([(x, 0), (x, H)], fill=(*TN["blue"], alpha), width=1)

    for y in range(0, H + gap, gap):
        alpha = int(40 + 20 * math.sin(y * 0.01))
        draw.line([(0, y), (W, y)], fill=(*TN["blue"], alpha), width=1)

    # Horizon glow
    for i in range(30):
        y = H // 2 + int(50 * math.sin(i * 0.3))
        alpha = int(60 - i * 2)
        soft_glow(draw, W // 2, y, 200 + i * 10, TN["cyan"], 4)

    # Sun
    draw_circle(draw, W // 2, H // 2 + 40, 80, (*TN["cyan"], 200))
    draw_circle(draw, W // 2, H // 2 + 40, 60, (*TN["blue"], 220))
    draw_circle(draw, W // 2, H // 2 + 40, 30, (255, 255, 255, 200))

    return img


def wallpaper_04_concentric():
    """Anillos concéntricos con glow"""
    img = Image.new("RGBA", (W, H))
    gradient_diag(img, TN["bg"], (30, 34, 55))
    draw = ImageDraw.Draw(img)

    centers = [
        (W // 3, H // 3),
        (2 * W // 3, 2 * H // 3),
        (W // 2, H // 2),
    ]
    colors = [TN["blue"], TN["purple"], TN["cyan"]]

    for cx, cy in centers:
        for r in range(50, 600, 30):
            color = random.choice(colors)
            alpha = int(60 - (r / 600) * 40)
            draw.ellipse(
                [cx - r, cy - r, cx + r, cy + r],
                outline=(*color, alpha),
                width=2,
            )

        # Center glow
        soft_glow(draw, cx, cy, 80, random.choice(colors), 6)

    return img


def wallpaper_05_blobs():
    """Material You blobs - formas orgánicas"""
    img = Image.new("RGBA", (W, H), TN["bg"])
    draw = ImageDraw.Draw(img)

    gradient_v(img, TN["bg"], (30, 34, 52))

    blobs = [
        (600, 400, 350, TN["blue"]),
        (1400, 600, 300, TN["purple"]),
        (400, 800, 250, TN["cyan"]),
        (1000, 300, 280, TN["pink"]),
        (1600, 350, 200, TN["green"]),
        (200, 200, 180, TN["orange"]),
    ]

    for cx, cy, r, color in blobs:
        pts = []
        for a in range(0, 360, 3):
            rad = math.radians(a)
            noise = r + random.randint(-30, 30) + 20 * math.sin(rad * 3) + 15 * math.cos(rad * 5)
            px = cx + noise * math.cos(rad)
            py = cy + noise * math.sin(rad)
            pts.append((px, py))

        draw.polygon(pts, fill=(*color, 120))
        draw.polygon(pts, outline=(*color, 200), width=2)

    return img


def wallpaper_06_waves():
    """Olas luminosas - sine waves con glow"""
    img = Image.new("RGBA", (W, H), TN["bg"])
    draw = ImageDraw.Draw(img)

    gradient_v(img, (20, 22, 38), (30, 34, 55))

    waves_params = [
        (TN["blue"], 0.2, 0.4, 0.005),
        (TN["cyan"], 0.4, 0.6, 0.003),
        (TN["purple"], 0.6, 0.8, 0.004),
        (TN["pink"], 0.8, 0.5, 0.006),
    ]

    for color, amp, base, freq in waves_params:
        for offset in range(-15, 16):
            alpha = int(80 - abs(offset) * 3)
            pts = []
            for x in range(0, W, 2):
                y = H * base + amp * H * math.sin(x * freq + offset * 0.3)
                pts.append((x, y + offset * 5))
            if len(pts) > 1:
                draw.line(pts, fill=(*color, alpha), width=2)

    return img


def wallpaper_07_particles():
    """Partículas conectadas - network visual"""
    img = Image.new("RGBA", (W, H), (18, 19, 30))
    draw = ImageDraw.Draw(img)

    particles = []
    for _ in range(80):
        x = random.randint(0, W)
        y = random.randint(0, H)
        vx = random.uniform(-0.5, 0.5)
        vy = random.uniform(-0.5, 0.5)
        color = random.choice([TN["blue"], TN["cyan"], TN["purple"], TN["green"]])
        particles.append([x, y, vx, vy, color])

    # connections + draw
    for i, p in enumerate(particles):
        for j, q in enumerate(particles[i + 1 :]):
            dist = math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
            if dist < 200:
                alpha = int(80 * (1 - dist / 200))
                draw.line([(p[0], p[1]), (q[0], q[1])], fill=(*p[4], alpha), width=1)

    for p in particles:
        draw_circle(draw, int(p[0]), int(p[1]), 4, (*p[4], 200))
        draw_circle(draw, int(p[0]), int(p[1]), 8, (*p[4], 60))

    return img


def wallpaper_08_stripes():
    """Barras verticales degradadas"""
    img = Image.new("RGBA", (W, H), TN["bg"])
    draw = ImageDraw.Draw(img)

    colors = [
        TN["blue"], TN["purple"], TN["cyan"],
        TN["pink"], TN["green"], TN["orange"],
    ]

    n = 24
    bar_w = W // n

    for i in range(n):
        t = i / n
        color = random.choice(colors)
        alpha = int(80 + 40 * math.sin(t * math.pi))
        x0 = i * bar_w
        x1 = x0 + bar_w - 2

        grad = Image.new("RGBA", (bar_w, H))
        gd = ImageDraw.Draw(grad)
        for y in range(H):
            ya = y / H
            c = lerp_color((*color, alpha), TN["bg"], ya * 0.6)
            gd.line([(0, y), (bar_w, y)], fill=c)

        img.paste(grad, (x0, 0), grad)

    return img


def wallpaper_09_minimal_sunrise():
    """Minimal - gradiente horizontal + sol"""
    img = Image.new("RGBA", (W, H))
    gradient_h(img, (20, 22, 38), (40, 35, 60))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        t = y / H
        c = lerp_color((40, 35, 60), (20, 22, 38), t)
        draw.line([(0, y), (W, y)], fill=c)

    cx, cy = W // 2, H // 2
    r = 120
    for i in range(40):
        rr = r + i * 8
        alpha = int(40 - i)
        draw.ellipse(
            [cx - rr, cy - rr, cx + rr, cy + rr],
            fill=(*TN["orange"], max(alpha, 0)),
        )

    draw_circle(draw, cx, cy, r, (*TN["orange"], 255))
    draw_circle(draw, cx - 10, cy - 10, r - 30, (255, 220, 180, 200))
    draw_circle(draw, cx, cy, int(r * 0.3), (255, 255, 255, 150))

    # thin horizon line
    draw.line([(0, H // 2), (W, H // 2)], fill=(*TN["subtext"], 80), width=1)

    return img


def wallpaper_10_hexagons():
    """Hexágonos - patrón geométrico"""
    img = Image.new("RGBA", (W, H), TN["bg"])
    draw = ImageDraw.Draw(img)

    gradient_v(img, TN["bg"], (22, 24, 42))

    def hexagon(cx, cy, r, color, alpha=80):
        pts = []
        for i in range(6):
            a = math.radians(60 * i - 30)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        draw.polygon(pts, outline=(*color, alpha), width=2)

        # inner glow
        if random.random() > 0.7:
            inner_pts = []
            for i in range(6):
                a = math.radians(60 * i - 30)
                inner_pts.append((cx + r * 0.3 * math.cos(a), cy + r * 0.3 * math.sin(a)))
            draw.polygon(inner_pts, fill=(*color, 40))

    colors = [TN["blue"], TN["purple"], TN["cyan"], TN["green"], TN["pink"]]
    gap = 100
    r = 50

    for row in range(-1, H // gap + 2):
        for col in range(-1, W // gap + 2):
            cx = col * gap * 1.5 + (row % 2) * gap * 0.75
            cy = row * gap * 0.9
            color = random.choice(colors)
            hexagon(int(cx), int(cy), r, color, alpha=random.randint(50, 120))

    # big central hex
    hexagon(W // 2, H // 2, 200, TN["blue"], 60)
    hexagon(W // 2, H // 2, 150, TN["cyan"], 80)
    hexagon(W // 2, H // 2, 100, TN["purple"], 100)

    soft_glow(draw, W // 2, H // 2, 120, TN["blue"], 6)
    soft_glow(draw, W // 2, H // 2, 80, TN["cyan"], 4)

    return img


def save_wallpaper(img, name):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name)
    img.convert("RGB").save(path, "PNG")
    print(f"  ✓ {path} ({os.path.getsize(path) // 1024} KB)")


def generate_all():
    print(f"\n  Generando wallpapers en {OUT_DIR}/\n")
    print(f"  Resolución: {W}x{H}\n")

    wallpapers = [
        ("tokyo-night-aurora.png", wallpaper_01_aurora),
        ("tokyo-night-mountains.png", wallpaper_02_mountains),
        ("tokyo-night-neon-grid.png", wallpaper_03_neongrid),
        ("tokyo-night-concentric.png", wallpaper_04_concentric),
        ("tokyo-night-blobs.png", wallpaper_05_blobs),
        ("tokyo-night-waves.png", wallpaper_06_waves),
        ("tokyo-night-particles.png", wallpaper_07_particles),
        ("tokyo-night-stripes.png", wallpaper_08_stripes),
        ("tokyo-night-minimal-sunrise.png", wallpaper_09_minimal_sunrise),
        ("tokyo-night-hexagons.png", wallpaper_10_hexagons),
    ]

    for name, fn in wallpapers:
        print(f"  Generando {name}...")
        img = fn()
        save_wallpaper(img, name)

    print(f"\n  ¡Listo! {len(wallpapers)} wallpapers generados.\n")


if __name__ == "__main__":
    generate_all()
