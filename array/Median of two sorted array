from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array= nums1+nums2
        merged_array.sort()
        l=len(merged_array)
        if l%2 !=0:
            median = merged_array[l// 2]
        else:
            median = (merged_array[l//2 - 1] + merged_array[l//2]) / 2
        return(median)
