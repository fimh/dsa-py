"""
Question:   Add Two Numbers
Difficulty: Medium
Link:       https://leetcode.com/problems/add-two-numbers
Ref:        https://xiaozhuanlan.com/topic/4720839156

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time - O(n), space - O(1)
        """

        dummyNode = currNode = ListNode(0)
        value, carry = 0, 0

        while l1 or l2:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next

            # if value >= 10:
            #     value -= 10
            #     carry = 1
            # else:
            #     carry = 0
            carry, value = divmod(value, 10)

            currNode.next = ListNode(value)
            currNode = currNode.next

        # Check if still carry over
        if carry == 1:
            currNode.next = ListNode(1)

        return dummyNode.next


def print_linked_list(l: ListNode):
    curr = l
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next

    print()


if __name__ == '__main__':
    l1 = ListNode(2)
    l11 = ListNode(4)
    l12 = ListNode(3)
    l1.next = l11
    l11.next = l12

    l2 = ListNode(5)
    l21 = ListNode(6)
    l22 = ListNode(4)
    l2.next = l21
    l21.next = l22

    l3 = Solution1().addTwoNumbers(l1, l2)

    print_linked_list(l1)
    print_linked_list(l2)
    print_linked_list(l3)
