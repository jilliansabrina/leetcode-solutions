class Solution:
    def isPalindrome(self, x: int) -> bool:
        revInt = []
        for y in range(len(str(x)) - 1, -1, -1):
            revInt += str(x)[y]
        
        if str(x) == "".join(revInt):
            return True
        else: 
            return False
