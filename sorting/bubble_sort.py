class BubbleSort:
    @staticmethod
    def bubble_sort(arr):
        """
        Bubble sort.

        :param arr: List[int], list to be sorted
        :return: List[int], sorted list
        """
        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # compare every adjacent elements
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # swap two elements in general way
                    # tmp = arr[j]
                    # arr[j] = arr[j + 1]
                    # arr[j + 1] = tmp

                    # swap two elements in python way
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]

        return arr

    @staticmethod
    def bubble_sort_optimized(arr):
        """
        Optimized bubble sort.

        :param arr: List[int], list to be sorted
        :return: List[int], sorted list
        """
        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # Set a flag to indicate whether we have swapped element or not
        for i in range(0, n):
            swapped = False  # we have swapped element or not
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # swap two elements in general way
                    # tmp = arr[j]
                    # arr[j] = arr[j + 1]
                    # arr[j + 1] = tmp

                    # swap two elements in python way
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]

                    swapped = True

            if swapped is False:  # no need to continue, since it's already in order
                break

        return arr


if __name__ == '__main__':
    print(BubbleSort.bubble_sort_optimized([4, 5, 6, 3, 2, 1]))

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)

        time_start = time.process_time()

        BubbleSort.bubble_sort_optimized(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
