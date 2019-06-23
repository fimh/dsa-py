class Sort:

    @staticmethod
    def selection_sort_min_version(arr):
        """
        Selection sort in selecting-min-element style. Note that selection is the slowest of all the common sorting
        algorithms. It requires quadratic time even in the best case (i.e., when the array is already sorted).

        :param arr: List[int], list to be sorted
        :return: List[int], sorted list
        """
        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # i - range in order
        # j - range out of order
        for i in range(0, n):
            min_index = i
            j = i + 1

            # select min element in range[j, n)
            while j < n:
                if arr[j] < arr[min_index]:
                    min_index = j
                j += 1

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    @staticmethod
    def selection_sort_max_version(arr):
        """
        Selection sort in selecting-max-element style. Note that selection is the slowest of all the common sorting
        algorithms. It requires quadratic time even in the best case (i.e., when the array is already sorted).

        :param arr: List[int], list to be sorted
        :return: List[int], sorted list
        """
        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # i - range in order
        # j - range out of order
        for i in range(n - 1, 0, -1):
            max_index = i
            j = i - 1

            # select max element in range[0, j]
            while j >= 0:
                if arr[j] > arr[max_index]:
                    max_index = j
                j -= 1

            arr[i], arr[max_index] = arr[max_index], arr[i]

        return arr


if __name__ == '__main__':
    print(Sort.selection_sort_min_version([4, 5, 6, 3, 2, 1]))
    print(Sort.selection_sort_max_version([4, 5, 6, 3, 2, 1]))

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)

        time_start = time.process_time()

        Sort.selection_sort_max_version(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
