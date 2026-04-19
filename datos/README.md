# Tarea 1: Redes Sociales

## Tema
Crecimiento y métricas de plataformas de redes sociales.

## Integrantes
- Matias Barrera
- Elias Valle

---

## Datasets originales

### Social Media Usage and Emotional Well-Being
- **Autor:** Emirhan Bulut
- **Licencia:** MIT
- **URL:** https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being
- **Descripción:** Registros de usuarios con información sobre plataforma usada, tiempo de uso diario, posts por día, likes recibidos, comentarios, mensajes enviados y emoción dominante del día.
- **Archivos originales:** `train.csv`, `val.csv`, `test.csv`
- **Filas tras limpieza:** 1.156 (se eliminaron filas con valores nulos o categorías no reconocidas)

### Social Media Sentiments Analysis Dataset
- **URL:** https://www.kaggle.com/datasets/kashishparmar02/social-media-sentiments-analysis-dataset
- **Descripción:** 732 publicaciones de Facebook, Instagram y Twitter con información de likes, retweets, país y hora de publicación.
- **Archivo original:** `sentimentdataset.csv`

---

## Archivos CSV generados

| Archivo | Usado en | Variables | Filas |
|---|---|---|---|
| `flujo_plataforma_emocion.csv` | Sankey (Int. 1) | Platform, Dominant_Emotion, count | 42 |
| `tiempo_uso_por_emocion.csv` | Violin (Int. 1) | Dominant_Emotion, Daily_Usage_Time | 1.246 |
| `engagement_por_plataforma.csv` | Radar (Int. 2) | plataforma, posts, likes, comentarios, mensajes | 7 |
| `likes_por_hora.csv` | Heatmap (Int. 2) | plataforma × hora → likes promedio | 3 × 22 |
| `metricas_por_plataforma.csv` | Parallel coord. (Grupal) | plataforma + 5 métricas | 7 |

---

## Gráficos

### Matias — Criterio A: Diagrama de Sankey (`matias/sankey.py`)
Flujo de usuarios desde cada plataforma hacia su emoción dominante. Muestra qué redes sociales se asocian a emociones positivas o negativas. Fuente: dataset de Emotional Well-Being, n=1.156.

### Matias — Criterio B: Violin Plot (`matias/violin.py`)
Distribución del tiempo de uso diario (minutos) según la emoción dominante del usuario. Revela que los usuarios con Happiness usan ~155 min/día, mientras que los de Boredom apenas ~60 min. Las emociones están ordenadas de menor a mayor mediana. Líneas internas: Q1, mediana, Q3. Fuente: dataset de Emotional Well-Being, n=1.246.

### Elias — Criterio A: Radar Chart (`elias/radar.py`)
Métricas de engagement promedio por plataforma: posts por día, likes recibidos, comentarios y mensajes enviados. Permite comparar el perfil completo de actividad de cada red social en un solo gráfico. Fuente: dataset de Emotional Well-Being, n=1.156.

### Elias — Criterio B: Heatmap (`elias/heatmap.py`)
Likes promedio recibidos según la hora del día y la plataforma. Permite identificar los momentos de mayor engagement a lo largo del día en Facebook, Instagram y Twitter. Fuente: Social Media Sentiments Analysis Dataset, n=732.

### Grupal — Parallel Coordinates Plot (`grupal/parallel_coordinates.py`)
Correlación entre todas las métricas de comportamiento por plataforma: tiempo de uso diario, posts, likes, comentarios y mensajes. Los ejes están normalizados a [0,1] con la escala real indicada en los extremos. Fuente: dataset de Emotional Well-Being, n=1.156.

**Prompt utilizado (Claude Sonnet):**
> "Genera código Python con matplotlib para un parallel coordinates plot usando datos reales de uso de redes sociales. Las plataformas son los sujetos y los ejes son: tiempo de uso diario (min), posts por día, likes por día, comentarios por día y mensajes por día. Normaliza cada eje a [0,1] para comparación justa y muestra la escala real en los extremos de cada eje. Usa un color distinto por plataforma. Aplica estilo limpio y profesional con fondo gris claro."