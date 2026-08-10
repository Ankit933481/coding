class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        s=[]
        n=len(nums)
        for i in range(n-1):
            for m in range(nums[i] + 1, nums[i + 1]):
                s.append(m)

        return s
            

