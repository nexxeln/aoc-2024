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


def topological_sort(nums, graph):
    nums_set = set(nums)
    in_degree = {num: 0 for num in nums}
    for num in nums:
        if num in graph:
            for next_num in graph[num]:
                if next_num in nums_set:
                    in_degree[next_num] += 1

    queue = [n for n in nums if in_degree[n] == 0]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)
        if current in graph:
            for next_num in graph[current]:
                if next_num in nums_set:
                    in_degree[next_num] -= 1
                    if in_degree[next_num] == 0:
                        queue.append(next_num)

    return result


with open(0) as f:
    rules, seqs = f.read().split("\n\n")
    graph = build_graph(rules.splitlines())
    total = 0
    for seq in seqs.splitlines():
        nums = list(map(int, seq.split(",")))
        if not is_valid_order(seq, graph):
            sorted_nums = topological_sort(nums, graph)
            total += sorted_nums[len(sorted_nums) // 2]
    print(total)
