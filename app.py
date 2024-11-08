from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

# Load the data and similarity model
movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)

def recommend(movie):
    # Find the movie index
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Return the titles of recommended movies
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

@app.route('/')
def home():
    return render_template('index.html', movie_list=movies['title'].values)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    movie_name = request.form.get('movie')
    recommendations = recommend(movie_name)
    return render_template('index.html', movie_list=movies['title'].values, recommendations=recommendations, selected_movie=movie_name)

if __name__ == '__main__':
    app.run(debug=True)
