#!/usr/bin/env python
# Created by Justin Park at 2026/07/14 00:15
# leetgo: 1.4.17
# https://leetcode.com/problems/partition-labels/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of string, k = size of alphabet
    # Time Complexity: O(N)
    # Auxiliary Space Complexity: O(k)
    # Output Space Complexity: O(k)
    def partitionLabels(self, s: str) -> list[int]:
        last_char_index: dict[str, int] = {}
        result: list[int] = []
        partition_boundary = 0

        for i, char in enumerate(s):
            if char not in last_char_index:
                result.append(1)
            else:
                while (
                    partition_boundary > 0
                    and partition_boundary > last_char_index[char]
                ):
                    partition_boundary -= result.pop()

                result.append(i + 1 - partition_boundary)

            last_char_index[char] = i
            partition_boundary = i + 1

        return result


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionLabels(s)
    print("\noutput:", serialize(ans, "integer[]"))
