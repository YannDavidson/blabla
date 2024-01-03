import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --- Step 1: Simulate Data ---
# Simulate user data
users = pd.DataFrame({
    'user_id': range(1, 6),
    'current_title': ['Data Scientist', 'Project Manager', 'Software Engineer', 'Graphic Designer', 'Web Developer'],
    'experience': np.random.randint(1, 20, 5),
    'location': ['New York', 'San Francisco', 'Los Angeles', 'Seattle', 'Austin']
})

# Simulate job data with some factors
jobs = pd.DataFrame({
    'job_id': range(1, 11),
    'title': ['Data Scientist', 'Project Manager', 'Software Engineer', 'Graphic Designer', 'Web Developer', 'Data Analyst', 'Systems Administrator', 'Product Manager', 'UI/UX Designer', 'Database Administrator'],
    'required_experience': np.random.randint(1, 10, 10),
    'location': ['New York', 'New York', 'San Francisco', 'Los Angeles', 'Seattle', 'Austin', 'Austin', 'San Francisco', 'Los Angeles', 'Seattle']
})

# Simulate salary data based on job title, location, and experience
np.random.seed(42)
salaries = pd.DataFrame({
    'job_id': np.repeat(jobs['job_id'], 10),
    'experience': np.tile(np.arange(1, 11), 10),
    'salary': np.random.randint(50000, 150000, 100)
})

# --- Step 2: Feature Engineering ---
# Convert categorical data to numerical features
# Note: In a real-world scenario, consider more sophisticated encoding and normalization techniques
jobs_encoded = pd.get_dummies(jobs, columns=['title', 'location'])
user_encoded = pd.get_dummies(users, columns=['current_title', 'location'])

# --- Step 3: Model Building ---
# For simplicity, let's use a linear regression model to predict salary based on job features and experience
X = pd.merge(salaries, jobs_encoded, on='job_id')
y = X.pop('salary')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train[['experience']+list(jobs_encoded.columns[2:])], y_train)  # Using experience and job features

# --- Step 4: Salary Prediction ---
def predict_salary(user_id, job_id):
    user = user_encoded[user_encoded['user_id'] == user_id]
    job = jobs_encoded[jobs_encoded['job_id'] == job_id]
    
    user_experience = user['experience'].values[0]
    job_features = job.iloc[:, 2:]
    
    # Constructing the input for prediction
    input_features = np.concatenate(([user_experience], job_features))
    predicted_salary = model.predict([input_features])
    return round(predicted_salary[0], 2)

# Predict salary for a specific user and job
salary_prediction = predict_salary(1, 5)  # Change user_id and job_id to predict for different scenarios
print("Predicted Salary for User 1 and Job 5: $", salary_prediction)

