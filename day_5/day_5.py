

def part_1():
    with open("input.txt") as f:
        data = f.readlines()

    fresh = []
    start_index = 0
    for index, line in enumerate(data):
        if line == "\n":
            start_index = index
            break
        bot, top = line.strip().split("-")
        fresh.append((int(bot), int(top)))

    total = 0
    for line in data[start_index+1:]:
        line = line.strip()
        val = int(line)
        for bot, top in fresh:
            if bot <= val <= top:
                total += 1
                break

    print(total)


def part_2():
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f]

    ranges = []
    for line in lines:
        if line.strip() == "":
            break
        bot, top = line.split("-")
        bot, top = int(bot), int(top)
        if bot > top:
            bot, top = top, bot
        ranges.append((bot, top))


    ranges.sort(key=lambda t: t[0])

    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            if end > cur_end:
                cur_end = end
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))


    total = 0
    for bot, top in merged:
        total += top - bot + 1

    print(total)


part_2()



