import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('../data/movies.csv', encoding='latin-1', sep='\t', usecols=['title', 'genres'])
data['genres'] = data['genres'].apply(lambda x : x.replace('|', ' ').replace('-', ''))


class Recommendation:
    def __init__(self):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(data['genres'])
        cosine_sim = pd.DataFrame(cosine_similarity(tfidf_matrix), index=data['title'], columns=data['title'])
        self.model = cosine_sim

    def get_name_movie(self):
        return self.model.index

    def recommend(self, name_movie: str, limit: int=10):
        if name_movie not in self.get_name_movie():
            raise ValueError(f"Can't find that movie name")
        recommended_movies = self.model[name_movie].sort_values(ascending=False).drop(name_movie).index
        return list(recommended_movies)[:limit]