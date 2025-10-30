# app.py
from recommender import MovieRecommender

# Ruta del dataset
csv_path = "data/clean_movies.csv"

# Crear el recomendador
recommender = MovieRecommender(csv_path)

# Película base para las recomendaciones
selected_title = "Inception"

# Obtener las 5 recomendaciones más similares
recommendations = recommender.recommend(selected_title, n=5)

# Mostrar resultados
print(f"\n🎬 Película seleccionada: {selected_title}")
print("🎥 Recomendaciones similares:")
for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")
