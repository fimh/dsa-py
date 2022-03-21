"""
Question:   Maximum Product Subarray
Difficulty: Medium
Link:       https://leetcode.com/problems/maximum-product-subarray/
Ref:        https://leetcode-cn.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # For space, only need 2x2 actually
        max_product = [0 for _ in nums]
        minus_max_product = [0 for _ in nums]

        max_product[0], minus_max_product[0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            max_product[i] = max(max_product[i - 1] * nums[i], minus_max_product[i - 1] * nums[i], nums[i])
            minus_max_product[i] = min(minus_max_product[i - 1] * nums[i], max_product[i - 1] * nums[i], nums[i])
            res = max(max_product[i], res)

        return res

    def maxProduct2(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        dp = [[0 for _ in range(2)] for _ in nums]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res


if __name__ == '__main__':
    test_data = [2, 3, -2, 4, 2]
    ret = Solution().maxProduct(test_data)
    print(ret)
