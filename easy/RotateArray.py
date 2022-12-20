class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_ = dict(zip([i for i in range(0,len(nums))],nums))
        for count, value in enumerate(nums):
            print(count+k )
            nums[(count+k)%len(nums)] = dict_[count]