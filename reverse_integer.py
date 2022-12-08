class Solution:
    def reverse(self, x: int) -> int:
        revInt = ''
        if(x < 0):
            revInt += '-'
            x *= -1
        x = str(x)
        
        for digit in range(len(x) - 1, -1, -1):
            revInt += str(x[digit])

        revInt = int(revInt)
        
        if(revInt < -2 ** 31 or revInt > 2 ** 31 - 1):
            return 0;
        else:
            return revInt;