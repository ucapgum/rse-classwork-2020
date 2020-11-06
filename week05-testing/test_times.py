import pytest
import yaml
from times import compute_overlap_time, time_range

with open('week05-testing/fixture.yaml') as f:
    inputs = yaml.load(f, Loader=yaml.FullLoader)

@pytest.mark.parametrize("interval1, interval2, expected", [x.values() for x in inputs.values()], ids=inputs.keys())
def test_input(interval1, interval2, expected):
    result = compute_overlap_time(eval(interval1), eval(interval2))
    assert result == list(map(eval, expected))

def test_backwards_date():
    with pytest.raises(ValueError):
        time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")