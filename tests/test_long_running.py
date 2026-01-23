import time
import pytest

@pytest.mark.slow
def test_long_process():
    time.sleep(5)
    assert True
