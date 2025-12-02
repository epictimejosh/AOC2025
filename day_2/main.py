

def repeats(s):
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def part_1():
    with (open("input.txt") as f):
        data = f.read()
    data = data.strip().split(",")

    total = 0

    for r in data:
        start, end = r.split("-")
        start, end = int(start), int(end)

        for n in range(start, end + 1):
            if repeats(str(n)):
                total += n

    print(total)


def repeated_any(s):
    n = len(s)
    for size in range(1, n):
        if n % size == 0:
            chunk = s[:size]
            if chunk * (n // size) == s:
                return True
    return False


def part_2():
    with open("input.txt") as f:
        data = f.read()
    data = data.strip().split(",")

    total = 0

    for r in data:
        start, end = map(int, r.split("-"))

        for n in range(start, end + 1):
            if repeated_any(str(n)):
                total += n

    print(total)


part_2()


