# https://leetcode.com/problems/longest-palindromic-substring/
# Time complexity: O(n)
# Space Complexity: O(n)
class Solution:
    # def longestPalindrome(s: str) -> str:
    #     """
    #     My Solution
    #     :return:
    #     """
    #
    #     def checkPalindrome(s: str) -> bool:
    #         length_palindrome_s = len(palindrome_s)
    #         for i in range(length_palindrome_s//2+1):
    #             if s[i] != s[length_palindrome_s-i-1]:
    #                 return False
    #         return True
    #
    #     length_s = len(s)
    #     for i in range(length_s):
    #         for j in range(i+1):
    #             palindrome_s = s[j:j+length_s-i]
    #             # print(palindrome_s)
    #             if checkPalindrome(palindrome_s):
    #                 return palindrome_s
    #     return

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # In this function l and r are the middle indecees, as palindrome is created from the middle, we expand from inner (middle) to outer

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]  # l+1 because we take the previous sliceas when we exit the while loop it will no longer be palindromic

        res = ""
        for i in range(len(s)):
            odd = helper(i, i)  # odd case, like "aba"
            even = helper(i, i + 1)  # even case, like "abba"
            res = max(odd, res, even,
                      key=lambda x: len(x))  # compare between odd,even and res according to the max length
            print(i, odd, even, res)

        return res


# if __name__ == "__main__":
s = 'babad'
s = 'madam'
# s = 'cbbd'
# s = 'a'
# s = 'ac'
s = "dtgrtoxuybwyfskikukcqlvprfipgaygawcqnfhpxoifwgpnzjfdnhpgmsoqzlpsaxmeswlhzdxoxobxysgmpkhcylvqlzenzhzhnakctrliyyngrquiuvhpcrnccapuuwrrdufwwungaevzkvwbkcietiqsxpvaaowrteqgkvovcoqumgrlsxvouaqzwaylehybqchsgpzbkfugujrostopwhtgrnrggocprnxwsecmvofawkkpjvcchtxixjtrnngrzqpiwywmnbdnjwqpmnifdiwzpmabosrmzhgdwgcgidmubywsnshcgcrawjvfiuxzyzxsbpfhzpfkjqcpfyynlpshzqectcnltfimkukopjzzmlfkwlgbzftsddnxrjootpdhjehaafudkkffmcnimnfzzjjlggzvqozcumjyazchjkspdlmifvsciqzgcbehqvrwjkusapzzxyiwxlcwpzvdsyqcfnguoidiiekwcjdvbxjvgwgcjcmjwbizhhcgirebhsplioytrgjqwrpwdciaeizxssedsylptffwhnedriqozvfcnsmxmdxdtflwjvrvmyausnzlrgcchmyrgvazjqmvttabnhffoe"
sl = Solution()
print(sl.longestPalindrome(s))
