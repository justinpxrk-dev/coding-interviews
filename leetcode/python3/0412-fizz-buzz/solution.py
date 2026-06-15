# Created by Justin Park at 2026/06/13 12:36
# leetgo: 1.4.17
# https://leetcode.com/problems/fizz-buzz/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer: list[str] = []

        for i in range(1, n + 1):
            s = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
            answer.append(s or str(i))

        return answer


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().fizzBuzz(n)
    print("\noutput:", serialize(ans, "string[]"))
