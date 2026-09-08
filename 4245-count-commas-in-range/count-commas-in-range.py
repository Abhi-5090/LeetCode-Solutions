class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        step = 1000
        while n >= step:
            total_commas += (n - step + 1)
            step *= 1000
        return total_commas
        