/*
https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?

Complexity Analysis

Time Complexity: O(d/2)

d here is the no. of digits in the given input number. Time complexity of this algorithm is O(d/2) because we only have to check half of the digits in the given number x (last to middle) to determine if the given number is a palindrome.


Space Complexity: O(1)

No extra space is used.
*/
package main

import "fmt"

func isPalindrome(x int) bool {
	// If x is a negative number it is not a palindrome
	// If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	reversedNum := 0
	for x > reversedNum {
		reversedNum = reversedNum*10 + x%10
		x = x / 10
	}

	// If x is equal to reversed number then it is a palindrome
	// If x has odd number of digits, dicard the middle digit before comparing with x
	// Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
	// So, reversedNum/10 = 23, which is equal to x
	return x == reversedNum || x == reversedNum/10
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(0))
	fmt.Println(isPalindrome(23132))
	fmt.Println(isPalindrome(11111))
}
