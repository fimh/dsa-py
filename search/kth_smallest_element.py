from sorting.quick_sort import QuickSort
import random

class KthSmallestElement:

    @staticmethod
    def kth_smallest_sort(arr, k):
        """
        Find the kth smallest element via sorting.
        Time complexity: O(nlogn)

        :param arr: List[int], the given list
        :param k: int, kth element, ranging from [1, n]
        :return: int, the value of kth element in the given array.
        """

        # check parameters
        KthSmallestElement.__check_parameters(arr, k)

        # sort the given array first
        # arr.sort()
        QuickSort.quick_sort(arr)

        # return the kth element in the sorted array
        return arr[k - 1]

    @staticmethod
    def kth_smallest_quick_select(arr, k):
        """
        Find the kth smallest element via quick sort idea.
        Time complexity: worst - O(n^2), average - O(n)

        :param arr: List[int], the given list
        :param k: int, kth element, ranging from [1, n]
        :return: int, the value of kth element in the given array.
        """

        # check parameters
        KthSmallestElement.__check_parameters(arr, k)

        return KthSmallestElement.__kth_smallest_quick_select(arr, 0, len(arr) - 1, k)

    @staticmethod
    def __check_parameters(arr, k):
        """If the given parameter is invalid, we throw an exception directly."""

        if arr is None:
            raise ValueError('arr is None')

        if k < 1 or k > len(arr):
            raise ValueError('k incorrect')

    @staticmethod
    def __kth_smallest_quick_select(arr, l, r, k):
        """
        Find the kth smallest element via quick sort idea.
        Time complexity: worst - O(n^2), average - O(n)

        :param arr: List[int], the given list
        :param l: int, start index of the list, inclusive
        :param r: int, end index of the list, inclusive
        :param k: int, kth element in current recursion ranging from [1, n]
        :return: int, the value of kth element in the given array.
        """

        # partition the array around last element and get position of pivot element of sorted array
        pivot_idx = KthSmallestElement.__partition_random(arr, l, r)

        # k - 1, the index the kth element
        # pivot_idx -l, the pivot index in current recursion
        if pivot_idx - l == k - 1:
            return arr[pivot_idx]
        if pivot_idx - l > k - 1:
            return KthSmallestElement.__kth_smallest_quick_select(arr, l, pivot_idx - 1, k)
        else:
            return KthSmallestElement.__kth_smallest_quick_select(arr, pivot_idx + 1, r, k - 1 - pivot_idx + l)

    @staticmethod
    def __partition(arr, l, r):
        """
        Standard partition process of QuickSort(). i.e., it considers the last element as pivot
        and moves all smaller elements to left of it and greater elements to right.

        :param arr: List[int], the list to be partitioned
        :param l: int, start index of the list, inclusive
        :param r: int, end index of the list, inclusive
        :return: int, the pivot index in sorted array
        """

        return QuickSort.partition(arr, l, r)

    @staticmethod
    def __partition_random(arr, l, r):
        """
        Partition the input arr via a random pivot.

        :param arr: List[int], the list to be partitioned
        :param l: int, start index of the list, inclusive
        :param r: int, end index of the list, inclusive
        :return: int, the pivot index in sorted array
        """
        pivot_idx = random.randint(l, r)
        if pivot_idx != r:
            arr[pivot_idx], arr[r] = arr[r], arr[pivot_idx]

        return KthSmallestElement.__partition(arr, l, r)


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    k = 4
    ret = KthSmallestElement.kth_smallest_quick_select(arr, k)
    print('{}th smallest element is {}'.format(k, ret))

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)
        k = 120
        time_start = time.process_time()

        KthSmallestElement.kth_smallest_quick_select(random_arr, k)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
