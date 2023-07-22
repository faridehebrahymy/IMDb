import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('genre.csv')

df = df.dropna(subset=['Genre'])

genres = df['Genre'].unique().tolist()
genre = st.selectbox("Please select your desired genre:", genres)

filtered_df = df[df['Genre'] == genre]

sorted_df = filtered_df.sort_values(by='gross_us_canada', ascending=False)

top_10_movies = sorted_df.head(10)

data = {'Movies': top_10_movies['Title'], 'Revenue ($ million)': top_10_movies['gross_us_canada']}

st.bar_chart(data=data, use_container_width=True, x='Movies', y='Revenue ($ million)')
