from collections import defaultdict
from typing import List


class Solution:

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_tree = defaultdict(list)
        for node in range(1, n):
            orig_tree[parent[node]].append(node)

        new_parent = [-1] * n
        last_seen = {}

        def dfs_reparent(u: int) -> None:
            char = s[u]
            if char in last_seen:
                new_parent[u] = last_seen[char]
            else:
                new_parent[u] = parent[u]

            prev_node = last_seen.get(char)
            last_seen[char] = u

            for v in orig_tree[u]:
                dfs_reparent(v)

            if prev_node is not None:
                last_seen[char] = prev_node
            else:
                del last_seen[char]

        dfs_reparent(0)

        final_tree = defaultdict(list)
        for node in range(1, n):
            final_tree[new_parent[node]].append(node)

        ans = [0] * n

        def dfs_size(u: int) -> int:
            size = 1
            for v in final_tree[u]:
                size += dfs_size(v)
            ans[u] = size
            return size

        dfs_size(0)
        return ans