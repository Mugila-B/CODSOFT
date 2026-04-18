import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": [
        "Titanic", "Avatar", "The Notebook",
        "Avengers", "Iron Man", "Captain America"
    ],
    "genre": [
        "romance drama", "sci-fi adventure", "romance drama",
        "action superhero", "action superhero", "action superhero"
    ]
}

df = pd.DataFrame(data)

cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

similarity = cosine_similarity(matrix)

def recommend(movie):
    if movie not in df["title"].values:
        print("Movie not found")
        return
    
    index = df[df["title"] == movie].index[0]
    scores = list(enumerate(similarity[index]))
    
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print(f"Recommendations for {movie}:")
    for i in scores[1:4]:
        print(df.iloc[i[0]]["title"])

movie_name = input("Enter a movie name: ")
recommend(movie_name)
