#author:ChaozhuangZHANG
#complexity:o(nlogn)
#language:python
#description of the question:
'''
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1

        while left<right:
            mid = (left+right)/2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            elif nums[mid]<nums[mid-1]:
                right = mid-1
            else:
                return mid
        return left

a= Solution()
b=a.findPeakElement([1,2,3,4,2])
print b
