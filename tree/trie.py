class TrieNode:
    def __init__(self, data: str):
        self.data = data
        self.children = [None] * 26
        self.is_ending_char = False

    def __repr__(self):
        new_list = [c for c in self.children if c]
        # equivalent to the following expression using filter & lambda
        # new_list2 = list(filter(lambda x: x is not None, self.children))
        return "{} -> {} <- {}-{}".format(self.data, new_list,
                                          'ending' if self.is_ending_char else 'not-ending',
                                          self.data)


class Trie:
    """
    One application - auto completion.

    """

    def __init__(self):
        self._root = TrieNode('/')

    def insert(self, text: str) -> None:
        node = self._root
        for index, char in map(lambda x: (ord(x) - ord('a'), x), text):
            if not node.children[index]:
                node.children[index] = TrieNode(char)
            node = node.children[index]
        node.is_ending_char = True

    def find(self, pattern: str) -> bool:
        node = self._root
        for index in map(lambda x: ord(x) - ord('a'), pattern):
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_ending_char

    # FIXME get all strings starting with prefix
    # can we get a faster approach to get all strings with specified prefix instead of pre-order way?
    def find_with_prefix(self, prefix: str) -> None:
        node = self._root
        for index in map(lambda x: ord(x) - ord('a'), prefix):
            if not node.children[index]:
                return
            node = node.children[index]

        self._pre_order(node, 0)

    def _pre_order(self, node: TrieNode, level: int) -> None:
        if level != 0:
            print(node.data, end='')
        if node.is_ending_char:
            print()
            return

        children = [n for n in node.children if n]
        for n in children:
            self._pre_order(n, level + 1)


if __name__ == '__main__':
    strs = ['how', 'her', 'hi', 'hello', 'so', 'see']
    trie = Trie()
    for s in strs:
        trie.insert(s)

    for s in strs:
        print(s, trie.find(s))

    print()
    tar = 'swift'
    print(tar, trie.find(tar))

    prefix = 's'
    print('\nstart with {}:'.format(prefix))
    trie.find_with_prefix(prefix)
