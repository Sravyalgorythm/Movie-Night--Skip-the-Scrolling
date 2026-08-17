# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:44:30 2026

@author: Usha
"""

import pandas as pd
import streamlit as st

movies = [
    {
        "Movie": "Interstellar",
        "Released": 2014,
        "Genre": ["Sci-Fi", "Adventure", "Drama"],
        "Platform":["Netflix","Prime Video"],
        "IMDB" : 8.7,
        "Poster": "posters/interstellar.jpg"
    },

    {
        "Movie": "John Wick",
        "Released": 2014,
        "Genre": ["Action", "Thriller"],
        "Platform":["Netflix","Disney Plus Hotstar"],
        "IMDB":7.5,
        "Poster": "posters/john_wick.jpg"
    },

    {
        "Movie": "Mean Girls",
        "Released": 2004,
        "Genre": ["Comedy", "Teen"],
        "Platform":["Prime Video"],
        "IMDB":7.1,
        "Poster": "posters/mean_girls.jpg"
    },

    {
        "Movie": "The Dark Knight",
        "Released": 2008,
        "Genre": ["Action", "Crime", "Drama"],
        "Platform":["Netflix","Hulu"],
        "IMDB":9.1,
        "Poster": "posters/the_dark_knight.jpg"
    },

    {
        "Movie": "La La Land",
        "Released": 2016,
        "Genre": ["Romance", "Drama", "Musical"],
        "Platform":["Prime Video"],
        "IMDB":8.0,
        "Poster": "posters/la_la_land.jpg"
    },

    {
        "Movie": "Parasite",
        "Released": 2019,
        "Genre": ["Thriller", "Drama"],
        "Platform":["Netflix","Disney Plus Hotstar"],
        "IMDB":8.5,
        "Poster": "posters/parasite.jpg"
        
    },

    {
        "Movie": "Spider-Man: Into the Spider-Verse",
        "Released": 2018,
        "Genre": ["Animation", "Action", "Adventure"],
        "Platform":["Netflix"],
        "IMDB":8.4,
        "Poster": "posters/spider_verse.jpg"
        
    },

    {
        "Movie": "The Notebook",
        "Released": 2004,
        "Genre": ["Romance", "Drama"],
        "Platform":["Jio Cinema"],
        "IMDB":7.8,
        "Poster": "posters/the_notebook.jpg"
    },

    {
        "Movie": "Get Out",
        "Released": 2017,
        "Genre": ["Horror", "Thriller"],
        "Platform":["Netflix"],
        "IMDB":7.8,
        "Poster": "posters/get_out.jpg"
    },

    {
        "Movie": "The Hangover",
        "Released": 2009,
        "Genre": ["Comedy"],
        "Platform":["Netflix","Prime Video","Jio Cinema","Disney Plus Hotstar"],
        "IMDB":7.7,
        "Poster": "posters/the_hangover.jpg"
    },
    {
         "Movie": "Relax",
         "Released":2005,
         "Genre":["Thriller", "Drama", "Suspense"],
         "Platform":["Youtube"],
         "IMDB":4.7,
         "Poster": "posters/relax.jpg"
     
     }
    
]

movie_df = pd.DataFrame(movies)

st.title("Movie Night")
st.subheader("Skip The Scrolling.")
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
watched = st.multiselect(
    "Already watched?",
    movie_df["Movie"].tolist()
)

def recommend_movies(movie_df, choice, platform, min_rating,watched):
    matches = []

    for i, r in movie_df.iterrows():
        genre_match = choice.lower() in [g.lower() for g in r["Genre"]]

        platform_match = (
            platform.lower() == "any"
            or platform.lower() in [p.lower() for p in r["Platform"]]
        )

        rating_match = r["IMDB"] >= min_rating

        if genre_match and platform_match and rating_match and r['Movie'] not in watched:
            matches.append(r)

    matches.sort(key=lambda r: r["IMDB"], reverse=True)
    return matches
    


if st.button("Recommend"):
    matches = recommend_movies(
        movie_df,
        choice,
        platform,
        min_rating,
        watched
    )

    if len(matches) == 0:
        st.write("Sorry, no matches right now.")
    else:
        st.write(f"You have {len(matches)} recommendation(s)!")

        for r in matches:
            poster_col, info_col, rating_col = st.columns([1, 3, 1])

            with poster_col:
                if pd.notna(r["Poster"]):
                    st.image(r["Poster"], width=150)

            with info_col:
                st.subheader(r["Movie"])
                st.write(f"Released: {r['Released']}")
                st.write(f"Available on: {', '.join(r['Platform'])}")

            with rating_col:
                st.metric("IMDb", r["IMDB"])
