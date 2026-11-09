from freeslots import main


def test_no_bookings():
    assert main([]) == ["08:00-17:00"]


def test_single_middle():
    assert main(["09:00-10:30"]) == ["08:00-09:00", "10:30-17:00"]


def test_overlapping_and_unordered():
    assert main(["11:00-12:00", "09:00-11:30", "10:00-10:30"]) == [
        "08:00-09:00",
        "12:00-17:00",
    ]


def test_touching():
    assert main(["09:00-10:00", "10:00-11:00"]) == ["08:00-09:00", "11:00-17:00"]


def test_full_day():
    assert main(["08:00-12:00", "12:00-17:00"]) == []


def test_outside_working_hours_clipped():
    assert main(["07:00-09:00", "16:00-18:00"]) == ["09:00-16:00"]


def test_booking_entirely_outside():
    assert main(["06:00-07:00", "18:00-19:00"]) == ["08:00-17:00"]


def test_blank_lines_ignored():
    assert main(["", "09:00-10:00", "\n"]) == ["08:00-09:00", "10:00-17:00"]
