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
        "Genre": ["Sci-Fi", "Adventure", "Drama"],
        "Platform":["Netflix","Prime Video"]
    },

    {
        "Movie": "John Wick",
        "Released": 2014,
        "Genre": ["Action", "Thriller"],
        "Platform":["Netflix","Disney Plus Hotstar"]
    },

    {
        "Movie": "Mean Girls",
        "Released": 2004,
        "Genre": ["Comedy", "Teen"],
        "Platform":["Prime Video"]
    },

    {
        "Movie": "The Dark Knight",
        "Released": 2008,
        "Genre": ["Action", "Crime", "Drama"],
        "Platform":["Netflix","Hulu"]
    },

    {
        "Movie": "La La Land",
        "Released": 2016,
        "Genre": ["Romance", "Drama", "Musical"],
        "Platform":["Prime Video"]
    },

    {
        "Movie": "Parasite",
        "Released": 2019,
        "Genre": ["Thriller", "Drama"],
        "Platform":["Netflix","Disney Plus Hotstar"]
        
    },

    {
        "Movie": "Spider-Man: Into the Spider-Verse",
        "Released": 2018,
        "Genre": ["Animation", "Action", "Adventure"],
        "Platform":["Netflix"]
    },

    {
        "Movie": "The Notebook",
        "Released": 2004,
        "Genre": ["Romance", "Drama"],
        "Platform":["Jio Cinema"]
    },

    {
        "Movie": "Get Out",
        "Released": 2017,
        "Genre": ["Horror", "Thriller"],
        "Platform":["Netflix"]
    },

    {
        "Movie": "The Hangover",
        "Released": 2009,
        "Genre": ["Comedy"],
        "Platform":["Netflix","Prime Video","Jio Cinema","Disney Plus Hotstar"]
    }
]
movie_df=pd.DataFrame(movies)
print(movie_df)

choice=input("What Genre are you feeling? - ")

platform=input("What streaming service would you prefer? (any, Netflix, Prime Video, Hulu, Jio Cinema, Disney Plus Hotstar) - ")
print("Your rec for tonight - ")
count=1
for i,r in movie_df.iterrows():
    genre_match=(choice.lower() in [g.lower() for g in r["Genre"]])
    platform_match=(platform.lower()=="any"
                    or platform.lower() in [p.lower() for p in r["Platform"]])
    if genre_match and platform_match:
        print(f"{count}) {r['Movie']}")
        print("Release date - ",r["Released"])
        print("Available on - ",", ".join(r["Platform"]))
        count=count+1
if count!=1:
    print("Enjoy!")
else:
    print("Oops- Looks like your Genre isnt here right now.")
       
