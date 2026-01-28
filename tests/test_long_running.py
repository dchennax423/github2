import time
import pytest

@pytest.mark.slow
def test_long_process():
    time.sleep(20)   # demo purpose (20 sec)
    assert True
