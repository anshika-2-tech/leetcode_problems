class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        p1 = 0
        p2 = len(string) - 1
        while p1 <= p2:
            if string[p1] != string[p2]:
                return False
            p1 += 1
            p2 -= 1
        # last check
        return True