class Sort:

    @staticmethod
    def insertion_sort(arr):
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
            # and move elements greater than value to the right
            while j >= 0 and arr[j] > value:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = value  # place the element from out-of-order range into the right position

        return arr


if __name__ == '__main__':
    print(Sort.insertion_sort([4, 5, 6, 1, 3, 2]))
