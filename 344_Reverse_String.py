from typing import List
class Solution:
    def reverseString(self,s:str)->str:
        s = list(s)
        left = 0
        right = len(s)-1
        while left<=right:
            s[left] , s[right] = s[right] , s[left]
            left += 1
            right -=1
        return ''.join(s)
    # In Leetcode Don't return this and make s to list because we have to do it in-place 
s1 = Solution()
s = "abcdef"
result = s1.reverseString(s)
print(result)