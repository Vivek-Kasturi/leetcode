class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<2:
            return 0
        mean_prices=sum(prices)/n #mean
        deviations=[p-mean_prices for p in prices] #deviation from mean
        min_dev=float('inf') #minimum deviation
        max_profit=0
        for dev in deviations:
            if dev<min_dev:
                min_dev=dev
            else:
                max_profit=max(max_profit,dev-min_dev)
        return int(max_profit)

