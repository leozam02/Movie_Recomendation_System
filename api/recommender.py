import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_path: str):
        # Cargar el dataset limpio
        self.df = pd.read_csv(csv_path)
        self.df = self.df.dropna(subset=['overview']).reset_index(drop=True)

        # Vectorizar las sinopsis
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['overview'])

        # Calcular la similitud
        self.similarity = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

        # Mapeo de títulos
        self.title_indices = pd.Series(self.df.index, index=self.df['title'].str.lower())

    def recommend(self, title: str, n: int = 5):
        title = title.lower()
        if title not in self.title_indices:
            return ["Película no encontrada."]

        idx = self.title_indices[title]
        sim_scores = list(enumerate(self.similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
        movie_indices = [i[0] for i in sim_scores]

        return self.df['title'].iloc[movie_indices].tolist()
