# [743. Network Delay Time][link] (Medium)

[link]: https://leetcode.com/problems/network-delay-time/

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given
`times`, a list of travel times as directed edges `times[i] = (uᵢ, vᵢ, wᵢ)`, where
`uᵢ` is the source node, `vᵢ` is the target node, and `wᵢ` is the time it takes
for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes
for all the_ `n` _nodes to receive the signal_. If it is impossible for all the
`n` nodes to receive the signal, return `-1`.

**Example 1:**

![link](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```text
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

**Example 2:**

```text
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

**Example 3:**

```text
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

**Constraints:**

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= uᵢ, vᵢ <= n`
- `uᵢ != vᵢ`
- `0 <= wᵢ <= 100`
- All the pairs `(uᵢ, vᵢ)` are **unique**. (i.e., no multiple edges.)
