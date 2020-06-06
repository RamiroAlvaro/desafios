"""
https://www.programcreek.com/2015/03/rotate-array-in-java/
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. How many different ways do
you know to solve this problem?
"""


def rotate_array(lts, k):
    return lts[-k:] + lts[:-k]


assert rotate_array(lts=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate_array(lts=[1, 2, 3, 4, 5, 6], k=2) == [5, 6, 1, 2, 3, 4]
assert rotate_array(lts=[0, 1, 2, 3, 4, 5, 6], k=1) == [6, 0, 1, 2, 3, 4, 5]
assert rotate_array(lts=[1, 2, 3, 4, 5, 6, 7], k=0) == [1, 2, 3, 4, 5, 6, 7]
