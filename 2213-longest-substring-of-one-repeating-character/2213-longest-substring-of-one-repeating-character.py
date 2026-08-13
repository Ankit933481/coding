class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s_list = list(s)
        
        # Segment tree arrays stored flat for optimal performance
        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_lc = [''] * (4 * n)
        tree_rc = [''] * (4 * n)

        def merge(node: int, left_node: int, right_node: int, l_len: int, r_len: int):
            lc_lc = tree_lc[left_node]
            lc_rc = tree_rc[left_node]
            rc_lc = tree_lc[right_node]
            rc_rc = tree_rc[right_node]

            tree_lc[node] = lc_lc
            tree_rc[node] = rc_rc

            # Update Prefix Length
            if tree_pref[left_node] == l_len and lc_rc == rc_lc:
                tree_pref[node] = l_len + tree_pref[right_node]
            else:
                tree_pref[node] = tree_pref[left_node]

            # Update Suffix Length
            if tree_suff[right_node] == r_len and rc_lc == lc_rc:
                tree_suff[node] = r_len + tree_suff[left_node]
            else:
                tree_suff[node] = tree_suff[right_node]

            # Update Max Length
            m = max(tree_max[left_node], tree_max[right_node])
            if lc_rc == rc_lc:
                m = max(m, tree_suff[left_node] + tree_pref[right_node])
            tree_max[node] = m

        def build(node: int, l: int, r: int):
            if l == r:
                tree_max[node] = 1
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_lc[node] = s_list[l]
                tree_rc[node] = s_list[l]
                return
            
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            build(left_node, l, mid)
            build(right_node, mid + 1, r)
            merge(node, left_node, right_node, mid - l + 1, r - mid)

        def update(node: int, l: int, r: int, idx: int, ch: str):
            if l == r:
                tree_lc[node] = ch
                tree_rc[node] = ch
                return
            
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            if idx <= mid:
                update(left_node, l, mid, idx, ch)
            else:
                update(right_node, mid + 1, r, idx, ch)
            
            merge(node, left_node, right_node, mid - l + 1, r - mid)

        # Build initial segment tree
        build(1, 0, n - 1)
        
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != ch:
                s_list[idx] = ch
                update(1, 0, n - 1, idx, ch)
            ans.append(tree_max[1])
            
        return ans