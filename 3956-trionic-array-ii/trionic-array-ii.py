class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        NEG = float('-inf')

        inc = [NEG] * n   # strictly increasing (len >= 2)
        dec = [NEG] * n   # inc → dec
        tri = [NEG] * n   # inc → dec → inc

        # Phase 1: increasing
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc[i] = max(
                    nums[i - 1] + nums[i],   # start new inc
                    inc[i - 1] + nums[i]     # extend inc
                )

        # Phase 2: decreasing
        for i in range(2, n):
            if nums[i - 1] > nums[i]:
                dec[i] = max(
                    inc[i - 1] + nums[i],    # start dec after inc
                    dec[i - 1] + nums[i]     # extend dec
                )

        # Phase 3: increasing again
        for i in range(3, n):
            if nums[i - 1] < nums[i]:
                tri[i] = max(
                    dec[i - 1] + nums[i],    # start final inc
                    tri[i - 1] + nums[i]     # extend final inc
                )

        return max(tri)
