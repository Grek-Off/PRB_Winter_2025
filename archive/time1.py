import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///students.db")

query = "SELECT * FROM students"
df_students = pd.read_sql(query, engine)

print(df_students)
