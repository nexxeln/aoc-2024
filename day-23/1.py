graph = {}
for line in map(str.strip, open(0)):
    a, b = line.split("-")
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)


count = 0
for node in graph:
    neighbors = graph[node]
    for n1 in neighbors:
        if n1 < node:
            continue
        for n2 in neighbors:
            if n2 < n1:
                continue
            if n2 in graph[n1]:
                if any(x.startswith("t") for x in (node, n1, n2)):
                    count += 1

print(count)
