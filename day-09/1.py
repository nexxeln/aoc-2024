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


def compact_files(blocks):
    right = len(blocks) - 1
    left = 0

    while right >= 0 and blocks[right] is None:
        right -= 1
    while left < right and blocks[left] is not None:
        left += 1

    while right >= 0 and left < right:
        blocks[left], blocks[right] = blocks[right], None
        right -= 1
        left += 1
        while right >= 0 and blocks[right] is None:
            right -= 1
        while left < right and blocks[left] is not None:
            left += 1

    return blocks


def calculate_checksum(blocks):
    return sum(i * b for i, b in enumerate(blocks) if b is not None)


with open(0) as f:
    nums = [int(c) for c in f.read().strip()]
    print(calculate_checksum(compact_files(create_blocks(nums))))
