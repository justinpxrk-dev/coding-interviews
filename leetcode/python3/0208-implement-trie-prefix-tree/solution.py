#!/usr/bin/env python
# Created by Justin Park at 2026/10/14 03:33
# leetgo: 1.5.1
# https://leetcode.com/problems/implement-trie-prefix-tree/


from leetgo_py import deserialize, join_array, read_line, serialize, split_array

# @lc code=begin


class Trie:
    class TrieNode:
        links: dict[str, "Trie.TrieNode"]
        end_of_word: bool

        def __init__(self):
            self.links = {}
            self.end_of_word = False

        def contains_key(self, char: str) -> bool:
            return char in self.links

        def get(self, char: str) -> "Trie.TrieNode":
            return self.links[char]

        def put(self, char: str, trie_node: "Trie.TrieNode") -> None:
            self.links[char] = trie_node

        def is_end_of_word(self) -> bool:
            return self.end_of_word

        def set_end_of_word(self) -> None:
            self.end_of_word = True

    head: TrieNode

    # N = length of longest word, k = number of words
    # Space Complexity: O(kN)
    def __init__(self):
        self.head = self.TrieNode()

    # N = length of word
    # Time Complexity: O(N)
    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if not curr.contains_key(char):
                curr.put(char, self.TrieNode())
            next = curr.get(char)
            assert next is not None
            curr = next

        curr.set_end_of_word()

    # N = length of word
    # Time Complexity: O(N)
    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            if not curr.contains_key(char):
                return False
            next = curr.get(char)
            assert next is not None
            curr = next

        return curr.end_of_word

    # N = length of word
    # Time Complexity: O(N)
    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if not curr.contains_key(char):
                return False
            next = curr.get(char)
            assert next is not None
            curr = next

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# @lc code=end

if __name__ == "__main__":
    ops: list[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Trie()

    for i in range(1, len(ops)):
        word: str
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                word = deserialize("str", method_params[0])
                obj.insert(word)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                word = deserialize("str", method_params[0])
                ans = serialize(obj.search(word))
                output.append(ans)
            case "startsWith":
                method_params = split_array(params[i])
                prefix: str = deserialize("str", method_params[0])
                ans = serialize(obj.startsWith(prefix))
                output.append(ans)

    print("\noutput:", join_array(output))
