"""Print the free slots of the working day, given the booked ones."""
import re
import sys
DAY_START = 8 * 60
DAY_END = 17 * 60
SLOT_RE = re.compile(r"^(\d{1,2}):(\d{2})-(\d{1,2}):(\d{2})$")
def parse_slot(line):
    """Parse `HH:MM-HH:MM` into a (start, end) pair of minutes.

    Raise `ValueError` if the text is malformed or the end is not
    after the start.
    """
    match = SLOT_RE.match(line.strip())
    if match is None:
        raise ValueError(f"bad time slot: {line.strip()!r}")
    h1, m1, h2, m2 = (int(g) for g in match.groups())
    if m1 > 59 or m2 > 59 or h1 > 23 or h2 > 24:
        raise ValueError(f"time out of range: {line.strip()!r}")
    start, end = h1 * 60 + m1, h2 * 60 + m2
    if end <= start:
        raise ValueError(f"slot must end after it starts: {line.strip()!r}")
    return start, end
def format_slot(start, end):
    """Format a (start, end) pair of minutes as `HH:MM-HH:MM`."""
    s_h, s_m = divmod(start, 60)
    e_h, e_m = divmod(end, 60)
    return f"{s_h:02d}:{s_m:02d}-{e_h:02d}:{e_m:02d}"
def merge(slots):
    """Return the sorted, disjoint union of (start, end) pairs."""
    merged = []
    for start, end in sorted(slots):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
def free_slots(bookings, day_start=DAY_START, day_end=DAY_END):
    """Return the free (start, end) pairs between `day_start` and `day_end`."""
    free = []
    cursor = day_start
    for start, end in merge(bookings):
        if start > cursor:
            free.append((cursor, min(start, day_end)))
        cursor = max(cursor, end)
        if cursor >= day_end:
            break
    if cursor < day_end:
        free.append((cursor, day_end))
    return free
def free_slot_lines(lines):
    """Map booking lines to the formatted free-slot lines."""
    bookings = [parse_slot(line) for line in lines if line.strip()]
    return [format_slot(s, e) for s, e in free_slots(bookings)]


def main():
    """Read bookings from standard input and print the free slots."""
    try:
        for line in free_slot_lines(sys.stdin):
            print(line)
    except ValueError as err:
        sys.exit(f"freeslots: {err}")
if __name__ == "__main__":
    main()
