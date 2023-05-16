class NutritionCalculator:

    @staticmethod
    def calculate_imc(weight: float,
                      height: float) -> float:
        if weight <= 0 or weight >= 300 or height <= 0   or height >= 2.5:
            return 0
        
        return round(weight/(height**2),ndigits=2)
    
    @staticmethod
    def diagnose_imc(imc:float):
        pass