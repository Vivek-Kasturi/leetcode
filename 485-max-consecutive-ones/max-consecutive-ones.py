class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len, start = 0,0
        for i in range(len(nums)):
            if nums[i]==0:
                #slice from last start to i
                max_len = max(max_len, len(nums[start:i]))
                start = i+1 #next segment start after 0
        #final slice
        return(max(max_len, len(nums[start:len(nums)])))
        