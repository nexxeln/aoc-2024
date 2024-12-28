import re

lines = [line.strip() for line in open(0)]
regs = {"A": 0, "B": 0, "C": 0}

for line in lines[:3]:
    reg, val = re.match(r"Register (.): (\d+)", line).groups()
    regs[reg] = int(val)

program = [int(x) for x in re.findall(r"\d+", lines[-1])]


def get_val(op, regs):
    return op if op <= 3 else regs["ABC"[op - 4]]


def solve(program, regs):
    outputs = []
    ip = 0
    ops = {
        0: lambda x: regs.update({"A": regs["A"] // 2 ** get_val(x, regs)}),
        1: lambda x: regs.update({"B": regs["B"] ^ x}),
        2: lambda x: regs.update({"B": get_val(x, regs) % 8}),
        4: lambda: regs.update({"B": regs["B"] ^ regs["C"]}),
        5: lambda x: outputs.append(str(get_val(x, regs) % 8)),
        6: lambda x: regs.update({"B": regs["A"] // 2 ** get_val(x, regs)}),
        7: lambda x: regs.update({"C": regs["A"] // 2 ** get_val(x, regs)}),
    }
    while ip < len(program) - 1:
        op, x = program[ip : ip + 2]
        if op == 3 and regs["A"]:
            ip = x
            continue
        if op in ops:
            ops[op](x)
        ip += 2
    return ",".join(outputs)


print(solve(program, regs))
