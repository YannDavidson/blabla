import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# --- Step 1: Simulate Data ---
# Simulate user data
users = pd.DataFrame({
    'user_id': range(1, 6),
    'experience': np.random.randint(1, 10, 5),
    'preferred_location': ['New York', 'San Francisco', 'Los Angeles', 'Seattle', 'Austin'],
    'preferred_tag': ['Engineering', 'Data Science', 'Design', 'Management', 'Marketing']
})

# Simulate job data
jobs = pd.DataFrame({
    'job_id': range(1, 11),
    'required_experience': np.random.randint(1, 10, 10),
    'location': ['New York', 'New York', 'San Francisco', 'Los Angeles', 'Seattle', 'Austin', 'Austin', 'San Francisco', 'Los Angeles', 'Seattle'],
    'tag': ['Engineering', 'Management', 'Data Science', 'Design', 'Engineering', 'Marketing', 'Data Science', 'Design', 'Management', 'Marketing']
})

# --- Step 2: Feature Engineering ---
# One-hot encoding for categorical data (location and tags)
user_location_dummies = pd.get_dummies(users['preferred_location'], prefix='location')
user_tag_dummies = pd.get_dummies(users['preferred_tag'], prefix='tag')

job_location_dummies = pd.get_dummies(jobs['location'], prefix='location')
job_tag_dummies = pd.get_dummies(jobs['tag'], prefix='tag')

# Combine features back to the original dataframes
users = pd.concat([users, user_location_dummies, user_tag_dummies], axis=1)
jobs = pd.concat([jobs, job_location_dummies, job_tag_dummies], axis=1)

# --- Step 3: Matching Algorithm ---
# For simplicity, we'll calculate similarity based on location and tag preferences only

def recommend_jobs(user_id):
    user = users[users['user_id'] == user_id]
    similarity_scores = cosine_similarity(user.iloc[:, 4:], jobs.iloc[:, 4:])  # Calculate cosine similarity
    job_indices = np.argsort(similarity_scores[0])[::-1]  # Descending order of similarity
    top_jobs = jobs.iloc[job_indices[:5]]  # Top 5 job recommendations
    return top_jobs

# --- Step 4: Ranking ---
# Recommend jobs for a specific user
recommended_jobs = recommend_jobs(3)  # Change the user_id to recommend for different users
print("Recommended Jobs for User 3:")
print(recommended_jobs[['job_id', 'location', 'tag']])


