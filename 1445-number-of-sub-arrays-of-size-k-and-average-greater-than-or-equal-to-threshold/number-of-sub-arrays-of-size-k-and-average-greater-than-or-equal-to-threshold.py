class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target=k*threshold
        window_sum=sum(arr[:k])
        count=1 if window_sum>=target else 0
        for i in range(k,len(arr)):
            window_sum+=arr[i]-arr[i-k]
            if window_sum>=target:
                count+=1
        return count