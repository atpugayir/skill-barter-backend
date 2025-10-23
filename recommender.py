import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example dataset
ITEMS = [
    "Python Programming",
    "Data Science",
    "Web Development",
    "Machine Learning",
    "Flask Framework",
    "ReactJS Frontend"
]

def get_recommendations(user_input, top_n=3):
    if not user_input:
        return []

    corpus = ITEMS + [user_input]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    sim_scores = list(enumerate(similarity[0]))
    sim_scores.sort(key=lambda x: x[1], reverse=True)
    recommended = [ITEMS[i] for i, score in sim_scores[:top_n]]
    return recommended
