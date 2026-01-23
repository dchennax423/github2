import time
import pytest

@pytest.mark.slow
def test_long_running_job():
    time.sleep(20)
    assert True
