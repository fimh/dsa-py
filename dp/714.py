"""
Question:   Best Time to Buy and Sell Stock with Transaction Fee
Difficulty: Medium
Link:       https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Ref:        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[len(prices) - 1][0]


if __name__ == '__main__':
    test_prices = [1, 3, 2, 8, 4, 9]
    test_fee = 2
    ret = Solution().maxProfit(test_prices, test_fee)
    print(ret)
