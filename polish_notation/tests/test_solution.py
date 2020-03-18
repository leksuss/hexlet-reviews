from solution import calc_in_polish_notation


def test_calc_in_polish_notation():
    assert calc_in_polish_notation([1, 2, '+', 4, '*', 3, '+']) == 15
    assert calc_in_polish_notation([7, 2, 3, '*', '-']) == 1
    assert calc_in_polish_notation([1, 2, '+', 2, '*']) == 6
