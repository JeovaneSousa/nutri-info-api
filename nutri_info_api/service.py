from nutri_info_api.models import IdealWeightReport, WeightGoal, NutritionalReport
class NutritionCalculator:

    @staticmethod
    def calculate_bmi(weight: float,
                      height: float) -> float:
        if weight <= 0 or weight >= 300 or height <= 0   or height >= 2.5:
            return None
        
        return round(weight/(height**2),ndigits=2)
    
    @staticmethod
    def diagnose_bmi(bmi:float) -> str:
        if bmi < 18.5: return 'Underweight'
        elif bmi < 25: return 'Eutrophy'
        elif bmi < 30: return "Overweight"
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
        
class ApiService:
    def complete_report(self,report: NutritionalReport) -> NutritionalReport:
            report.bmi = NutritionCalculator.calculate_bmi(report.weight,report.height)
            report.bmi_diagnosis = NutritionCalculator.diagnose_bmi(report.bmi)
            report.ideal_weight_range = NutritionCalculator.calculate_ideal_weight_range(report.height)
            report.water_requirement = NutritionCalculator.calculate_water_requirement(report.weight)
            report.calorie_intake_requirement = NutritionCalculator.calculate_calorie_requirement(report.weight, report.goal)
            
            return report
