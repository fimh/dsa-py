"""
Question:   Search in Rotated Sorted Array
Difficulty: Medium
Link:       https://leetcode.com/problems/search-in-rotated-sorted-array/
Ref:        https://xiaozhuanlan.com/topic/2039467185

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""


class Solution(object):
    def search(self, nums, target):
        """
        Use binary search to solve this problem.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:  # if mid in right half
                # if target in (nums[mid], nums[r]], (i.e., target in right half), then we divide right half again
                # else, divide left half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # if mid in left half
                # if target in [nums[l], nums[mid]), (i.e., target in left half) then we divide left half again
                # else, divide right half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    ret_idx = Solution().search(nums, target)
    print(ret_idx)
