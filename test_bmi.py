import lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(height=1.73, weight=65)
    assert (result == 0)

def test_bmi_underweight():

    result = bmi.calculate_bmi(height=1.73, weight=50)
    assert (result == -1)

def test_bmi_overweight():
    result = bmi.calculate_bmi(height=1.73, weight=80)
    assert (result == 1)