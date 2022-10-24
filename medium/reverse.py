class Solution:
    def reverse(self, x: int) -> int:

        str_x = str(x)
        sign = ""
        end = 0
        if str_x[0] == "-":
            sign += "-"
            end = 1
        for i in range(len(str_x) - 1, end - 1, -1):
            sign += str_x[i]
        out  = int(sign)
        if out < -2147483648 or out > 2147483648:
            return 0
        
        return out