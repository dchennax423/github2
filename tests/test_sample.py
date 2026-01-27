from app.calculator import add
import pytest

def test_addition():
    assert add(2, 3) == 5

@pytest.mark.slow
def test_addition_slow():
    import time
    time.sleep(5)
    assert add(10, 20) == 30
