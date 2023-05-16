import pytest
from nutri_info_api.service import NutritionCalculator

class TestNutritionCalculator:
    
    def test_calculate_imc_with_valid_values(self):
        assert NutritionCalculator.calculate_imc(85, 1.75) == 27.76

    def test_calculate_imc_with_off_range_values(self):
        assert NutritionCalculator.calculate_imc(0,1.75) == 0
        assert NutritionCalculator.calculate_imc(301,1.75) == 0
        assert NutritionCalculator.calculate_imc(75, 0) == 0
        assert NutritionCalculator.calculate_imc(85, 3) == 0

    def test_calculate_imc_lenght_after_comma(self):
        after_comma = ""

        result:float = NutritionCalculator.calculate_imc(85, 1.75)

        result:list[str] = str(result).split(sep='.')

        if len(result) > 1:
            after_comma = result.pop()
        
        assert len(after_comma) < 3
                