class StringSearching:
    """
    String-searching algorithms, sometimes called string-matching algorithms, are an important
    class of string algorithms that try to find a place where one or several strings (also called
    patterns) are found within a larger string or text.

    Algorithms: Brute-force, RK (Rabin-Karp), ...

    """

    @staticmethod
    def bf(ori: str, pattern: str) -> int:
        """
        Brute Force algorithm for string searching.
        For details, refer to str.find() method

        :param ori: the original string
        :param pattern: the substring we want to find in original string
        :return: the lowest index in string ori where substring pattern is found, otherwise -1
        """

        n = len(ori)
        m = len(pattern)

        if n <= m:
            return 0 if pattern == ori else -1

        # use nested loops to find the string pattern
        for i in range(n - m + 1):
            for j in range(m):
                if ori[i + j] == pattern[j]:
                    if j == m - 1:
                        return i
                    else:
                        continue
                else:
                    break

        return -1

    @staticmethod
    def rk(ori: str, pattern: str) -> int:
        """
        RK (Rabin-Karp) algorithm for string searching.
        For details, refer to str.find() method

        :param ori: the original string
        :param pattern: the substring we want to find in original string
        :return: the lowest index in string ori where substring pattern is found, otherwise -1
        """

        n = len(ori)
        m = len(pattern)

        if n <= m:
            return 0 if pattern == ori else -1

        # hash values for all substrings in string ori
        hashes_ori = [0] * (n - m + 1)
        hashes_ori[0] = StringSearching._simple_hash(ori, 0, m)
        for i in range(1, n - m):
            hashes_ori[i] = hashes_ori[i - 1] - \
                            StringSearching._simple_hash(ori, i - 1, i) + \
                            StringSearching._simple_hash(ori, i + m - 1, i + m)

        # hash value for pattern string
        hash_p = StringSearching._simple_hash(pattern, 0, m)

        # compare hash values
        for i, h in enumerate(hashes_ori):
            # in case of hash collision
            if h == hash_p and pattern == ori[i:i + m]:
                return i

        return -1

    @staticmethod
    def _simple_hash(s: str, start: int, end: int):
        """
        Calculate the hash value of the given string s via the summation of each character's
        unicode code point.

        :param s:
        :param start: start index of the given string s, inclusive
        :param end: end index of the given string s, exclusive
        :return: the hash value of the given string s
        """

        assert start <= end - 1

        h = 0
        for c in s[start:end]:
            h += ord(c)  # ord - return the unicode code point for the given character

        return h


if __name__ == '__main__':
    import time

    print('time consume:')
    o_str = 'a' * 10000
    p_str = 'a' * 200 + 'b'

    t = time.process_time()
    print('[bf] result', StringSearching.bf(o_str, p_str))
    print('[bf] time cost: {0:.4}s'.format(time.process_time() - t))

    t = time.process_time()
    print('[rk] result', StringSearching.rk(o_str, p_str))
    print('[rk] time cost: {0:.4}s'.format(time.process_time() - t))

    print('\nsearch')
    o_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'thelazy'
    print('[bf] result', StringSearching.bf(o_str, p_str))
    print('[rk] result', StringSearching.rk(o_str, p_str))
