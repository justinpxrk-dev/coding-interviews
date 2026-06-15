# [261. Graph Valid Tree][link] (Medium)

[link]: https://leetcode.com/problems/graph-valid-tree/

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of
`edges` where `edges[i] = [aᵢ, bᵢ]` indicates that there is an undirected edge between nodes `aᵢ`
and `bᵢ` in the graph.

Return `true`if the edges of the given graph make up a valid tree, and `false`otherwise.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg)

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

**Constraints:**

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= aᵢ, bᵢ < n`
- `aᵢ != bᵢ`
- There are no self-loops or repeated edges.
