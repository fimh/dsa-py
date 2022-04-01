"""
Question:   Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
Link:       https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Ref:        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP approach

        Three states:
        1. dp[i][0] - buy one share at ith day
        2. dp[i][1] - sell one share at ith day
        3. dp[i][2] - cooldown at ith day
        """
        if len(prices) <= 1:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = dp[i - 1][1]

        return dp[-1][1]


if __name__ == '__main__':
    test_prices = [1, 2, 3, 0, 2]
    ret = Solution().maxProfit(test_prices)
    print(ret)
