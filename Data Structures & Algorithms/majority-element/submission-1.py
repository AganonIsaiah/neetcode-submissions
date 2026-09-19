class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        half = len(nums) // 2
        prev_count = float('-inf')
        prev_val = float('-inf')

        for k,v in c.items():
            if v > half:
                prev_count = max(v, prev_count)
                prev_val = max(k, prev_val)

        return prev_val