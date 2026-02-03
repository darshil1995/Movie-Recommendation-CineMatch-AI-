import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def run_extraction():
    print("--- Stage 1: Extraction & Profiling ---")
    if not os.path.exists('plots'): os.makedirs('plots')

    # Loading
    movies = pd.read_csv('data/raw/movies.csv')
    ratings = pd.read_csv('data/raw/ratings.csv')
    links = pd.read_csv('data/raw/links.csv')

    # Quick Profiling Plot
    movie_counts = ratings.groupby('movieId').size()
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=movie_counts)
    plt.xscale('log')
    plt.title('Movie Popularity Distribution')
    plt.savefig(r'D:\ML_Projects\2_MovieRecommender\plots\popularity_distribution.png')

    # Save temp files
    movies = pd.merge(movies, links[['movieId', 'tmdbId']], on='movieId', how='left')
    movies.to_csv('data/raw/temp_movies.csv', index=False)
    ratings[['movieId', 'rating']].to_csv('data/raw/temp_ratings.csv', index=False)
    print("Extraction complete. Plots saved in /plots/")