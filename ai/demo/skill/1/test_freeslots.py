import io

import pytest

from freeslots import *


def test_parse_slot():
  assert parse_slot("09:00-10:30") == (540, 630)
  assert parse_slot(" 9:05 - 9:10\n") == (545, 550)

def test_parse_slot_rejects_garbage():
  for bad in ["", "foo", "09:00", "10:00-09:00", "09:60-10:00"]:
    with pytest.raises(ValueError):
      parse_slot(bad)
def test_merge_unordered_and_overlapping():
  slots = [(600, 700), (540, 620), (800, 900)]
  assert merge_slots(slots) == [(540, 700), (800, 900)]

def test_merge_touching():
  assert merge_slots([(540, 600), (600, 660)]) == [(540, 660)]

def test_merge_contained():
  assert merge_slots([(540, 900), (600, 660)]) == [(540, 900)]

def test_merge_empty():
  assert merge_slots([]) == []
def test_free_no_bookings():
  assert free_slots([]) == [(480, 1020)]

def test_free_gaps_between_and_at_edges():
  booked = [(540, 600), (720, 780)]
  assert free_slots(booked) == [(480, 540), (600, 720), (780, 1020)]

def test_free_fully_booked():
  assert free_slots([(480, 1020)]) == []

def test_free_back_to_back_has_no_empty_gap():
  assert free_slots([(480, 600), (600, 1020)]) == []

def test_free_bookings_outside_day_are_clipped():
  booked = [(360, 540), (1000, 1200), (1100, 1200)]
  assert free_slots(booked) == [(540, 1000)]

def test_free_booking_entirely_after_close():
  assert free_slots([(1080, 1140)]) == [(480, 1020)]
def test_format_slot():
  assert format_slot((480, 545)) == "08:00-09:05"

def test_main_end_to_end():
  stdin = io.StringIO("13:00-14:00\n09:00-10:30\n\n10:00-11:00\n11:00-12:00\n")
  stdout = io.StringIO()
  main(stdin, stdout)
  assert stdout.getvalue().splitlines() == [
    "08:00-09:00",
    "12:00-13:00",
    "14:00-17:00",
  ]
