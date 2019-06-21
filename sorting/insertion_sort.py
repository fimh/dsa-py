class Sort:

    @staticmethod
    def insertionSort(arr):
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
            j = i

            # find the right position for the new element from out-of-order range
            while j >= 0:
                j -= 1
                if j < 0:   # FIXME how to write more gracefully?
                    break
                if arr[j] > value:
                    arr[j + 1] = arr[j]  # move data
                else:
                    break
            arr[j + 1] = value  # place the element from out-of-order range into the right position

        return arr


if __name__ == '__main__':
    print(Sort.insertionSort([4, 5, 6, 1, 3, 2]))
