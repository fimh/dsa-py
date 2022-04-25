"""
Question:   Valid Parentheses
Difficulty: Easy
Link:       https://leetcode.com/problems/valid-parentheses/
Ref:        https://leetcode-cn.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in mapping:  # if c in mapping.values():
                stack.append(c)
            else:
                if not stack or mapping[c] != stack.pop():
                    return False
        return not stack


if __name__ == '__main__':
    test_input = "([[[]]])"
    ret = Solution().isValid(test_input)
    print(test_input, ret)
    pass
