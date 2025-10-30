# 🎬✨ Sistema de Recomendación de Películas (NLP + TF‑IDF) ✨🎬

🎞️ Bienvenido — un sistema de recomendación basado en contenido que usa TF‑IDF y similitud del coseno para sugerir películas a partir de su descripción (`overview`). Incluye visualizaciones estilo "Netflix" para explorar resultados de forma atractiva.



[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org) [![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow?logo=power-bi&logoColor=white)](https://powerbi.microsoft.com) [![Matplotlib](https://img.shields.io/badge/matplotlib-3.x-282C34?logo=matplotlib&logoColor=white)](https://matplotlib.org) [![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0-green?logo=scikit-learn&logoColor=white)](https://scikit-learn.org) [![TF-IDF](https://img.shields.io/badge/TF--IDF-NLP-blue)](#)



---

## 🔍 Características destacadas
- 🎯 Recomendaciones basadas en contenido (TF‑IDF + Cosine Similarity).  
- 🎥 Visualización de la película seleccionada (póster, sinopsis y reparto).  
- 🔥 Mapa de calor de géneros compartidos entre la película seleccionada y las recomendadas.  
- 📊 Gráfica estilo Netflix con los géneros más frecuentes entre las recomendaciones.  
- 🎛️ Salidas listas para integrar en dashboards o presentaciones.

---

## 🗂️ Estructura sugerida del proyecto
.......

---

## ⚙️ Requisitos rápidos
- Python 3.8+  
- Recomendada instalación en entorno virtual (venv / conda)

Instalar dependencias:
```bash
pip install pandas matplotlib seaborn scikit-learn pillow requests
```

Librerías principales:
- pandas — manejo de datos  
- matplotlib, seaborn — visualizaciones  
- scikit-learn — TF‑IDF y similitud del coseno  
- requests, Pillow — descarga y manejo de imágenes (TMDb)

---

## 🛠️ Configuración necesaria

1) Ruta del dataset  
   Asegurarse de que los scripts referencien la ruta correcta a `clean_movies.csv`. Ejemplo (Windows):
   ```python
   movie_df = pd.read_csv(r"C:/Users//Desktop/ProyectoCIAP/data/clean_movies.csv")
   ```

2) API Key (solo si usas el script que descarga pósters desde TMDb)  
   - Crear cuenta en https://www.themoviedb.org  
   - Generar API Key  
   - Insertar la clave en el script:
   ```python
   API_KEY = "TU_API_KEY_AQUI"
   ```

---

## ⚙️ Cómo funciona (resumen técnico)
- 🧮 Vectorización: las descripciones (`overview`) se transforman en vectores con TF‑IDF.  
- 📐 Similitud: se calcula la similitud del coseno entre vectores para medir cercanía.  
- 🏷️ Recomendación: se ordenan las películas por puntuación de similitud y se devuelven las más próximas.  
- 📈 Visualizaciones: gráfico de barras (géneros más frecuentes) y mapa de calor (géneros compartidos).

---

## 📝 Notas finales
- Verificar que el CSV tenga columnas `title`, `overview` y `genres` bien formateadas.  
- Incorporar manejo de valores nulos para `overview` y `genres` si se amplía el dataset.  
- Contribuciones, mejoras y visuales extra son bienvenidas — ¡haz un fork y envía PR! 🍿

---

## 📦 Generar / actualizar requirements.txt

Generar desde el entorno activo (recomendado):
```powershell
pip freeze > requirements.txt
```

