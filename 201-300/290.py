"""
Question:   Word Pattern
Difficulty: Easy
Link:       https://leetcode.com/problems/word-pattern/
Ref:        https://xiaozhuanlan.com/topic/6345907812

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a
single space.

"""


class Solution1:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        Time - O(n^2), Space - O(n)
        We use a map to store the unique pattern-str couple. The following two cases denote the input
        is not a full match,
        1). If we find a new pattern with existing value
        2). If we find an existing pattern with new value

        :param pattern:
        :param str:
        :return:
        """

        # pre-processing and initial checking
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False

        lookup = {}
        for i in range(len(str_list)):
            if pattern[i] not in lookup:
                # check whether str_list[i] has already occurred in values or not
                # this will take O(n) since lookup.values is a list
                if str_list[i] in lookup.values():
                    return False
                lookup[pattern[i]] = str_list[i]
            elif lookup[pattern[i]] != str_list[i]:
                return False

        return True


class Solution2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        Time - O(n), Space - O(n)
        We use a map to store the unique pattern-str couple. The following two cases denote the input
        is not a full match,
        1). If we find a new pattern with existing value
        2). If we find an existing pattern with new value
        For case 1, we can exploit a set to achieve O(1) time for searching operation

        :param pattern:
        :param str:
        :return:
        """

        # pre-processing and initial checking
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False

        lookup = {}
        values = set()
        for i in range(len(str_list)):
            if pattern[i] not in lookup:
                # check whether str_list[i] has already occurred in values or not
                # this will take O(1) since values is a set
                if str_list[i] in values:
                    return False
                values.add(str_list[i])
                lookup[pattern[i]] = str_list[i]
            elif lookup[pattern[i]] != str_list[i]:
                return False

        return True


class Solution3:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        Time - O(n), Space - O(n)
        If str has the same pattern with pattern, the number of unique compounds of str and pattern should be equal to
        that of str and pattern respectively.

        :param pattern:
        :param str:
        :return:
        """

        # pre-processing and initial checking
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False

        compound = set()
        p = set()
        v = set()
        for i in range(len(str_list)):
            compound.add((pattern[i], str_list[i]))
            p.add(pattern[i])
            v.add(str_list[i])
        return len(p) == len(compound) and len(v) == len(compound)


if __name__ == '__main__':
    pattern = 'abba'
    str = 'dog cat cat dog'
    print(Solution3().wordPattern(pattern, str))
