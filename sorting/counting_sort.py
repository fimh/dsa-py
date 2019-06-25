class CountingSort:

    @staticmethod
    def counting_sort(arr):
        """
        Counting sort arr in place.

        :param arr: List[int], the list to be sorted.
        :return: void, list will be sorted in place
        """

        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # find the counting scope, i.e., the max value
        max_value = arr[0]
        for i in range(1, n):
            if arr[i] > max_value:
                max_value = arr[i]

        # init the counting array via list comprehension
        count_arr = [0 for _ in range(max_value + 1)]

        # update the counting number
        for i in arr:
            count_arr[i] += 1

        # update the total counting number
        for i in range(1, max_value + 1):
            count_arr[i] += count_arr[i - 1]

        # store sorted result in a temp array, why scan inversely?
        # note reverse-scanning can guarantee the sort result is stable
        tmp_arr = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            idx = count_arr[arr[i]] - 1
            tmp_arr[idx] = arr[i]
            count_arr[arr[i]] -= 1

        # copy result back to original array
        for i in range(n):
            arr[i] = tmp_arr[i]


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    CountingSort.counting_sort(arr)
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

        CountingSort.counting_sort(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
