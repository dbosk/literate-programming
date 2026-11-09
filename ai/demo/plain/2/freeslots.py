import sys

DAY_START = 8 * 60
DAY_END = 17 * 60


def parse_time(s):
    h, m = s.strip().split(":")
    return int(h) * 60 + int(m)


def fmt(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def parse_slot(line):
    start, end = line.split("-")
    return parse_time(start), parse_time(end)


def free_slots(bookings):
    """bookings: iterable of (start, end) minutes. Returns free (start, end) list."""
    free = []
    cursor = DAY_START
    for start, end in sorted(bookings):
        if start > cursor:
            free.append((cursor, min(start, DAY_END)))
        cursor = max(cursor, end)
        if cursor >= DAY_END:
            break
    if cursor < DAY_END:
        free.append((cursor, DAY_END))
    return free


def main(lines=None):
    if lines is None:
        lines = sys.stdin
    bookings = [parse_slot(l) for l in (x.strip() for x in lines) if l]
    return [f"{fmt(s)}-{fmt(e)}" for s, e in free_slots(bookings)]


if __name__ == "__main__":
    for out in main():
        print(out)
