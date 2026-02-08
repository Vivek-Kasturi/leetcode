class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_left  = A[i] if i >= 0 else float("-inf")
            A_right = A[i+1] if (i+1) < len(A) else float("inf")
            B_left  = B[j] if j >= 0 else float("-inf")
            B_right = B[j+1] if (j+1) < len(B) else float("inf")

            # correct partition
            if A_left <= B_right and B_left <= A_right:
                if total % 2:  # odd
                    return min(A_right, B_right)
                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
