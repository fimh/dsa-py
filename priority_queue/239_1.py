"""
Question:   Sliding Window Maximum
Difficulty: Hard
Link:       https://leetcode.com/problems/sliding-window-maximum/
Ref:        https://leetcode-cn.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

"""
import heapq
from queue import PriorityQueue
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Priority Queue Approach
        """
        n = len(nums)
        if n < k:
            return []
        pq = [(-nums[i], i) for i in range(k)]
        heapq.heapify(pq)
        ans = [-pq[0][0]]
        for i in range(k, n):
            heapq.heappush(pq, (-nums[i], i))
            while pq[0][1] <= i - k:
                heapq.heappop(pq)
            ans.append(-pq[0][0])
        return ans


if __name__ == '__main__':
    test_k = 5
    test_arr = [9, 10, 9, -7, -4, -8, 2, -6]
    ret = Solution().maxSlidingWindow(test_arr, test_k)
    print(ret)
