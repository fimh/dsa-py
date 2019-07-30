import random

from sorting.heap_sort import HeapSort
from sorting.sort_helper import SortHelper
from tree.heap import Heap


def top_k(nums, k):
    """

    :param nums: List[int], input arr
    :param k: int, specify how many top elements will be returned
    :return: List[int], top k elements from the original arr nums
    """

    # whether k >= length
    length = len(nums)
    if length <= k:
        return nums

    min_heap = Heap(k, False)

    # fill up the heap with [0, k) firstly
    for i in range(0, k):
        min_heap.insert(nums[i])

    # compare the heap-top with elements in [k, length)
    # if current element greater than heap-top, then it indicates heap-top is not in top-k,
    # so we need to current heap-top, and insert the current element into the min-heap
    for i in range(k, length):
        top = min_heap.get_top()
        curr = nums[i]
        if curr > top:
            min_heap.remove_top()
            min_heap.insert(curr)

    return min_heap.get_arr()


if __name__ == '__main__':

    k = 5
    nums = []
    for i in range(20):
        nums.append(random.randint(1, 100))

    # or, you can use this handy function - random.sample to generate a random list
    # generate a list with random number
    # nums = random.sample(range(1, 100), 20)

    print('original nums:')
    print(nums)

    print('\ntop {} elements:'.format(k))
    print(top_k(nums, k))

    print('\nverifying, sorted nums:')
    HeapSort.heap_sort(nums)
    print(nums, SortHelper.is_array_sorted(nums))
    print('last {} elements are {}'.format(k, nums[-k::]))
