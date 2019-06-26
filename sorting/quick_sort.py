class QuickSort:

    @staticmethod
    def quick_sort(arr):
        """
        Quick sort arr in place.

        :param arr: List[int], the list to be sorted.
        :return: void, list will be sorted in place
        """
        # No need to sort
        if arr is None:
            return

        n = len(arr)
        if n <= 1:
            return

        QuickSort.do_quick_sort(arr, 0, n - 1)

    @staticmethod
    def do_quick_sort(arr, start, end):
        """
        Quick sort array in memory with given range.
        
        :param arr: List[int], list to be sorted 
        :param start: int, start index of the list to be sorted, inclusive
        :param end: int, end index of the list to be sorted, inclusive
        :return: void, list will be sorted in place
        """
        if start < end:
            pi = QuickSort.partition(arr, start, end)

            QuickSort.do_quick_sort(arr, start, pi - 1)
            QuickSort.do_quick_sort(arr, pi + 1, end)

    @staticmethod
    def partition(arr, start, end):
        """
        Divide the input arr(list) into three part: [start, pivot), pivot, (pivot, end].
        The elements in left part are all smaller than pivot, and the elements in right part are all greater or equal to
        pivot.
        This function takes last element as pivot, places the pivot element at its correct position in sorted array, and
        places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot.

        :param arr: List[int], the list to be partitioned
        :param start: int, start index of the list, inclusive
        :param end: int, end index of the list, inclusive
        :return: int, the pivot index in partitioned list
        """
        pivot = arr[end]
        i = start  # index of the pivot in new array

        for j in range(start, end):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[end] = arr[end], arr[i]
        return i


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    QuickSort.quick_sort(arr)
    print(arr)

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)

        time_start = time.process_time()

        QuickSort.quick_sort(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
