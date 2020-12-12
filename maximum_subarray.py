"""

Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2, 1, −3, 4, −1, 2, 1, −5, 4],
the contiguous subarray [4, −1, 2, 1] has the largest sum = 6.
"""


def max_subarray_quadratic(list_):
    if not list_:
        return list_, 0
    stop = len(list_)
    sum_ = list_[0]
    result = [sum_]
    start = 1
    for index_start, _ in enumerate(list_):
        for index_stop in range(start, stop + 1):
            if sum_ < sum(list_[index_start:index_stop]):
                sum_ = sum(list_[index_start:index_stop])
                result = list_[index_start:index_stop]
        start += 1
    return result, sum_


assert max_subarray_quadratic([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == ([4, -1, 2, 1], 6)
assert max_subarray_quadratic([10, -1, -3, -4, -1, 2, 1, -5, 4]) == ([10], 10)
assert max_subarray_quadratic([1, -1, -3, -4, -1, 2, 1, -5, 9]) == ([9], 9)
assert max_subarray_quadratic([]) == ([], 0)
assert max_subarray_quadratic([11]) == ([11], 11)
assert max_subarray_quadratic([1, 2, 3, 4]) == ([1, 2, 3, 4], 10)
assert max_subarray_quadratic([-1, -2, -3, -4]) == ([-1], -1)
assert max_subarray_quadratic([-1, -2, 3, -3, -4]) == ([3], 3)


def max_subarray_linear(list_):
    if not list_:
        return 0
    result = list_[0]
    sum_ = list_[0]
    stop = len(list_)
    for index in range(1, stop):
        sum_ = max(list_[index], sum_ + list_[index])
        result = max(result, sum_)
    return result


assert max_subarray_linear([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_linear([10, -1, -3, -4, -1, 2, 1, -5, 4]) == 10
assert max_subarray_linear([1, -1, -3, -4, -1, 2, 1, -5, 9]) == 9
assert max_subarray_linear([]) == 0
assert max_subarray_linear([11]) == 11
assert max_subarray_linear([1, 2, 3, 4]) == 10
assert max_subarray_linear([-1, -2, -3, -4]) == -1
assert max_subarray_linear([-1, -2, 3, -3, -4]) == 3
