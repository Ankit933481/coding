class Node:
    def __init__(self, k: int, prod: int = 1, remain=None):
        self.k = k
        self.prod = prod
        self.remain = remain if remain is not None else [0] * k

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def merge(self, left: Node, right: Node) -> Node:
        res_prod = (left.prod * right.prod) % self.k
        res_remain = list(left.remain)
        for i in range(self.k):
            res_remain[(i * left.prod) % self.k] += right.remain[i]
        return Node(self.k, res_prod, res_remain)

    def build(self, nums: list[int], cur: int, left: int, right: int):
        if left == right:
            rem = [0] * self.k
            rem[nums[left]] = 1
            self.tree[cur] = Node(self.k, nums[left], rem)
            return
        mid = (left + right) // 2
        self.build(nums, 2 * cur + 1, left, mid)
        self.build(nums, 2 * cur + 2, mid + 1, right)
        self.tree[cur] = self.merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

    def update(self, treeIndex: int, lo: int, hi: int, i: int, val: int):
        if lo == hi:
            rem = [0] * self.k
            rem[val] = 1
            self.tree[treeIndex] = Node(self.k, val, rem)
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self.update(2 * treeIndex + 1, lo, mid, i, val)
        else:
            self.update(2 * treeIndex + 2, mid + 1, hi, i, val)
        self.tree[treeIndex] = self.merge(self.tree[2 * treeIndex + 1], self.tree[2 * treeIndex + 2])

    def query(self, treeIndex: int, lo: int, hi: int, i: int, j: int) -> Node:
        if i <= lo and hi <= j:
            return self.tree[treeIndex]
        if j < lo or hi < i:
            return Node(self.k, 1, [0] * self.k)
        mid = (lo + hi) // 2
        left_res = self.query(2 * treeIndex + 1, lo, mid, i, j)
        right_res = self.query(2 * treeIndex + 2, mid + 1, hi, i, j)
        return self.merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        nums = [num % k for num in nums]
        n = len(nums)
        seg = SegmentTree(nums, k)
        ans = []
        for q in queries:
            idx, val, start, x = q[0], q[1] % k, q[2], q[3] % k
            seg.update(0, 0, n - 1, idx, val)
            q_res = seg.query(0, 0, n - 1, start, n - 1)
            ans.append(q_res.remain[x])
        return ans