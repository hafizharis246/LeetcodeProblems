from typing import List

class Solution:
    # Method to count unique substrings of length 3 in the given string
    def uniqueSubstings(self,s:str)->int:
        count = 0  # Initialize counter for unique substrings
        # Loop through the string to extract substrings of length 3
        for i in range(len(s) - 2):
            substring = s[i:i+3]  # Get the current substring of length 3
            # Check if the substring contains all unique characters
            if len(set(substring)) == 3:
                count+= 1  # Increment the count for unique substrings
        return count  # Return the total count of unique substrings

s1 = Solution()  # Create an instance of the Solution class
s = "xyzzaz"  # Input string
result = s1.uniqueSubstings(s)  # Call the method to get the result
print(result)  # Print the result