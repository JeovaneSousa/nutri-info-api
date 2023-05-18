from nutri_info_api.models import IdealWeightReport, WeightGoal
class NutritionCalculator:

    @staticmethod
    def calculate_imc(weight: float,
                      height: float) -> float:
        if weight <= 0 or weight >= 300 or height <= 0   or height >= 2.5:
            return None
        
        return round(weight/(height**2),ndigits=2)
    
    @staticmethod
    def diagnose_imc(imc:float) -> str:
        if imc < 18.5: return 'Underweight'
        elif imc < 25: return 'Eutrophy'
        elif imc < 30: return "Overweight"
        else: return "Obesety" 
    
    @staticmethod
    def calculate_ideal_weight_range(height:float) -> IdealWeightReport:
        if height <= 0 or height >= 2.5:
            return None
        height_squared:float = height**2

        min: float = round(18.5 * height_squared, ndigits=2)

        max: float = round(25 * height_squared, ndigits=2)

        return IdealWeightReport(min, max)
    
    @staticmethod
    def calculate_water_requirement(weight:float) -> int:
        if weight <= 0 or weight > 200:
            return None
        return round(35 * weight)
    
    @staticmethod
    def calculate_calorie_requirement(weight:float,
                                      goal:WeightGoal) -> int:
        if weight <= 0 or weight > 200:
            return None
        if goal.name == WeightGoal.weight_loss.name:
            return round(23 * weight)
        elif goal.name == WeightGoal.weight_maintenance.name:
            return round(27 * weight)
        else: 
            return round(33 * weight)