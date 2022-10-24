class Solution:
    def searchInsert(self, nums , target: int) -> int:
        x = list(nums)
        item = self.find(x,target,0, len(nums)-1)
        return item
        
    def find(self, NUM , target: int, left_index, right_index) -> int:
        med = (left_index+right_index)//2
        print(left_index,right_index)
        if NUM[med] == target:
            return med
        elif NUM[left_index] > target:
            return left_index 
        elif NUM[right_index] < target:
            return right_index + 1
        elif NUM[med] > target :
            return self.find(NUM,target,left_index,med - 1)
        elif NUM[med] < target :
            return self.find(NUM,target,med + 1, right_index)