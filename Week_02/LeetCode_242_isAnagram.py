class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
       
        if len(s_counter) != len(t_counter):
            return False
        for c in s_counter:
            if c in t_counter:
                s_counter[c] = t_counter[c]- s_counter[c]
                
            else:
                return False
        for num in s_counter.values():
            if num != 0:
                return False
        return True