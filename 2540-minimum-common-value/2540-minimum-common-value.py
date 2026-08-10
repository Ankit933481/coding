class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = {}

        for i, num in enumerate(nums1):
            seen[num] = i

        for i in nums2:
            if i in seen:
                return i

        return -1