import answer

def test_add():
    assert (answer.add(1, 2) == 3)
    assert (answer.add(1, 1) == 2)
    assert (answer.add(100, 200) == 300)
    assert (answer.add(0, 1) == 1)
    assert (answer.add(-1, 1) == 0)