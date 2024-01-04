import pandas as pd
import numpy as np

# --- Step 1: Simulate Data ---
# Simulate user data with skills
users = pd.DataFrame({
    'user_id': range(1, 6),
    'skills': [
        {'Python', 'SQL', 'Data Analysis'},
        {'Project Management', 'Excel', 'SQL'},
        {'Java', 'Spring', 'SQL'},
        {'Photoshop', 'Illustrator', 'Design'},
        {'HTML', 'CSS', 'JavaScript'}
    ]
})

# Simulate job data with required skills
jobs = pd.DataFrame({
    'job_id': range(1, 11),
    'required_skills': [
        {'Python', 'Machine Learning', 'Data Analysis'},
        {'Project Management', 'Agile', 'Scrum'},
        {'Java', 'Spring', 'Hibernate'},
        {'Graphic Design', 'Photoshop', 'Illustrator'},
        {'HTML', 'CSS', 'React'},
        {'Python', 'Flask', 'SQL'},
        {'Excel', 'Communication', 'SQL'},
        {'Java', 'Microservices', 'Docker'},
        {'UX Design', 'Photoshop', 'Wireframing'},
        {'JavaScript', 'Node.js', 'MongoDB'}
    ]
})

# --- Step 2: Matching Algorithm ---
def calculate_skill_match_score(user_skills, job_skills):
    # Calculate the intersection of user skills and job required skills
    matching_skills = user_skills.intersection(job_skills)
    # Score can be a simple count of matching skills or a more complex function
    score = len(matching_skills)
    return score

def recommend_jobs_for_user(user_id):
    user_skills = users.loc[users['user_id'] == user_id, 'skills'].values[0]
    scores = []
    
    for _, job in jobs.iterrows():
        score = calculate_skill_match_score(user_skills, job['required_skills'])
        scores.append((job['job_id'], score))
    
    # Sort jobs by descending order of score
    scores.sort(key=lambda x: x[1], reverse=True)
    
    # Create a DataFrame for better visualization
    score_df = pd.DataFrame(scores, columns=['job_id', 'score'])
    return score_df

# --- Step 3: Scoring ---
# Recommend jobs for a specific user
recommended_jobs = recommend_jobs_for_user(1)  # Change the user_id to recommend for different users
print("Skill Match Scores for User 1:")
print(recommended_jobs)

