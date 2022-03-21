"""
Question:   Longest Increasing Subsequence
Difficulty: Medium
Link:       https://leetcode.com/problems/longest-increasing-subsequence/
Ref:        https://leetcode-cn.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from bisect import bisect_left
from typing import List


# from bisect import bisect_left


def binary_search(nums: List[int], x: int) -> int:
    i = bisect_left(nums, x)
    if i != len(nums) and nums[i] == x:
        return i
    else:
        return -1


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        dp = [1 for _ in range(len(nums) + 1)]  # Each one is the shortest increasing sequence
        res = 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:  # Ensure increasing
                    dp[i] = max(dp[i], dp[j] + 1)

            res = max(dp[i], res)

        return res

    def lengthOfLIS2(self, nums: List[int]) -> int:
        lis = []  # Maintain an increasing sequence

        for i in range(len(nums)):
            idx = bisect_left(lis, nums[i])  # Find the insert position
            if idx == len(lis):
                lis.append(nums[i])  # Add this
            else:
                lis[idx] = nums[i]  # Replace

        return len(lis)


if __name__ == '__main__':
    test_data = [10, 9, 2, 5, 3, 7, 101, 18]
    ret = Solution().lengthOfLIS2(test_data)
    print(ret)
