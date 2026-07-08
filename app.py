import streamlit as st
import pickle
import pandas as pd
import requests



movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_df = pd.DataFrame(movies_dict)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e2651e9ef4bd28b3852c2d8c1566e4ed&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movies_df.iloc[i[0]].movie_id))   
    return recommended_movies, recommended_movie_posters

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Select Movie",
    movies_df["title"].values
)

if st.button("Watch Recommendations"):
    name, posters = recommend(selected_movie)
    st.header("Recommended Movies:")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])

    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])

    with col4:
        st.text(name[3])
        st.image(posters[3])

    with col5:
        st.text(name[4])
        st.image(posters[4])
   