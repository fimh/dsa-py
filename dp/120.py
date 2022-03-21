"""
Question:   Triangle
Difficulty: Medium
Link:       https://leetcode.com/problems/triangle/
Ref:        https://leetcode-cn.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Stand DP"""
        rows = len(triangle)
        dp = [[0 for j in range(len(triangle[j]))] for j in range(rows)]
        for i in range(len((triangle[rows - 1]))):
            dp[rows - 1][i] = triangle[rows - 1][i]

        for i in range(rows - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        """Reduce space complexity"""
        rows = len(triangle)
        # dp = [triangle[rows - 1][i] for i in range(len(triangle[rows - 1]))]
        dp = triangle[rows - 1]

        for i in range(rows - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


if __name__ == '__main__':
    test_data = [[2], [3, 4], [6, 5, 7], [4, 2, 8, 3]]
    ret = Solution().minimumTotal2(test_data)
    print(ret)
