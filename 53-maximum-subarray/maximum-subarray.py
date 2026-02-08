class Solution:
    def maxSubArray(self, nums):
        # mean-based reinterpretation:
        # maximize prefix[j] - min(prefix[i])
        prefix = 0
        min_prefix = 0
        best = float("-inf")

        for x in nums:
            prefix += x
            best = max(best, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return best
