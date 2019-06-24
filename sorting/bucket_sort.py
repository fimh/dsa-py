from sorting.insertion_sort import InsertionSort


class BucketSort:

    @staticmethod
    def bucket_sort(arr):
        """
        Bucket sort arr in place.

        :param arr: List[int], the list to be sorted.
        :return: void, list will be sorted in place
        """

        # No need to sort
        if arr is None:
            return arr

        n = len(arr)
        if n <= 1:
            return arr

        # initialize buckets
        bucket_list = []
        bucket_num = n // 2
        if bucket_num == 0:
            bucket_num = 1
        [bucket_list.append([]) for _ in range(bucket_num)]

        # put array elements into different buckets
        # [bucket_list[Sort.hash(bucket_num, i)] for i in arr]
        for i in arr:
            idx = BucketSort.hash(bucket_num, i)
            curr_bucket = bucket_list[idx]
            curr_bucket.append(i)

            # sort each bucket respectively
            BucketSort.sort_single_bucket(curr_bucket)

        # concatenate the result
        k = 0
        for i in range(bucket_num):
            for j in range(len(bucket_list[i])):
                arr[k] = bucket_list[i][j]
                k += 1

    @staticmethod
    def hash(bucket_num, element):
        """Calculate the bucket index for the given element."""

        supposed_max = 1000  # FIXME actually, we should know the input data in advance
        return int(element / supposed_max * bucket_num)

    @staticmethod
    def sort_single_bucket(bucket):
        """
        Sorting the given input bucket, which is backed by insertion sort.
        :param bucket: List[int], the bucket to be sorted.
        :return: void, the bucked will be sorted in place.
        """

        # QuickSort.quick_sort(bucket)
        InsertionSort.insertion_sort(bucket)


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    BucketSort.bucket_sort(arr)
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

        BucketSort.bucket_sort(random_arr)

        # print(random_arr)

        # calculate the exact total time for sorting
        time_dur = time.process_time() - time_start
        time_total += time_dur

    print('elapsed time: {} ms'.format(time_total * 1000))
