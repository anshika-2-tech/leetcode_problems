from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        pos = {}
        for i in range(len(nums)):
            if nums[i] in pos and i - pos[nums[i]] <= k:
                return True
            pos[nums[i]] = i
        return False
        
        