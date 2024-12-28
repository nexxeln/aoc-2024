from collections import deque


def get_positions(keypad):
    return {
        keypad[r][c]: (r, c)
        for r in range(len(keypad))
        for c in range(len(keypad[r]))
        if keypad[r][c] is not None
    }


def get_valid_moves(pos, keypad):
    r, c = pos
    moves = [
        ((r - 1, c), "^"),
        ((r + 1, c), "v"),
        ((r, c - 1), "<"),
        ((r, c + 1), ">"),
    ]
    return [
        (pos, move)
        for pos, move in moves
        if 0 <= pos[0] < len(keypad)
        and 0 <= pos[1] < len(keypad[0])
        and keypad[pos[0]][pos[1]] is not None
    ]


def find_paths(start, target, keypad):
    def bfs():
        possibilities = []
        q = deque([(start, "")])
        optimal = float("inf")

        while q:
            pos, moves = q.popleft()

            for (nr, nc), nm in get_valid_moves(pos, keypad):
                if keypad[nr][nc] == target:
                    if optimal < len(moves) + 1:
                        return possibilities
                    optimal = len(moves) + 1
                    possibilities.append(moves + nm + "A")
                else:
                    q.append(((nr, nc), moves + nm))

        return possibilities

    return ["A"] if keypad[start[0]][start[1]] == target else bfs()


def compute_seqs(keypad):
    positions = get_positions(keypad)
    result = {}
    for x in positions.keys():
        for y in positions.keys():
            result[(x, y)] = find_paths(positions[x], y, keypad)
    return result


def cartesian_product(lists):
    if not lists:
        return [[]]
    result = []
    for item in lists[0]:
        for rest in cartesian_product(lists[1:]):
            result.append([item] + rest)
    return result


def solve(string, seqs):
    seq_lists = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in cartesian_product(seq_lists)]


def create_dir_lengths(dir_seqs):
    return {key: len(value[0]) for key, value in dir_seqs.items()}


length_cache = {}


def compute_length(seq, dir_seqs, dir_lengths, depth=25):
    cache_key = seq + str(depth)
    if cache_key in length_cache:
        return length_cache[cache_key]

    if depth == 1:
        result = sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    else:
        result = sum(
            min(
                compute_length(subseq, dir_seqs, dir_lengths, depth - 1)
                for subseq in dir_seqs[(x, y)]
            )
            for x, y in zip("A" + seq, seq)
        )

    length_cache[cache_key] = result
    return result


def process_line(line, num_seqs, dir_seqs, dir_lengths):
    inputs = solve(line, num_seqs)
    length = min(compute_length(seq, dir_seqs, dir_lengths) for seq in inputs)
    return length * int(line[:-1])


num_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
dir_keypad = [[None, "^", "A"], ["<", "v", ">"]]

num_seqs = compute_seqs(num_keypad)
dir_seqs = compute_seqs(dir_keypad)
dir_lengths = create_dir_lengths(dir_seqs)

with open(0) as f:
    total = sum(
        process_line(line.strip(), num_seqs, dir_seqs, dir_lengths) for line in f
    )

print(total)
