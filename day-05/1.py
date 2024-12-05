def build_graph(rules):
    graph = {}
    for rule in rules:
        before, after = map(int, rule.split("|"))
        if before not in graph:
            graph[before] = set()
        if after not in graph:
            graph[after] = set()
        graph[before].add(after)
    return graph


def is_valid_order(sequence, graph):
    nums = list(map(int, sequence.split(",")))
    for i, a in enumerate(nums):
        for b in nums[i + 1 :]:
            if b in graph and a in graph[b]:
                return False
    return True


with open(0) as f:
    rules, seqs = f.read().split("\n\n")
    graph = build_graph(rules.splitlines())
    total = 0
    for seq in seqs.splitlines():
        nums = list(map(int, seq.split(",")))
        if is_valid_order(seq, graph):
            total += nums[len(nums) // 2]
    print(total)
