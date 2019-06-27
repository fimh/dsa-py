class BinarySearch:

    @staticmethod
    def binary_search_iterative(arr, val):
        """
        Returns the index of the specified val in arr via iteration.

        :param arr: List[int], list array
        :param val: int, value to be searched
        :return: int, the index of the specified val in arr if has, otherwise -1
        """

        # check parameter
        if arr is None or len(arr) == 0:
            return -1

        low = 0
        high = len(arr) - 1

        while low <= high:
            # mid = (low + high) // 2
            # mid = low + (high - low) // 2
            mid = low + ((high - low) >> 1)
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    @staticmethod
    def binary_search_recursive(arr, val):
        """
        Returns the index of the specified val in arr via recursion.

        :param arr: List[int], list array
        :param val: int, value to be searched
        :return: int, the index of the specified val in arr if has, otherwise -1
        """

        # check parameter
        if arr is None or len(arr) == 0:
            return -1

        return BinarySearch.__binary_search_recursive(arr, 0, len(arr) - 1, val)

    @staticmethod
    def __binary_search_recursive(arr, low, high, val):
        # terminal condition
        if low > high:
            return -1

        # divide the current question into two sub-questions
        mid = low + ((high - low) >> 1)
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return BinarySearch.__binary_search_recursive(arr, mid + 1, high, val)
        else:
            return BinarySearch.__binary_search_recursive(arr, low, mid - 1, val)


if __name__ == '__main__':
    arr = [2, 5, 8, 12, 90, 123, 697]
    val = 123
    idx = BinarySearch.binary_search_recursive(arr, val)
    print(idx)

    import random
    import time

    time_total = 0
    time_start = 0
    time_dur = 0
    for idx in range(10000):
        # generate a list with random number
        random_arr = random.sample(range(0, 1000), 200)
        random_arr.sort()
        val = random.randrange(0, 1000)
        time_start = time.process_time()

        ret_idx = BinarySearch.binary_search_iterative(random_arr, val)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

        print('{} with index[{}] in {}'.format(val, ret_idx, random_arr))

    print('elapsed time: {} ms'.format(time_total * 1000))
