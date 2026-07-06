# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:46:31 2026

@author: Sravya
"""
import pandas as pd

movies = [
    {
        "Movie": "Interstellar",
        "Released": 2014,
        "Genre": ["Sci-Fi", "Adventure", "Drama"]
    },

    {
        "Movie": "John Wick",
        "Released": 2014,
        "Genre": ["Action", "Thriller"]
    },

    {
        "Movie": "Mean Girls",
        "Released": 2004,
        "Genre": ["Comedy", "Teen"]
    },

    {
        "Movie": "The Dark Knight",
        "Released": 2008,
        "Genre": ["Action", "Crime", "Drama"]
    },

    {
        "Movie": "La La Land",
        "Released": 2016,
        "Genre": ["Romance", "Drama", "Musical"]
    },

    {
        "Movie": "Parasite",
        "Released": 2019,
        "Genre": ["Thriller", "Drama"]
    },

    {
        "Movie": "Spider-Man: Into the Spider-Verse",
        "Released": 2018,
        "Genre": ["Animation", "Action", "Adventure"]
    },

    {
        "Movie": "The Notebook",
        "Released": 2004,
        "Genre": ["Romance", "Drama"]
    },

    {
        "Movie": "Get Out",
        "Released": 2017,
        "Genre": ["Horror", "Thriller"]
    },

    {
        "Movie": "The Hangover",
        "Released": 2009,
        "Genre": ["Comedy"]
    }
]
movie_df=pd.DataFrame(movies)
print(movie_df)

choice=input("What Genre are you feeling? - ")
print("Your rec for tonight - ")
count=1
for i,r in movie_df.iterrows():
    if choice.lower() in [g.lower() for g in r["Genre"]}:
        print(f"{count}) {r['Movie']}")
        print("Release date - ",r["Released"])
        count=count+1
if count!=1:
    print("Enjoy!")
else:
    print("Oops- Looks like your Genre isnt here right now.")
       
