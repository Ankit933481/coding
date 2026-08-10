class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        rank={}
        for i, num in enumerate(s):
            if num not in rank:
                rank[num]=i+1
        a=[]
        for i in arr:
            a.append(rank[i])
        return a