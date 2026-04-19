import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from estilo import FUENTE, TAMANO_TITULO, TAMANO_ETIQUETA, TAMANO_TICK, DPI

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datos/metricas_por_plataforma.csv")
df = pd.read_csv(DATA_PATH, index_col='plataforma')

COLORES = {
    "Facebook":  "#1877F2", "Instagram": "#C13584", "LinkedIn":  "#0A66C2",
    "Snapchat":  "#FF6B00", "Telegram":  "#26A5E4", "Twitter":   "#555555",
    "Whatsapp":  "#25D366",
}
ETIQUETAS_EJES = ["Tiempo diario\n(min)", "Posts\npor día",
                  "Likes\npor día", "Comentarios\npor día", "Mensajes\npor día"]
n_ejes = len(ETIQUETAS_EJES)
xs = np.arange(n_ejes)

# ── Normalización [0,1] por eje ────────────────────────────────────────────
raw = df.values.astype(float)
mins = raw.min(axis=0)
maxs = raw.max(axis=0)
norm = (raw - mins) / (maxs - mins)

# ── Figura ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("#FAFAFA")
ax.set_facecolor("#F0F0F0")

for i, plat in enumerate(df.index):
    color = COLORES.get(plat, '#999')
    ax.plot(xs, norm[i], color=color, linewidth=2.4,
            alpha=0.88, solid_capstyle='round', label=plat)
    ax.scatter(xs, norm[i], color=color, s=55, zorder=5,
               edgecolors='white', linewidth=1.2)

# ── Ejes paralelos y escala real ───────────────────────────────────────────
for j in range(n_ejes):
    ax.axvline(j, color='#BBB', linewidth=1.2, zorder=1)
    ax.text(j, -0.09, f"{mins[j]:.1f}", ha='center', va='top',
            fontsize=8, color='#666', fontfamily=FUENTE)
    ax.text(j,  1.06, f"{maxs[j]:.1f}", ha='center', va='bottom',
            fontsize=8, color='#666', fontfamily=FUENTE)

# ── Etiquetas min/max ──────────────────────────────────────────────────────
ax.text(-0.35, -0.09, "mín →", ha='right', va='top',
        fontsize=7.5, color='#999', fontfamily=FUENTE)
ax.text(-0.35,  1.06, "máx →", ha='right', va='bottom',
        fontsize=7.5, color='#999', fontfamily=FUENTE)

ax.set_xticks(xs)
ax.set_xticklabels(ETIQUETAS_EJES, fontsize=TAMANO_TICK, fontfamily=FUENTE)
ax.set_xlim(-0.4, n_ejes - 0.6)
ax.set_ylim(-0.18, 1.18)
ax.yaxis.set_visible(False)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(length=0)

ax.legend(loc='upper right', fontsize=TAMANO_TICK, frameon=True,
          facecolor='#FAFAFA', edgecolor='#DDD')
ax.set_title("Perfil multidimensional de comportamiento por plataforma",
             fontsize=TAMANO_TITULO, fontfamily=FUENTE, fontweight='bold', pad=14)
ax.text(0.5, -0.18,
        "Fuente: Kaggle – Social Media Usage and Emotional Well-Being (Emirhan Bulut) · n=1.156",
        transform=ax.transAxes, ha='center', fontsize=8,
        color='#888', fontfamily=FUENTE, style='italic')

plt.tight_layout()
plt.savefig("output/grupal_parallel_coordinates.png", dpi=DPI, bbox_inches='tight')
plt.show()
print("Guardado: output/grupal_parallel_coordinates.png")
