
# ========== AUFGABE 1 ==========

class TreeNode(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def enumerate(self):
        pass   # write a generator here...

    def enumerate_first(self):
        pass   # write a generator here...

    def enumerate_last(self):
        pass   # write a generator here...


def test_tree1():
    tree1 = TreeNode(5, TreeNode(3, TreeNode(1, None,
                                                TreeNode(2, None,
                                                            None)),
                                    TreeNode(4, None,
                                                None)),
                        TreeNode(7, TreeNode(6, None,
                                                None),
                                    TreeNode(8, None,
                                                TreeNode(9, None,
                                                            None))))
    assert list(tree1.enumerate()) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(tree1.enumerate_first()) == [5, 3, 1, 2, 4, 7, 6, 8, 9]
    assert list(tree1.enumerate_last()) == [2, 1, 4, 3, 6, 9, 8, 7, 5]
