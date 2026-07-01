# Integrante 1 — Elias Valle

## sunburst.py
Gráfico radial jerárquico (sunburst) de las **razones de uso** de las redes sociales.
Anillo interno: cuatro categorías (conexión social, entretenimiento, información, compras y marcas).
Anillo externo: los motivos específicos, con su porcentaje.
- Marca: área (arco / cuña).
- Canales: ángulo (peso del motivo), color (categoría), nivel radial (jerarquía).
- Fuente: DataReportal / GWI — Digital 2025. Datos definidos en el script.
- Salida: `viz_sunburst.png`.

## ridgeline.py
Gráfico de crestas (ridgeline) con la **distribución de horas diarias** de uso entre quienes usan
cada plataforma, a partir de la encuesta propia.
- Marca: área.
- Canales: posición X (horas/día), altura (proporción de usuarios), posición Y apilada + color (plataforma).
- Fuente: `../../datos/Habitos_de_uso_de_redes_sociales.csv` (encuesta propia, n = 25).
- Salida: `viz_ridgeline.png`.

Ejecutar desde esta carpeta: `python3 sunburst.py && python3 ridgeline.py`
