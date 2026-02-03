class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1. strictly increasing from start
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        p = i
        if p == 0 or p == n - 1:
            return False

        # 2. strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        q = i
        if q == p or q == n - 1:
            return False

        # 3. strictly increasing again
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
