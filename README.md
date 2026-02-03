# 🍿 CineMatch AI: Modular Movie Recommendation System

An end-to-end Machine Learning project that leverages an **ETL (Extract, Transform, Load) Pipeline** to provide movie recommendations based on content similarity. This system is trained on the **MovieLens 32M Dataset** and features a modern web interface.

## 🚀 The Challenge

Working with the MovieLens 32M dataset presented several real-world engineering hurdles:

* **Data Volume:** Handling over 32 million ratings and 2 million tags locally can easily lead to "Out of Memory" errors.
* **Data Sparsity:** Many movies have only one or two ratings, creating "noise" that can degrade recommendation quality.
* **Cold Start & UI Performance:** Generating a  similarity matrix while maintaining a fast, responsive user interface.

## 🛠️ What I Did (The Solution)

To solve these challenges, I built a modular architecture that separates data processing from the application layer:

* **Modular ETL Pipeline:** I decoupled the process into distinct stages—**Extract, Transform, and Load**—to optimize memory usage by clearing the RAM between stages.
* **Smart Filtering:** I implemented a popularity threshold, focusing on movies with **500+ ratings**, which reduced the dataset size while significantly improving recommendation reliability.
* **Feature Engineering:** I created a "Content Soup" by merging genres and user-generated tags into a unified text feature for TF-IDF vectorization.
* **Modern Web UI:** Developed a Streamlit interface featuring **shimmer/skeleton loading**, progress bars, and custom CSS for a premium user experience.

## 📁 Project Structure

```text
2_MovieRecommender/
├── data/               # Raw MovieLens CSV files (movies, ratings, tags, links)
├── model/              # Stores generated .pkl files (Similarity Matrix)
├── notebook/           # Exploratory Data Analysis (EDA.ipynb)
├── plots/              # Automated EDA plots generated during extraction
├── extract.py          # Stage 1: Data extraction and automated profiling
├── transform.py        # Stage 2: Data cleaning and feature engineering
├── load_model.py       # Stage 3: TF-IDF Vectorization and similarity modeling
├── main.py             # Pipeline Orchestrator (Runs the ETL process)
├── app.py              # Streamlit Web Application
├── .env                # API Key for TMDB (The Movie Database)
└── requirements.txt    # Project dependencies

```

## Demo
![App Demo](demo/streamlit_ui_demo.gif)

## ⚙️ Setup & Installation

1. **Clone the Repo:**
```bash
git clone https://github.com/darshil1995/Movie-Recommendation-CineMatch-AI-

```


2. **Install Requirements:**
```bash
pip install -r requirements.txt

```


3. **Configure API:** Create a `.env` file and add your `TMDB_API_KEY`.
4. **Run Pipeline:** `python main.py` to generate the model.
5. **Launch App:** `streamlit run app.py`.

## ✨ Key Features

* **Automated Data Profiling:** The extraction script automatically generates and saves EDA plots (Rating distributions, word clouds) in the `/plots` folder.
* **Dynamic Search:** Cleaned movie titles (regex-based) for a seamless search experience.
* **Interactive UI:** Users can choose to see between 5 to 20 recommendations via a sidebar slider.

---

Developed by **Darshil** as part of a career transition into AI & Machine Learning.
