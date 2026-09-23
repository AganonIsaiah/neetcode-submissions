class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_s = "".join(sorted(s))
        t_s = "".join(sorted(t))
        for x,y in zip(s_s,t_s):
            if x != y: return False

        return True