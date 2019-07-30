import math


class Heap:
    """
    This is a max-heap / min-heap with root node starting from 1.
    """

    def __init__(self, capacity: int, max_heap: bool = True, init_data=None):
        """
        :param capacity: int, capacity of the current heap
        :param max_heap: bool, True - max-heap, False - min-heap
        :param init_data: List[int], initial passed-in data
        """

        self.arr = [0] * (capacity + 1)
        self.max_size = capacity
        self.count = 0
        self._max_heap = max_heap

        if type(init_data) is list and len(init_data) <= self.max_size:
            for i in range(0, len(init_data)):
                self.arr[i + 1] = init_data[i]

            self.count = len(init_data)

            # build heap on the init data
            for i in range(self.count // 2, 0, -1):  # [n//2, 1]
                Heap.heapify_downwards_1_based(self.arr, self.count, i, self._max_heap)

    def insert(self, data):
        if self.count >= self.max_size:  # heap is full
            return

        # add the new element to the tail
        self.count += 1
        self.arr[self.count] = data

        # heapify from bottom to top
        self.heapify_upwards_1_based(self.arr, self.count, self._max_heap)

    def remove_top(self):
        if self.count == 0:  # heap is empty
            return

        # copy the tail element to the top, then remove the tail element
        self.arr[1] = self.arr[self.count]
        self.count -= 1

        # heapify from top to bottom
        self.heapify_downwards_1_based(self.arr, self.count, 1, self._max_heap)

    def get_top(self):
        if self.count == 0:
            return None

        return self.arr[1]

    def get_arr(self):
        if self.count == 0:
            return None

        return self.arr[1:self.count + 1]

    @staticmethod
    def heapify_upwards_1_based(arr, i, max_heap: bool = True):
        """
        Heapify the given array at index = i from bottom to top.
        :param arr: List[int], the heap array
        :param i: int, the starting index to heapify
        :param max_heap: bool, true - max heap, false - min heap
        :return: void, the operation is in place
        """

        while i > 1:
            p = i // 2
            if (max_heap and arr[i] > arr[p]) or (not max_heap and arr[i] < arr[p]):
                arr[i], arr[p] = arr[p], arr[i]
                i = p
            else:
                break

    @staticmethod
    def heapify_upwards_0_based(arr, i, max_heap: bool = True):
        """
        Heapify the given array at index = i from bottom to top.
        :param arr: List[int], the heap array
        :param i: int, the starting index to heapify
        :param max_heap: bool, true - max heap, false - min heap
        :return: void, the operation is in place
        """

        while i > 0:
            p = (i - 1) // 2
            if (max_heap and arr[i] > arr[p]) or (not max_heap and arr[i] < arr[p]):
                arr[i], arr[p] = arr[p], arr[i]
                i = p
            else:
                break

    @staticmethod
    def heapify_downwards_0_based(arr, n, i, max_heap: bool = True):
        """
        Heapify the given array at index = i from top to bottom.
        The root node of heap will start from 0.
        :param arr: List[int], the heap array
        :param n: int, the heap size
        :param i: int, the starting index to heapify
        :param max_heap: bool, true - max heap, false - min heap
        :return: void, the operation is in place
        """

        while True:
            target_pos = i
            left_child = i * 2 + 1
            right_child = i * 2 + 2
            if left_child <= n - 1 and ((max_heap and arr[i] < arr[left_child])
                                        or
                                        (not max_heap and arr[i] > arr[left_child])):
                target_pos = left_child
            if right_child <= n - 1 and ((max_heap and arr[target_pos] < arr[right_child])
                                         or
                                         (not max_heap and arr[target_pos] > arr[right_child])):
                target_pos = right_child
            if target_pos == i:  # no change, break the loop
                break

            arr[i], arr[target_pos] = arr[target_pos], arr[i]
            i = target_pos

    @staticmethod
    def heapify_downwards_1_based(arr, n, i, max_heap: bool = True):
        """
        Heapify the given array at index = i from top to bottom.
        The root node of heap will start from 1.
        :param arr: List[int], the heap array
        :param n: int, the heap size
        :param i: int, the starting index to heapify
        :param max_heap: bool, true - max heap, false - min heap
        :return: void, the operation is in place
        """

        while True:
            target_pos = i
            left_child = i * 2
            right_child = i * 2 + 1
            if left_child <= n and ((max_heap and arr[i] < arr[left_child])
                                    or
                                    (not max_heap and arr[i] > arr[left_child])):
                target_pos = left_child
            if right_child <= n and ((max_heap and arr[target_pos] < arr[right_child])
                                     or
                                     (not max_heap and arr[target_pos] > arr[right_child])):
                target_pos = right_child
            if target_pos == i:
                break

            arr[i], arr[target_pos] = arr[target_pos], arr[i]
            i = target_pos

    @staticmethod
    def draw_heap(arr, zero_based=True):
        """
        Print heap in a human readable way.
        :param arr: the heap
        :param zero_based: true, the root node is starting from 0; else, false
        :return: the printed string
        """

        if arr is None:
            return 'None'

        if len(arr) == 0:
            return 'Empty heap'

        ret = ''
        for i, n in enumerate(arr):
            ret += str(n)
            # add line break
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(arr) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret


if __name__ == '__main__':
    arr = [32, 64, 20, 27, 56, 40]
    heap = Heap(12, init_data=arr)

    # for i in arr:
    #     heap.insert(i)
    print(heap.arr, heap.count)
    print(heap.get_arr())
    print()
    print(Heap.draw_heap(heap.get_arr()))

    for i in range(2):
        heap.remove_top()
        print(heap.arr, heap.count)

    print('\nCompare two heapify approaches:')
    import random
    import time

    time_total_1 = 0
    time_total_2 = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)

        # 1st - heapify when creating -------------- @start
        # time complexity: O(n), not O(nlogn); for details, refer to https://time.geekbang.org/column/article/69913
        time_start = time.process_time()

        tmp_heap = Heap(len(random_arr), init_data=random_arr)

        # calculate the exact total time
        time_dur = time.process_time() - time_start
        time_total_1 += time_dur

        # 1st - heapify when creating -------------- @end

        # 2ed - heapify via inserting -------------- @start
        time_start = time.process_time()

        tmp_heap_2 = Heap(len(random_arr))
        for node in random_arr:
            tmp_heap_2.insert(node)

        # calculate the exact total time
        time_dur = time.process_time() - time_start
        time_total_2 += time_dur

        # 2ed - heapify via inserting -------------- @end

    print('elapsed time for heapify when creating: {} ms'.format(time_total_1 * 1000))
    print('elapsed time for heapify when inserting: {} ms'.format(time_total_2 * 1000))
