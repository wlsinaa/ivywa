class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        retu = []
        for i in range(1,n+1):
            m3 = i%3
            m5 = i%5
            out = ""
            if m3 == 0:
                out += "Fizz"
            if m5 == 0:
                out += "Buzz"
            if m5 != 0 and m3 != 0:
                out += str(i)
            retu.append(out)
        return retu