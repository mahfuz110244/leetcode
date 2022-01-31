 # https://leetcode.com/problems/two-sum/
 # Time complexity: O(n)
 # Space Complexity: O(n)
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    visited = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in visited:
            return [visited[difference], index]
        else:
            visited[number] = index


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    print(twoSum(arr, target))
