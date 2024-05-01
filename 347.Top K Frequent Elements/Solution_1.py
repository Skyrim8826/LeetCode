from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqdict = defaultdict(int)
        for num in nums:
            freqdict[num]+=1
        
        return list(dict(sorted(freqdict.items(), key=lambda x: x[1],reverse=True)).keys())[:k]