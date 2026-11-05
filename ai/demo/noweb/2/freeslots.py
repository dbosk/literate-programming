#!/usr/bin/env python3
"""Print the free slots of the working day given booked slots on stdin."""
import sys

DAY_START = 8 * 60
DAY_END = 17 * 60
def parse_time(text):
    """Convert 'HH:MM' to minutes since midnight."""
    hours, minutes = text.strip().split(":")
    h, m = int(hours), int(minutes)
    if not (0 <= h <= 24 and 0 <= m < 60) or (h == 24 and m != 0):
        raise ValueError(f"invalid time: {text!r}")
    return h * 60 + m


def format_time(minutes):
    """Convert minutes since midnight to 'HH:MM'."""
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def parse_slot(line):
    """Convert 'HH:MM-HH:MM' to a (start, end) pair of minutes."""
    start, end = line.strip().split("-")
    start, end = parse_time(start), parse_time(end)
    if end < start:
        raise ValueError(f"slot ends before it starts: {line!r}")
    return start, end


def format_slot(slot):
    return f"{format_time(slot[0])}-{format_time(slot[1])}"
def free_slots(bookings, day_start=DAY_START, day_end=DAY_END):
    """Return the free (start, end) pairs in the day, given bookings."""
    free = []
    cursor = day_start
    for start, end in sorted(bookings):
        if start > cursor:
            free.append((cursor, min(start, day_end)))
        cursor = max(cursor, end)
        if cursor >= day_end:
            break
    if cursor < day_end:
        free.append((cursor, day_end))
    return free
def main(stdin=None, stdout=None):
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    bookings = [parse_slot(line) for line in stdin if line.strip()]
    for slot in free_slots(bookings):
        print(format_slot(slot), file=stdout)

if __name__ == "__main__":
    main()
