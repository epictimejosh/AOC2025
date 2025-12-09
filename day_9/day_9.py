

def part_1():
    with open("input.txt") as f:
        data = f.readlines()

    cords = []
    for d in data:
        cords.append(tuple(map(int, d.strip().split(","))))

    largest_area = 0
    for i, cord_i in enumerate(cords):
        for j, cord_j in enumerate(cords[i:]):
            area = (abs(cord_i[0] - cord_j[0])+ 1) * (abs(cord_i[1] - cord_j[1]) + 1)
            if area > largest_area:
                largest_area = area

    print(largest_area)


def point_on_boundary(x, y, horizontals, verticals):
    for yy, x1, x2 in horizontals:
        if y == yy and x1 <= x <= x2:
            return True
    for xx, y1, y2 in verticals:
        if x == xx and y1 <= y <= y2:
            return True
    return False


def point_in_poly(x, y, horizontals, verticals):
    if point_on_boundary(x, y, horizontals, verticals):
        return True

    crossings = 0
    for xx, y1, y2 in verticals:
        if y1 <= y < y2 and xx > x:
            crossings ^= 1

    return crossings == 1


def rectangle_intersects_boundary(minx, max_x, miny, max_y, horizontals, verticals):
    for yy, x1, x2 in horizontals:
        if miny < yy < max_y:
            if x2 > minx and x1 < max_x:
                return True

    for xx, y1, y2 in verticals:
        if minx < xx < max_x:
            if y2 > miny and y1 < max_y:
                return True

    return False


def part_2():
    with open("input.txt") as f:
        data = f.readlines()

    cords = []
    for d in data:
        cords.append(tuple(map(int, d.strip().split(","))))

    n = len(cords)
    horizontals = []
    verticals = []

    for i in range(n):
        x1, y1 = cords[i]
        x2, y2 = cords[(i + 1) % n]

        if x1 == x2:
            if y1 <= y2:
                ya = y1
                yb = y2
            else:
                ya = y2
                yb = y1

            verticals.append((x1, ya, yb))
        elif y1 == y2:
            if x1 <= x2:
                xa = x1
                xb = x2
            else:
                xa = x2
                xb = x1

            horizontals.append((y1, xa, xb))

    largest = 0

    for i in range(n):
        x1, y1 = cords[i]
        for j in range(i + 1, n):
            x2, y2 = cords[j]

            if x1 <= x2:
                minx = x1
                max_x = x2
            else:
                minx = x2
                max_x = x1

            if y1 <= y2:
                miny = y1
                max_y = y2
            else:
                miny = y2
                max_y = y1

            b = (minx, max_y)
            d = (max_x, miny)

            if not point_in_poly(b[0], b[1], horizontals, verticals):
                continue
            if not point_in_poly(d[0], d[1], horizontals, verticals):
                continue

            if rectangle_intersects_boundary(minx, max_x, miny, max_y, horizontals, verticals):
                continue

            area = (max_x - minx + 1) * (max_y - miny + 1)
            if area > largest:
                largest = area

    print(largest)


part_2()