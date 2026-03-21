from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       a=0
       for i in range(len(nums)):
        if nums[i]!=val:
            nums[a],nums[i] = nums[i],nums[a]
            a+=1
       return a          