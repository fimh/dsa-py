"""
Question:   Reverse Linked List
Difficulty: Easy
Link:       https://leetcode.com/problems/reverse-linked-list/
Ref:        https://leetcode-cn.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        """Iterative approach"""
        curr, prev = head, None
        while curr is not None:
            curr.next, curr, prev = prev, curr.next, curr

        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        """Recursive approach - problem"""
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head


def print_list_node(head: ListNode) -> None:
    print("[", end="")

    while head is not None:
        print(head.val, end="")
        print(",", end="")
        head = head.next

    print("]")


def construct_test_head(test_input: List[int]) -> ListNode:
    test_nodes = []
    for i in range(len(test_input)):
        test_nodes.append(ListNode(test_input[i]))

    for i in range(len(test_input) - 1):
        test_nodes[i].next = test_nodes[i + 1]

    return None if len(test_nodes) == 0 else test_nodes[0]


if __name__ == '__main__':
    test_input = [1, 2, 3, 4, 5]
    test_head = construct_test_head(test_input)

    print_list_node(test_head)
    ret = Solution().reverseList(test_head)
    print_list_node(ret)
