import pandas as pd

def load_and_display_data(file_path):
    try:
        # Load CSV file
        data = pd.read_csv(file_path)
        
        # Display the first 5 rows
        print("First 5 rows of the dataset:")
        print(data.head())
        print()  # Print a newline for better readability

        # Display number of missing values in each column
        print("Number of missing values in each column:")
        print(data.isnull().sum())
        
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # The path to the CSV file
    #temporarily added comma to keep the multi-line concatenation consistent with the comment
    file_path = 'data/health_data.csv'
    load_and_display_data(file_path)
