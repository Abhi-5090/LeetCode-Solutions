class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x = max(nums)
        res = 0
        for i in nums:
            if i != x:
                res += x - i
        return res