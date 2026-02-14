class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeroes=[x for x in nums if x!=0]
        zeroes=[0] * (len(nums)-len(non_zeroes))
        #combine slices
        nums[:len(non_zeroes)] = non_zeroes
        nums[len(non_zeroes):]=zeroes
        print(nums)