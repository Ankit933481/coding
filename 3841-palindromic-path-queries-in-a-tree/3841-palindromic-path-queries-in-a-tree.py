import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200_000)


class SegmentTree:

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node, start, mid, l, r) ^ self.query(
            2 * node + 1, mid + 1, end, l, r
        )


class Solution:

    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        size = [0] * n

        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            sz = 1
            max_sz = 0
            for v in adj[u]:
                if v != p:
                    sz += dfs1(v, u, d + 1)
                    if sz > max_sz:
                        max_sz = sz
                        heavy[u] = v
            size[u] = sz
            return sz

        dfs1(0, -1, 0)

        cur_pos = 0

        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)

        seg = SegmentTree(n)
        masks = [1 << (ord(c) - ord("a")) for c in s]
        for i in range(n):
            seg.update(1, 0, n - 1, pos[i], masks[i])

        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= seg.query(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg.query(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                masks[u] = 1 << (ord(c) - ord("a"))
                seg.update(1, 0, n - 1, pos[u], masks[u])
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                if mask == 0 or (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans