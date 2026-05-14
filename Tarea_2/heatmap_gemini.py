import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Preparación de los datos
# Creamos un diccionario con los datos de la encuesta
data = {
    'Plataforma': ['Instagram', 'YouTube', 'TikTok', 'X / Twitter', 'Facebook', 'LinkedIn'],
    '0-1 h': [0, 1, 0, 0, 1, 0],
    '1-3 h': [9, 8, 3, 2, 0, 2],
    '3-5 h': [8, 7, 6, 1, 1, 0],
    '+5 h': [3, 3, 2, 1, 0, 0]
}

# Convertir a DataFrame de Pandas y establecer la Plataforma como índice
df = pd.DataFrame(data)
df.set_index('Plataforma', inplace=True)

# 2. Configuración estética del gráfico
plt.figure(figsize=(10, 6))
sns.set_theme(style="white")

# 3. Creación del Heatmap
# annot=True muestra los números, fmt="d" asegura que sean enteros
# cmap="Purples" aplica la paleta de tonos morados
heatmap = sns.heatmap(df, 
                      annot=True, 
                      fmt="d", 
                      cmap="Purples", 
                      cbar_kws={'label': 'Número de Usuarios'},
                      linewidths=.5)

# 4. Personalización de etiquetas y títulos
plt.title("Distribución de usuarios por plataforma y horas de uso diario", fontsize=14, pad=20)
plt.xlabel("Rango de Horas Diarias", fontsize=12)
plt.ylabel("Plataforma", fontsize=12)

# Añadir la fuente de datos al pie del gráfico (alineado a la derecha)
plt.figtext(0.95, 0.01, "Fuente: Encuesta propia — Visualización de Datos, UTFSM 2026", 
            ha="right", fontsize=9, style='italic')

# Ajustar el diseño para evitar recortes en los bordes
plt.tight_layout()

# 5. Guardar la imagen en alta resolución
plt.savefig('heatmap_redes_sociales.png', dpi=150)

# Mostrar el gráfico
plt.show()