class Solution:
    def isHappy(self, n: int) -> bool:
        num = [int(x)**2 for x in str(n)]
        sumNum = sum(num)
        if sumNum == 1:
            return True
        elif len(str(sumNum)) == 1 and sumNum != 7: # and != 1 not necessary because of previous if statement
            return False
        else:
            num.clear()
            return self.isHappy(sumNum)
