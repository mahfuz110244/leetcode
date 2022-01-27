# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = sorted(nums1 + nums2)
    len_of_nums = len(nums)
    if len_of_nums % 2 != 0:
        return float("{0:.5f}".format(nums[len_of_nums // 2]))
    else:
        medium_point = len_of_nums // 2
        return float("{0:.5f}".format((nums[medium_point] + nums[medium_point - 1]) / 2))


def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = sorted(nums1 + nums2)
    len_of_nums = len(nums)
    if len_of_nums % 2 != 0:
        return nums[len_of_nums // 2]
    else:
        medium_point = len_of_nums // 2
        return (nums[medium_point] + nums[medium_point - 1]) / 2


if __name__ == "__main__":
    l1 = [1, 3]
    l2 = [2]

    l1, l2 = [1, 4], [2, 8]
    print(findMedianSortedArrays(l1, l2))
    print(find_median_sorted_arrays(l1, l2))
