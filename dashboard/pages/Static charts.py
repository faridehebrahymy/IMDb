import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# Load the dataset
df_mov = pd.read_csv('movie.csv')

# Sort the dataframe by gross_us_canada in descending order
df = df_mov.sort_values(by='gross_us_canada', ascending=False)

# Select the top 10 movies
top_10 = df.head(10)

# Create a bar chart using Altair
chart = alt.Chart(top_10, width=800, height=600).mark_bar().encode(
    x=alt.X('Title:N', title='Movie Title', sort=alt.EncodingSortField(field='gross_us_canada')),
    y=alt.Y('gross_us_canada:Q', title='Gross US/Canada', axis=alt.Axis(labelAngle=0))
)

# Set the chart title and axis labels
chart = chart.properties(
    title={
        "text": ["Top 10 Highest Grossing Movies in US/Canada"],
        "subtitle": ["Source: IMDB"],
        "color": "black"
    }
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)
#--2-----------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

movies_df = pd.read_csv('stars.csv')

top_star = movies_df['Star'].value_counts().sort_values(ascending=False)
top_stars=top_star.head(5)

sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
plt.title("Top 5 actors with the most movies in IMDB top 250", fontsize=16)
plt.xlabel("Star", fontdict={'fontsize':14, 'fontweight':'bold'})
plt.ylabel("Count", fontdict={'fontsize':14, 'fontweight':'bold'})
sns.barplot(x=top_stars.index, y=top_stars.values, color='blue')
st.set_option('deprecation.showPyplotGlobalUse', False)


plt.xticks(rotation=45)

st.pyplot()


#-3------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('genre.csv')

movies = df.dropna(subset=['Genre'])
movies['Genre'] = movies['Genre'].astype(str)

genres, genre_counts = np.unique(movies['Genre'].str.lower(), return_counts=True)

data = {
    'Genres': genres,
    'Count': genre_counts
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(df['Count'], labels=None)
ax.set_title('Distribution of Movie Genres', fontsize=16)
ax.legend(title='Genres', labels=[f'{genre} ({count})' for genre, count in zip(df['Genres'], df['Count'])], loc='center left', bbox_to_anchor=(1, 0.5))
ax.axis('equal')

st.pyplot(fig)


#==4==========================================================================================================
import pandas as pd
import matplotlib.pyplot as plt


# خواندن داده‌ها از فایل CSV
df = pd.read_csv('movie.csv')

# تعداد داده‌های منحصر به فرد در ستون "Parental Guide" را بشماریم
parental_guide_counts = df['ParentalGuide'].value_counts()



parental_guide = df.dropna(subset=['ParentalGuide'])
parental_guide['ParentalGuide'] = parental_guide['ParentalGuide'].astype(str)

# شمردن تعداد فیلم‌های هر ژانر
parental_guide, parental_guide_counts = np.unique(movies['ParentalGuide'].str.lower(), return_counts=True)

# ایجاد دیتافریم
data = {
    'Parental Guides': parental_guide,
    'Count':  parental_guide_counts
}
df = pd.DataFrame(data)
# نمودار دایره‌ای
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(df['Count'], labels=None)
ax.set_title('Distribution of Parental Guides ', fontsize=16)
ax.legend(title='Parental Guides', labels=[f'{genre} ({count})' for genre, count in zip(df['Parental Guides'], df['Count'])], loc='center left', bbox_to_anchor=(1, 0.5))
ax.axis('equal')

# نمایش نمودار در streamlit
st.pyplot(fig)

#====5============================================================================================
import pandas as pd
import altair as alt
import streamlit as st

# Read data
data = pd.read_csv('genre.csv')

st.subheader("Parental Guide by Genre for  Movies")

genre_parental_guide = data.groupby(['Genre', 'ParentalGuide']).size().reset_index(name='Count')

# Create Altair chart
chart = alt.Chart(genre_parental_guide).mark_bar().encode(
    x=alt.X('Genre', sort='-y'),
    y='Count',
    color='ParentalGuide'
).properties(
    height=400
)

# Display chart using Streamlit
st.altair_chart(chart, use_container_width=True)
