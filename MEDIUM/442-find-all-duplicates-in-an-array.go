/*
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
*/

package main

import (
	"fmt"
)

/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
func findDuplicates1(nums []int) []int {
	numsDict := make(map[int]int)
	result := []int{}
	for i, num := range nums {
		fmt.Println(i, num)
		if _, found := numsDict[num]; found {
			result = append(result, num)
		} else {
			numsDict[num] = i
		}
	}
	return result

}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func findDuplicates(nums []int) []int {
	/*
		Time Complexity: O(n)
		Space Complexity: O(1)
	*/
	result := []int{}
	for _, num := range nums {
		if nums[Abs(num)-1] > 0 {
			nums[Abs(num)-1] *= -1
		} else {
			result = append(result, Abs(num))
		}
	}
	return result
}

func main() {
	fmt.Println(findDuplicates([]int{4, 3, 2, 7, 8, 2, 3, 1}))
	fmt.Println(findDuplicates([]int{1, 1, 2}))
	fmt.Println(findDuplicates([]int{1}))
}
