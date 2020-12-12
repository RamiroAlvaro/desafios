"""

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""


def max_subarray(list_):
    stop = len(list_)
    sum_ = 0
    result = []
    start = 1
    for index_start, _ in enumerate(list_):
        for index_stop in range(start, stop):
            if sum_ < sum(list_[index_start:index_stop]):
                sum_ = sum(list_[index_start:index_stop])
                result = list_[index_start:index_stop]
        start += 1
    return result, sum_


assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == ([4, -1, 2, 1], 6)
