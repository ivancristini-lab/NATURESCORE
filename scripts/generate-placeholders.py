"""
NatureScore™ — Generador de imágenes placeholder.

Cada imagen sigue el tratamiento "ficha de espécimen / archivo médico antiguo":
- fondo casi negro con vignetting,
- composición visual abstracta-orgánica que sugiere el concepto,
- grano fotográfico sutil encima,
- tipografía técnica en las esquinas (catálogo, fecha, sensor, dimensión).

Las imágenes quedan nombradas imagen1.jpg … imagen16.jpg + og-image.jpg.
Federico las reemplaza después con las generadas por IA manteniendo
nombre y proporciones (ver IMAGENES.md para los prompts).

USO:
    pip install pillow numpy
    cd scripts/
    python3 generate-placeholders.py

Esto regenera todo el contenido de assets/images/ y assets/og/.
"""

import os
import math
import random
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# -------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------

# Path relativo desde scripts/ — sube un nivel y entra a assets/images
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
OUT_DIR = REPO_ROOT / "assets" / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

VOID  = (4, 4, 4)
BONE  = (240, 235, 225)
EARTH = (196, 168, 130)
MOSS  = (74, 124, 89)
BLOOD = (90, 24, 16)
MIST  = (140, 130, 115)
MIST_DIM = (90, 84, 75)

FONT_MONO   = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_SERIF  = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_IT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"
FONT_SANS   = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# -------------------------------------------------------------
# TEXTURA BASE: vignetting + grano
# -------------------------------------------------------------

def base_canvas(w, h, seed=42):
    """Fondo void con vignetting radial suave."""
    rng = np.random.default_rng(seed)

    # base sólida void
    arr = np.full((h, w, 3), VOID, dtype=np.float32)

    # vignetting radial (mas oscuro en bordes)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = w / 2, h / 2
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    d_max = np.sqrt(cx ** 2 + cy ** 2)
    vignette = 1.0 - (d / d_max) ** 1.6 * 0.55
    vignette = np.clip(vignette, 0.35, 1.0)

    # subo brillo levemente en el centro para tener algo de "luz interior"
    arr = arr * vignette[..., None]
    return arr


def add_grain(arr, seed=42, strength=10):
    """Grano fotográfico sutil."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    noise = rng.normal(0, strength, (h, w))
    arr = arr + noise[..., None]
    return arr


def add_scanlines(arr, intensity=0.05, gap=3):
    """Líneas horizontales tipo CCTV/sensor antiguo, muy sutiles."""
    h, w, _ = arr.shape
    mask = np.ones((h, w), dtype=np.float32)
    for y in range(0, h, gap):
        mask[y] = 1.0 - intensity
    arr = arr * mask[..., None]
    return arr


def finalize(arr):
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, mode="RGB")


# -------------------------------------------------------------
# OVERLAY DE FICHA: catálogo, fecha, sensor, dimensión
# -------------------------------------------------------------

def draw_catalog_overlay(img, catalog_id, sensor_label, dim_label, year="MMXXVI"):
    """Tipografía de esquina estilo ficha de museo de historia natural."""
    d = ImageDraw.Draw(img, "RGBA")
    w, h = img.size

    # tamaño relativo al ancho (para que escale)
    fs_tag = max(11, int(w * 0.010))
    fs_label = max(13, int(w * 0.014))

    f_mono = font(FONT_MONO, fs_tag)
    f_mono_big = font(FONT_MONO, fs_label)

    margin = int(w * 0.025)

    earth_a = EARTH + (170,)
    mist_a  = BONE  + (110,)

    # esquina TL: catálogo
    d.text((margin, margin), f"NS · CAT. {catalog_id}", font=f_mono, fill=earth_a)

    # esquina TR: año / sesión
    d.text(
        (w - margin, margin),
        f"{year}\nSESSION 0417",
        font=f_mono,
        fill=mist_a,
        anchor="ra",
    )

    # esquina BL: sensor
    d.text(
        (margin, h - margin),
        sensor_label.upper(),
        font=f_mono_big,
        fill=earth_a,
        anchor="ld",
    )

    # esquina BR: dimensión
    d.text(
        (w - margin, h - margin),
        dim_label,
        font=f_mono,
        fill=mist_a,
        anchor="rd",
    )

    # marcas de medición en bordes (4 ticks)
    tick_color = MIST + (110,)
    tick_len = max(8, int(w * 0.012))
    # borde superior centro
    cx = w // 2
    d.line([(cx, 0), (cx, tick_len)], fill=tick_color, width=1)
    d.line([(0, h // 2), (tick_len, h // 2)], fill=tick_color, width=1)
    d.line([(w - tick_len, h // 2), (w, h // 2)], fill=tick_color, width=1)
    d.line([(cx, h - tick_len), (cx, h)], fill=tick_color, width=1)

    return img


# -------------------------------------------------------------
# COMPOSICIONES VISUALES POR ESCENA
# -------------------------------------------------------------

def scene_forest(arr, seed):
    """Bosque oscuro vertical: líneas verticales irregulares."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # 40-60 líneas verticales con diferente densidad y altura
    n = rng.integers(45, 65)
    for _ in range(int(n)):
        x = int(rng.integers(0, w))
        thick = int(rng.choice([1, 1, 1, 2, 2, 3]))
        # las del fondo más tenues, las cercanas más sólidas
        shade = int(rng.integers(20, 130))
        alpha = int(rng.integers(60, 200))
        top = int(h * rng.uniform(0.0, 0.35))
        bot = int(h * rng.uniform(0.65, 1.0))
        # leve irregularidad
        wobble = int(rng.integers(-3, 3))
        d.line(
            [(x, top), (x + wobble, bot)],
            fill=(shade, shade - 5, shade - 10, alpha),
            width=thick,
        )

    # niebla horizontal sutil hacia el centro
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(over)
    od.rectangle(
        [(0, int(h * 0.45)), (w, int(h * 0.7))],
        fill=BONE + (12,),
    )
    over = over.filter(ImageFilter.GaussianBlur(40))
    img = Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")

    return np.array(img, dtype=np.float32)


