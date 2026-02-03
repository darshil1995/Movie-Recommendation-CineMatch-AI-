import pandas as pd
import re


def clean_title(title):
    return re.sub(r'\s\(\d{4}\)', '', title).strip()


def run_transformation():
    print("--- Stage 2: Transformation ---")
    movies = pd.read_csv('data/raw/temp_movies.csv')
    ratings = pd.read_csv('data/raw/temp_ratings.csv')
    tags = pd.read_csv('data/raw/tags.csv')

    # 1. Drop duplicate movies based on title or ID
    movies = movies.drop_duplicates(subset=['movieId'])

    # Popularity Filter (500+ ratings)
    counts = ratings.groupby('movieId').size()
    popular_ids = counts[counts >= 500].index
    df = movies[movies['movieId'].isin(popular_ids)].copy()

    # Feature Engineering
    df['search_title'] = df['title'].apply(clean_title)
    df['genres'] = df['genres'].str.replace('|', ' ', regex=False)

    tags['tag'] = tags['tag'].fillna('').astype(str).str.lower()
    movie_tags = tags.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()

    df = pd.merge(df, movie_tags, on='movieId', how='left').fillna('')
    df['combined_features'] = (df['search_title'] + " " + df['genres'] + " " + df['tag']).str.lower()

    df.to_csv('data/processed/processed_data.csv', index=False)
    print("Transformation complete.")