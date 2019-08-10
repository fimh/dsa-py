"""
Question:   Find Median from Data Stream
Difficulty: Hard
Link:       https://leetcode.com/problems/find-median-from-data-stream
Ref:        https://leetcode.com/articles/find-median-from-data-stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

"""

import bisect
from heapq import heappush, heappop


class MedianFinder1:
    """
    Approach 1 - Simple Sorting

    Store the numbers in a resizable container. Every time you need to output the median,
    sort the container and output the median.

    Time - O(nlogn), Space - O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()

        n = len(self.nums)
        if n % 2 == 0:  # has even numbers
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) * 0.5
        else:
            return self.nums[n // 2]


class MedianFinder2:
    """
    Approach 2 - Insertion Sort

    Keeping our input container always sorted (i.e. maintaining the sorted nature of the
    container as an invariant) via the idea of insertion sort.

    Time - O(n), Space - O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.nums = []

    def addNum(self, num: int) -> None:
        if len(self.nums) == 0:
            self.nums.append(num)
        else:
            # equivalent to bisect.insort_left(self.nums, num)
            # equivalent to std::lower_bound() in c++
            # https://docs.python.org/3.6/library/bisect.html
            # http://www.cplusplus.com/reference/algorithm/lower_bound/?kw=lower_bound
            self.nums.insert(bisect.bisect_left(self.nums, num), num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 0:  # has even numbers
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) * 0.5
        else:
            return self.nums[n // 2]


class MedianFinder3:
    """
    Approach 3 - Two Heaps

    Maintain two heaps.
    A max-heap to store the smaller half of the input numbers
    A min-heap to store the larger half of the input numbers

    Time - O(logn), Space - O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """

        # note that, built-in heapq is min heap
        # self.lo = []  # max heap
        # self.hi = []  # min heap
        self.lo = DynamicHeap(False)  # max heap
        self.hi = DynamicHeap()  # min heap

    def addNum(self, num: int) -> None:
        # heappush(self.lo, -num)  # add to max heap
        self.lo.push(num)

        # balancing step
        # heappush(self.hi, -heappop(self.lo))
        self.hi.push(self.lo.pop())

        # maintain size property
        # if len(self.lo) < len(self.hi):
        #     heappush(self.lo, -heappop(self.hi))
        if self.lo.size() < self.hi.size():
            self.lo.push(self.hi.pop())

    def findMedian(self) -> float:
        # return -self.lo[0] if len(self.lo) > len(self.hi) else (-self.lo[0] + self.hi[0]) * 0.5
        return self.lo.top() if self.lo.size() > self.hi.size() else (self.lo.top() + self.hi.top()) * 0.5


class DynamicHeap:

    def __init__(self, min_heap: bool = True):
        self._pq = []
        self._min_heap = min_heap

    def push(self, num: int) -> None:
        t_val = num if self._min_heap else -num
        heappush(self._pq, t_val)

    def pop(self) -> int:
        t_val = heappop(self._pq)
        return t_val if self._min_heap else -t_val

    def top(self) -> int:
        return self._pq[0] if self._min_heap else -self._pq[0]

    def size(self) -> int:
        return len(self._pq)

    # def __sizeof__(self):
    #     len(self._pq)


if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder3()

    obj.addNum(5)
    obj.addNum(2)
    obj.addNum(1)
    print('median is: {}'.format(obj.findMedian()))

    obj.addNum(39)
    obj.addNum(20)
    print('median is: {}'.format(obj.findMedian()))
