# This is a sample Python script.
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import pickle
import requests

st.title('Recommendation System')

movies = pickle.load(open('movies_dict.pkl', 'rb'))
moviess = pd.DataFrame(movies)
movies_list = moviess['title'].values
option = st.selectbox('How would you like to be contacted?', movies_list)

sim = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=ab62de18df712054047ba5db7101e730&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path





def recommend(movie):
    movie_index = moviess[moviess['title'] == movie].index[0]
    distance = sorted(list(enumerate(sim[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_poster=[]

    for i in distance:
        movie_id=moviess.iloc[i[0]].id

        recommended_movies.append(moviess.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_poster


if st.button('RECOMMEND'):
    recommended_movies,recommended_poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_poster[4])

