class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        x = set(s)
        if x == set(t):
            for i in x:
                if s.count(i) != t.count(i):
                    return False
            return True
        