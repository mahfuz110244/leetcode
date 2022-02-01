"""
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
"""

def isPalindrome1( x: int) -> bool:
    if x < 0: 
        return False
    if len(str(x))==1:
        return True
    palindromStr = ""
    n = x
    while n!=0:
        palindromStr +=str(n % 10)
        # print(palindromStr)
        n = n // 10
    if str(x) == palindromStr:
        return True
    return False

def isPalindrome2( x: int) -> bool:
    return str(x) == str(x)[::-1]

"""
Complexity Analysis

Time Complexity: O(d/2)

d here is the no. of digits in the given input number. Time complexity of this algorithm is O(d/2) because we only have to check half of the digits in the given number x (last to middle) to determine if the given number is a palindrome.


Space Complexity: O(1)

No extra space is used.
"""
def isPalindrome(x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        if x < 0 or (x > 0 and x%10 == 0):   
            return False

        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10

        # If x is equal to reversed number then it is a palindrome
        # If x has odd number of digits, dicard the middle digit before comparing with x
        # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
        # So, reversedNum/10 = 23, which is equal to x
        return True if (x == reversedNum or x == reversedNum // 10) else False


if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))
    print(isPalindrome(0))
    print(isPalindrome(111))
