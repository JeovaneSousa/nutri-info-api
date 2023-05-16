from fastapi import FastAPI, Path, Query
from typing import Annotated
from nutri_info_api.models import WeightGoal

app = FastAPI()  
    
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