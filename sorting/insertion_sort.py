class InsertionSort:

    @staticmethod
    def insertion_sort(arr):
        """
        Insertion sort.

        :param arr: List[int], list to be sorted
        :return: List[int], sorted list
        """
        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # i - range out of order
        # j = range in order
        for i in range(1, n):
            value = arr[i]
            j = i - 1

            # find the right position for the new element from out-of-order range
            # and shift elements greater than value to the right
            while j >= 0 and arr[j] > value:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = value  # place the element from out-of-order range into the right position

        return arr


if __name__ == '__main__':
    print(InsertionSort.insertion_sort([4, 5, 6, 3, 2, 1]))

    import random
    import time

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(1000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)

        time_start = time.process_time()

        InsertionSort.insertion_sort(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
