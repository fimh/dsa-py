"""
Question:   Climbing Stairs
Difficulty: Easy
Link:       https://leetcode.com/problems/climbing-stairs/
Ref:        https://leetcode-cn.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


if __name__ == '__main__':
    target_step = 45
    ret = Solution().climbStairs(target_step)
    print(ret)
