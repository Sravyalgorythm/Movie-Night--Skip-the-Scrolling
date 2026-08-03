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
available_genres=[]
for i in movie_df["Genre"]:
    for j in i:
        if j not in available_genres: 
            available_genres.append(j)
available_genres.sort()
print("AVAILABLE GENRES - ")
for i in available_genres:
    print(f" ~ {i}",end="\n")
choice=input("What Genre are you feeling? - ")
available_platforms=[]
for i in movie_df["Platform"]:
    for j in i:
        if j not in available_platforms:
            available_platforms.append(j)
available_platforms.sort()
for i in available_platforms:
    print(f" ~ {i}",end='\n')

platform=input("What streaming service would you prefer? ( enter ANY for all platforms - ")
print("Your rec for tonight - ")
count=1
matches=[]
for i,r in movie_df.iterrows():
    genre_match=(choice.lower() in [g.lower() for g in r["Genre"]])
    platform_match=(platform.lower()=="any"
                    or platform.lower() in [p.lower() for p in r["Platform"]])
    if genre_match and platform_match:
        matches.append(r)
        
if (len(matches)==1):
    print(f"\nYou have {len(matches)} recommendation!\n")
else:
    print(f"\nYou have {len(matches)} recommendations!\n")
for r in matches:
    print(f"{count}) {r['Movie']}")
    print("Release date - ",r["Released"])
    print("Available on - ",", ".join(r["Platform"]))
    count=count+1
if len(matches)!=0:
    print("Enjoy!")
else:
    print("Oops- Looks like your Genre isnt here right now.")
       
