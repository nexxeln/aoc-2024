def parse_input():
    wires = {}
    gates = []

    for line in open(0):
        if ":" in line:
            name, val = line.split(":")
            wires[name.strip()] = int(val)
        elif "->" in line:
            in1, op, in2, _, out = line.split()
            gates.append((in1, op, in2, out))

    return wires, gates


def solve():
    values, gates = parse_input()
    ops = {"AND": "&", "OR": "|", "XOR": "^"}

    while gates:
        remaining = gates[:]
        gates.clear()

        for a, op, b, out in remaining:
            if a in values and b in values:
                values[out] = eval(f"{values[a]} {ops[op]} {values[b]}")
            else:
                gates.append((a, op, b, out))

    bits = []
    i = 0
    while f"z{i:02d}" in values:
        bits.append(str(values[f"z{i:02d}"]))
        i += 1

    return int("".join(bits[::-1]), 2) if bits else 0


print(solve())
