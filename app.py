import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import SalaryPredictor

app = FastAPI()

obj = None


class SalaryRequest(BaseModel):
    job_title: str
    experience_years: int
    education_level: str
    skills_count: int
    industry: str
    company_size: str
    location: str
    remote_work: str
    certifications: int


def get_predictor():
    global obj

    if obj is None:
        print("Cargando modelo...")
        obj = SalaryPredictor()
        print("Modelo listo")

    return obj


@app.get("/")
def healthcheck():
    return {"message": "Salary Prediction API activa"}


@app.post("/predict")
def predict(request: SalaryRequest):
    try:
        payload = request.model_dump()
        pred = get_predictor().predict(payload)

        return {
            "prediction": round(float(pred), 2)
        }

    except Exception as e:
        print("ERROR DETECTADO")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e)) from e
