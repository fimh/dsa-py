"""
Question:   Best Time to Buy and Sell Stock III
Difficulty: Hard
Link:       https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Ref:        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP approach

        state: dp[ii][kk][j]
        i: ith day, range - [0, n-1]
        k: transaction times, range - [0, 2]
        j: hold shares, range - [0, 1]

        Note that, kk + 1 when buying one share
        """
        if len(prices) <= 1:
            return 0

        times = 2  # Two transactions at most
        dp = [[[0 for _ in range(2)] for _ in range(times + 1)] for _ in range(len(prices))]
        dp[0][1][1], dp[0][2][1] = -prices[0], -prices[0]

        res = dp[0][0][0]
        for ii in range(1, len(prices)):
            for kk in range(1, times + 1):
                dp[ii][kk][0] = max(dp[ii - 1][kk][0], dp[ii - 1][kk][1] + prices[ii])  # Sell one share
                dp[ii][kk][1] = max(dp[ii - 1][kk][1], dp[ii - 1][kk - 1][0] - prices[ii])  # Buy one share

                if dp[ii][kk][0] > res:
                    res = dp[ii][kk][0]

        return res


if __name__ == '__main__':
    test_prices = [3, 3, 5, 0, 0, 3, 1, 4]
    ret = Solution().maxProfit(test_prices)
    print(ret)
