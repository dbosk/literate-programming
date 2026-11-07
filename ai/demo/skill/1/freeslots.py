"""Print the free slots of the working day, given booked slots."""
import re
import sys

DAY_START = 8 * 60
DAY_END = 17 * 60
SLOT_RE = re.compile(r"^\s*(\d{1,2}):(\d{2})\s*-\s*(\d{1,2}):(\d{2})\s*$")
def parse_slot(line):
    """Return the slot `HH:MM-HH:MM` in `line` as (start, end) minutes.

    Raise `ValueError` if the line is malformed or ends before it starts.
    """
    match = SLOT_RE.match(line)
    if not match:
        raise ValueError(f"invalid slot: {line.strip()!r}")
    h1, m1, h2, m2 = (int(g) for g in match.groups())
    if h1 > 24 or h2 > 24 or m1 > 59 or m2 > 59:
        raise ValueError(f"invalid time in slot: {line.strip()!r}")
    start, end = h1 * 60 + m1, h2 * 60 + m2
    if end < start:
        raise ValueError(f"slot ends before it starts: {line.strip()!r}")
    return start, end
def merge_slots(slots):
    """Merge overlapping or touching (start, end) slots.

    Return a sorted list of disjoint slots.
    """
    merged = []
    for start, end in sorted(slots):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
def free_slots(booked, day_start=DAY_START, day_end=DAY_END):
    """Return the free (start, end) slots of the day given `booked` slots."""
    free = []
    cursor = day_start
    for start, end in merge_slots(booked):
        if start > cursor:
            free.append((cursor, min(start, day_end)))
        cursor = max(cursor, end)
        if cursor >= day_end:
            break
    if cursor < day_end:
        free.append((cursor, day_end))
    return [(s, e) for s, e in free if s < e]
def format_slot(slot):
    """Format a (start, end) pair of minutes as `HH:MM-HH:MM`."""
    start, end = slot
    return "%02d:%02d-%02d:%02d" % (*divmod(start, 60), *divmod(end, 60))
def main(infile=None, outfile=None):
    """Read bookings from `infile`, print free slots to `outfile`."""
    infile = infile or sys.stdin
    outfile = outfile or sys.stdout
    booked = [parse_slot(line) for line in infile if line.strip()]
    for slot in free_slots(booked):
        print(format_slot(slot), file=outfile)
if __name__ == "__main__":
    main()
