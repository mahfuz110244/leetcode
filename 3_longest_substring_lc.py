# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time complexity: O(n)
# Space Complexity: O(n)
from typing import List


def lengthOfLongestSubstring(s: str) -> int:
    maxSize = l = 0
    window = {}
    for index, char in enumerate(s):
        print("Before")
        print(window, l, maxSize)
        l = window[char] + 1 if char in window and window[char] >= l else l
        window[char] = index
        maxSize = max(maxSize, index - l + 1)
        print("after")
        print(window, l, maxSize)
    return maxSize


if __name__ == "__main__":
    s = 'abcabcd'
    # s = 'abcabcbb'
    # s = 'pwwkew'
    # s = 'bbbbb'
    print(lengthOfLongestSubstring(s))
