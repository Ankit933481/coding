class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=0
        s=[]
        for i in range(len(nums)):
            if i > 0:
                a+=nums[i-1]
            s.append(a)
        b=0
        r=[]
        for i in range(len(nums)-1,-1,-1):
            if i < len(nums)-1:
                b+=nums[i+1]
            r.append(b)
        r.reverse()
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(s[i]-r[i]))
        return ans
