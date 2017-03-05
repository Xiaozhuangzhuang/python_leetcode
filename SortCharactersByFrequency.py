from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join([i*j for i,j in Counter(s).most_common()])
