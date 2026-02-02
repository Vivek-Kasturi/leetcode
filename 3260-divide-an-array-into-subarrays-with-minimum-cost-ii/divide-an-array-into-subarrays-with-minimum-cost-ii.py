from sortedcontainers import SortedList

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)

        # store (value, index)
        kMinimum = SortedList()
        remaining = SortedList()

        total = 0  # sum of (k-1) minimum elements

        i = 1
        # build initial window
        while i - dist < 1:
            kMinimum.add((nums[i], i))
            total += nums[i]

            if len(kMinimum) > k - 1:
                temp = kMinimum[-1]  # largest among kMinimum
                total -= temp[0]
                remaining.add(temp)
                kMinimum.remove(temp)

            i += 1

        result = float("inf")

        # sliding window
        while i < n:
            kMinimum.add((nums[i], i))
            total += nums[i]

            if len(kMinimum) > k - 1:
                temp = kMinimum[-1]
                total -= temp[0]
                remaining.add(temp)
                kMinimum.remove(temp)

            result = min(result, total)

            # remove outgoing element
            remove = (nums[i - dist], i - dist)

            if remove in kMinimum:
                kMinimum.remove(remove)
                total -= remove[0]

                if len(remaining) > 0:
                    temp = remaining[0]  # smallest in remaining
                    kMinimum.add(temp)
                    total += temp[0]
                    remaining.remove(temp)
            else:
                if remove in remaining:
                    remaining.remove(remove)

            i += 1

        return nums[0] + result
