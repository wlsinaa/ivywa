import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = list(map(lambda x : x**2, nums))
        x.sort()
        return x