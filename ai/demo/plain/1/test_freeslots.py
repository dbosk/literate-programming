import subprocess
import sys

import pytest

from freeslots import main


def run(*lines):
    return main(list(lines))


def test_no_bookings():
    assert run() == ["08:00-17:00"]


def test_single_booking():
    assert run("09:00-10:30") == ["08:00-09:00", "10:30-17:00"]


def test_overlapping():
    assert run("09:00-11:00", "10:00-12:00") == ["08:00-09:00", "12:00-17:00"]


def test_touching_no_zero_length_gap():
    assert run("09:00-10:00", "10:00-11:00") == ["08:00-09:00", "11:00-17:00"]


def test_unordered():
    assert run("13:00-14:00", "09:00-10:00") == [
        "08:00-09:00", "10:00-13:00", "14:00-17:00"]


def test_contained_booking():
    assert run("09:00-15:00", "10:00-11:00") == ["08:00-09:00", "15:00-17:00"]


def test_full_day():
    assert run("08:00-17:00") == []


def test_outside_day_clipped():
    assert run("06:00-09:00", "16:00-19:00") == ["09:00-16:00"]


def test_entirely_outside_day():
    assert run("05:00-07:00", "18:00-19:00") == ["08:00-17:00"]


def test_blank_lines_ignored():
    assert run("", "09:00-10:00\n", "  ") == ["08:00-09:00", "10:00-17:00"]


def test_invalid_time():
    with pytest.raises(ValueError):
        run("09:00-25:99")


def test_cli():
    r = subprocess.run([sys.executable, "freeslots.py"], input="12:00-13:00\n",
                       capture_output=True, text=True)
    assert r.stdout == "08:00-12:00\n13:00-17:00\n"
