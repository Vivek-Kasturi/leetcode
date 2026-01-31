import numpy as np
class Solution:
    def square(self,a)->int:
        return a*a
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=np.array(nums)
        return np.sort(self.square(a)).tolist()
        