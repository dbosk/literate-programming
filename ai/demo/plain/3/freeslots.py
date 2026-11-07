#!/usr/bin/env python3
"""Read booked slots (HH:MM-HH:MM) from stdin, print free slots of the working day."""
import sys

DAY_START = 8 * 60
DAY_END = 17 * 60


def parse_time(s):
    h, m = s.strip().split(":")
    h, m = int(h), int(m)
    if not (0 <= h <= 24 and 0 <= m < 60):
        raise ValueError(f"invalid time: {s!r}")
    return h * 60 + m


def fmt(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def parse_slot(line):
    start, end = line.strip().split("-")
    return parse_time(start), parse_time(end)


def free_slots(bookings, day_start=DAY_START, day_end=DAY_END):
    """bookings: iterable of (start, end) minutes. Returns list of free (start, end)."""
    free = []
    cursor = day_start
    for start, end in sorted(bookings):
        if end <= start:
            continue
        if start > cursor:
            free.append((cursor, min(start, day_end)))
        cursor = max(cursor, end)
        if cursor >= day_end:
            break
    if cursor < day_end:
        free.append((cursor, day_end))
    return free


def main(lines=None):
    lines = sys.stdin if lines is None else lines
    bookings = []
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            bookings.append(parse_slot(line))
        except ValueError:
            sys.exit(f"line {n}: invalid slot {line.strip()!r}")
    for s, e in free_slots(bookings):
        print(f"{fmt(s)}-{fmt(e)}")


if __name__ == "__main__":
    main()
