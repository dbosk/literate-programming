import pytest

import freeslots
from freeslots import free_slots, main, parse_slot


def run(bookings):
    return [f"{freeslots.fmt(s)}-{freeslots.fmt(e)}"
            for s, e in free_slots([parse_slot(b) for b in bookings])]


def test_no_bookings():
    assert run([]) == ["08:00-17:00"]


def test_single_middle():
    assert run(["09:00-10:30"]) == ["08:00-09:00", "10:30-17:00"]


def test_touching():
    assert run(["09:00-10:00", "10:00-11:00"]) == ["08:00-09:00", "11:00-17:00"]


def test_overlapping_and_unordered():
    assert run(["11:00-12:30", "09:00-11:30", "12:00-13:00"]) == [
        "08:00-09:00", "13:00-17:00"]


def test_contained():
    assert run(["09:00-15:00", "10:00-11:00"]) == ["08:00-09:00", "15:00-17:00"]


def test_gap_between():
    assert run(["09:00-10:00", "12:00-13:00"]) == [
        "08:00-09:00", "10:00-12:00", "13:00-17:00"]


def test_fully_booked():
    assert run(["08:00-12:00", "12:00-17:00"]) == []


def test_outside_working_hours():
    assert run(["06:00-09:00", "16:00-19:00"]) == ["09:00-16:00"]
    assert run(["05:00-07:00", "18:00-20:00"]) == ["08:00-17:00"]


def test_booking_covers_day():
    assert run(["07:00-18:00"]) == []


def test_main(capsys):
    main(["10:00-11:00\n", "\n", "08:00-09:00\n"])
    assert capsys.readouterr().out == "09:00-10:00\n11:00-17:00\n"


def test_main_invalid():
    with pytest.raises(SystemExit):
        main(["garbage\n"])
