from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    Pregnancies: int = Field(..., ge=0, example=2)
    Glucose: float = Field(..., gt=0, example=130)
    BloodPressure: float = Field(..., ge=0, example=80)
    SkinThickness: float = Field(..., ge=0, example=20)
    Insulin: float = Field(..., ge=0, example=85)
    BMI: float = Field(..., gt=0, example=28.5)
    DiabetesPedigreeFunction: float = Field(..., ge=0.0, example=0.627)
    Age: int = Field(..., ge=0, example=45)

    class Config:
        schema_extra = {
            "example": {
                "Pregnancies": 2,
                "Glucose": 130,
                "BloodPressure": 80,
                "SkinThickness": 20,
                "Insulin": 85,
                "BMI": 28.5,
                "DiabetesPedigreeFunction": 0.627,
                "Age": 45
            }
        }
