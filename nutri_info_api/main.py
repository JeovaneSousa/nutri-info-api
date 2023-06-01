from fastapi import FastAPI, Path, Query
from typing import Annotated
from nutri_info_api.models import WeightGoal, NutritionalReport
from nutri_info_api.service import ApiService

app = FastAPI()  
api_service = ApiService()

@app.get('/', status_code=200)
async def home():
    return {
        'Welcome!': 'Hope you like this simple API.',
        'Go try it out': 'Add "/docs" to the path to check de documentation'
        }
    
@app.get("/nutri-info/{name}", status_code=200)
async def generate_nutritional_report(name: Annotated[str, Path( 
                                                description='Name of the person that will be presented in the report.',
                                                min_length=3,
                                                max_length=30)],
                                        weight: Annotated[float, Query(
                                                        description='Weight value in kilograms.',
                                                        gt=0, 
                                                        le=200)],
                                        height: Annotated[float, Query(
                                                        description='Height value in meters.',
                                                        gt=0,
                                                        le=2.5
                                                        )],
                                        goal: WeightGoal):
    

    report = NutritionalReport(name,weight,height,goal)
    report = api_service.complete_report(report)

    return report
