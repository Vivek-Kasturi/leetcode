class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)

        # 1. Compute mean of the entire array
        mean_val = sum(nums) / n

        # 2. Convert nums → deviations from mean
        dev = [x - mean_val for x in nums]

        # 3. Compute the sum of the first window
        window_sum = sum(dev[:k])
        max_window_sum = window_sum

        # 4. Slide the window across deviations
        for i in range(k, n):
            window_sum += dev[i] - dev[i - k]
            max_window_sum = max(max_window_sum, window_sum)

        # 5. Convert deviation-sum back to actual average
        #    (mean cancels out, but we reconstruct the real average)
        return max_window_sum / k + mean_val
