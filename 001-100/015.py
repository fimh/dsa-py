"""
Link:   https://leetcode.com/problems/3sum/
Ref:    https://xiaozhuanlan.com/topic/9504236871

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution1(object):
    def threeSum(self, nums):
        """
        Three tired nested loops.
        Time complexity: O(n^3)
        FIXME Space complexity: O(n) or O(1)?
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0 and j != i and k != j and k != i:
                        curRes = [nums[i], nums[j], nums[k]]
                        if curRes not in res:
                            res.append(curRes)
        return res


class Solution2(object):
    def threeSum(self, nums):
        """
        Convert 3sum to 2sum.
        Time complexity: O(n^3)
        Space complexity: O(n)
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(numsInner, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            lookup = {}
            for num in numsInner:
                if target - num in lookup:
                    if (-target, target - num, num) not in res:
                        res.append((-target, target - num, num))
                lookup[num] = target - num

        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            twoSum(nums[i + 1:], 0 - nums[i])

        return [list(i) for i in res]


if __name__ == '__main__':
    print(Solution2().threeSum([-1, 0, 1, 2, -1, -4]))
