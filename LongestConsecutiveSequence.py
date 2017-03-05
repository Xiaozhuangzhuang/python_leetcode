#author:ChaozhuangZHANG
#complexity:o(n)
#language:python
#description of the question:
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example,Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        maxlen = 0
        for i in nums:
            dic[i]=1
        for i in nums:
            if dic.get(i):
                temp = i
                while(dic.get(temp-1)):
                    del dic[temp-1]
                    dic[i]+=1
                    temp-=1
                temp = i
                while(dic.get(temp+1)):
                    del dic[temp+1]
                    dic[i]+=1
                    temp+=1
                maxlen = max(maxlen,dic[i])
        return maxlen

a= Solution()
b=a.longestConsecutive([100,4,200,1,3,2])
print b
