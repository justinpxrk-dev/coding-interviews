# Created by Justin Park at 2026/06/29 14:13
# leetgo: 1.4.17
# https://leetcode.com/problems/longest-palindromic-substring/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        transformed: str = f"^#{'#'.join(s)}#$"
        n = len(transformed)
        radii: list[int] = [0] * n
        center = 1
        right = 1

        for i in range(1, n - 1):
            if i < right:
                mirror_radius = radii[2 * center - i]
                radii[i] = min(mirror_radius, right - i)

            while transformed[i + radii[i] + 1] == transformed[i - radii[i] - 1]:
                radii[i] += 1

            if i + radii[i] > right:
                center = i
                right = i + radii[i]

        radius, center = max((radius, i) for i, radius in enumerate(radii))
        start = (center - radius) // 2
        return s[start : start + radius]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
