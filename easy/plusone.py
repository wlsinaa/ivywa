class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = list(map(str, digits))
        y = ''.join(x)
        int_y = int(y) + 1
        str_yplusone = str(int_y)
        out = []
        for i in str_yplusone:
            out.append(int(i))
        return out