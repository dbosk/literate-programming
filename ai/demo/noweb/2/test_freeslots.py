import io

import pytest

from freeslots import free_slots, main, parse_slot, parse_time


def run(text):
    out = io.StringIO()
    main(io.StringIO(text), out)
    return out.getvalue().splitlines()


def test_no_bookings():
    assert run("") == ["08:00-17:00"]


def test_single_booking_in_middle():
    assert run("09:00-10:30\n") == ["08:00-09:00", "10:30-17:00"]


def test_unordered():
    assert run("13:00-14:00\n09:00-10:00\n") == [
        "08:00-09:00", "10:00-13:00", "14:00-17:00"]


def test_overlapping():
    assert run("09:00-11:00\n10:00-12:00\n") == ["08:00-09:00", "12:00-17:00"]


def test_nested():
    assert run("09:00-15:00\n10:00-11:00\n") == ["08:00-09:00", "15:00-17:00"]


def test_touching_leaves_no_gap():
    assert run("09:00-10:00\n10:00-11:00\n") == ["08:00-09:00", "11:00-17:00"]


def test_fully_booked():
    assert run("08:00-12:00\n12:00-17:00\n") == []


def test_clipped_to_working_day():
    assert run("06:00-09:00\n16:00-20:00\n") == ["09:00-16:00"]


def test_outside_day_ignored():
    assert run("05:00-07:00\n18:00-19:00\n") == ["08:00-17:00"]


def test_blank_lines_and_whitespace():
    assert run("\n 09:00-10:00 \n\n") == ["08:00-09:00", "10:00-17:00"]


def test_duplicate_bookings():
    assert run("09:00-10:00\n09:00-10:00\n") == ["08:00-09:00", "10:00-17:00"]


def test_free_slots_function():
    assert free_slots([(540, 600)]) == [(480, 540), (600, 1020)]


def test_parse():
    assert parse_time("09:05") == 545
    assert parse_slot("09:00-10:30") == (540, 630)


@pytest.mark.parametrize("bad", ["foo", "09:00", "25:00-26:00",
                                 "10:00-09:00", "09:70-10:00"])
def test_invalid(bad):
    with pytest.raises(ValueError):
        run(bad + "\n")
