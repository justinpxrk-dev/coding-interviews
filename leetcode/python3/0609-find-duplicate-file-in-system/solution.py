# Created by Justin Park at 2026/06/05 08:12
# leetgo: 1.4.17
# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_to_paths: dict[str, list[str]] = defaultdict(list)

        for path in paths:
            path_split = path.split()
            directory = path_split[0]
            for i in range(1, len(path_split)):
                file_name, content = path_split[i].rstrip(")").split("(")
                content_to_paths[content].append(f"{directory}/{file_name}")

        group_duplicate_paths: list[list[str]] = []
        for _, _paths in content_to_paths.items():
            if len(_paths) >= 2:
                group_duplicate_paths.append([])
                for _path in _paths:
                    group_duplicate_paths[-1].append(_path)

        return group_duplicate_paths


# @lc code=end

if __name__ == "__main__":
    paths: list[str] = deserialize("List[str]", read_line())
    ans = Solution().findDuplicate(paths)
    print("\noutput:", serialize(ans, "string[][]"))
