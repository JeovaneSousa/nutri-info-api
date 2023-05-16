from fastapi import FastAPI, Path, Query
from typing import Annotated
from enum import Enum

app = FastAPI()

class WeightGoal(str, Enum):
    GAIN = "Gain_Weight"
    MAINTAIN = "Maintain_Body_Weight"
    LOSE = "Lose_Weight"

class IdealWeightReport():
    min_weight: float
    max_weight: float

    def __init__(self) -> None:
        pass

class NutritionalReport():
    name: str
    imc: float
    imc_diagnosis: str
    ideal_weight_range: IdealWeightReport
    water_requirement: int
    calorie_intake_requirement: int
    
@app.get("/nutri-info/{name}", status_code=200)
async def get_nutritional_report(name: Annotated[str, 
                                                Path( 
                                                description='Name of the person that will be presented in the report.',
                                                min_length=3,
                                                max_length=20)],
                                weight: Annotated[float,
                                                Query(
                                                description='Weight value in kilograms.',
                                                gt=0, 
                                                le=200)],
                                height: Annotated[float,
                                                  Query(
                                                description='Height value in meters.',
                                                gt=0,
                                                le=2.5
                                                )],
                                goal: WeightGoal):
    

    pass