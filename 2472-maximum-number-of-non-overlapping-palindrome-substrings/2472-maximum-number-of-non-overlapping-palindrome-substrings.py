class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1

        for i in range(k - 1, n):
            # Check for a palindrome of length k ending at index i
            if i - k + 1 > last_end and s[i - k + 1 : i + 1] == s[
                i - k + 1 : i + 1
            ][::-1]:
                ans += 1
                last_end = i
            # Check for a palindrome of length k + 1 ending at index i
            elif (
                i - k >= 0
                and i - k > last_end
                and s[i - k : i + 1] == s[i - k : i + 1][::-1]
            ):
                ans += 1
                last_end = i

        return ans