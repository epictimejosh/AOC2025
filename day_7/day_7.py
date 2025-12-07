

def part_1_search_grid(grid, pos, visited):
    new_pos = (pos[0]+1, pos[1])
    if new_pos in visited:
        return 0
    visited.add(new_pos)
    if new_pos[0] == len(grid)-1:
        return 0

    if grid[new_pos[0]][new_pos[1]] == "^":
        left_pos = pos[1] - 1
        right_pos = pos[1] + 1
        if left_pos >= 0 and right_pos < len(grid[0]):
            return 1 + part_1_search_grid(grid, (pos[0], left_pos), visited) + part_1_search_grid(grid, (pos[0], right_pos), visited)
        elif left_pos >= 0:
            return 1 + part_1_search_grid(grid, (pos[0], left_pos), visited)
        else:
            return 1 + part_1_search_grid(grid, (pos[0], right_pos), visited)

    return part_1_search_grid(grid, new_pos, visited)


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()

    for index, line in enumerate(data):
        subarray = []
        for ch in line:
            subarray.append(ch)
        data[index] = subarray

    start_pos = None
    for index, elem in enumerate(data[0]):
        if elem == "S":
            start_pos = (0, index)

    print(part_1_search_grid(data, start_pos, set()))


def part_2_search_grid(row, col, data, memo):
    rows = len(data)
    cols = len(data[0])
    if (row, col) in memo:
        return memo[(row, col)]

    new_row = row + 1

    if new_row >= rows:
        memo[(row, col)] = 1
        return 1

    if data[new_row][col] == "^":
        total = 0
        if col - 1 >= 0:
            total += part_2_search_grid(new_row, col - 1, data, memo)
        if col + 1 < cols:
            total += part_2_search_grid(new_row, col + 1, data, memo)
        memo[(row, col)] = total
        return total

    result = part_2_search_grid(new_row, col, data, memo)
    memo[(row, col)] = result
    return result


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()

    for index, line in enumerate(data):
        subarray = []
        for ch in line:
            subarray.append(ch)
        data[index] = subarray

    start_pos = data[0].index("S")

    print(part_2_search_grid(0, start_pos, data, {}))


part_2()
