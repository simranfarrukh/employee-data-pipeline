import pandas as pd
from sqlalchemy import create_engine


def load_data(file_path):
    """Ingest data from a CSV file."""
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """Clean the dataset by removing invalid rows and filling missing data."""
    # Remove rows with missing names
    df_cleaned = df.dropna(subset=['name'])

    # Fill missing salary with the average salary
    average_salary = df_cleaned['salary'].mean()
    df_cleaned['salary'].fillna(average_salary, inplace=True)

    # Keep only valid statuses (Active/Inactive)
    df_cleaned = df_cleaned[df_cleaned['status'].isin(['Active', 'Inactive'])]

    return df_cleaned


def save_to_db(df, db_name='employee_data.db'):
    """Save the cleaned data into an SQLite database."""
    # Create SQLite engine
    engine = create_engine(f'sqlite:///{db_name}')
    # Save to the database
    df.to_sql('employees', con=engine, if_exists='replace', index=False)


def run_pipeline(file_path):
    """Run the entire data pipeline."""
    # Step 1: Load data
    df = load_data(file_path)
    print("Original Data:")
    print(df)

    # Step 2: Clean data
    df_cleaned = clean_data(df)
    print("\nCleaned Data:")
    print(df_cleaned)

    # Step 3: Save cleaned data to database
    save_to_db(df_cleaned)
    print("\nData pipeline complete. Cleaned data saved to database.")


# Run the pipeline with the specified CSV file
file_path = 'employee_data.csv'
run_pipeline(file_path)
