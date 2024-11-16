from typing import List
class Solution:
    def reverseString(self, s:str, k:int)->str:
        # Sliding window Approach
        s = list(s)
        for i in range(0,len(s), 2*k):
            left = i
            right = i+k-1
            while left<=right:
                s[left] , s[right] = s[right] , s[left]
                left += 1
                right -=1
        return ''.join(s)
    
        # Without Sliding Window
        # result = []
        # for i in range(0,len(s), 2*k):
        #     result.append(s[i:i+k][::-1])
        #     result.append(s[i+k:i+(2*k)])
        # return ''.join(result)


s1 = Solution()
s = "abcdefg"
k = 2
result = s1.reverseString(s , k)
print(result)