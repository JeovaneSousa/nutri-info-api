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
    goal_description: str
    bmi: float | None = None
    bmi_diagnosis: str | None = None
    ideal_weight_range: IdealWeightReport | None = None
    water_requirement: int |  None = None
    calorie_intake_requirement: int |  None = None
    disclaimer: str

    def __init__(self,
                 name: str,
                 weight: float,
                 height: float,
                 goal: WeightGoal) -> None:
        self.name = name
        self.weight = weight
        self.height = height
        self.goal = goal
        self.goal_description = goal.name
        self.disclaimer = 'The water requirement may change due to temperature, sweat rate, umidity, amongst other factors.\nThere is a need to consider other factors for the calorie requirement such as daily activities and exercise routines.\nThe calorie restriction or surplus should not go above 600kcal a day.\nThe BMI and ideal weight should be analyzed with caution. Remember, BMI does not take into consideration what is muscle mass and what is fat, only body weight as a whole.\nThis API was created for study purpose only, although it uses real nutrition calculation formulas, it shouldn`t be used in a clinic setting or for treatment without a supervising professional.'
