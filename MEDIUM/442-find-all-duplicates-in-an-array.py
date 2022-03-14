"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
Accepted
381,581
Submissions
528,692
"""

from typing import List


"""
Time Complexity: O(n)
Space Complexity: O(n) 
"""
def findDuplicates2(nums: List[int]) -> List[int]:
    print(nums)
    hashmap = {}
    res = []
    for key in range(len(nums)):
        if nums[key] in hashmap:
            res.append(nums[key])
        else:
            hashmap[nums[key]] = True
    return res



"""
Time Complexity: O(n)
Space Complexity: O(n) 
"""
def findDuplicates1(nums: List[int]) -> List[int]:
    print(nums)
    nums_set, res = set(), []
    for num in nums:
        if num in nums_set:
            res.append(num)
        else:
            nums_set.add(num)
    return res


"""
Time Complexity: O(n)
Space Complexity: O(1) 
"""
def findDuplicates(nums: List[int]) -> List[int]:
    print(nums)
    res = []
    for num in nums:
        if nums[abs(num)-1] > 0:
            nums[abs(num)-1] *= -1
        else:
            res.append(abs(num))
    print(nums)
    return res

if __name__ == '__main__':
    print(findDuplicates1([4,3,2,7,8,2,3,1]))
    print(findDuplicates([4,3,2,7,8,2,3,1]))
    # print(findDuplicates([1,1,2]))
    # print(findDuplicates([1]))