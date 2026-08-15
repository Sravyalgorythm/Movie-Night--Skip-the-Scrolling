# -*- coding: utf-8 -*-



import pandas as pd
import streamlit as st

movies = [
    {
        "Movie": "Interstellar",
        "Released": 2014,
        "Genre": ["Sci-Fi", "Adventure", "Drama"],
        "Platform":["Netflix","Prime Video"],
        "IMDB" : 8.7
    },

    {
        "Movie": "John Wick",
        "Released": 2014,
        "Genre": ["Action", "Thriller"],
        "Platform":["Netflix","Disney Plus Hotstar"],
        "IMDB":7.5
    },

    {
        "Movie": "Mean Girls",
        "Released": 2004,
        "Genre": ["Comedy", "Teen"],
        "Platform":["Prime Video"],
        "IMDB":7.1
    },

    {
        "Movie": "The Dark Knight",
        "Released": 2008,
        "Genre": ["Action", "Crime", "Drama"],
        "Platform":["Netflix","Hulu"],
        "IMDB":9.1
    },

    {
        "Movie": "La La Land",
        "Released": 2016,
        "Genre": ["Romance", "Drama", "Musical"],
        "Platform":["Prime Video"],
        "IMDB":8.0
    },

    {
        "Movie": "Parasite",
        "Released": 2019,
        "Genre": ["Thriller", "Drama"],
        "Platform":["Netflix","Disney Plus Hotstar"],
        "IMDB":8.5
        
    },

    {
        "Movie": "Spider-Man: Into the Spider-Verse",
        "Released": 2018,
        "Genre": ["Animation", "Action", "Adventure"],
        "Platform":["Netflix"],
        "IMDB":8.4
    },

    {
        "Movie": "The Notebook",
        "Released": 2004,
        "Genre": ["Romance", "Drama"],
        "Platform":["Jio Cinema"],
        "IMDB":7.8
    },

    {
        "Movie": "Get Out",
        "Released": 2017,
        "Genre": ["Horror", "Thriller"],
        "Platform":["Netflix"],
        "IMDB":7.8
    },

    {
        "Movie": "The Hangover",
        "Released": 2009,
        "Genre": ["Comedy"],
        "Platform":["Netflix","Prime Video","Jio Cinema","Disney Plus Hotstar"],
        "IMDB":7.7
    }
]

movie_df = pd.DataFrame(movies)

st.title("Movie Night")
st.write("Welcome to my movie recommendation app!")



available_genres = []

for i in movie_df["Genre"]:
    for j in i:
        if j not in available_genres:
            available_genres.append(j)

available_genres.sort()
choice = st.selectbox("What genre are you feeling?", available_genres)

available_platforms = []

for i in movie_df["Platform"]:
    for j in i:
        if j not in available_platforms:
            available_platforms.append(j)

available_platforms.sort()

platform = st.selectbox(
    "What streaming service would you prefer?",
    ["ANY"] + available_platforms
)
min_rating = st.number_input("Minimum IMDb rating",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1)

if st.button("Recommend"):
    matches = []
    for i, r in movie_df.iterrows():
        genre_match = choice.lower() in [g.lower() for g in r["Genre"]]

        platform_match = (
            platform.lower() == "any"
            or platform.lower() in [p.lower() for p in r["Platform"]]
            )
        rating_match = r["IMDB"] >= min_rating

        if genre_match and platform_match and rating_match:
            matches.append(r)
        matches.sort(key=lambda r: r["IMDB"], reverse=True)

    if len(matches) == 0:
        st.write("Sorry, no matches right now.")

    else:
        st.write(f"You have {len(matches)} recommendation(s)!")

    for r in matches:
        st.subheader(r["Movie"])
        st.write("Release date:", r["Released"])
        st.write("Available on:", ", ".join(r["Platform"]))
        st.write("IMDB:", r["IMDB"])eleased"])
        st.write("Available on:", ", ".join(r["Platform"]))
        st.write("IMDB:", r["IMDB"])
