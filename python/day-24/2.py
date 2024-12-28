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
    _, gates = parse_input()
    wt = {}
    ot = {}

    types = {"XOR": "sum", "AND": "carry", "OR": "carry_chain"}
    for a, op, b, out in gates:
        if {a, b} == {"x00", "y00"}:
            continue
        a, b = sorted([a, b])

        if a.startswith("x") and b.startswith("y"):
            ot[out] = {"xor_out" if op == "XOR" else "and_out"}
            continue

        t = types[op]
        wt[a] = wt.get(a, set()) | {t}
        wt[b] = wt.get(b, set()) | {t}
        ot[out] = {t}

    def valid(w):
        return (
            w.startswith("z")
            and ot[w] == {"sum"}
            and w not in wt
            or w == "z45"
            and ot[w] == {"carry_chain"}
            or wt.get(w, set()) == {"sum", "carry"}
            and ot[w] == {"xor_out"}
            or wt.get(w, set()) == {"carry_chain"}
            and ot[w] == {"and_out"}
            or wt.get(w, set()) == {"carry_chain"}
            and ot[w] == {"carry"}
            or wt.get(w, set()) == {"sum", "carry"}
            and ot[w] == {"carry_chain"}
        )

    return ",".join(sorted(w for w in ot if not valid(w)))


print(solve())
