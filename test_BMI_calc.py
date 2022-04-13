import pytest
from BMI_calc import BMI_calc_category

# Weak N x 1 Test Cases
# [0, 18.5): -0.1, 0, 9, 18.4, 18.5
# [18.5, 24.9]: 18.4, 18.5, 22, 24.9, 25
# [25, 29.9]: 24.9, 25, 27, 29.9, 30
# [30, infinity) 29.9, 30, 45

# Pytest Testing
# [0, 18.5): -0.1, 0, 9, 18.4, 18.5
@pytest.mark.parametrize("BMI, BMI_category", [(-0.1,"Error"), (0,"Underweight"), (9, "Underweight"), (18.4, "Underweight"), (18.5, "Normal")])
def test_BMI_calc_category_underweight(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

# [18.5, 24.9]: 18.4, 18.5, 22, 24.9, 25
@pytest.mark.parametrize("BMI, BMI_category", [(18.4,"Underweight"), (18.5,"Normal"), (22, "Normal"), (24.9, "Normal"), (25, "Overweight")])
def test_BMI_calc_category_normal(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

# [25, 29.9]: 24.9, 25, 27, 29.9, 30
@pytest.mark.parametrize("BMI, BMI_category", [(24.9,"Normal"), (25,"Overweight"), (27, "Overweight"), (29.9, "Overweight"), (30, "Obese")])
def test_BMI_calc_category_overweight(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

# [30, infinity) 29.9, 30, 45
@pytest.mark.parametrize("BMI, BMI_category", [(29.9,"Overweight"), (30,"Obese"), (45, "Obese")])
def test_BMI_calc_category_obese(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category