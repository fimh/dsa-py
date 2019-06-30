from tree.tree_node import TreeNode


class BinaryTreeTraversal(object):

    def pre_order(self, root: TreeNode):
        if root is None:
            return

        print(root.val, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root: TreeNode):
        if root is None:
            return

        self.in_order(root.left)
        print(root.val, end=' ')
        self.in_order(root.right)

    def post_order(self, root: TreeNode):
        if root is None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val, end=' ')


if __name__ == '__main__':
    # construct a binary tree
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')

    b = TreeNode('b', d, e)
    c = TreeNode('c', f, g)

    a = TreeNode('a', b, c)

    # traverse the binary via different approaches
    print('pre-order:', end='\t')
    BinaryTreeTraversal().pre_order(a)

    print('\nin-order:', end='\t')
    BinaryTreeTraversal().in_order(a)

    print('\npost-order:', end='\t')
    BinaryTreeTraversal().post_order(a)
