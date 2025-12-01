

def part_1():
    with open("input.txt") as f:
        data = f.readlines()

    dial_value = 50
    total = 0

    for line in data:
        distance = int(line[1:])
        if line[0] == "L":
            dial_value -= distance
        else:
            dial_value += distance

        dial_value = dial_value % 100

        if dial_value == 0:
            total += 1

    print(total)


def part_2():
    with open("input.txt") as f:
        data = f.readlines()

    dial_value = 50
    total = 0

    for line in data:
        distance = int(line[1:])
        if line[0] == "L":
            rot = -distance
        else:
            rot = distance

        dial_value = (dial_value + rot) % 100

        if dial_value == 0:
            total += 1

        total += abs(rot) // 100

        if rot > 0:
            leftover = rot % 100
            if dial_value < leftover and dial_value != 0:
                total += 1

        else:
            leftover = abs(rot) % 100
            if dial_value > 100 - leftover:
                total += 1

    print(total)

part_2()
