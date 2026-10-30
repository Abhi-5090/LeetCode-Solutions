class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        arr = []
        for i in nums:
            if nums.count(i) == 1:
                arr.append(i)
        return(sum(arr))
        