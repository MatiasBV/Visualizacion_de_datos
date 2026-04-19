import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from estilo import FUENTE, TAMANO_TITULO, TAMANO_ETIQUETA, TAMANO_TICK, DPI

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datos/engagement_por_plataforma.csv")
df = pd.read_csv(DATA_PATH, index_col='plataforma')

COLORES = {
    "Facebook":  "#1877F2", "Instagram": "#C13584", "LinkedIn":  "#0A66C2",
    "Snapchat":  "#FF6B00", "Telegram":  "#26A5E4", "Twitter":   "#555555",
    "Whatsapp":  "#25D366",
}
ETIQUETAS_EJES = ["Posts\npor día", "Likes\npor día", "Comentarios\npor día", "Mensajes\npor día"]
n = len(ETIQUETAS_EJES)
angulos = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
angulos += angulos[:1]

# ── Figura ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor("#FAFAFA")
ax.set_facecolor("#F5F5F5")

for plat in df.index:
    vals = df.loc[plat].tolist() + [df.loc[plat].tolist()[0]]
    color = COLORES[plat]
    ax.plot(angulos, vals, linewidth=2.2, color=color, label=plat)
    ax.fill(angulos, vals, alpha=0.10, color=color)

# ── Ejes ───────────────────────────────────────────────────────────────────
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(ETIQUETAS_EJES, fontsize=TAMANO_TICK, fontfamily=FUENTE)
ax.set_rlabel_position(25)

# Escala dinámica basada en los datos reales
max_val = df.values.max()
ticks = np.linspace(0, max_val, 5)[1:]
ax.set_yticks(ticks)
ax.set_yticklabels([f"{v:.0f}" for v in ticks], fontsize=7.5, color='#777')
ax.set_ylim(0, max_val * 1.1)

ax.grid(color='#CCC', linestyle='--', linewidth=0.6, alpha=0.8)
ax.spines['polar'].set_color('#CCC')

ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15),
          fontsize=TAMANO_TICK, frameon=True,
          facecolor='#FAFAFA', edgecolor='#DDD')
ax.set_title("Métricas de engagement promedio por plataforma",
             fontsize=TAMANO_TITULO, fontfamily=FUENTE, fontweight='bold', pad=24)

fig.text(0.5, 0.02,
         "Fuente: Kaggle – Social Media Usage and Emotional Well-Being (Emirhan Bulut) · n=1.156",
         ha='center', fontsize=8, color='#888', fontfamily=FUENTE, style='italic')

plt.tight_layout()
plt.savefig("output/integrante2_radar.png", dpi=DPI, bbox_inches='tight')
plt.show()
print("Guardado: output/integrante2_radar.png")
