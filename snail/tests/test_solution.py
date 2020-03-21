from solution import snail, snail2


def test_snail():
    assert snail([[]]) == []
    assert snail([[0]]) == [0]
    assert snail([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert snail([
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert snail([
        [None, 0, True],
        [-1, '', False],
        [[], 'foo', object],
    ]) == [None, 0, True, False, object, 'foo', [], -1, '']


def test_snail2():
    assert snail2([[]]) == []
    assert snail2([[0]]) == [0]
    assert snail2([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert snail2([
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert snail2([
        [None, 0, True],
        [-1, '', False],
        [[], 'foo', object],
    ]) == [None, 0, True, False, object, 'foo', [], -1, '']
