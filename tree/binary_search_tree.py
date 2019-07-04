from tree.tree_node import TreeNode
from tree.binary_tree_traversal import BinaryTreeTraversal


class BinarySearchTree:

    @staticmethod
    def find(tree: TreeNode, data):
        p = tree
        while p is not None:
            if data < p.val:
                p = p.left
            elif data > p.val:
                p = p.right
            else:
                return p

        return None

    @staticmethod
    def insert(tree: TreeNode, data):
        if tree is None:
            return TreeNode(data)

        p = tree
        if data > p.val:
            if p.right is None:
                p.right = TreeNode(data)
                return tree
            else:
                return BinarySearchTree.insert(p.right, data)
        else:  # data <= p.val
            if p.left is None:
                p.left = TreeNode(data)
                return tree
            else:
                return BinarySearchTree.insert(p.left, data)

    @staticmethod
    def insert_iterative(tree: TreeNode, data):
        if tree is None:
            return TreeNode(data)

        p = tree
        while p is not None:
            if data > p.val:
                if p.right is None:
                    p.right = TreeNode(data)
                    return tree
                else:
                    p = p.right
            else:  # data <= p.val
                if p.left is None:
                    p.left = TreeNode(data)
                    return tree
                else:
                    p = p.left

    @staticmethod
    def delete(tree: TreeNode, data):
        p = tree  # the node to be deleted
        pp = None  # the parent node of the node to be deleted
        # find target node
        while (p is not None) and p.val != data:
            pp = p
            if data > p.val:
                p = p.right
            else:
                p = p.left

        if p is None:  # cannot find the target node
            return tree

        # if the target node has two children nodes
        if (p.left is not None) and (p.right is not None):
            # find the smallest node min_p in right sub tree
            # or we can use the largest node in left sub tree
            min_p = p.right
            min_pp = p
            while min_p.left is not None:
                min_pp = min_p
                min_p = min_p.left

            # copy min_p's value into p, then we delete node min_p
            p.val = min_p.val
            p = min_p
            pp = min_pp

        # if the target node only has one or zero child node
        child = None  # the child node of the target node
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right

        if pp is None:
            tree = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

        return tree


if __name__ == '__main__':
    # construct a binary tree
    m_19 = TreeNode(19)
    n_27 = TreeNode(27)
    o_55 = TreeNode(55)

    h_15 = TreeNode(15)
    i_17 = TreeNode(17)
    j_25 = TreeNode(25, m_19, n_27)
    k_51 = TreeNode(51, right=o_55)
    l_66 = TreeNode(66)

    d_13 = TreeNode(13, right=h_15)
    e_18 = TreeNode(18, i_17, j_25)
    f_34 = TreeNode(34)
    g_58 = TreeNode(58, k_51, l_66)

    b_16 = TreeNode(16, d_13, e_18)
    c_50 = TreeNode(50, f_34, g_58)

    a_33 = TreeNode(33, b_16, c_50)

    BinaryTreeTraversal.level_order(a_33)

    BinarySearchTree.delete(a_33, 13)
    BinaryTreeTraversal.level_order(a_33)

    BinarySearchTree.delete(a_33, 18)
    BinaryTreeTraversal.level_order(a_33)

    BinarySearchTree.delete(a_33, 55)
    BinaryTreeTraversal.level_order(a_33)
