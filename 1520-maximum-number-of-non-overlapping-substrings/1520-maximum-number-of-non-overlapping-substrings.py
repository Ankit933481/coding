class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        left = [n] * 26
        right = [-1] * 26
        
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if left[idx] == n:
                left[idx] = i
            right[idx] = i
            
        intervals = []
        for i in range(26):
            if left[i] == n:
                continue
            l, r = left[i], right[i]
            valid = True
            j = l
            while j <= r:
                c_idx = ord(s[j]) - ord('a')
                if left[c_idx] < l:
                    valid = False
                    break
                l = min(l, left[c_idx])
                r = max(r, right[c_idx])
                j += 1
            if valid:
                intervals.append([l, r])
                
     
        intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                res.append(s[l:r+1])
                last_end = r
        return res