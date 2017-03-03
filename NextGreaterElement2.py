class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        res = [-1]*len(nums)
        stack = []
        temp = range(len(nums))
        temp.extend(temp)
        for i in temp:
            if len(stack)==0:
                stack.append(i)
            else:
                if nums[i]<nums[stack[-1]]:
                    stack.append(i)
                else:
                    while(len(stack)>0 and nums[stack[-1]]<nums[i]):
                        res[stack[-1]]=nums[i]
                        stack.pop()
                    stack.append(i)
        return res
if __name__=="__main__":
    import sys
    a=Solution()
    b = a.nextGreaterElements([1,2,1]);
    print b
