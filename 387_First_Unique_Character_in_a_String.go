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

// func firstUniqChar(s string) int {
// 	asciiArray := make([]int, 26)
// 	for i := 0; i < len(s); i++ {
// 		fmt.Println(s[i], 'a', int(s[i]-'a'))
// 		asciiArray[int(s[i])-'a']++
// 	}
// 	fmt.Println(asciiArray)
// 	for i := 0; i < len(s); i++ {
// 		if asciiArray[int(s[i]-'a')] == 1 {
// 			return i
// 		}
// 	}
// 	return -1
// }

// func firstUniqChar(s string) int {
// 	asciiArray := make([]int, 26)
// 	for _, v := range s {
// 		asciiArray[int(v-'a')]++
// 	}
// 	for i, v := range s {
// 		if asciiArray[int(v-'a')] == 1 {
// 			return i
// 		}
// 	}
// 	return -1
// }

func firstUniqChar(s string) int {
	asciiArray := [26]int{}
	for _, ch := range s {
		asciiArray[int(ch)-97]++
	}
	for i, ch := range s {
		if asciiArray[int(ch)-97] == 1 {
			return i
		}
	}
	return -1
}

/* python3 solution
   def firstUniqChar(s: str) -> int:
       asciiArray = [0]*26
       for i in range(len(s)):
           asciiArray[ord(s[i])-97] +=1
       for i in range(len(s)):
           if asciiArray[ord(s[i])-97] == 1:
               return i
       return -1
*/

func main() {
	s := "leetcode"
	fmt.Println(s, firstUniqChar(s))

	s = "loveleetcode"
	fmt.Println(s, firstUniqChar(s))

	s = "aabb"
	fmt.Println(s, firstUniqChar(s))
}
