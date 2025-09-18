from main import sum

def test_basic_sum():
    assert sum(3, 5) == 8
    assert sum(10, 7) == 17
    assert sum(11, 21) == 32
    
def test_negative_sum():
    assert sum(-3, -8) == -11
    assert sum(-10, 5) == -5
    assert sum(-14, -66) == -80

def test_float_sum():
    assert sum(0.43, 26) == 26.43
    assert sum(27.816, 71.66) == 99.476
    assert sum(-17.62, 29.01) == 11.39
    assert sum(-12.89, -26.710) == -39.6
