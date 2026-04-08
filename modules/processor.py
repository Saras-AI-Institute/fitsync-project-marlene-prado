import pandas as pd


def load_data():
    """
    Loads and cleans the health data from a CSV file.

    - Fills missing values intelligently:
        - Steps: filled with the median value
        - Sleep_Hours: filled with 7.0
        - Heart_Rate_bpm: filled with 68
        - Other columns: filled with their respective median values
    - Converts the 'Date' column to datetime objects

    Returns:
        A cleaned pandas DataFrame.
    """
    # Load the data from the CSV file
    data = pd.read_csv('data/health_data.csv')

    # Fill missing values in 'Steps' with the median value of the column
    data['Steps'].fillna(data['Steps'].median(), inplace=True)

    # Fill missing values in 'Sleep_Hours' with a constant value of 7.0
    data['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing values in 'Heart_Rate_bpm' with a constant value of 68
    data['Heart_Rate_bpm'].fillna(68, inplace=True)

    # For all other columns, fill missing values with the median of each column
    for column in data.columns:
        if column not in ['Steps', 'Sleep_Hours', 'Heart_Rate_bpm', 'Date']:
            data[column].fillna(data[column].median(), inplace=True)

    # Convert 'Date' column to datetime objects
    data['Date'] = pd.to_datetime(data['Date'])

    return data


def calculate_recovery_score(df):
    """
    Calculates and adds a 'Recovery_Score' column to the DataFrame.

    Recovery score is calculated based on:
    - Sleep Hours: Good sleep improves recovery score significantly.
    - Heart Rate: Lower heart rate indicates better recovery.
    - Steps: High activity can slightly reduce recovery due to strain.
    """
    # Define the base score
    base_score = 50

    # Calculate recovery score for each entry
    def recovery_logic(row):
        score = base_score

        # Modify score based on Sleep_Hours
        if row['Sleep_Hours'] >= 7:
            score += 20  # Good sleep
        elif row['Sleep_Hours'] < 6:
            score -= 20  # Poor sleep

        # Modify score based on Heart_Rate_bpm
        score -= (row['Heart_Rate_bpm'] - 50) * 0.5  # Lower heart rate is better

        # Modify score based on Steps (Activity)
        if row['Steps'] > 12000:
            score -= 5  # High activity can cause strain

        # Limit the score between 0 and 100
        return max(0, min(100, score))

    # Apply the logic to each row and create a new column
    df['Recovery_Score'] = df.apply(recovery_logic, axis=1)

    return df


def process_data():
    """
    Main data processing function to be used by the Streamlit dashboard.

    Loads the cleaned data and calculates the recovery score.

    Returns:
        final processed pandas DataFrame.
    """
    # Call load_data to get the cleaned DataFrame
    df = load_data()

    # Call calculate_recovery_score to add the Recovery Score
    processed_df = calculate_recovery_score(df)

    # Return the final processed DataFrame
    return processed_df

