from kalkulator.bmi import BMI


def test_bmi():
    hitung = BMI()
    assert hitung.hitung_bmi(45, 1.5) == 20
