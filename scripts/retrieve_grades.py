import pandas as pd
from sqlalchemy import create_engine

# Connect to database
engine = create_engine('sqlite:///db/grades.db')

# Load students table
df = pd.read_sql('students', con=engine)

# Print all data
print("✅ Retrieved Grades from Database:\n")
print(df)
