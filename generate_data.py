import pandas as pd
import numpy as np

# Setting the random seed for reproducibility
np.random.seed(0)

# Define the date range for the year 2025
start_date = '2025-01-01'
end_date = '2025-12-31'
date_range = pd.date_range(start=start_date, end=end_date)

# Number of days to generate data for
num_days = len(date_range)

# Generate realistic data
steps = np.random.normal(8500, 3000, num_days).clip(3000, 18000)
sleep_hours = np.random.normal(7.2, 1.0, num_days).clip(4.5, 9.5)
heart_rate = np.random.normal(68, 10, num_days).clip(48, 110)
calories_burned = np.random.uniform(1800, 2400, num_days)
active_minutes = np.random.uniform(20, 180, num_days)

# Create a DataFrame
fitness_data = pd.DataFrame({
    'Date': date_range,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Introduce 5% missing values
for column in fitness_data.columns[1:]:  # skip the 'Date' column
    fitness_data.loc[fitness_data.sample(frac=0.05).index, column] = np.nan

# Save to CSV file
fitness_data.to_csv('data/health_data.csv', index=False)