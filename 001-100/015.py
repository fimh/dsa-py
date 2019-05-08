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


class Solution3(object):
    def threeSum(self, nums):
        """
        Sort first
        Then, fix left boundary, increase it when encountering a duplicated element
        Finally, use two pointers to scan the rest list from both side to the center.
        Time complexity: O(n^2)
        Space complexity: O(n)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif tmp > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    print(Solution3().threeSum([-1, 0, 1, 2, -1, -4]))
