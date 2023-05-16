from enum import Enum
from nutri_info_api.service import NutritionCalculator

class WeightGoal(str, Enum):
    GAIN = "gain_weight"
    MAINTAIN = "maintain_body_weight"
    LOSE = "lose_weight"  

class IdealWeightReport():
    min_weight: float
    max_weight: float

    def __init__(self, min_weight: float, max_weight: float) -> None:
        self.min_weight = min_weight
        self.max_weight = max_weight    

class NutritionalReport():
    name: str
    weight: float
    height: float
    goal: WeightGoal
    imc: float
    imc_diagnosis: str
    ideal_weight_range: IdealWeightReport
    water_requirement: int
    calorie_intake_requirement: int

    def __init__(self,
                 name: str,
                 weight: float,
                 height: float,
                 goal: WeightGoal) -> None:
        self.name = name
        self.weight = weight
        self.height = height
        self.goal = goal.name
        self.imc = NutritionCalculator.calculate_imc(weight, height)

