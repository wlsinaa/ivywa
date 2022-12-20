class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = dict(zip(nums, [0]*len(nums) ))
        default = False
        for x in nums:
            if x in t.keys():
                t[x] += 1
                if t[x] > 1:
                    default = True
                    break
        return default