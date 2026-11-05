import io
import pytest
import freeslots
from freeslots import free_slots, parse_slot, format_slot


def run(*lines):
    return [format_slot(s) for s in free_slots([parse_slot(l) for l in lines])]


def test_no_bookings():
    assert run() == ["08:00-17:00"]

def test_single_booking_middle():
    assert run("09:00-10:30") == ["08:00-09:00", "10:30-17:00"]

def test_touching():
    assert run("08:00-09:00", "09:00-10:00") == ["10:00-17:00"]

def test_overlapping_unordered():
    assert run("11:00-12:00", "09:00-11:30", "10:00-10:30") == [
        "08:00-09:00", "12:00-17:00"]

def test_nested():
    assert run("09:00-15:00", "10:00-11:00") == ["08:00-09:00", "15:00-17:00"]

def test_fully_booked():
    assert run("07:00-18:00") == []

def test_outside_day_ignored():
    assert run("06:00-07:00", "18:00-19:00") == ["08:00-17:00"]

def test_partially_outside():
    assert run("07:00-09:00", "16:00-18:00") == ["09:00-16:00"]

def test_gap_between_bookings():
    assert run("08:00-09:00", "10:00-17:00") == ["09:00-10:00"]

def test_bad_input():
    with pytest.raises(ValueError):
        parse_slot("25:00-26:00")
    with pytest.raises(ValueError):
        parse_slot("10:00-09:00")

def test_main(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("09:00-10:00\n\n13:00-14:00\n"))
    freeslots.main()
    assert capsys.readouterr().out.splitlines() == [
        "08:00-09:00", "10:00-13:00", "14:00-17:00"]
