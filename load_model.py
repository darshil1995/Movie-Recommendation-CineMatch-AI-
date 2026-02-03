import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def run_modeling():
    print("--- Stage 3: Modeling ---")
    df = pd.read_csv('data/processed/processed_data.csv')

    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    matrix = tfidf.fit_transform(df['combined_features'].fillna(''))
    sim = cosine_similarity(matrix)

    pickle.dump(df, open('model/movie_list.pkl', 'wb'))
    pickle.dump(sim, open('model/similarity.pkl', 'wb'))
    print("Model saved to .pkl files.")