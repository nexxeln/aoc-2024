import re


def fn(line):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    return sum(int(x) * int(y) for x, y in matches)


print(fn(open(0).read()))
