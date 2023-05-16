from enum import Enum

class WeightGoal(str, Enum):
    GAIN = "Gain_Weight"
    MAINTAIN = "Maintain_Body_Weight"
    LOSE = "Lose_Weight"  

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

    def __init__(self, name, weight, height, imc, imc_diagnosis, ideal_weight_range, water_requirement, calorie_intake_requirement) -> None:
        self.name = name
        self.weight = weight
        self.height = height
        self.goal = 


    def calculate_imc(self,
                      weight: float,
                      height: float) -> float:
    
    def calculate