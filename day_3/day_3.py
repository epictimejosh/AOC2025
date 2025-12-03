def part_1():
    with open("input.txt") as f:
        data = f.readlines()

    total = 0

    for line in data:
        line = line.strip()

        best = 0
        max_left = int(line[0])

        for char in line[1:]:
            d = int(char)

            candidate = max_left * 10 + d
            if candidate > best:
                best = candidate

            if d > max_left:
                max_left = d

        total += best

    print(total)


def part_2():
    with open("input.txt") as f:
        data = f.readlines()

    total = 0

    for line in data:
        line = line.strip()
        digits = []
        for c in line:
            digits.append(int(c))

        to_remove = len(digits) - 12

        stack = []

        for d in digits:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        if to_remove > 0:
            stack = stack[:-to_remove]

        chosen = stack[:12]

        for x in chosen:
            total += (int("".join(str(x))))

    print(total)


part_2()

