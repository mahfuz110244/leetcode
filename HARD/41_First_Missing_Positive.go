/* https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1*/

package main

import "fmt"

func firstMissingPositive(nums []int) int {
	n := len(nums)
	nums_dict := make(map[int]bool)
	for _, v := range nums {
		if v > 0 {
			nums_dict[v] = true
		}
	}

	for i := 1; i < n+1; i++ {
		if _, found := nums_dict[i]; !found {
			return i
		}
	}
	return n + 1
}

/* python3 solution
def firstMissingPositive(nums: List[int]) -> int:
	n = len(nums)
	nums_dict = {}
	for i in range(n):
		if nums[i]>0:
			nums_dict[nums[i]] = 1
	for i in range(1, n+1):
		if i not in nums_dict:
			return i
	return n+1
*/

func main() {
	nums := []int{1, 2, 0}
	fmt.Println(nums, firstMissingPositive(nums))
	nums = []int{3, 4, -1, 1}
	fmt.Println(nums, firstMissingPositive(nums))
	nums = []int{7, 8, 9, 11, 12}
	fmt.Println(nums, firstMissingPositive(nums))
	nums = []int{1, 2, 3, 4, 5}
	fmt.Println(nums, firstMissingPositive(nums))
}
