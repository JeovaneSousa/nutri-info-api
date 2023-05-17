from fastapi import FastAPI, Path, Query
from typing import Annotated
from nutri_info_api.models import WeightGoal, NutritionalReport
from nutri_info_api.service import NutritionCalculator

app = FastAPI()  
    
@app.get("/nutri-info/{name}", status_code=200)
async def generate_nutritional_report(name: Annotated[str, 
                                                Path( 
                                                description='Name of the person that will be presented in the report.',
                                                min_length=3,
                                                max_length=30)],
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
    
    report = NutritionalReport(name,weight,height,goal.name)
    report.imc = NutritionCalculator.calculate_imc(weight,height)
    report.imc_diagnosis = NutritionCalculator.diagnose_imc(report.imc)
    report.ideal_weight_range = NutritionCalculator.calculate_ideal_weight_range(height)
    report.water_requirement = NutritionCalculator.calculate_water_requirement(weight)
    report.calorie_intake_requirement = NutritionCalculator.calculate_calorie_requirement(weight, goal)

    return report
