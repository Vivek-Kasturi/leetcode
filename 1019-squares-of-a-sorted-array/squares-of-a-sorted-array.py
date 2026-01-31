import numpy as np
from typing import List
class Solution:
    def square(self,a :np.ndarray)->ndarray:
        return a*a
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=np.array(nums)
        return np.sort(self.square(a)).tolist()
        