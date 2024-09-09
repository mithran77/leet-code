# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from array import array


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         char_count = array('i', [0] * 128)

#         ans = 0
#         lptr = rptr = 0

#         while rptr < len(s):
#             r = s[rptr]
#             char_count[ord(r)] += 1

#             while char_count[ord(r)] > 1:
#                 l = s[lptr]
#                 char_count[ord(l)] -= 1
#                 lptr += 1

#             ans = max(ans, rptr - lptr + 1)
#             rptr += 1

#         return ans


class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        substr = set()
        res = s = 0

        for f in range(len(str)):
            while str[f] in substr:
                substr.remove(str[s])
                s += 1

            substr.add(str[f])
            res = max(res, f - s + 1)

        return res

if __name__ == '__main__':
    res = Solution()
    # print(res.lengthOfLongestSubstring("abcabcbb"))
    # print(res.lengthOfLongestSubstring("bbbbb"))
    # print(res.lengthOfLongestSubstring("pwwkew"))
    print(res.lengthOfLongestSubstring("dvdf"))
    # print(res.lengthOfLongestSubstring("aab"))
