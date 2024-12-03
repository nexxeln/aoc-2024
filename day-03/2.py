import re


def fn(line):
    matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", line)

    enabled = True
    total = 0

    for match in matches:
        instruction = match[0]
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            x, y = map(int, match[1:3])
            total += x * y

    return total


print(fn(open(0).read()))
