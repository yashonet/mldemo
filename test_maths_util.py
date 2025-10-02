import maths_utils
def test_add():
    assert maths_utils.add(2,3) == 5
    assert maths_utils.add(-1,1) == 0
    assert maths_utils.add(0,0) == 0

def test_subtract():
    assert maths_utils.subtract(5,3) == 2
    assert maths_utils.subtract(-1,1) == -2
    assert maths_utils.subtract(0,0) == 0