class suhu():
    def __init__(self):
        pass

    def CK(self, c):
        k = c + 273  # Celcius to Kelvin = C + 273
        return k

    def CR(self, c):
        r = c * (4/5)  # Celcius to Reamur = 4/5 C
        return r

    def CF(self, c):
        f = c * (9/5) + 32  # Celcius to Fahrenheit = (9/5 C) + 32
        return f

    def FC(self, f):
        c = (f - 32) * (5/9)  # Fahrenheit to Celcius = 5/9 * (F-32)
        return c

    def FR(self, f):
        r = (f - 32) * (4/9)  # Fahrenheit to Reamur = 4/9 * (F-32)
        return r

    def KC(self, k):
        c = k - 273  # Kelvin to Celcius = K - 273
        return c

    def KR(self, k):
        r = (k - 273) * (4/5)  # Kelvin to Reamur = 4/5 * (K-273)
        return r

    def RC(self, r):
        c = r * (5/4)  # Reamur to Celcius = 5/4 R
        return c

    def RF(self, r):
        f = r * (9/4) + 32  # Reamur to Fahrenheit = (9/4 R) + 32
        return f

    def RK(self, r):
        k = r * (5/4) + 273  # Reamur to Kelvin = (5/4 R) + 273
        return k
