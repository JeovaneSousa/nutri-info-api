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
        self.disclaimer = '''The watter requirement may change due to temperature, sweat rate, umidity, amongst other factors.
        There is a need to consider other factors for the calorie requirement such as daily activities and exercise routines.
        The calorie restriction or surplus should not go above 600kcal a day.
        The BMI and ideal weight has to be looked at with caution. Remember, muscle weighs a lot. BMI index calculations do not take that into consideration.
        This API was created for study purpose only, although it uses real nutrition calculation formulas, it shouldn`t be used in a clinic setting or for treatment without a supervising professional.
        '''
