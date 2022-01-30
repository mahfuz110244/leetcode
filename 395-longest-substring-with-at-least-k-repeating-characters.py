"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""

"""
Time Complexity: O(2n) = O(n)
Space Complexity: O(n) 
"""

from collections import Counter

def longestSubstring(s: str, k: int) -> int:
        
        if len(s)==0:
            return 0
        
        cnt = Counter(s)
        # print("-----------------------------------------", cnt)
        
        for i in cnt:
            # print(i)
            if cnt[i] < k:
                # print(s.split(i))
                return max(longestSubstring(p,k) for p in s.split(i))
                
        return len(s)

if __name__ == "__main__":
    s = "aaabb"
    s = "ababbcddddddddddd"
    k = 2
    print(longestSubstring("aaabb",3))
    print(longestSubstring("ababbc",2))
    print(longestSubstring("ababbcddddddddddd",2))
    print(longestSubstring("ababbcd",3))