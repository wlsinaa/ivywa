class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = {}
        index = 0
        for i in nums:
            x[i] = index
            index += 1
        index_y =0
        for y in nums:
            t = target - y
            if t in x.keys():
                if x[t] == index_y:
                    index_y += 1
                    continue
                if x[t] > index_y:
                    return [index_y,x[t]]
                else:
                    return [x[t],index_y]
            index_y += 1
        