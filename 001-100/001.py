"""
Question:   Two Sum
Difficulty: Easy
Link:       https://leetcode.com/problems/two-sum
Ref:        https://xiaozhuanlan.com/topic/6347850291

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution1(object):
    def twoSum(self, nums, target):
        """
        Brute force - nested loop
        Time complexity: O(n^2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2(object):
    def twoSum(self, nums, target):
        """
        Use hashmap to check whether the target number exists and store its index.
        Time complexity: O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            else:
                lookup[num] = i


if __name__ == '__main__':
    print(Solution2().twoSum([3, 2, 7, 9], 11))
