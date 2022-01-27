""" https://leetcode.com/problems/first-missing-positive/
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
-231 <= nums[i] <= 231 - 1
"""

"""
Time Complexity: O(2n) = O(n)
Space Complexity: O(n) 
"""

def firstUniqChar(s: str) -> int:
	asciiArray = [0]*26
	for i in range(len(s)):
		asciiArray[ord(s[i])-97] +=1
	for i in range(len(s)):
		if asciiArray[ord(s[i])-97] == 1:
			return i
	return -1

if __name__ == "__main__":
	s = "leetcode"
	print(s, firstUniqChar(s))

	s = "loveleetcode"
	print(s, firstUniqChar(s))

	s = "aabb"
	print(s, firstUniqChar(s))
