from collections import defaultdict
import collections
class Solution:
    def uniqueletterstring(self, s: str) -> int:
        cur=res=0
        pos_dict = collections.defaultdict(lambda:[-1,-1])
        for i,ch in enumerate(s):
            cur += (i - pos_dict[ch][0]) - (pos_dict[ch][0] - pos_dict[ch][1])
            pos_dict[ch][1] = pos_dict[ch][0]
            pos_dict[ch][0] = i
            res += cur
        return res
    
s1 = Solution()
s = "ABA"
result = s1.uniqueletterstring(s)
print(result)
    