import streamlit as st
st.markdown(
    """
        <style>
            /* Change title color to black */
            .css-1qy5h6s {
                color: black !important;
            }
            /* Change subheader color to yellow */
            .css-hi6a2p {
                color: yellow !important;
            }
        </style>
    """,
    unsafe_allow_html=True,
)
st.title("IMDB Top 250 Movies")

st.subheader(" Dashboard for visualizing the top 250 movies on imdb")

