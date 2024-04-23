class Solution(object):
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        letter_s = set(s)
        letter_t = set(t)
        if letter_s != letter_t:
            return False
        for l in letter_s:
            if s.count(l) != t.count():
                return False
        return True

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        for i in range(1,len(strs)):
            result = []
            result.append(strs[i-1])
            for x in range(i, len(strs)):
                if self.isAnagram(strs[i-1],strs[x]):
                    result.append(strs[i-1])
            