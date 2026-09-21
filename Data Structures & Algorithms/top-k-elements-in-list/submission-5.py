class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        n = len(nums)+1
        x = [[] for _ in range(n)]
        res = []

        for key,v in c.items():
            x[v].append(key)

        for i in range(n-1,0,-1):
            for num in x[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res