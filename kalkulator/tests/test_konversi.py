from kalkulator.konversi import suhu


def test_konversi():
    ubah = suhu()
    assert ubah.CK(50) == 323
    assert ubah.CR(50) == 40
    assert ubah.CF(50) == 122
    assert ubah.FC(122) == 50
    assert ubah.FR(122) == 40
    assert ubah.KC(323) == 50
    assert ubah.KR(323) == 40
    assert ubah.RC(40) == 50
    assert ubah.RF(40) == 122
    assert ubah.RK(40) == 323
