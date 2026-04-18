import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import pandas as pd
from estilo import FUENTE, TAMANO_TITULO, TAMANO_ETIQUETA, TAMANO_TICK, DPI

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datos/flujo_plataforma_emocion.csv")
df = pd.read_csv(DATA_PATH)

# ── Paletas ────────────────────────────────────────────────────────────────
COLOR_PLATAFORMA = {
    "Facebook":  "#1877F2", "Instagram": "#C13584", "LinkedIn":  "#0A66C2",
    "Snapchat":  "#FF6B00", "Telegram":  "#26A5E4", "Twitter":   "#14171A",
    "Whatsapp":  "#25D366",
}
COLOR_EMOCION = {
    "Anger":     "#E74C3C", "Anxiety":   "#E67E22", "Boredom":   "#95A5A6",
    "Happiness": "#F1C40F", "Neutral":   "#3498DB", "Sadness":   "#8E44AD",
}

plataformas = sorted(df['Platform'].unique())
emociones   = sorted(df['Dominant_Emotion'].unique())

# ── Calcular alturas de nodos ──────────────────────────────────────────────
total_plat = df.groupby('Platform')['count'].sum()
total_emoc = df.groupby('Dominant_Emotion')['count'].sum()
grand_total = total_plat.sum()

GAP = 0.02        # espacio entre nodos
NODE_W = 0.04     # ancho del nodo
HEIGHT = 1.0      # altura total disponible

def compute_positions(totals, order):
    """Devuelve dict {nombre: (y_inicio, altura)}."""
    usable = HEIGHT - GAP * (len(order) - 1)
    pos = {}
    y = 0
    for name in order:
        h = totals[name] / grand_total * usable
        pos[name] = (y, h)
        y += h + GAP
    return pos

pos_plat = compute_positions(total_plat, plataformas)
pos_emoc = compute_positions(total_emoc, emociones)

# ── Figura ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#FAFAFA")
ax.set_facecolor("#FAFAFA")
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.05, 1.08)
ax.axis('off')

X_LEFT  = 0.12
X_RIGHT = 0.88

# ── Dibujar flujos (bezier) ────────────────────────────────────────────────
# Acumuladores para saber desde dónde partir en cada nodo
offset_plat = {p: pos_plat[p][0] for p in plataformas}
offset_emoc = {e: pos_emoc[e][0] for e in emociones}

for _, row in df.iterrows():
    plat = row['Platform']
    emoc = row['Dominant_Emotion']
    cnt  = row['count']
    h    = cnt / grand_total * (HEIGHT - GAP * (len(plataformas) - 1))

    y0_start = offset_plat[plat]
    y1_start = offset_emoc[emoc]
    offset_plat[plat] += h
    offset_emoc[emoc] += h

    # Bezier cúbico
    verts = [
        (X_LEFT + NODE_W, y0_start),
        (X_LEFT + NODE_W, y0_start),
        ((X_LEFT + NODE_W + X_RIGHT) / 2, y0_start),
        ((X_LEFT + NODE_W + X_RIGHT) / 2, y1_start),
        (X_RIGHT, y1_start),
        (X_RIGHT, y1_start),
        (X_RIGHT, y1_start + h),
        (X_RIGHT, y1_start + h),
        ((X_LEFT + NODE_W + X_RIGHT) / 2, y1_start + h),
        ((X_LEFT + NODE_W + X_RIGHT) / 2, y0_start + h),
        (X_LEFT + NODE_W, y0_start + h),
        (X_LEFT + NODE_W, y0_start + h),
    ]
    from matplotlib.path import Path
    codes = [Path.MOVETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.LINETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.CLOSEPOLY]
    path = Path(verts, codes)
    patch = mpatches.PathPatch(path,
                               facecolor=COLOR_PLATAFORMA[plat],
                               alpha=0.35, edgecolor='none', zorder=1)
    ax.add_patch(patch)

# ── Dibujar nodos ──────────────────────────────────────────────────────────
for plat in plataformas:
    y0, h = pos_plat[plat]
    rect = mpatches.FancyBboxPatch((X_LEFT, y0), NODE_W, h,
                                   boxstyle="square,pad=0",
                                   facecolor=COLOR_PLATAFORMA[plat],
                                   edgecolor='white', linewidth=0.5, zorder=2)
    ax.add_patch(rect)
    ax.text(X_LEFT - 0.015, y0 + h / 2, plat,
            ha='right', va='center', fontsize=TAMANO_TICK,
            fontfamily=FUENTE, fontweight='bold',
            color=COLOR_PLATAFORMA[plat])

for emoc in emociones:
    y0, h = pos_emoc[emoc]
    rect = mpatches.FancyBboxPatch((X_RIGHT, y0), NODE_W, h,
                                   boxstyle="square,pad=0",
                                   facecolor=COLOR_EMOCION[emoc],
                                   edgecolor='white', linewidth=0.5, zorder=2)
    ax.add_patch(rect)
    ax.text(X_RIGHT + NODE_W + 0.015, y0 + h / 2, emoc,
            ha='left', va='center', fontsize=TAMANO_TICK,
            fontfamily=FUENTE, fontweight='bold',
            color=COLOR_EMOCION[emoc])

ax.set_title("Flujo de plataforma a emoción dominante en usuarios de redes sociales",
             fontsize=TAMANO_TITULO, fontfamily=FUENTE, fontweight='bold', pad=14)
ax.text(0.5, -0.04,
        "Fuente: Kaggle – Social Media Usage and Emotional Well-Being (Emirhan Bulut) · n=1.156",
        transform=ax.transAxes, ha='center', fontsize=8,
        color='#888', fontfamily=FUENTE, style='italic')

plt.tight_layout()
plt.savefig("../../output/Grafico_1_sankey.png", dpi=DPI, bbox_inches='tight')
plt.show()
print("Guardado: output/Grafico_1_sankey.png")
