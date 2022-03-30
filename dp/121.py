"""
Question:   Best Time to Buy and Sell Stock
Difficulty: Easy
Link:       https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Ref:        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_v = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            curr_p = prices[i] - min_v
            if curr_p > profit:  # Update profit
                profit = curr_p
            if curr_p < 0:  # Update min value, same with prices[i] < min_v
                min_v = prices[i]

        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        """DP approach"""
        if len(prices) <= 1:
            return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        res = 0

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]  # No action
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])

            res = max(res, dp[i][0], dp[i][1], dp[i][2])

        return res


if __name__ == '__main__':
    test_prices = [7, 1, 5, 3, 6, 4]
    ret = Solution().maxProfit2(test_prices)
    print(ret)
