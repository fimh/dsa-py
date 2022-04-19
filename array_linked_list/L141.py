"""
Question:   Linked List Cycle
Difficulty: Medium
Link:       https://leetcode.com/problems/linked-list-cycle/
Ref:        https://leetcode-cn.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
# Definition for singly-linked list.
from typing import Optional

from L206 import construct_test_head, ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        curr = head
        cache = set()
        while curr:
            cache.add(curr)
            curr = curr.next
            if curr in cache:
                return True
        return False


def locate_node(head: ListNode, pos: int) -> ListNode:
    target = head
    if pos < 0:
        return None
    for _ in range(pos):
        if target is None:
            return None
        target = target.next
    return target


if __name__ == '__main__':
    pos = 1
    test_input = [3, 2, 0, -4]
    test_head = construct_test_head(test_input)

    test_tail = locate_node(test_head, len(test_input) - 1)
    test_start_recycle = locate_node(test_head, pos)
    test_tail.next = test_start_recycle

    ret = Solution().hasCycle2(test_head)
    print(ret)
