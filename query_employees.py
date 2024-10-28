from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Create a connection to the SQLite database
engine = create_engine('sqlite:///employee_data.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example query: Get all employees
result = session.execute(text("SELECT * FROM employees"))
print("All Employees:")
for row in result:
    print(row)

# Example query with conditions: Get active employees
result_active = session.execute(text("SELECT * FROM employees WHERE status = 'Active'"))
print("\nActive Employees:")
for row in result_active:
    print(row)

# Query all employees into a DataFrame
df_employees = pd.read_sql(text("SELECT * FROM employees"), con=engine)
print("\nEmployees DataFrame:")
print(df_employees)

# Close the session
session.close()
