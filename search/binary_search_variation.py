class BinarySearchVariation:

    @staticmethod
    def binary_search_1st(arr, val):
        """
        Returns the index of the first occurrence of the specified val in arr.

        :param arr: List[int], list array
        :param val: int, value to be searched
        :return: int, the index of the first occurrence of the specified val in arr if has, otherwise -1
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
            if arr[mid] < val:
                low = mid + 1
            elif arr[mid] > val:
                high = mid - 1
            else:
                if mid == 0 or arr[mid - 1] != val:
                    return mid
                else:
                    high = mid - 1

        return -1

    @staticmethod
    def binary_search_last(arr, val):
        """
        Returns the index of the last occurrence of the specified val in arr.

        :param arr: List[int], list array
        :param val: int, value to be searched
        :return: int, the index of the last occurrence of the specified val in arr if has, otherwise -1
        """

        # check parameter
        if arr is None or len(arr) == 0:
            return -1

        low = 0
        high = len(arr) - 1
        last = high

        while low <= high:
            # mid = (low + high) // 2
            # mid = low + (high - low) // 2
            mid = low + ((high - low) >> 1)
            if arr[mid] < val:
                low = mid + 1
            elif arr[mid] > val:
                high = mid - 1
            else:
                if mid == last or arr[mid + 1] != val:
                    return mid
                else:
                    low = mid + 1

        return -1

    @staticmethod
    def binary_search_1st_greater_or_equal(arr, val):
        """
        Returns the index of the first element greater than or equal to the specified val in arr.

        :param arr: List[int], list array
        :param val: int, value to be searched
        :return: int, the index of the first element greater than or equal to the specified val in arr if has, otherwise -1
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
            if arr[mid] >= val:
                if mid == 0 or arr[mid - 1] < val:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1

        return -1

    @staticmethod
    def binary_search_last_less_or_equal(arr, val):
        """
        Returns the index of the last element less than or equal to the specified val in arr.

        :param arr: List[int], list array
        :param val: int, value to be searched
        :return: int, the index of the last element less than or equal to the specified val in arr if has, otherwise -1
        """

        # check parameter
        if arr is None or len(arr) == 0:
            return -1

        low = 0
        high = len(arr) - 1
        last = high

        while low <= high:
            # mid = (low + high) // 2
            # mid = low + (high - low) // 2
            mid = low + ((high - low) >> 1)
            if arr[mid] <= val:
                if mid == last or arr[mid + 1] > val:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == '__main__':
    arr = [2, 5, 8, 12, 20, 123, 123, 123, 697]
    idx = BinarySearchVariation.binary_search_1st(arr, 123)
    print(idx)

    idx = BinarySearchVariation.binary_search_last(arr, 123)
    print(idx)

    idx = BinarySearchVariation.binary_search_1st_greater_or_equal(arr, 9)
    print(idx)

    idx = BinarySearchVariation.binary_search_last_less_or_equal(arr, 120)
    print(idx)
