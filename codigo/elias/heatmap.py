import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from estilo import FUENTE, TAMANO_TITULO, TAMANO_ETIQUETA, TAMANO_TICK, DPI

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datos/likes_por_hora.csv")
df = pd.read_csv(DATA_PATH, index_col='plataforma')

# Ordenar horas de forma numérica
df = df[sorted(df.columns, key=lambda x: int(x))]
data = df.values.astype(float)
plataformas = df.index.tolist()
horas = [f"{int(h):02d}:00" for h in df.columns]

# ── Figura ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 4))
fig.patch.set_facecolor("#FAFAFA")

cmap = sns.color_palette("rocket", as_cmap=True)
im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=data.min(), vmax=data.max())

# Etiquetas en celdas
for i in range(len(plataformas)):
    for j in range(data.shape[1]):
        val = data[i, j]
        color_txt = 'white' if val > (data.max() * 0.55) else '#222'
        ax.text(j, i, f"{val:.0f}", ha='center', va='center',
                fontsize=7, color=color_txt, fontfamily=FUENTE)

# ── Ejes ───────────────────────────────────────────────────────────────────
ax.set_xticks(range(len(horas)))
ax.set_xticklabels(horas, fontsize=7, fontfamily=FUENTE, rotation=45, ha='right')
ax.set_yticks(range(len(plataformas)))
ax.set_yticklabels(plataformas, fontsize=TAMANO_ETIQUETA, fontfamily=FUENTE, fontweight='bold')
ax.set_xlabel("Hora del día", fontsize=TAMANO_ETIQUETA, fontfamily=FUENTE, labelpad=8)
ax.set_title("Likes promedio por hora del día y plataforma",
             fontsize=TAMANO_TITULO, fontfamily=FUENTE, fontweight='bold', pad=14)

cbar = fig.colorbar(im, ax=ax, fraction=0.015, pad=0.01)
cbar.set_label("Likes promedio", fontsize=TAMANO_TICK, fontfamily=FUENTE)
cbar.ax.tick_params(labelsize=7.5)

for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(length=0)

ax.text(0.5, -0.32,
        "Fuente: Kaggle – Social Media Sentiments Analysis Dataset · n=732 publicaciones",
        transform=ax.transAxes, ha='center', fontsize=8,
        color='#888', fontfamily=FUENTE, style='italic')

plt.tight_layout()
plt.savefig("output/integrante2_heatmap.png", dpi=DPI, bbox_inches='tight')
plt.show()
print("Guardado: output/integrante2_heatmap.png")
