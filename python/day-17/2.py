import re

lines = [line.strip() for line in open(0)]
program = [int(x) for x in re.findall(r"\d+", lines[-1])]


def get_val(op, regs):
    return op if op <= 3 else regs["ABC"[op - 4]]


def solve():
    a = 0
    target_pos = len(program) - 1
    stack = []

    while target_pos >= 0:
        found_output = False

        if not stack or stack[-1][1] != target_pos:
            stack.append((a, target_pos, 0))
        else:
            a, _, t = stack.pop()
            if t < 7:
                stack.append((a, target_pos, t + 1))
            elif stack:
                a, target_pos, t = stack[-1]
                continue
            else:
                return None

        a, target_pos, t = stack[-1]
        a = (a << 3) | t
        regs = {"A": a, "B": 0, "C": 0}

        for i in range(0, len(program) - 2, 2):
            op, x = program[i : i + 2]

            if op == 0:
                regs["A"] //= 2 ** get_val(x, regs)
            elif op == 1:
                regs["B"] ^= x
            elif op == 2:
                regs["B"] = get_val(x, regs) % 8
            elif op == 3:
                continue
            elif op == 4:
                regs["B"] ^= regs["C"]
            elif op == 5:
                if get_val(x, regs) % 8 == program[target_pos]:
                    found_output = True
                break
            elif op == 6:
                regs["B"] = regs["A"] // 2 ** get_val(x, regs)
            elif op == 7:
                regs["C"] = regs["A"] // 2 ** get_val(x, regs)

        if found_output:
            target_pos -= 1

    return a


print(solve())