def scene_closed_eye(arr, seed):
    """Ojos cerrados: una elipse horizontal + línea de horizonte."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    cx, cy = w // 2, h // 2
    rx = int(w * 0.30)
    ry = int(h * 0.04)

    # forma de párpado cerrado: arco sutil
    for i in range(3):
        d.arc(
            [cx - rx - i, cy - ry - i, cx + rx + i, cy + ry + i],
            start=0, end=180,
            fill=BONE + (max(20, 90 - i * 25),),
            width=2,
        )

    # línea horizontal larga, cierre
    d.line(
        [(cx - rx - 30, cy + ry), (cx + rx + 30, cy + ry)],
        fill=EARTH + (190,),
        width=2,
    )

    # pestañas mínimas, hacia abajo
    for i in range(-12, 13, 2):
        x = cx + int(i * rx / 14)
        d.line([(x, cy + ry + 2), (x, cy + ry + 10 + abs(i) // 3)],
               fill=BONE + (90,), width=1)

    return np.array(img, dtype=np.float32)


def scene_earth_touch(arr, seed):
    """Mano tocando tierra: ondulación horizontal terrosa + huella en el centro."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # bandas horizontales terrosas
    for i, y_frac in enumerate([0.55, 0.62, 0.7, 0.78, 0.88]):
        y = int(h * y_frac)
        shade = (max(20, EARTH[0] - i * 30),
                 max(15, EARTH[1] - i * 28),
                 max(10, EARTH[2] - i * 25))
        for x in range(0, w, 2):
            wobble = int(rng.normal(0, 1.5))
            d.point((x, y + wobble), fill=shade + (int(120 - i * 20),))

    # huella circular en el centro
    cx, cy = w // 2, int(h * 0.55)
    for r in range(4, 60, 4):
        alpha = max(30, 180 - r * 3)
        d.ellipse(
            [cx - r, cy - r, cx + r, cy + r],
            outline=EARTH + (alpha,),
            width=1,
        )

    return np.array(img, dtype=np.float32)


