from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((1,6),(2,5))
    assert overlapping_intervals((3,6),(1,5))
    assert overlapping_intervals((2,5),(1,6))
    assert overlapping_intervals((0,0),(0,0))
    assert overlapping_intervals((1,9),(1,1))