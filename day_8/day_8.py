import math

def euclidean_distance(point1, point2):
    total = 0
    for x in range(len(point1)):
        total += (point1[x] - point2[x])**2
    return math.sqrt(total)


def part_1():
    with open("input.txt") as f:
        data = f.readlines()

    points = []
    for line in data:
        line = line.strip()
        points.append(tuple(map(int, line.split(","))))

    n = len(points)

    all_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            all_edges.append([dist, i, j])

    all_edges.sort(key=lambda x: x[0])

    circuits = []

    def find_circuit(index):
        for c_idx, circuit in enumerate(circuits):
            if index in circuit:
                return c_idx
        return -1

    for edge_i in range(1000):
        i, a, b = all_edges[edge_i]

        c1 = find_circuit(a)
        c2 = find_circuit(b)

        if c1 == -1 and c2 == -1:
            circuits.append([a, b])

        elif c1 != -1 and c2 == -1:
            circuits[c1].append(b)

        elif c1 == -1 and c2 != -1:
            circuits[c2].append(a)

        elif c1 != c2:
            circuits[c1].extend(circuits[c2])
            del circuits[c2]

    used = set()
    for circuit in circuits:
        used.update(circuit)

    for i in range(n):
        if i not in used:
            circuits.append([i])

    sizes = []
    for circuit in circuits:
        sizes.append(len(circuit))

    sizes.sort(reverse=True)

    total = sizes[0] * sizes[1] * sizes[2]
    print(total)

def part_2():
    with open("input.txt") as f:
        data = f.readlines()

    points = []
    for line in data:
        line = line.strip()
        points.append(tuple(map(int, line.split(","))))

    n = len(points)

    all_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            all_edges.append([dist, i, j])

    all_edges.sort(key=lambda x: x[0])

    circuits = []

    def find_circuit(index):
        for c_idx, circuit in enumerate(circuits):
            if index in circuit:
                return c_idx
        return -1

    last_merge = None

    for dist, a, b in all_edges:

        c1 = find_circuit(a)
        c2 = find_circuit(b)

        if c1 == -1 and c2 == -1:
            circuits.append([a, b])
            last_merge = (a, b)

        elif c1 != -1 and c2 == -1:
            circuits[c1].append(b)
            last_merge = (a, b)

        elif c1 == -1 and c2 != -1:
            circuits[c2].append(a)
            last_merge = (a, b)

        elif c1 != c2:
            circuits[c1].extend(circuits[c2])
            del circuits[c2]
            last_merge = (a, b)


        if len(circuits) == 1 and len(circuits[0]) == n:
            break

    a, b = last_merge
    xa = points[a][0]
    xb = points[b][0]

    print(xa * xb)


part_2()
