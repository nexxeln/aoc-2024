def create_blocks(nums):
    blocks = [None] * sum(nums)

    pos = 0
    file_id = 0
    for i, length in enumerate(nums):
        if i % 2 == 0:
            blocks[pos : pos + length] = [file_id] * length
            file_id += 1
        pos += length
    return blocks


def find_file_spans(blocks):
    spans = {}
    i = 0
    while i < len(blocks):
        if blocks[i] is not None:
            start = i
            file_id = blocks[i]
            length = 0
            while i < len(blocks) and blocks[i] == file_id:
                length += 1
                i += 1
            spans[file_id] = (start, length)
        else:
            i += 1
    return spans


def find_leftmost_space(blocks, start, needed_length):
    i = 0
    while i < start:
        if blocks[i] is None:
            space_start = i
            length = 0
            while i < start and blocks[i] is None:
                length += 1
                i += 1
            if length >= needed_length:
                return space_start
            i += 1
        else:
            i += 1
    return None


def compact_files(blocks):
    spans = find_file_spans(blocks)

    for file_id in range(len(spans) - 1, -1, -1):
        start, length = spans[file_id]

        new_start = find_leftmost_space(blocks, start, length)

        if new_start is not None:
            file_blocks = [file_id] * length
            blocks[new_start : new_start + length] = file_blocks
            blocks[start : start + length] = [None] * length

    return blocks


def calculate_checksum(blocks):
    return sum(i * b for i, b in enumerate(blocks) if b is not None)


with open(0) as f:
    nums = [int(c) for c in f.read().strip()]
    print(calculate_checksum(compact_files(create_blocks(nums))))
