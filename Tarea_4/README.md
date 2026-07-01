# Periodismo de Datos — Redes Sociales: Hábitos de Uso

Trabajo práctico final del curso **Visualización de Datos** (UTFSM, primer semestre 2026).
Reúne las Tareas 1, 2 y 3 en un único proyecto de periodismo de datos: un informe y una
infografía sobre los hábitos de uso de las redes sociales.

## Integrantes
- **Elias Valle** — sunburst, ridgeline
- **Matias Barrera** — radar

## Estructura
```
datos/                 fuentes de datos (CSV) + descripción
codigo/integrante1/    Elias  — sunburst.py, ridgeline.py
codigo/integrante2/    Matias — radar.py
informe/               informe (PDF y DOCX) + infografía final (PNG)
```

## Las 6 visualizaciones
Tres reutilizadas de tareas anteriores y tres nuevas, sin repetir tipo y sin gráficos comunes:

| # | Gráfico | Origen | Autor |
|---|---------|--------|-------|
| 1 | Heatmap (minutos por edad y red) | Tarea 1 | — |
| 2 | Treemap (plataformas más usadas) | Tarea 2 | Elias |
| 3 | Coropleta (penetración por país) | Tarea 3 | Elias |
| 4 | Sunburst (razones de uso) | Nueva | Elias |
| 5 | Radar (perfil de plataformas) | Nueva | Matias |
| 6 | Ridgeline (horas por plataforma) | Nueva | Elias |

## Cómo ejecutar
Requiere Python 3 con `numpy`, `pandas`, `matplotlib` y `scipy`.
```bash
cd codigo/integrante1 && python3 sunburst.py && python3 ridgeline.py
cd ../integrante2 && python3 radar.py
```
Cada script genera su PNG. `ridgeline.py` lee `datos/Habitos_de_uso_de_redes_sociales.csv`.

## Fuentes de datos
- DataReportal / GWI — Global Social Media Statistics / Digital 2024-2025
- We Are Social / Meltwater — Digital 2024 y 2025
- Statista — Most popular social networks worldwide (oct. 2025)
- World Population Review — Social media users by country
- Encuesta propia — Google Forms, n = 25 (mayo 2026)
