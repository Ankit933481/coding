class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            val = lazy[node]
            if val != 0:
                mid = (l + r) // 2
                lc = 2 * node
                rc = 2 * node + 1
                
                # Left child
                len_l = mid - l + 1
                tree_sq[lc] = (tree_sq[lc] + 2 * val * tree_sum[lc] + val * val * len_l) % MOD
                tree_sum[lc] = (tree_sum[lc] + val * len_l) % MOD
                lazy[lc] = (lazy[lc] + val) % MOD
                
                # Right child
                len_r = r - mid
                tree_sq[rc] = (tree_sq[rc] + 2 * val * tree_sum[rc] + val * val * len_r) % MOD
                tree_sum[rc] = (tree_sum[rc] + val * len_r) % MOD
                lazy[rc] = (lazy[rc] + val) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
                tree_sum[node] = (tree_sum[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        last = {}
        total_sum = 0
        
        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            last[x] = i
            total_sum = (total_sum + tree_sq[1]) % MOD
            
        return total_sum