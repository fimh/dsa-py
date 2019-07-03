from tree.tree_node import TreeNode


class BinaryTreeTraversal(object):

    @staticmethod
    def pre_order(root: TreeNode):
        if root is None:
            return

        print(root.val, end=' ')
        BinaryTreeTraversal.pre_order(root.left)
        BinaryTreeTraversal.pre_order(root.right)

    @staticmethod
    def in_order(root: TreeNode):
        if root is None:
            return

        BinaryTreeTraversal.in_order(root.left)
        print(root.val, end=' ')
        BinaryTreeTraversal.in_order(root.right)

    @staticmethod
    def post_order(root: TreeNode):
        if root is None:
            return

        BinaryTreeTraversal.post_order(root.left)
        BinaryTreeTraversal.post_order(root.right)
        print(root.val, end=' ')

    @staticmethod
    def level_order(root: TreeNode):
        if root is None:
            return
        arr = [root]
        while len(arr) != 0:
            node = arr.pop(0)
            print(node.val, end=' ')

            if node.left is not None:
                arr.append(node.left)
            if node.right is not None:
                arr.append(node.right)

    @staticmethod
    def height(root: TreeNode):
        if root is None:
            return 0
        else:
            # compute the height of each subtree
            l_height = BinaryTreeTraversal.height(root.left)
            r_height = BinaryTreeTraversal.height(root.right)

            # return the larger one
            return max(l_height, r_height) + 1


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
    print('pre-order:', end='\t\t')
    BinaryTreeTraversal.pre_order(a)

    print('\nin-order:', end='\t\t')
    BinaryTreeTraversal.in_order(a)

    print('\npost-order:', end='\t\t')
    BinaryTreeTraversal.post_order(a)

    print('\nlevel-order:', end='\t')
    BinaryTreeTraversal.level_order(a)

    print('\nheight:', end='\t')
    print(BinaryTreeTraversal.height(a))
