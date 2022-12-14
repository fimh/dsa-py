"""
Question:   Valid Anagram
Difficulty: Easy
Link:       https://leetcode.com/problems/valid-anagram/
Ref:        https://leetcode-cn.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""
import heapq
from queue import PriorityQueue
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}
        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        for c in t:
            dict2[c] = dict2.get(c, 0) + 1
        return dict1 == dict2

    def isAnagram3(self, s: str, t: str) -> bool:
        dict1 = {}
        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        for c in t:
            new_c = dict1.get(c, 0) - 1
            if new_c > 0:
                dict1[c] = new_c
            elif new_c == 0:
                dict1.pop(c)
            else:
                return False
        return not dict1


if __name__ == '__main__':
    test_s = "anagram"
    test_t = "nagaram"
    ret = Solution().isAnagram3(test_s, test_t)
    print(ret)
