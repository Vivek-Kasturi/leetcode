class Solution(object):
    def minimumCost(self, nums):
        n = len(nums)
        best = float('inf')

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                cost = nums[0] + nums[i] + nums[j]
                best = min(best, cost)

        return best
