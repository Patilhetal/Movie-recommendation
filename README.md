# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using **Python**, **Streamlit**, and **Machine Learning**. The application recommends movies similar to the one selected by the user based on movie metadata and displays their posters using the TMDB API.

---
## 🌐 Live Demo
-  https://movie-recommendation-1-xgxs.onrender.com/

## 📌 Features

- 🎥 Recommend 5 similar movies instantly
- 🖼️ Display movie posters using The Movie Database (TMDB) API
- ⚡ Fast recommendations using a precomputed similarity matrix
- 🌐 Interactive web interface built with Streamlit
- 📱 Simple and user-friendly UI
- 🚀 Deployed online for easy access

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- Transformers
- PyTorch
- Scikit-learn
- Pandas
- NumPy
- Requests
- Pickle
- TMDB API

## 📂 Project Structure

```
Movie-Recommender-System/
│
├── app.py                 # Main Streamlit application
├── movie_dict.pkl         # Movie dataset
├── similarity.pkl         # Cosine similarity matrix
├── requirements.txt
├── README.md

```

---

## ⚙️ How It Works

1. The user selects a movie from the dropdown menu.
2. The system locates the selected movie in the dataset.
3. A precomputed cosine similarity matrix is used to find the most similar movies.
4. The top five recommendations are retrieved.
5. Movie posters are fetched dynamically using the TMDB API.
6. The recommended movies along with their posters are displayed.

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Filtering** recommendation technique powered by **Sentence Transformers**.

### Workflow

1. Movie metadata (overview, genres, keywords, cast, etc.) is preprocessed.
2. Each movie is converted into a dense semantic embedding using the **SentenceTransformer** model.
3. Cosine similarity is computed between movie embeddings.
4. The similarity matrix is stored using Pickle for fast recommendations.
5. When a user selects a movie, the system retrieves the five most semantically similar movies and displays their posters using the TMDB API.

---

## 🤖 Model Used

- **Sentence Transformers**
- **Model:** `all-MiniLM-L6-v2`
- **Similarity Measure:** Cosine Similarity

Sentence Transformers generate contextual embeddings that understand the meaning of movie descriptions, resulting in more accurate recommendations than traditional keyword-based methods.

---

## 📈 Recommendation Pipeline

```
Movie Metadata
       │
       ▼
Text Preprocessing
       │
       ▼
Sentence Transformer
(all-MiniLM-L6-v2)
       │
       ▼
Movie Embeddings
       │
       ▼
Cosine Similarity
       │
       ▼
Similarity Matrix
       │
       ▼
Top 5 Recommended Movies
```

---

## 📊 Model Highlights

- Semantic similarity-based recommendations
- Context-aware movie embeddings
- Fast inference using a precomputed similarity matrix
- Poster retrieval using the TMDB API
- Interactive web application built with Streamlit

## 📊 Future Improvements

- Semantic Search using Sentence Transformers
- Hybrid Recommendation System
- Movie Search with Auto-complete
- User Ratings and Reviews
- Recommendation Explanation
- Genre Filters
- IMDb Rating Display
- Trailer Integration
- User Authentication
- Personalized Recommendations

---

## 📌 Dataset

Movie metadata is obtained from the **TMDB Movie Dataset**.

Poster images are fetched using the **TMDB API**.

---

## 🙋 Author

**Hetal Patil**

AI/ML Enthusiast | Python Developer | Machine Learning

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
