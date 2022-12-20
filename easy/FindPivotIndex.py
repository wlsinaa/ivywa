class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        default = -1
        left = 0
        right = 0
        sum_ = sum (nums)
        if len(nums) == 1:
            return 0
        for key in range(len(nums)):
            if key == 0 :
                left = 0
                right = sum_ - nums[key]
                if left == right:
                    return key
                left += nums[key]

            elif key == len(nums) - 1:
                left = sum_ - nums[key]
                right = 0
                if left == right:
                    return key

            else:
                right = sum_ - left - nums[key]
                if left == right:
                    return key
                left += nums[key]
        return default