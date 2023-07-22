import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import random


st.set_page_config(
    page_title='imdb illustration',

)
st.title("first ; Filtering Tables")
#1++++++++=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
movie_df = pd.read_csv("movie.csv")

st.subheader('Filter by year')

start_year = st.slider('Select start year', 1900, 2023, 1990)
end_year = st.slider('Select end year', start_year, 2023, 2021)
filtered_df = movie_df[(movie_df['Year'] >= start_year) & (movie_df['Year'] <= end_year)]
st.dataframe(filtered_df)
#2=============================================================================================================================================
st.subheader('Filter by Runtime')
maxm = int(max(movie_df['Runtime']))
min_value, max_value = st.slider('Range of values', 0, 100, (0, maxm))

filtered_df1 = movie_df[movie_df['Runtime'].between(min_value, max_value)]

st.dataframe(filtered_df1)
#3==================================================================================================================================================

df = pd.read_csv("Stars.csv")
st.subheader('Filter by Actors')

# Create a list of unique actors in the Star column
actors = df['Star'].unique().tolist()

# Create a checkbox list for the user to select actors
selected_actors = st.multiselect('Select actors', options=actors)

# Filter dataframe based on selected actors
filtered_df = df[df['Star'].isin(selected_actors)]

# Display the results to the user
st.write(filtered_df)


#==============================================================================================================================================



st.subheader('Filter by Genres')
df1 = pd.read_csv('genre.csv')
df1['Genre'] = df1['Genre'].str.strip("'") 
selected_genre = st.selectbox('Please select a genre:', df1['Genre'].unique())
filtered_df = df1[df1['Genre'] == selected_genre]
st.write('Table of movies by genre {}:'.format(selected_genre))
st.dataframe(filtered_df)
























