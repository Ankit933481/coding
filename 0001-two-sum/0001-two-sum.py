class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        # l=0
        # r=n-1
        # for i in range(n-1):
        #     if
        seen={} 
        
        for i,num in enumerate(nums):
            c=target-num
            if c in seen:
                return [seen[c],i]
            seen[num]=i

        