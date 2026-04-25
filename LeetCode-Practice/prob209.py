class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        total = 0
        left = 0
        minLen = float("inf")

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if minLen == float("inf") else minLen


# Test cases
solution = Solution()
target1 = 7
nums1 = [2, 3, 1, 2, 4, 3]
print(f"Input: target = {target1}, nums = {nums1}")
print(f"Output: {solution.minSubArrayLen(target1, nums1)}")  # Expected: 2

target2 = 4
nums2 = [1, 4, 4]
print(f"\nInput: target = {target2}, nums = {nums2}")
print(f"Output: {solution.minSubArrayLen(target2, nums2)}")  # Expected: 1

target3 = 11
nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
print(f"\nInput: target = {target3}, nums = {nums3}")
print(f"Output: {solution.minSubArrayLen(target3, nums3)}")  # Expected: 0
