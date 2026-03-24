import joblib
import pandas as pd
import warnings
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


class SalaryPredictor:
    def __init__(self):
        connector = joblib.load("salary_model.pkl")
        self.model = connector["model"]
        self.scaler = connector["scaler"]
        self.columns = connector["columns"]

    def predict(self, data):
        df = pd.DataFrame([data])
        df = pd.get_dummies(df)
        df = df.reindex(columns=self.columns, fill_value=0)
        df_scaled = self.scaler.transform(df)
        prediction = self.model.predict(df_scaled)[0]
        return float(prediction)



