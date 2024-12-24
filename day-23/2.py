graph = {}

for line in map(str.strip, open(0)):
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)


def bron_kerbosch(r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return

    pivot = max((len(p & graph[v]), v) for v in p | x)[1] if p | x else None

    for v in set(p) - (graph[pivot] if pivot else set()):
        bron_kerbosch(r | {v}, p & graph[v], x & graph[v], cliques)
        p.remove(v)
        x.add(v)


cliques = []
nodes = set(graph.keys())
bron_kerbosch(set(), nodes, set(), cliques)

largest_clique = max(cliques, key=len)
print(",".join(sorted(largest_clique)))
