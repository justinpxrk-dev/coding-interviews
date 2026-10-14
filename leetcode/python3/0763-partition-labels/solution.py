#!/usr/bin/env python
# Created by Justin Park at 2026/07/14 00:15
# leetgo: 1.4.17
# https://leetcode.com/problems/partition-labels/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of string, k = number of letters in alphabet
    # Time Complexity: O(N)
    # Auxiliary Space Complexity: O(k)
    # Output Space Complexity: O(min(N, k))
    def partitionLabels(self, s: str) -> list[int]:
        last_char_index: dict[str, int] = {}
        partitions: list[int] = []

        for i, ch in enumerate(s):
            last_char_index[ch] = i

        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, last_char_index[ch])

            if i == end:
                partitions.append(end + 1 - start)
                start = end + 1

        return partitions


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionLabels(s)
    print("\noutput:", serialize(ans, "integer[]"))
