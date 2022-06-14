import pytest
from test1 import function_BMI
parametrize = pytest.mark.parametrize

@parametrize(
    "mass, weight, error_msg",
    [
        (-10.1, 10, "mass must be positive"),
        (10, 0, "height cannot be zero"),
    ],
)
def test_bmi_raises(mass, weight, error_msg):
    with pytest.raises(AssertionError, match=error_msg):
        bmi = function_BMI(mass, weight)
        
