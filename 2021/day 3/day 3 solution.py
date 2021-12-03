from typing import Counter

with open('input.txt') as f:
    inp = f.read().splitlines()
    
bits = list(zip(*[list(x) for x in inp]))


def part_one():
    gamma = "".join([Counter(b_n).most_common()[0][0] for b_n in bits])
    epsilon = "".join(
        [sorted(Counter(b_n).keys(), key=lambda x: Counter(b_n)[x])[0] for b_n in bits])

    return int(gamma, base=2) * int(epsilon, base=2)


def part_two():
    oxygen = inp.copy()
    co2 = inp.copy()

    i = 0
    while not len(oxygen) == 1:
        common = ""
        for x in list(zip(*[list(x) for x in oxygen])):
            one_count = x.count("1")
            zero_count = x.count("0")
            common += "1" if one_count >= zero_count else "0"
        oxygen = list(filter(lambda x: x[i] == common[i], oxygen))
        i += 1

    i = 0
    while not len(co2) == 1:
        uncommon = ""
        for x in list(zip(*[list(x) for x in co2])):
            one_count = x.count("1")
            zero_count = x.count("0")
            uncommon += "1" if one_count < zero_count else "0"
        co2 = list(filter(lambda x: x[i] == uncommon[i], co2))
        i += 1
    return int(oxygen[0], base=2) * int(co2[0], base=2)


print(f"Part one = {part_one()}")
print(f"Part two = {part_two()}")
