"""
Question:   Reverse Nodes in k-Group
Difficulty: Hard
Link:       https://leetcode.com/problems/reverse-nodes-in-k-group/
Ref:        https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
from typing import Optional
from L206 import ListNode, construct_test_head, print_list_node


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next, pre = head, sentinel
        while head:
            # identity a group
            tail = pre
            for _ in range(k):
                tail = tail.next
                if tail is None:
                    return sentinel.next
            # process in the current group
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nxt
            pre = tail
            head = tail.next

        return sentinel.next

    def reverse(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        pre, curr = tail.next, head
        while pre != tail:
            curr.next, pre, curr = pre, curr, curr.next
        return tail, head


if __name__ == '__main__':
    test_input = [1, 2, 3, 4, 5]
    test_k = 3
    test_head = construct_test_head(test_input)

    print_list_node(test_head)
    ret = Solution().reverseKGroup(test_head, test_k)
    print_list_node(ret)
