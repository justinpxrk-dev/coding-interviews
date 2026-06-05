# Created by Justin Park at 2026/06/05 09:56
# leetgo: 1.4.17
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count: dict[str, int] = {}
        left = 0
        longest_substring_length = 0
        for right, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            while char_count[char] > 1:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1

            if right + 1 - left > longest_substring_length:
                longest_substring_length = right + 1 - left

        return longest_substring_length


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
