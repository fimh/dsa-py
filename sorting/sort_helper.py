class SortHelper:

    @staticmethod
    def is_array_sorted(arr, ascending=True):
        """
        Check whether the given array is sorted or not.
        :param arr: List[int], array to be checked
        :param ascending: Bool, ascending order or descending order
        :return: True, the given array is sorted; False, not sorted
        """

        # No need to continue
        if arr is None:
            return True

        n = len(arr)
        if n <= 1:
            return True

        if ascending:
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    return False

            return True
        else:
            for i in range(n - 1):
                if arr[i] < arr[i + 1]:
                    return False

            return True
