from freeslots import *
import pytest


def test_parse_and_format_roundtrip():
  assert parse_slot("09:00-10:30") == (540, 630)
  assert format_slot(540, 630) == "09:00-10:30"


@pytest.mark.parametrize(
  "bad",
  ["", "9-10", "10:00-09:00", "10:00-10:00", "25:00-26:00", "09:60-10:00"],
)
def test_parse_rejects_bad_input(bad):
  with pytest.raises(ValueError):
    parse_slot(bad)
def test_merge_overlap_touch_nested_and_unordered():
  slots = [(600, 660), (540, 600), (630, 700), (650, 660), (800, 810)]
  assert merge(slots) == [(540, 700), (800, 810)]


def test_merge_empty():
  assert merge([]) == []
def test_no_bookings_whole_day_free():
  assert free_slots([]) == [(DAY_START, DAY_END)]


def test_gaps_between_and_around_bookings():
  booked = [(540, 630), (630, 720), (660, 690)]
  assert free_slots(booked) == [(480, 540), (720, 1020)]


def test_bookings_outside_day_are_clipped():
  assert free_slots([(0, 9 * 60), (16 * 60, 20 * 60)]) == [(540, 960)]
  assert free_slots([(0, 7 * 60)]) == [(DAY_START, DAY_END)]
  assert free_slots([(18 * 60, 19 * 60)]) == [(DAY_START, DAY_END)]


def test_fully_booked_day():
  assert free_slots([(480, 700), (700, 1020)]) == []
def test_free_slot_lines_end_to_end():
  lines = ["13:00-14:00\n", "\n", "09:00-10:30\n", "10:00-11:00\n"]
  assert free_slot_lines(lines) == [
    "08:00-09:00",
    "11:00-13:00",
    "14:00-17:00",
  ]
