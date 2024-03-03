class BMI():  # BMI Body Mass Index
    def __init__(self):
        pass

    def hitung_bmi(self, bb, t):    # bb = berat badan, t = tinggi
        bmi = bb / (t ** 2)  # BMI = berat badan (kg)/ (tinggi badan^2)(m)
        return bmi
