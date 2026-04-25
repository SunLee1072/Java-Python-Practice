class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        set1 = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):

            while s[right] in set1:
                set1.remove(s[left])
                left += 1
            
            set1.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen


# Test cases
solution = Solution()
s1 = "abcabcbb"
print(f"Input: s = \"{s1}\"")
print(f"Output: {solution.lengthOfLongestSubstring(s1)}")  # Expected: 3

s2 = "bbbbb"
print(f"\nInput: s = \"{s2}\"")
print(f"Output: {solution.lengthOfLongestSubstring(s2)}")  # Expected: 1

s3 = "pwwkew"
print(f"\nInput: s = \"{s3}\"")
print(f"Output: {solution.lengthOfLongestSubstring(s3)}")  # Expected: 3

        