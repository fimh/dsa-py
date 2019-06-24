class MergeSort:

    @staticmethod
    def merge_sort(arr):
        """
        Merge sort arr in place.

        :param arr: List[int], the list to be sorted.
        :return: void, list will be sorted in place.
        """
        copy = list(arr)

        MergeSort.do_merge_sort(copy, arr, 0, len(arr))

    @staticmethod
    def do_merge_sort(ref, result, start, end):
        """
        Merge sort array in memory with given range.

        :param ref: List[int], extra space for storing temporarily sub-array sorting result
        :param result: List[int], the sorting result will be merged into this list
        :param start: int, start index of the list to be sorted, inclusive
        :param end: int, end index of the list to be sorted, exclusive
        :return: void, list will be sorted in place.
        """
        if end - start < 2:
            return
        if end - start == 2:
            if result[start] > result[start + 1]:
                result[start], result[start + 1] = result[start + 1], result[start]
            return

        # now we have 3 elements at least to divide into two groups
        mid = start + (end - start) // 2
        # it's a little tricky here
        # pass ref as result to sub recursive calls, so we can get sorted sub-list in ref,
        # then we merge two sub-ref into result
        MergeSort.do_merge_sort(result, ref, start, mid)
        MergeSort.do_merge_sort(result, ref, mid, end)

        # merge ref left- and right- side into result
        i = start
        j = mid
        idx = start
        while idx < end:
            if j >= end or (i < mid and ref[i] < ref[j]):
                result[idx] = ref[i]
                i += 1
            else:
                result[idx] = ref[j]
                j += 1

            idx += 1


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    MergeSort.merge_sort(arr)
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

        MergeSort.merge_sort(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
