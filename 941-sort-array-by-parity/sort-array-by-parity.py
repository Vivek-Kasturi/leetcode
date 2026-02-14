#use indexing and slicing
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens=[x for x in nums if x%2==0]
        odds=[x for x in nums if x%2!=0]
        return evens+odds