class Sort:
    @staticmethod
    def bubble_sort(arr):
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
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp

        return arr

    @staticmethod
    def optimized_bubble_sort(arr):
        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # Set a flag to indicate whether we have swapped element or not
        for i in range(0, n):
            flag = False  # we have swapped element or not
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp
                    flag = True

            if flag is False:  # no need to continue, since it's already in order
                break

        return arr


if __name__ == '__main__':
    print(Sort.optimized_bubble_sort([4, 5, 6, 3, 2, 1]))
