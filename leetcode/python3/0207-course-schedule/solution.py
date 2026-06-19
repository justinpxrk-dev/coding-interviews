# Created by Justin Park at 2026/06/14 22:59
# leetgo: 1.4.17
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque
from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: dict[int, set[int]] = defaultdict(set)
        indegrees: list[int] = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].add(course)
            indegrees[course] += 1

        queue: deque[int] = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        while queue:
            prereq = queue.popleft()
            if prereq in graph:
                for course in graph[prereq]:
                    indegrees[course] -= 1
                    if indegrees[course] == 0:
                        queue.append(course)

        return sum(indegrees) == 0


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFinish(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "boolean"))
