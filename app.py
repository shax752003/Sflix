import streamlit as st
import pickle
import pandas as pd
import requests





def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.wallpapersafari.com/18/62/XV3iUF.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b12aa3c682f78e930ad0971e27f7468d&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movie_dict = pickle.load(open('movies_dict.pkl','rb'))


similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movie_dict)


new_title = '<p style="font-family:Bahnschrift; color:Green; font-size: 50px;  ">Movie Recommender System</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.markdown(""" <style> .font {
font-size:100px ; font-family: 'Freestyle Script'; color: #e3e6e4;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Sflix</p>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
     'Enter the movie name and find the suitable movie of your taste',
     movies['title'].values)


if st.button('Recommend'):
   names,posters = recommend(selected_movie_name)
   col1, col2, col3 , col4 , col5 = st.columns(5)

   with col1:
       st.text(names[0])
       st.image(posters[0])

   with col2:
       st.text(names[1])
       st.image(posters[1])

   with col3:
       st.text(names[2])
       st.image(posters[2])

   with col4:
       st.text(names[3])
       st.image([posters[3]])

   with col5:
       st.text(names[4])
       st.image(posters[4])


