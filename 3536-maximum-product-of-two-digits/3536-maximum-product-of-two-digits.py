class Solution:
    def maxProduct(self, n: int) -> int:
        s=list(map(int,str(n)))
        s.sort()
        a=(s[len(s)-1])*(s[len(s)-2])
        return a      