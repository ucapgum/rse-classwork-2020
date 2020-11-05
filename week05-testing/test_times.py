from times import compute_overlap_time, time_range

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap1():
    interval1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    interval2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    result = compute_overlap_time(interval1, interval2)
    expected = []
    assert result == expected

def test_no_overlap2():
    interval1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    interval2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    result = compute_overlap_time(interval2, interval1)
    expected = []
    assert result == expected


def test_several_intervals():
    interval1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    interval2 = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 2, 60)
    result = compute_overlap_time(interval1, interval2)
    expected = [("2010-01-12 11:00:30", "2010-01-12 11:59:30")]
    assert result == expected

def test_same_end():
    interval1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    interval2 = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00")
    result = compute_overlap_time(interval1, interval2)
    expected = []
    assert result == expected