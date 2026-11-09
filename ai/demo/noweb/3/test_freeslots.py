import io
import pytest
from freeslots import free_slots, parse_slot, format_slot, main


def run(*lines):
    out = io.StringIO()
    main(io.StringIO("\n".join(lines) + "\n"), out)
    return out.getvalue().splitlines()


def test_no_bookings():
    assert run() == ["08:00-17:00"]

def test_single_booking_middle():
    assert run("09:00-10:30") == ["08:00-09:00", "10:30-17:00"]

def test_unordered():
    assert run("13:00-14:00", "09:00-10:00") == [
        "08:00-09:00", "10:00-13:00", "14:00-17:00"]

def test_overlapping():
    assert run("09:00-11:00", "10:00-12:00") == ["08:00-09:00", "12:00-17:00"]

def test_contained():
    assert run("09:00-12:00", "10:00-11:00") == ["08:00-09:00", "12:00-17:00"]

def test_touching():
    assert run("09:00-10:00", "10:00-11:00") == ["08:00-09:00", "11:00-17:00"]

def test_full_day():
    assert run("08:00-17:00") == []

def test_covered_by_several():
    assert run("08:00-12:00", "12:00-17:00") == []

def test_outside_working_hours():
    assert run("06:00-09:00", "16:00-20:00") == ["09:00-16:00"]

def test_entirely_outside():
    assert run("05:00-07:00", "18:00-19:00") == ["08:00-17:00"]

def test_starts_after_day_end():
    assert run("09:00-10:00", "17:30-18:00") == ["08:00-09:00", "10:00-17:00"]

def test_blank_lines_ignored():
    assert run("", "09:00-10:00", "") == ["08:00-09:00", "10:00-17:00"]

def test_duplicates():
    assert run("09:00-10:00", "09:00-10:00") == ["08:00-09:00", "10:00-17:00"]

def test_free_slots_function():
    assert free_slots([(540, 600)]) == [(480, 540), (600, 1020)]

def test_roundtrip():
    assert format_slot(parse_slot("09:05-10:30")) == "09:05-10:30"

import pytest

@pytest.mark.parametrize("bad", ["garbage", "10:00-09:00", "09:00-09:00",
                                 "25:00-26:00", "09:60-10:00", "9-10"])
def test_invalid(bad):
    with pytest.raises(ValueError):
        parse_slot(bad)
