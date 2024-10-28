# Simple Data Engineering Pipeline

## Project Overview
This project demonstrates a simple data engineering pipeline using Python. The pipeline reads data from a CSV file, performs data cleaning, and stores the cleaned data into an SQLite database. The goal is to provide a foundation for building more complex ETL (Extract, Transform, Load) pipelines and automate data processes.

---

## Features
- **Data Ingestion**: Load data from a CSV file.
- **Data Cleaning**:
  - Remove rows with missing employee names.
  - Fill missing salary values with the average salary.
  - Validate the employee status field to allow only "Active" or "Inactive".
- **Data Storage**: Store the cleaned data into a SQLite database.

----

## Project Structure
```
simple_data_pipeline/| 
├── employee_data.csv # Sample data file (input) 
├── pipeline.py # Main Python script for the pipeline 
├── README.md # Project documentation 
├── requirements.txt # Python dependencies (optional) 
└── employee_data.db # SQLite database (output)
```

---

## **Getting Started**

### **1. Prerequisites**
To run this project, you need to have the following installed:
- **Python 3.x**
- **Pip** (Python package manager)

### **2. Clone the Repository**
```bash
git clone https://github.com/yourusername/simple-data-pipeline.git
cd simple-data-pipeline
```
---

## Install Required Python Packages
Install the dependencies listed in the requirements.txt file.
```
pip install -r requirements.txt
```
Alternatively, you can install the packages manually:
```
pip install pandas sqlalchemy sqlite3
```
---

## Run the Pipeline
To run the data pipeline, simple execute the Python script:
```
python pipeline.py
```
---

## Check the Database
After running the pipeline, the cleaned data will be stored in an SQLite database (employee_data.db). You can use a tool like DB Browser for SQLite to inspect the database, or run queries using Python.
``` 
import pandas as pd
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///employee_data.db')

# Query the table to verify the data
df = pd.read_sql('SELECT * FROM employees', con=engine)
print(df)
```

---

## **Project Components**

### **Pipeline Script: `pipeline.py`**
This script is the core of the project and consists of three main functions:

- **`load_data(file_path)`**: Loads data from a CSV file into a Pandas DataFrame.
- **`clean_data(df)`**: Cleans the data by removing invalid rows and filling missing data.
- **`save_to_db(df, db_name)`**: Saves the cleaned data into an SQLite database.

The script runs all the steps in sequence through the **`run_pipeline(file_path)`** function.

### **Data Source: `employee_data.csv`**
The CSV file contains sample employee data with the following fields:

- **`employee_id`**: Unique identifier for each employee.
- **`name`**: Employee name (can have missing values).
- **`age`**: Employee age.
- **`department`**: Department name.
- **`salary`**: Salary (can have missing values).
- **`status`**: Employment status (should be either "Active" or "Inactive").

### **Database: `employee_data.db`**
This is the SQLite database where the cleaned data is stored. It contains one table:

- **`employees`**: Stores the cleaned employee data after ingestion and transformation.

---

## **How to Extend the Project**

- **Handle larger datasets**: Extend the project to use cloud-based storage systems like AWS S3 and databases like PostgreSQL or Redshift.
- **Integrate with Airflow**: Use Apache Airflow for scheduling and orchestrating the data pipeline.
- **Add new cleaning steps**: Enhance data cleaning by adding more sophisticated validation and transformation rules.
- **Integrate logging and monitoring**: Add logging and monitoring mechanisms for tracking pipeline failures or data anomalies.

---

## Example Usage
```
# Run the pipeline
python pipeline.py
```
```
# Verify data in the SQLite database
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///employee_data.db')
df = pd.read_sql('SELECT * FROM employees', con=engine)
print(df)

```
---

## **Contributing**
Feel free to contribute to this project! Fork the repository, make your changes, and submit a pull request.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author 
- **Simran**