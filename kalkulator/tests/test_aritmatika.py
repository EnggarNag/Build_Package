from kalkulator.aritmatika import InputBilangan


def test_aritmatika():
    hitung = InputBilangan(10, 10)
    assert hitung.kali() == 100
    assert hitung.bagi() == 1
    assert hitung.jumlah() == 20
    assert hitung.kurang() == 0
