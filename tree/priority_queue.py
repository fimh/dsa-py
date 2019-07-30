"""
One application of heap - PriorityQueue.
In essence, PriorityQueue is a heap, just compared by priority, not the numerical data directly.

For original implementation (which has been commented out), refer to https://github.com/wangzheng0822/algo/blob/master/python/28_binary_heap/priority_queue.py

The implementation here reuses the heapify logic (upwards and downwards) from tree.heap
"""

from tree.heap import Heap


class PQNode:

    def __init__(self, priority, data=None):
        assert type(priority) is int and priority >= 0
        self.priority = priority
        self.data = data

    def __repr__(self):
        return str((self.priority, self.data))

    # The following 6 methods are so-called rich comparison methods
    # For details, refer to PEP 207 -- Rich Comparisons at https://www.python.org/dev/peps/pep-0207/

    def __eq__(self, other):
        """Only compare priority."""

        return self.priority == other.priority

    def __ne__(self, other):
        return self.priority != other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority


class PriorityQueue:
    """
    Priority Queue, actually is a min-heap (with root node starting from 0).
    """

    def __init__(self, capacity=100):
        self._capacity = capacity
        self._q = []
        self._length = 0

    def get_length(self):
        return self._length

    def enqueue(self, data):
        if self._length >= self._capacity:
            return False

        # add the node at the tail
        self._q.append(data)
        self._length += 1

        # heapify this heap
        Heap.heapify_upwards_0_based(self._q, self._length - 1, False)
        return True

    # original implementation
    # def enqueue(self, data: PQNode):
    #     if self._length >= self._capacity:
    #         return False
    #
    #     self._q.append(data)
    #     self._length += 1
    #
    #     # update queue
    #     nn = self._length - 1
    #     while nn > 0:
    #         p = (nn - 1) // 2
    #         if self._q[nn].priority < self._q[p].priority:
    #             self._q[nn], self._q[p] = self._q[p], self._q[nn]
    #             nn = p
    #         else:
    #             break
    #
    #     return True

    def dequeue(self):
        if self._length <= 0:
            raise Exception('Empty queue')

        self._q[0], self._q[-1] = self._q[-1], self._q[0]
        ret = self._q.pop()
        self._length -= 1

        # heapify
        Heap.heapify_downwards_0_based(self._q, self._length, 0, False)
        return ret

    # original implementation
    # def dequeue(self):
    #     if self._length <= 0:
    #         raise Exception('the queue is empty....')
    #
    #     self._q[0], self._q[-1] = self._q[-1], self._q[0]
    #     ret = self._q.pop()
    #     self._length -= 1
    #
    #     if self._length > 1:
    #         # update queue
    #         lp = (self._length - 2) // 2
    #         idx = 0
    #
    #         while idx <= lp:
    #             lc = 2 * idx + 1
    #             rc = lc + 1
    #
    #             if rc <= self._length - 1:
    #                 tmp = lc if self._q[lc].priority < self._q[rc].priority else rc
    #             else:
    #                 tmp = lc
    #
    #             if self._q[tmp].priority < self._q[idx].priority:
    #                 self._q[tmp], self._q[idx] = self._q[idx], self._q[tmp]
    #                 idx = tmp
    #             else:
    #                 break
    #     return ret

    def __repr__(self):
        def formatter(node):
            assert type(node) is PQNode
            return node.priority, node.data

        data = list(map(formatter, self._q))
        return Heap.draw_heap(data)


if __name__ == '__main__':
    node5 = PQNode(5, 'Watch TV')
    node2 = PQNode(2, 'Learning')
    node10 = PQNode(10, 'Go Sleep')
    node0 = PQNode(0, 'Go Home')
    node7 = PQNode(7, 'Mobile Games')

    node51 = PQNode(5, 'Watch TV')
    print('PQNode')
    print(node5 == node51)
    print(node5 > node2)
    print(node5)

    print('\nPriorityQueue')
    pq = PriorityQueue()
    pq.enqueue(node5)
    pq.enqueue(node2)
    pq.enqueue(node10)
    pq.enqueue(node0)
    pq.enqueue(node7)
    print(pq)

    print('Dequeue of PriorityQueue')
    while pq.get_length() > 0:
        print(pq.dequeue())

    print('\nHeap as PriorityQueue')
    heap = Heap(100)
    heap.insert(node5)
    heap.insert(node2)
    heap.insert(node10)
    heap.insert(node0)
    heap.insert(node7)

    print(Heap.draw_heap(heap.get_arr()))
