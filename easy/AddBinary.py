class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x,y = int(a,2) , int (b,2)
        return "{0:b}".format(x+y)