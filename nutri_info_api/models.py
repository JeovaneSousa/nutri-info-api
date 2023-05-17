from enum import Enum

class WeightGoal(Enum):
    weight_gain = 'GAIN'
    weight_maintenance = "MAINTENANCE"
    weight_loss = "LOSS"

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
    imc: float | None = None
    imc_diagnosis: str | None = None
    ideal_weight_range: IdealWeightReport | None = None
    water_requirement: int |  None = None
    calorie_intake_requirement: int |  None = None

    def __init__(self,
                 name: str,
                 weight: float,
                 height: float,
                 goal: WeightGoal) -> None:
        self.name = name
        self.weight = weight
        self.height = height
        self.goal = goal
