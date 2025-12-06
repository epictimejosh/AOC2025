


def part_1():
    with open("input.txt") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        line = line.strip()
        data[index] = line.split()

    rows = len(data)
    total = 0

    for index in range(len(data[0])):
        operation = data[rows-1][index]
        values = []
        for row in range(0, rows-1):
            values.append(int(data[row][index]))

        if operation == "+":
            subtotal = sum(values)
        else:
            subtotal = values[0]
            for value in values[1:]:
                subtotal *= value

        total += subtotal

    print(total)


def part_2():
    with open("input.txt") as f:
        raw_lines = []
        for line in f:
            raw_lines.append(line.rstrip("\n"))

    grid = []
    for line in raw_lines:
        row_list = []
        for ch in line:
            row_list.append(ch)
        grid.append(row_list)

    row_count = len(grid)

    col_count = 0
    for row in grid:
        if len(row) > col_count:
            col_count = len(row)

    for row in grid:
        if len(row) < col_count:
            missing = col_count - len(row)
            for index in range(missing):
                row.append(" ")

    separator_columns = []
    for col in range(col_count):
        is_separator = True
        for row in range(row_count):
            if grid[row][col] != " ":
                is_separator = False
                break
        separator_columns.append(is_separator)

    blocks = []
    col = 0
    while col < col_count:
        if separator_columns[col]:
            col += 1
            continue

        block_start = col
        while col < col_count and not separator_columns[col]:
            col += 1

        block_end = col
        blocks.append((block_start, block_end))

    total = 0

    for block_start, block_end in blocks:
        operator = None

        bottom_row = row_count - 1
        for col in range(block_start, block_end):
            char = grid[bottom_row][col]
            if char == "+" or char == "*":
                operator = char
                break

        if operator is None:
            continue

        numbers = []
        for col in range(block_start, block_end):
            digits_in_column = []
            for row in range(row_count - 1):
                char = grid[row][col]
                if char.isdigit():
                    digits_in_column.append(char)

            if len(digits_in_column) > 0:
                number_string = ""
                for digit in digits_in_column:
                    number_string += digit
                numbers.append(int(number_string))

        if operator == "+":
            subtotal = sum(numbers)
        else:
            subtotal = numbers[0]
            for value in numbers[1:]:
                subtotal *= value

        total += subtotal

    print(total)


part_2()