def scene_silence_room(arr, seed):
    """Aula vacía: perspectiva de un cuadrilátero abierto al fondo."""
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # perspectiva en un punto, formando "habitación vacía"
    cx, cy = w // 2, int(h * 0.50)
    pad = int(w * 0.18)

    # rectángulo exterior (cercano)
    outer = [(pad, h - pad), (w - pad, h - pad),
             (w - pad, pad), (pad, pad)]
    # rectángulo interior pequeño (lejano)
    inner_pad = int(w * 0.38)
    inner = [(inner_pad, h - inner_pad // 2),
             (w - inner_pad, h - inner_pad // 2),
             (w - inner_pad, inner_pad // 2),
             (inner_pad, inner_pad // 2)]

    # líneas de perspectiva
    for i in range(4):
        d.line([outer[i], inner[i]], fill=BONE + (45,), width=1)

    # rectángulo interior (puerta abierta a oscuras)
    d.polygon(inner, outline=BONE + (90,), fill=(0, 0, 0, 200))

    return np.array(img, dtype=np.float32)


def scene_screen_attention(arr, seed):
    """Persona frente a pantalla: rectángulo brillante + silueta sugerida."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # rectángulo "pantalla" brillante al fondo
    sw, sh = int(w * 0.22), int(h * 0.35)
    sx, sy = int(w * 0.55), int(h * 0.30)
    # glow halo
    for i in range(20, 0, -2):
        d.rectangle(
            [sx - i, sy - i, sx + sw + i, sy + sh + i],
            outline=BONE + (max(0, 25 - i),),
            width=1,
        )
    d.rectangle([sx, sy, sx + sw, sy + sh], fill=BONE + (180,))

    # silueta de cabeza (semicírculo oscuro al frente)
    head_cx = int(w * 0.35)
    head_cy = int(h * 0.65)
    head_r = int(h * 0.18)
    d.ellipse(
        [head_cx - head_r, head_cy - head_r, head_cx + head_r, head_cy + head_r],
        fill=(0, 0, 0, 230),
    )

    return np.array(img, dtype=np.float32)


def scene_body_shadow(arr, seed):
    """Rostro en sombra: degradado vertical + óvalo apenas insinuado."""
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # óvalo de cabeza apenas iluminado de un lado
    cx, cy = w // 2, h // 2
    rx, ry = int(w * 0.18), int(h * 0.40)

    # lado iluminado (izquierdo)
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(over)
    od.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=BONE + (35,))
    over = over.filter(ImageFilter.GaussianBlur(30))
    img = Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")

    # contorno mínimo a la derecha del óvalo
    d = ImageDraw.Draw(img, "RGBA")
    d.arc([cx - rx, cy - ry, cx + rx, cy + ry],
          start=270, end=90, fill=BONE + (60,), width=1)

    return np.array(img, dtype=np.float32)


def scene_night_city(arr, seed):
    """Ciudad nocturna: grilla puntos de luz + horizonte sutil."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # horizonte
    hy = int(h * 0.62)
    d.line([(0, hy), (w, hy)], fill=BONE + (55,), width=1)

    # ventanas como puntos
    palette = [EARTH, BONE, MIST]
    for _ in range(int(w * h / 4000)):
        x = int(rng.integers(0, w))
        y = int(rng.integers(hy + 2, h - 10))
        bright = palette[int(rng.integers(0, 3))]
        sz = int(rng.choice([1, 1, 1, 2]))
        alpha = int(rng.integers(80, 220))
        d.rectangle([x, y, x + sz, y + sz], fill=bright + (alpha,))

    # verticales tenues que sugieren edificios
    for _ in range(int(w / 30)):
        x = int(rng.integers(0, w))
        top = int(rng.integers(hy - 80, hy - 10))
        d.line([(x, top), (x, h)], fill=BONE + (18,), width=1)

    return np.array(img, dtype=np.float32)


def scene_moon_branches(arr, seed):
    """Luna y ramas: círculo blanco + ramificaciones orgánicas."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())

    # luna con halo
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(over)
    mx, my = int(w * 0.70), int(h * 0.35)
    mr = int(h * 0.18)
    # halo difuso
    od.ellipse([mx - mr - 30, my - mr - 30, mx + mr + 30, my + mr + 30],
               fill=BONE + (25,))
    over = over.filter(ImageFilter.GaussianBlur(20))
    img = Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")

    d = ImageDraw.Draw(img, "RGBA")
    d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=BONE + (220,))

    # ramas que cruzan la luna desde abajo izquierda
    def branch(x, y, angle, length, depth):
        if depth == 0 or length < 4:
            return
        x2 = x + math.cos(angle) * length
        y2 = y - math.sin(angle) * length
        d.line([(x, y), (x2, y2)],
               fill=(15, 12, 10, 230), width=max(1, depth))
        # bifurcaciones
        if depth > 1:
            branch(x2, y2, angle + rng.uniform(0.1, 0.5),
                   length * rng.uniform(0.5, 0.75), depth - 1)
            branch(x2, y2, angle - rng.uniform(0.1, 0.5),
                   length * rng.uniform(0.5, 0.75), depth - 1)

    branch(int(w * 0.15), h, math.radians(60), h * 0.35, 5)
    branch(int(w * 0.30), h, math.radians(80), h * 0.30, 4)

    return np.array(img, dtype=np.float32)


def scene_hands(arr, seed):
    """Manos haciendo algo: líneas concéntricas + textura artesanal."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # forma "objeto entre manos" — círculo central + arcos que lo rodean
    cx, cy = w // 2, h // 2
    for r in range(20, int(h * 0.4), 6):
        alpha = max(20, 130 - r // 2)
        d.arc([cx - r, cy - r, cx + r, cy + r],
              start=200, end=340, fill=EARTH + (alpha,), width=1)
    for r in range(30, int(h * 0.35), 8):
        alpha = max(15, 100 - r // 2)
        d.arc([cx - r, cy - r, cx + r, cy + r],
              start=20, end=160, fill=EARTH + (alpha,), width=1)

    # punto central
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=BONE + (200,))

    return np.array(img, dtype=np.float32)


def scene_child_trees(arr, seed):
    """Niño mirando árboles: silueta pequeña + horizonte de árboles."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # horizonte de árboles (triángulos irregulares)
    for x in range(0, w, int(w * 0.04)):
        tw = int(rng.integers(20, 50))
        th = int(rng.integers(int(h * 0.25), int(h * 0.55)))
        ty = int(h * 0.70)
        d.polygon(
            [(x, ty), (x + tw // 2, ty - th), (x + tw, ty)],
            fill=(10, 12, 8, 230),
        )

    # suelo
    d.line([(0, int(h * 0.70)), (w, int(h * 0.70))], fill=BONE + (40,), width=1)

    # silueta de niño pequeña, centro-derecha
    chx, chy = int(w * 0.42), int(h * 0.70)
    chs = int(h * 0.18)
    # cuerpo
    d.rectangle([chx - chs // 6, chy - chs * 2 // 3, chx + chs // 6, chy],
                fill=(20, 18, 15, 240))
    # cabeza
    d.ellipse([chx - chs // 8, chy - chs - chs // 8, chx + chs // 8, chy - chs * 5 // 6],
              fill=(20, 18, 15, 240))

    return np.array(img, dtype=np.float32)


def scene_writing_dark(arr, seed):
    """Persona escribiendo en la oscuridad: líneas horizontales tipo escritura."""
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    # plano de "papel" tenue al centro
    px = int(w * 0.25)
    py = int(h * 0.30)
    pw = int(w * 0.50)
    ph = int(h * 0.40)

    # papel rectangular muy tenue
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(over)
    od.rectangle([px, py, px + pw, py + ph], fill=BONE + (22,))
    over = over.filter(ImageFilter.GaussianBlur(8))
    img = Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")

    # líneas de escritura: trazos cortos irregulares
    d = ImageDraw.Draw(img, "RGBA")
    for line in range(7):
        y = py + 20 + line * (ph - 40) // 6
        x = px + 15
        while x < px + pw - 15:
            seg = int(rng.integers(8, 60))
            if rng.random() > 0.15:  # espacios entre palabras
                d.line([(x, y), (x + seg, y)],
                       fill=BONE + (int(rng.integers(80, 180)),), width=1)
            x += seg + 6

    return np.array(img, dtype=np.float32)


def scene_species(arr, seed, signal_state):
    """
    Compositor para las 5 especies, según estado de señal.
    signal_state: 'dead', 'broken', 'partial', 'stable', 'anomaly'
    """
    rng = np.random.default_rng(seed)
    h, w, _ = arr.shape
    img = finalize(arr.copy())
    d = ImageDraw.Draw(img, "RGBA")

    cy = h // 2

    if signal_state == "dead":
        # línea plana, pequeño tic muerto al final
        d.line([(0, cy), (w, cy)], fill=BONE + (35,), width=1)
        d.line([(int(w * 0.55), cy), (int(w * 0.555), cy - 4)],
               fill=EARTH + (90,), width=1)
        d.line([(int(w * 0.555), cy - 4), (int(w * 0.56), cy)],
               fill=EARTH + (90,), width=1)
        # ceniza dispersa
        for _ in range(40):
            x = int(rng.integers(0, w))
            y = int(rng.normal(cy, 6))
            d.point((x, y), fill=MIST_DIM + (120,))

    elif signal_state == "broken":
        # línea con cortes — intermitente
        x = 0
        while x < w:
            seg = int(rng.integers(20, 100))
            if rng.random() > 0.30:
                # tramo "vivo" con poca amplitud
                pts = []
                for xi in range(x, min(x + seg, w), 2):
                    amp = rng.normal(0, 6)
                    pts.append((xi, cy + amp))
                if len(pts) > 1:
                    d.line(pts, fill=BONE + (140,), width=1)
            x += seg + int(rng.integers(5, 25))

    elif signal_state == "partial":
        # señal continua pero baja, con leves picos
        pts = []
        for xi in range(0, w, 2):
            base = math.sin(xi / 40) * 6
            spike = math.sin(xi / 9) * 4 if rng.random() > 0.7 else 0
            pts.append((xi, cy + base + spike + rng.normal(0, 1.5)))
        d.line(pts, fill=BONE + (170,), width=1)

    elif signal_state == "stable":
        # señal estable con picos rítmicos limpios
        pts = []
        for xi in range(0, w, 2):
            phase = xi / 80
            base = math.sin(phase * 2) * 14
            # pulso periódico
            pulse = 0
            if int(xi / 110) % 2 == 0 and (xi % 110) < 20:
                pulse = -25 * math.sin((xi % 110) / 6)
            pts.append((xi, cy + base + pulse))
        d.line(pts, fill=BONE + (210,), width=2)
        # eco verde tenue
        pts2 = [(p[0], p[1] + 18) for p in pts]
        d.line(pts2, fill=MOSS + (90,), width=1)

    elif signal_state == "anomaly":
        # ramificación anómala — múltiples señales superpuestas
        for layer, color, alpha, freq, amp in [
            (0, BONE,  220, 60, 18),
            (1, EARTH, 160, 35, 24),
            (2, MOSS,  140, 90, 14),
        ]:
            pts = []
            for xi in range(0, w, 2):
                v = (math.sin(xi / freq) * amp +
                     math.sin(xi / (freq * 0.4)) * (amp / 3))
                v += rng.normal(0, 2)
                pts.append((xi, cy + v + layer * 6 - 6))
            d.line(pts, fill=color + (alpha,), width=2 if layer == 0 else 1)

        # ramificaciones laterales como raíces saliendo arriba/abajo
        for _ in range(8):
            sx = int(rng.integers(int(w * 0.2), int(w * 0.8)))
            angle = rng.uniform(0, 2 * math.pi)
            length = rng.integers(20, 80)
            ex = sx + int(math.cos(angle) * length)
            ey = cy + int(math.sin(angle) * length)
            d.line([(sx, cy), (ex, ey)], fill=MOSS + (110,), width=1)

    return np.array(img, dtype=np.float32)


# -------------------------------------------------------------
# REGISTRO DE IMÁGENES A GENERAR
# -------------------------------------------------------------

IMAGES = [
    # (filename, (w,h), catalog_id, sensor_label, dim_label, scene_fn, seed, year)

    # — Pantallas narrativas —
    ("imagen1.png",  (1200, 1500), "0001 · HERO",     "FONDO · BOSQUE NOCTURNO",     "1200 × 1500 · 4:5",  scene_forest,      11, "MMXXVI"),
    ("imagen2.png",  ( 900,  900), "0002 · ADV",      "OJOS · CIERRE",                "900 × 900 · 1:1",   scene_closed_eye,  22, "MMXXVI"),

    # — 9 preguntas —
    ("imagen3.png",  (1400,  600), "0011 · Q01",      "SENSOR · NATURALEZA",          "1400 × 600 · 21:9", scene_earth_touch, 31, "MMXXVI"),
    ("imagen4.png",  (1400,  600), "0012 · Q02",      "SENSOR · SILENCIO",            "1400 × 600 · 21:9", scene_silence_room, 32, "MMXXVI"),
    ("imagen5.png",  (1400,  600), "0013 · Q03",      "SENSOR · ATENCIÓN",            "1400 × 600 · 21:9", scene_screen_attention, 33, "MMXXVI"),
    ("imagen6.png",  (1400,  600), "0014 · Q04",      "SENSOR · INTEROCEPCIÓN",       "1400 × 600 · 21:9", scene_body_shadow, 34, "MMXXVI"),
    ("imagen7.png",  (1400,  600), "0015 · Q05",      "SENSOR · ORIENTACIÓN",         "1400 × 600 · 21:9", scene_night_city,  35, "MMXXVI"),
    ("imagen8.png",  (1400,  600), "0016 · Q06",      "SENSOR · ABURRIMIENTO",        "1400 × 600 · 21:9", scene_moon_branches, 36, "MMXXVI"),
    ("imagen9.png",  (1400,  600), "0017 · Q07",      "SENSOR · TACTO",               "1400 × 600 · 21:9", scene_hands,       37, "MMXXVI"),
    ("imagen10.png", (1400,  600), "0018 · Q08",      "SENSOR · INTUICIÓN",           "1400 × 600 · 21:9", scene_child_trees, 38, "MMXXVI"),
    ("imagen11.png", (1400,  600), "0019 · Q09",      "SENSOR · VOZ PROPIA",          "1400 × 600 · 21:9", scene_writing_dark, 39, "MMXXVI"),

    # — 5 especies (resultado) —
    ("imagen12.png", (1600,  700), "0101 · SP-A",     "HOMO ALGORITHMICUS · 0-20",    "1600 × 700 · 16:7", lambda a, s: scene_species(a, s, "dead"),    41, "MMXXVI"),
    ("imagen13.png", (1600,  700), "0102 · SP-B",     "HOMO COMFORTIS · 21-40",       "1600 × 700 · 16:7", lambda a, s: scene_species(a, s, "broken"),  42, "MMXXVI"),
    ("imagen14.png", (1600,  700), "0103 · SP-C",     "HOMO SAPIENS FRAGMENTADO · 41-60", "1600 × 700 · 16:7", lambda a, s: scene_species(a, s, "partial"), 43, "MMXXVI"),
    ("imagen15.png", (1600,  700), "0104 · SP-D",     "HOMO SENSORIALIS · 61-80",     "1600 × 700 · 16:7", lambda a, s: scene_species(a, s, "stable"),  44, "MMXXVI"),
    ("imagen16.png", (1600,  700), "0105 · SP-E",     "HOMO SENSORIUS · 81-100",      "1600 × 700 · 16:7", lambda a, s: scene_species(a, s, "anomaly"), 45, "MMXXVI"),
]


# -------------------------------------------------------------
# RUN
# -------------------------------------------------------------

def generate_one(filename, size, catalog, sensor, dim, scene_fn, seed, year):
    w, h = size
    arr = base_canvas(w, h, seed=seed)
    arr = scene_fn(arr, seed)
    arr = add_grain(arr, seed=seed + 1, strength=8)
    arr = add_scanlines(arr, intensity=0.035, gap=4)

    img = finalize(arr)
    img = draw_catalog_overlay(img, catalog, sensor, dim, year=year)

    # convertir nombre a .jpg
    jpg_name = filename.replace(".png", ".jpg")
    out_path = OUT_DIR / jpg_name
    img.convert("RGB").save(out_path, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"  ✓ {jpg_name}  ({w}×{h})  →  {out_path.stat().st_size // 1024} KB")
    return out_path


def og_image():
    """Imagen Open Graph 1200×630 — wordmark + frase."""
    w, h = 1200, 630
    arr = base_canvas(w, h, seed=99)
    # Línea de señal anómala atrás
    arr = scene_species(arr, 99, "anomaly")
    arr = add_grain(arr, seed=100, strength=6)
    arr = add_scanlines(arr, intensity=0.025, gap=4)
    img = finalize(arr)

    d = ImageDraw.Draw(img, "RGBA")
    f_title = font(FONT_SERIF, 110)
    f_sub   = font(FONT_MONO, 22)
    f_tag   = font(FONT_MONO, 16)

    cx = w // 2
    cy = h // 2

    # Wordmark
    d.text((cx, cy - 30), "NatureScore™", font=f_title, fill=BONE + (255,), anchor="mm")
    d.text((cx, cy + 60), "HUMAN RECONNECTION INDEX", font=f_sub, fill=EARTH + (220,), anchor="mm")
    d.text((cx, cy + 120),
           "El sistema te desconectó, pieza por pieza. Esto mide cuánto te queda.",
           font=f_tag, fill=BONE + (150,), anchor="mm")

    # Tag esquinas
    d.text((40, 30), "NS · MMXXVI", font=f_tag, fill=EARTH + (180,))
    d.text((w - 40, 30), "SESSION 0417", font=f_tag, fill=BONE + (120,), anchor="ra")
    d.text((40, h - 30), "15 SENSORES · 8 SEÑALES · 1 DIAGNÓSTICO",
           font=f_tag, fill=EARTH + (180,), anchor="ld")

    out_path = OUT_DIR.parent / "og" / "og-image.jpg"
    img.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"  ✓ og-image.jpg  →  {out_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    print(f"Generando {len(IMAGES)} imágenes en {OUT_DIR}\n")
    for spec in IMAGES:
        generate_one(*spec)
    print()
    og_image()
    print("\nListo.")
