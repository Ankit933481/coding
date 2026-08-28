class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        if sum(1 for c in cnt if c % 2 != 0) > 1:
            return ""
        m = n // 2
        left_counts = [c // 2 for c in cnt]
        mid_char = ""
        for i in range(26):
            if cnt[i] % 2 != 0:
                mid_char = chr(ord('a') + i)
                break
        target_left_cnt = [0] * 26
        for ch in target[:m]:
            target_left_cnt[ord(ch) - ord('a')] += 1
        if target_left_cnt == left_counts:
            T_left = target[:m]
            p0 = T_left + mid_char + T_left[::-1]
            if p0 > target:
                return p0
        prefix_cnt = list(target_left_cnt)
        for i in range(m - 1, -1, -1):
            target_char_code = ord(target[i]) - ord('a')
            prefix_cnt[target_char_code] -= 1
            if any(prefix_cnt[c] > left_counts[c] for c in range(26)):
                continue
            rem = [left_counts[c] - prefix_cnt[c] for c in range(26)]
            chosen_code = -1
            for c in range(target_char_code + 1, 26):
                if rem[c] > 0:
                    chosen_code = c
                    break
            if chosen_code != -1:
                rem[chosen_code] -= 1
                tail = "".join(chr(ord('a') + c) * rem[c] for c in range(26))
                L = target[:i] + chr(ord('a') + chosen_code) + tail
                return L + mid_char + L[::-1]
        return ""