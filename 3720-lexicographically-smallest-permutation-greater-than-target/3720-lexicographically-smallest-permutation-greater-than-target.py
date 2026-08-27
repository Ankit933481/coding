class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        
        # Count frequency of each character in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
            
        best_i = -1
        best_char_idx = -1
        curr_freq = list(freq)
        
        # Step 1: Find the largest prefix index where we can pick a larger character
        for i in range(n):
            t_idx = ord(target[i]) - 97
            
            # Find the smallest available character strictly greater than target[i]
            for c in range(t_idx + 1, 26):
                if curr_freq[c] > 0:
                    best_i = i
                    best_char_idx = c
                    break
            
            # Consume target[i] to continue building the matching prefix
            if curr_freq[t_idx] > 0:
                curr_freq[t_idx] -= 1
            else:
                break
                
        if best_i == -1:
            return ""
            
        # Step 2: Reconstruct the optimal string
        res = []
        
        # Append target prefix up to best_i and update counts
        for i in range(best_i):
            ch_idx = ord(target[i]) - 97
            freq[ch_idx] -= 1
            res.append(target[i])
            
        # Append bumped character
        freq[best_char_idx] -= 1
        res.append(chr(97 + best_char_idx))
        
        # Append remaining characters in sorted order
        for c in range(26):
            if freq[c] > 0:
                res.append(chr(97 + c) * freq[c])
                
        return "".join(res)