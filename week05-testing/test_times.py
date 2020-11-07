import datetime
import json
import mock
import pytest
import yaml
from times import compute_overlap_time, time_range, iss_passes

with open('week05-testing/fixture.yaml') as f:
    inputs = yaml.load(f, Loader=yaml.FullLoader)

@pytest.mark.parametrize("interval1, interval2, expected", [x.values() for x in inputs.values()], ids=list(inputs.keys()))
def test_input(interval1, interval2, expected):
    result = compute_overlap_time(eval(interval1), eval(interval2))
    assert result == list(map(eval, expected))

def test_backwards_date():
    with pytest.raises(ValueError):
        time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")

def test_iss_passes():
    with mock.patch('requests.get') as mock_get:
        lat = 51.5246
        lon = 0.134
        n = 10
        with open('iss_mock.json', 'r') as f:
            data = json.load(f)
        mock_get.json.return_value = data
        expected = iss_passes(lat, lon, n)
        mock_get.assert_called_with(
            "http://api.open-notify.org/iss-pass.json",
            params={
                "lat" : lat,
                "lon" : lon,
                "n" : n
                }
        )
        assert expected == compute_overlap_time(expected, (datetime.datetime(2020, 11, 7), datetime.datetime(2020, 11, 10)))
