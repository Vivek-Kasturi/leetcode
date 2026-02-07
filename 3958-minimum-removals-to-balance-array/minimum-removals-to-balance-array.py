class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        max_len = 1

        for right in range(len(nums)):
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)

        return len(nums) - max_len
