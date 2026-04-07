import pytest
from medical_math import calculate_bmi,is_fever

#----------simple assert testing

def test_calculate_bmi():
    assert calculate_bmi(70,1.75)== 22.86


def test_is_fever():
    assert is_fever(42) is True

def test_is_fever1():
    assert is_fever(35) is False



