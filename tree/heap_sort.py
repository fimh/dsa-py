from sorting.sort_helper import SortHelper
from tree.heap import Heap


class HeapSort:
    """
    This implementation is based on max-heap with root node starting from 0.
    """

    @staticmethod
    def build_heap(arr, n):
        for i in range((n - 2) // 2, -1, -1):  # [(n-2)//2, 0]
            Heap.heapify_downwards_0_based(arr, n, i)

    @staticmethod
    def heap_sort(arr):
        # No need to sort
        if arr is None:
            return

        n = len(arr)
        if n <= 1:
            return

        HeapSort.build_heap(arr, n)
        k = n
        while k > 0:
            arr[0], arr[k - 1] = arr[k - 1], arr[0]
            k -= 1
            Heap.heapify_downwards_0_based(arr, k, 0)


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    HeapSort.heap_sort(arr)
    print(arr, SortHelper.is_array_sorted(arr))

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)

        time_start = time.process_time()

        HeapSort.heap_sort(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

        if SortHelper.is_array_sorted(random_arr) is False:
            print("not sorted")

    print('elapsed time: {} ms'.format(time_total * 1000))
