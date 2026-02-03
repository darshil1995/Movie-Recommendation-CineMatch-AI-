import streamlit as st
import pickle, requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")


@st.cache_resource
def load_assets():
    return pickle.load(open('model/movie_list.pkl', 'rb')), pickle.load(open('model/similarity.pkl', 'rb'))


def fetch_poster(tmdb_id):
    url = f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}?api_key={API_KEY}"
    try:
        data = requests.get(url, timeout=5).json()
        return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')
    except:
        return "https://via.placeholder.com/500x750?text=No+Poster"


movies, similarity = load_assets()

st.title("🍿 CineMatch AI")
num_recs = st.sidebar.slider("Number of Recommendations", 5, 20, 10)
selected = st.selectbox("Search Movie:", movies['search_title'].values)

if st.button("Recommend"):
    idx = movies[movies['search_title'] == selected].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:num_recs + 1]

    bar = st.progress(0)
    cols = st.columns(5)
    for i, (m_idx, dist) in enumerate(distances):
        bar.progress((i + 1) / num_recs)
        with cols[i % 5]:
            st.image(fetch_poster(movies.iloc[m_idx].tmdbId))
            st.caption(movies.iloc[m_idx].title)
    bar.empty()
    st.balloons()