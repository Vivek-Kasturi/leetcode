import math

class Solution:
    def productExceptSelf(self, nums):
        # 1. Handle zeros
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 1:
            total = 1
            for x in nums:
                if x != 0:
                    total *= x
            return [0 if x != 0 else total for x in nums]

        # 2. No zeros: log-sum trick with sign tracking
        logs = []
        total_log = 0.0
        total_sign = 1

        for x in nums:
            if x < 0:
                total_sign *= -1
            ax = abs(x)
            lx = math.log(ax)
            logs.append(lx)
            total_log += lx

        result = []
        for x, lx in zip(nums, logs):
            # magnitude of product except self
            mag = math.exp(total_log - lx)

            # sign of product except self
            sign_i = total_sign
            if x < 0:
                sign_i *= -1

            val = sign_i * mag
            # critical fix: round before int to avoid 23.9999 → 23
            result.append(int(round(val)))

        return result
