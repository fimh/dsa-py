"""
Question:   Linked List Cycle II
Difficulty: Medium
Link:       https://leetcode.com/problems/linked-list-cycle-ii/
Ref:        https://leetcode-cn.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
from typing import Optional

from L141 import locate_node
from L206 import construct_test_head, ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """set based"""
        curr = head
        cache = set()
        while curr:
            cache.add(curr)
            curr = curr.next
            if curr in cache:
                return curr
        return None

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """two pointers"""
        fast = slow = head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr = head
                while ptr != slow:  # Why does this approach work?
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None


if __name__ == '__main__':
    pos = 2
    test_input = [3, 2, 0, -4]
    test_head = construct_test_head(test_input)

    test_tail = locate_node(test_head, len(test_input) - 1)
    test_start_recycle = locate_node(test_head, pos)
    # test_tail.next = test_start_recycle

    ret = Solution().detectCycle2(test_head)
    if ret:
        print(ret.val)
    else:
        print(ret)
