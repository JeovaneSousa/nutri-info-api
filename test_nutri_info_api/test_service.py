import pytest
from nutri_info_api.service import NutritionCalculator
from nutri_info_api.models import IdealWeightReport

class TestNutritionCalculator:
    
    #IMC tests
    def test_calculate_imc_with_valid_values(self):
        assert NutritionCalculator.calculate_imc(85, 1.75) == 27.76

    def test_calculate_imc_with_off_range_values(self):
        assert NutritionCalculator.calculate_imc(0,1.75) is None
        assert NutritionCalculator.calculate_imc(301,1.75) is None
        assert NutritionCalculator.calculate_imc(75, 0) is None
        assert NutritionCalculator.calculate_imc(85, 3) is None

    def test_calculate_imc_lenght_after_comma(self):
        after_comma = ""

        result:float = NutritionCalculator.calculate_imc(85, 1.75)

        result:list[str] = str(result).split(sep='.')

        if len(result) > 1:
            after_comma = result.pop()
        
        assert len(after_comma) < 3
    
    #Ideal Weight Range tests
    def test_calculate_ideal_weight_range_with_out_of_range_values(self):
        assert NutritionCalculator.calculate_ideal_weight_range(0) is None
        assert NutritionCalculator.calculate_ideal_weight_range(-1) is None
        assert NutritionCalculator.calculate_ideal_weight_range(2.6) is None

    def test_calculate_ideal_weight_range_with_valid_values(self):
        range = IdealWeightReport(56.66, 76.56)
        test_range = NutritionCalculator.calculate_ideal_weight_range(1.75)
        assert test_range.min_weight == range.min_weight
        assert test_range.max_weight == range.max_weight

    def test_calculate_ideal_weight_range_lenght_after_comma(self):
        range = NutritionCalculator.calculate_ideal_weight_range(1.75)

        min: float = range.min_weight
        after_comma_min = ""
        max: float = range.max_weight
        after_comma_max = ""

        splited_min = str(min).split('.')
        if len(splited_min) > 1:
            after_comma_min = splited_min.pop()

        splited_max = str(max).split('.')
        if len(splited_max) > 1:
            after_comma_max = splited_max.pop()
            
        assert len(after_comma_min) < 3
        assert len(after_comma_max) < 3

    #Water Requirement tests
    def test_calculate_water_requirement_with_off_range_values(self):
        assert NutritionCalculator.calculate_water_requirement(0) is None
        assert NutritionCalculator.calculate_water_requirement(-1) is None
        assert NutritionCalculator.calculate_water_requirement(201) is None
        assert NutritionCalculator.calculate_water_requirement(300) is None

    def test_calculate_water_requirement_result_range(self):
        water_req = NutritionCalculator.calculate_water_requirement(75)
        assert len(str(water_req).split('.')) < 2



