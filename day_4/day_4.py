
def explore(data):
    max_y = len(data)
    max_x = len(data[0])

    total = 0
    valid_positions = []
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == "@":
                neighbours = 0

                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue

                        ny, nx = y + dy, x + dx

                        if 0 <= ny < max_y and 0 <= nx < max_x:
                            if data[ny][nx] == "@":
                                neighbours += 1

                if neighbours < 4:
                    total += 1
                    valid_positions.append((y, x))

    return total, valid_positions

def part_1():
    with open("input.txt") as f:
        raw_data = f.readlines()
    data = []
    for line in raw_data:
        data.append(list(line.strip()))

    total, valid_positions = explore(data)
    print(total)


def part_2():
    with open("input.txt") as f:
        raw_data = f.readlines()
    data = []
    for line in raw_data:
        data.append(list(line.strip()))

    total = 0
    new_found = -1
    while new_found != 0:
        new_found, valid_positions = explore(data)
        total += new_found
        for pos in valid_positions:
            data[pos[0]][pos[1]] = "x"

    print(total)

part_1()
