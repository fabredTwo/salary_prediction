import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv("job_salary_prediction_dataset.csv")

engine = create_engine(
    "mssql+pyodbc://admin:Aws123*Letonia@instancebasic.curqukw0mbns.us-east-1.rds.amazonaws.com:1433/INDUSTRY?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
)


data.to_sql("job_data", con=engine, if_exists="append", index=False)
