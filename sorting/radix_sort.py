class RadixSort:

    @staticmethod
    def radix_sort(arr):
        """
        Radix sort arr.

        :param arr: List[int], the list to be sorted
        :return: void, list will be sorted in place
        """

        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # find max value to know numbers of digits
        max_value = arr[0]
        for i in range(1, n):
            if arr[i] > max_value:
                max_value = arr[i]

        # or we can just use built-in function max
        # max_value = max(arr)

        # do counting sort for every digit. note that instead of passing digit number, exp is passed.
        # exp is 10^i where i is current digit number
        curr_exp = 1
        while max_value // curr_exp > 0:
            RadixSort.counting_sort(arr, curr_exp)
            curr_exp *= 10

    @staticmethod
    def counting_sort(arr, curr_exp):
        """
        Counting sort according to specified digit.
        :param arr: List[int], the list to be sorted
        :param curr_exp: int, this parameter indicates which digit, say we want to get 1st digit from right to left,
        then we pass 10^0
        :return: void, list will be sorted in place
        """

        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # find the counting scope - 0..9, i.e., the max value is 9 actually
        max_value = 9

        # init the counting array via
        count_arr = [0] * (max_value + 1)

        # update the counting number
        for i in arr:
            curr_digit = RadixSort.get_specified_digit(i, curr_exp)
            count_arr[curr_digit] += 1

        # update the total counting number
        for i in range(1, max_value + 1):
            count_arr[i] += count_arr[i - 1]

        # store sorted result in a temp array, why scan inversely?
        # note reverse-scanning can guarantee the sort result is stable
        tmp_arr = [0] * n
        for i in range(n - 1, -1, -1):
            curr_digit = RadixSort.get_specified_digit(arr[i], curr_exp)
            idx = count_arr[curr_digit] - 1
            tmp_arr[idx] = arr[i]
            count_arr[curr_digit] -= 1

        # copy result back to original array
        for i in range(n):
            arr[i] = tmp_arr[i]

    @staticmethod
    def get_specified_digit(num, curr_exp):
        """
        Return the specified digit of the given number.
        :param num: int, the input number
        :param curr_exp: int, 10^n, say 153, if you want to get the first digit 3, curr_exp should be 10^0=1
        :return: int, the specified digit of the given number
        """

        return (num // curr_exp) % 10


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    RadixSort.radix_sort(arr)
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

        RadixSort.radix_sort(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
