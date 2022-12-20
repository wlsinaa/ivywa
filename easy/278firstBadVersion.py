# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int, ) -> int:
        return self.findfirst(1,n)
    def findfirst(self, left, right):
        med = (left + right)//2
        if (right - left) == 1:
            if isBadVersion(left):
                return left
            else:
                return right
        elif left == right:
            return left
        elif isBadVersion(med):
            return self.findfirst(left,med)
        else:
            return self.findfirst(med , right)