class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr= prices[0]
        best = 0

        for price in prices:
            best = max(best, price - curr)
            curr = min(curr, price)
        return best 
        