import io

import pytest

from freeslots import *

def test_parse_and_format_roundtrip():
  assert parse_slot("09:00-10:30") == (540, 630)
  assert format_slot((540, 630)) == "09:00-10:30"


def test_parse_rejects_malformed_input():
  for bad in ["", "09:00", "9:75-10:00", "ab:cd-10:00", "10:00-09:00"]:
    with pytest.raises(ValueError):
      parse_slot(bad)
def test_merge_overlapping_touching_and_unordered():
  slots = [(600, 660), (540, 600), (630, 700), (900, 960)]
  assert merge_slots(slots) == [(540, 700), (900, 960)]


def test_merge_nested_booking_does_not_shrink():
  assert merge_slots([(540, 720), (600, 660)]) == [(540, 720)]
def test_free_slots_empty_calendar():
  assert free_slots([]) == [(480, 1020)]


def test_free_slots_between_bookings():
  booked = [(parse_slot("13:00-14:00")), parse_slot("09:00-10:30")]
  assert [format_slot(s) for s in free_slots(booked)] == [
    "08:00-09:00", "10:30-13:00", "14:00-17:00"]


def test_free_slots_fully_booked():
  assert free_slots([(480, 1020)]) == []


def test_free_slots_bookings_at_edges():
  assert free_slots([(480, 540), (960, 1020)]) == [(540, 960)]


def test_free_slots_outside_day_ignored():
  assert free_slots([(0, 480), (1020, 1200)]) == [(480, 1020)]
  assert free_slots([(420, 540)]) == [(540, 1020)]
def test_main_end_to_end(monkeypatch, capsys):
  text = "13:00-14:00\n09:00-10:00\n09:30-10:30\n10:30-11:00\n\n"
  monkeypatch.setattr("sys.stdin", io.StringIO(text))
  main()
  assert capsys.readouterr().out.splitlines() == [
    "08:00-09:00", "11:00-13:00", "14:00-17:00"]
