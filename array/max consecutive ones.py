from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        curr_sum = 0
        for num in nums:
            if num == 1:
                curr_sum +=1
            else:
                max_consec = max(max_consec, curr_sum)
                curr_sum = 0
        max_consec = max(max_consec, curr_sum)
        return max_consec
        