#author:ChaozhuangZHANG
#complexity:o(n)
#language:python
#description of the question
'''Given an array of n positive integers and a positive integer s
find the minimal length of a contiguous subarray of which the sum ≥ s
If there isn't one, return 0 instead
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left,right,tempsum=0,0,0
        res=len(nums)+1
        while right<len(nums):
            tempsum+=nums[right]
            right+=1
            while tempsum>=s:
                res=min(res,right-left)
                tempsum-=nums[left]
                left+=1

        return res if res<=len(nums) else 0


a=Solution()
b = a.minSubArrayLen(8,[2,3,1,4,5,2]);
print b
