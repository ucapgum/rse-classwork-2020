import pytest
from times import compute_overlap_time, time_range

inputs = []
inputs.append([time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), \
     [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]])
inputs.append([time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"), []])
inputs.append([time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"), []])
inputs.append([time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60), time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 2, 60), \
     [("2010-01-12 11:00:30", "2010-01-12 11:59:30")]])
inputs.append([time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"), time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00"), []])

@pytest.mark.parametrize("interval1, interval2, expected", inputs)
def test_input(interval1, interval2, expected):
    result = compute_overlap_time(interval1, interval2)
    assert result == expected

def test_backwards_date():
    with pytest.raises(ValueError):
        interval = time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")