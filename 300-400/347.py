"""
Question:   Top K Frequent Elements
Difficulty: Medium
Link:       https://leetcode.com/problems/top-k-frequent-elements
Ref:        https://xiaozhuanlan.com/topic/1356294870

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import collections
import heapq  # https://docs.python.org/3/library/heapq.html


class Solution1(object):

    def topKFrequent(self, nums, k):
        """
        Time - O(n), Space - O(n)

        Exploit the counting sort idea.
        """

        res, buckets = [], ['*'] * (len(nums) + 1)

        # calculate the frequency for each element
        # not recommend using the these advanced utility function, since they are not language-independent
        # maps = collections.Counter(nums)
        maps = {}
        for n in nums:
            fre = maps.get(n, 0)
            maps[n] = fre + 1

        for key in maps.keys():
            count = maps.get(key)
            if buckets[count] == '*':
                buckets[count] = []
            buckets[count].append(key)

        # get the result
        i = len(nums)
        while len(res) < k and i >= 0:
            if buckets[i] != '*':
                res.extend(buckets[i])
            i -= 1

        return res


class Solution2(object):
    class FreqNode:

        def __init__(self, num, freq):
            self.num = num
            self.freq = freq

        def __eq__(self, other):
            return self.freq == other.freq

        def __ne__(self, other):
            return self.freq != other.freq

        def __gt__(self, other):
            return self.freq > other.freq

        def __ge__(self, other):
            return self.freq >= other.freq

        def __lt__(self, other):
            return self.freq < other.freq

        def __le__(self, other):
            return self.freq <= other.freq

        def __repr__(self):
            return str((self.num, self.freq))

    def topKFrequent(self, nums, k):

        """
        Time - O(nlogn), Space - O(n)

        Exploit PriorityQueue (min-heap) to keep a k elements heap.
        """

        # calculate the frequency for each element
        maps = {}
        for n in nums:
            fre = maps.get(n, 0)
            maps[n] = fre + 1

        pq = []
        ret = []

        for key, val in maps.items():
            node = Solution2.FreqNode(key, val)
            if len(pq) < k:
                heapq.heappush(pq, node)
            elif node > pq[0]:
                # or, you can use heapq.heapreplace
                heapq.heappop(pq)
                heapq.heappush(pq, node)

        for n in pq:
            ret.append(n.num)

        return ret


class Solution3(object):

    def topKFrequent(self, nums, k):
        """
        Time - O(nlogn), Space - unknown, should dive into the implementation of most_common

        Do not use this approach in an interview, you can just experience these amazing built-in handy functions.
        """
        return [kk for kk, vv in collections.Counter(nums).most_common(k)]


if __name__ == '__main__':
    k = 3
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 1, 4]

    ret = Solution2().topKFrequent(nums, k)
    print(ret)
