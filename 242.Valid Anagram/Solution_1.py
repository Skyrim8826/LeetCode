class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            s_chars = sorted(s)
            t_chars = sorted(t)
            s_sorted = "".join(s_chars)
            t_sorted = "".join(t_chars)
            if s_sorted == t_sorted:
                return True
        return False


