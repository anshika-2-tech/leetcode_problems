from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=prices[0]
        m=0
        for i in prices:
            if(i<n):
                n=i
            elif((i-n)>m):
                m=i-n
        return m