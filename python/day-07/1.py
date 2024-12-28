def product(items, repeat):
    results = [[]]
    for _ in range(repeat):
        results = [r + [item] for r in results for item in items]
    return results


def can_solve_equation(test_value, nums):
    operators = [lambda x, y: x + y, lambda x, y: x * y]
    for ops in product(operators, len(nums) - 1):
        result = nums[0]
        for i in range(len(ops)):
            result = ops[i](result, nums[i + 1])
        if result == test_value:
            return True
    return False


with open(0) as f:
    total = 0
    for line in f:
        test_value, nums = line.split(": ")
        test_value = int(test_value)
        nums = [int(x) for x in nums.split()]

        if can_solve_equation(test_value, nums):
            total += test_value

    print(total)
