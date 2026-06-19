# Created by Justin Park at 2026/06/15 17:50
# leetgo: 1.4.17
# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict, deque
from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph: dict[int, set[int]] = defaultdict(set)
        indegrees: list[int] = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].add(course)
            indegrees[course] += 1

        queue: deque[int] = deque(
            [course for course, indegree in enumerate(indegrees) if indegree == 0]
        )
        order: list[int] = []
        while queue:
            course = queue.popleft()
            order.append(course)

            if course in graph:
                for neighbor in graph[course]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)

        return order if len(order) == numCourses else []


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findOrder(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "integer[]"))
