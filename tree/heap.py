import math


class Heap:
    """
    This is a max-heap with root node starting from 1.
    """

    def __init__(self, capacity: int):
        self.arr = [0] * (capacity + 1)
        self.max_size = capacity
        self.count = 0

    def insert(self, data: int):
        if self.count >= self.max_size:  # heap is full
            return

        # add the new element to the tail
        self.count += 1
        self.arr[self.count] = data

        # heapify from bottom to top
        self.heapify_upwards_1_based(self.arr, self.count)

    def remove_top(self):
        if self.count == 0:  # heap is empty
            return

        # copy the tail element to the top, then remove the tail element
        self.arr[1] = self.arr[self.count]
        self.count -= 1

        # heapify from top to bottom
        self.heapify_downwards_1_based(self.arr, self.count, 1)

    def get_top(self):
        if self.count == 0:
            return None

        return self.arr[1]

    def get_arr(self):
        if self.count == 0:
            return None

        return self.arr[1:self.count + 1]

    @staticmethod
    def heapify_upwards_1_based(arr, i):
        """
        Heapify the given array at index = i from bottom to top.
        :param arr: List[int], the heap array
        :param i: int, the starting index to heapify
        :return: void, the operation is in place
        """

        while i // 2 > 0 and arr[i] > arr[i // 2]:
            arr[i], arr[i // 2] = arr[i // 2], arr[i]
            i = i // 2

    @staticmethod
    def heapify_downwards_0_based(arr, n, i):
        """
        Heapify the given array at index = i from top to bottom.
        The root node of heap will start from 0.
        :param arr: List[int], the heap array
        :param n: int, the heap size
        :param i: int, the starting index to heapify
        :return: void, the operation is in place
        """

        while True:
            max_pos = i
            if i * 2 + 1 <= n - 1 and arr[i] < arr[i * 2 + 1]:
                max_pos = i * 2 + 1
            if i * 2 + 2 <= n - 1 and arr[max_pos] < arr[i * 2 + 2]:
                max_pos = i * 2 + 2
            if max_pos == i:
                break

            arr[i], arr[max_pos] = arr[max_pos], arr[i]
            i = max_pos

    @staticmethod
    def heapify_downwards_1_based(arr, n, i):
        """
        Heapify the given array at index = i from top to bottom.
        The root node of heap will start from 1.
        :param arr: List[int], the heap array
        :param n: int, the heap size
        :param i: int, the starting index to heapify
        :return: void, the operation is in place
        """

        while True:
            max_pos = i
            if i * 2 <= n and arr[i] < arr[i * 2]:
                max_pos = i * 2
            if i * 2 + 1 <= n and arr[max_pos] < arr[i * 2 + 1]:
                max_pos = i * 2 + 1
            if max_pos == i:
                break

            arr[i], arr[max_pos] = arr[max_pos], arr[i]
            i = max_pos

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
    heap = Heap(12)

    arr = [32, 64, 20, 27, 56, 40]
    for i in arr:
        heap.insert(i)
    print(heap.arr, heap.count)
    print(heap.get_arr())
    print()
    print(Heap.draw_heap(heap.get_arr()))

    for i in range(2):
        heap.remove_top()
        print(heap.arr, heap.count)
