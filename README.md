Movie Recommender System 🎬
Check it out -> https://movie-recommender-system-tmdb.onrender.com  
This is a movie recommender system developed using Python and deployed on Render. Utilizing a dataset of 5,000 movies from TMDB, the system leverages clustering techniques to offer users relevant movie recommendations based on their preferences.

Project Overview
This project provides a movie recommendation system that suggests movies similar to a user's preferred choices. Through clustering-based machine learning techniques, the recommender system achieved an 80% accuracy in matching user inputs with relevant movie recommendations. The deployed app on Render allows users to interact with the system without any local setup.


Features
Data Cleaning and Preprocessing: Removed 8% of duplicate entries and handled 12% of missing values.
Unsupervised Learning: Trained a clustering model to group similar movies and recommend based on these clusters.
User-Friendly Deployment: Accessible on Render, providing easy access to recommendations.

Data Preprocessing
The data preprocessing phase includes:

Model Training
Algorithm: Used clustering from scikit-learn for grouping similar movies based on features.
Model Performance: Trained and tested with 80% accuracy in providing relevant movie suggestions.

├── app.py                  # Main application script
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
├── data/                   # Contains the dataset files
└── models/                 # Stores trained models
