"""Print the free slots of the working day, given booked slots on stdin."""
import sys

DAY_START = 8 * 60
DAY_END = 17 * 60
def parse_time(text):
    """Return minutes since midnight for a time like `09:30`."""
    hours, sep, minutes = text.strip().partition(":")
    if not (sep and hours.isdigit() and minutes.isdigit()):
        raise ValueError(f"bad time: {text!r}")
    h, m = int(hours), int(minutes)
    if h > 23 or m > 59:
        raise ValueError(f"bad time: {text!r}")
    return h * 60 + m


def format_time(minutes):
    """Return `HH:MM` for a number of minutes since midnight."""
    return f"{minutes // 60:02d}:{minutes % 60:02d}"
def parse_slot(line):
    """Return `(start, end)` in minutes for a line like `09:00-10:30`."""
    start_text, sep, end_text = line.partition("-")
    if not sep:
        raise ValueError(f"bad slot: {line!r}")
    start, end = parse_time(start_text), parse_time(end_text)
    if end < start:
        raise ValueError(f"slot ends before it starts: {line!r}")
    return start, end


def format_slot(slot):
    """Return `HH:MM-HH:MM` for a `(start, end)` pair of minutes."""
    return f"{format_time(slot[0])}-{format_time(slot[1])}"
def merge_slots(slots):
    """Return the sorted, disjoint union of `(start, end)` slots."""
    merged = []
    for start, end in sorted(slots):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
def free_slots(bookings, day_start=DAY_START, day_end=DAY_END):
    """Return the free `(start, end)` slots of the day, in order."""
    clamped = [
        (max(start, day_start), min(end, day_end))
        for start, end in bookings
        if end > day_start and start < day_end
    ]
    free = []
    cursor = day_start
    for start, end in merge_slots(clamped):
        if start > cursor:
            free.append((cursor, start))
        cursor = max(cursor, end)
    if cursor < day_end:
        free.append((cursor, day_end))
    return free
def free_slots_from_lines(lines):
    """Return free slots as `HH:MM-HH:MM` strings for booking lines."""
    bookings = [parse_slot(line.strip()) for line in lines if line.strip()]
    return [format_slot(slot) for slot in free_slots(bookings)]
def main():
    """Read bookings from stdin and print the free slots."""
    for slot in free_slots_from_lines(sys.stdin):
        print(slot)

if __name__ == "__main__":
    main()
