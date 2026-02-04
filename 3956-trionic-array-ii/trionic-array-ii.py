class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)

        inc = [float('-inf')] * n
        dec = [float('-inf')] * n
        tri = [float('-inf')] * n

        # increasing needs at least 2 elements
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc[i] = max(nums[i - 1] + nums[i], inc[i - 1] + nums[i])

        # decreasing after increasing
        for i in range(2, n):
            if nums[i - 1] > nums[i]:
                dec[i] = max(
                    inc[i - 1] + nums[i],      # start decreasing
                    dec[i - 1] + nums[i]       # continue decreasing
                )

        # final increasing after valid dec
        for i in range(3, n):
            if nums[i - 1] < nums[i]:
                tri[i] = max(
                    dec[i - 1] + nums[i],      # start final increase
                    tri[i - 1] + nums[i]       # continue final increase
                )

        return max(tri)
