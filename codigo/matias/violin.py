import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from estilo import FUENTE, TAMANO_TITULO, TAMANO_ETIQUETA, TAMANO_TICK, DPI

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datos/tiempo_uso_por_emocion.csv")
df = pd.read_csv(DATA_PATH)

# Ordenadas de menor a mayor mediana para que el gráfico cuente una historia
ORDEN_EMOCIONES = ['Boredom', 'Neutral', 'Sadness', 'Anger', 'Anxiety', 'Happiness']
COLORES = {
    'Anger':     '#E74C3C',
    'Anxiety':   '#E67E22',
    'Boredom':   '#95A5A6',
    'Happiness': '#F1C40F',
    'Neutral':   '#3498DB',
    'Sadness':   '#8E44AD',
}
PALETTE = [COLORES[e] for e in ORDEN_EMOCIONES]

# ── Figura ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("#FAFAFA")
ax.set_facecolor("#F5F5F5")

sns.violinplot(
    data=df,
    x='Dominant_Emotion', y='Daily_Usage_Time (minutes)',
    order=ORDEN_EMOCIONES,
    hue='Dominant_Emotion', hue_order=ORDEN_EMOCIONES,
    palette=PALETTE,
    inner='quartile',
    linewidth=0.9,
    alpha=0.88,
    legend=False,
    ax=ax,
)

# Anotar mediana sobre cada violín
medians = df.groupby('Dominant_Emotion')['Daily_Usage_Time (minutes)'].median()
for i, emo in enumerate(ORDEN_EMOCIONES):
    med = medians[emo]
    ax.text(i, med + 7, f'{med:.0f} min',
            ha='center', va='bottom', fontsize=8.5,
            fontfamily=FUENTE, fontweight='bold',
            color=COLORES[emo])

# ── Estética ───────────────────────────────────────────────────────────────
ax.set_xlabel("Emoción dominante del usuario", fontsize=TAMANO_ETIQUETA,
              fontfamily=FUENTE, labelpad=10)
ax.set_ylabel("Tiempo de uso diario (minutos)", fontsize=TAMANO_ETIQUETA,
              fontfamily=FUENTE)
ax.set_title("¿Cuánto tiempo pasan en redes sociales según cómo se sienten?",
             fontsize=TAMANO_TITULO, fontfamily=FUENTE, fontweight='bold', pad=14)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontfamily(FUENTE)
    label.set_fontsize(TAMANO_TICK)

ax.grid(axis='y', color='white', linewidth=1.0, alpha=0.9)
ax.set_ylim(0, 230)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#CCC')
ax.spines['bottom'].set_color('#CCC')

ax.text(0.5, -0.13,
        "Fuente: Kaggle – Social Media Usage and Emotional Well-Being (Emirhan Bulut) · "
        "n=1.246 · Líneas internas: Q1, mediana, Q3",
        transform=ax.transAxes, ha='center', fontsize=8,
        color='#888', fontfamily=FUENTE, style='italic')

plt.tight_layout()
plt.savefig("../../output/Grafico_2_violin.png", dpi=DPI, bbox_inches='tight')
plt.show()
print("Guardado: output/Grafico_2_violin.png")
