"""
Question:   Best Time to Buy and Sell Stock IV
Difficulty: Hard
Link:       https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Ref:        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        DP approach

        state: dp[i][k][j]
        i: ith day, range - [0, n-1]
        k: transaction times, range - [0, k]
        j: hold shares, range - [0, 1]

        Note that, k + 1 when buying one share
        """
        if len(prices) <= 1:
            return 0

        times = k  # Two transactions at most
        dp = [[[0 for _ in range(2)] for _ in range(times + 1)] for _ in range(len(prices))]
        for k in range(times + 1):
            dp[0][k][1] = -prices[0]

        res = dp[0][0][0]
        for ii in range(1, len(prices)):
            for kk in range(1, times + 1):
                dp[ii][kk][0] = max(dp[ii - 1][kk][0], dp[ii - 1][kk][1] + prices[ii])  # Sell one share
                dp[ii][kk][1] = max(dp[ii - 1][kk][1], dp[ii - 1][kk - 1][0] - prices[ii])  # Buy one share

                if dp[ii][kk][0] > res:
                    res = dp[ii][kk][0]

        return res


if __name__ == '__main__':
    test_k = 1
    test_prices = [3, 2, 6, 5, 0, 3]
    ret = Solution().maxProfit(test_k, test_prices)
    print(ret)
