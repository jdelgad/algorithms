import unittest
from redblacktree.redblacktree import Node, RedBlackTree, RED, BLACK


class TestRedBlackTree(unittest.TestCase):
    def test_insert_three_nodes(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        rbtree.insert(Node(2))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)
        self.assertEqual(rbtree.root.left.key, 2)
        self.assertEqual(rbtree.root.right.color, RED)
        self.assertEqual(rbtree.root.right.key, 4)
        self.assertEqual(rbtree.root.right.color, RED)

    def test_insert_three_nodes_rebalance_left(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(4))
        rbtree.insert(Node(3))
        rbtree.insert(Node(2))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)
        self.assertEqual(rbtree.root.left.key, 2)
        self.assertEqual(rbtree.root.right.color, RED)
        self.assertEqual(rbtree.root.right.key, 4)
        self.assertEqual(rbtree.root.right.color, RED)

    def test_insert_three_nodes_rebalance_right(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(2))
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)
        self.assertEqual(rbtree.root.left.key, 2)
        self.assertEqual(rbtree.root.right.color, RED)
        self.assertEqual(rbtree.root.right.key, 4)
        self.assertEqual(rbtree.root.right.color, RED)

    def test_insert_four_nodes(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(2))
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        rbtree.insert(Node(1))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)

        # children
        self.assertEqual(rbtree.root.left.key, 2)
        self.assertEqual(rbtree.root.right.color, BLACK)
        self.assertEqual(rbtree.root.right.key, 4)
        self.assertEqual(rbtree.root.right.color, BLACK)

        # grandchildren
        self.assertEqual(rbtree.root.left.left.key, 1)
        self.assertEqual(rbtree.root.left.left.color, RED)

    def test_insert_five_nodes(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(2))
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        rbtree.insert(Node(1))
        rbtree.insert(Node(0))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)

        # children
        self.assertEqual(rbtree.root.left.key, 1)
        self.assertEqual(rbtree.root.right.color, BLACK)
        self.assertEqual(rbtree.root.right.key, 4)
        self.assertEqual(rbtree.root.right.color, BLACK)

        # grandchildren
        self.assertEqual(rbtree.root.left.left.key, 0)
        self.assertEqual(rbtree.root.left.left.color, RED)
        self.assertEqual(rbtree.root.left.right.key, 2)
        self.assertEqual(rbtree.root.left.right.color, RED)

    def test_insert_seven_nodes(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(2))
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        rbtree.insert(Node(1))
        rbtree.insert(Node(0))
        rbtree.insert(Node(5))
        rbtree.insert(Node(6))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)

        # children
        self.assertEqual(rbtree.root.left.key, 1)
        self.assertEqual(rbtree.root.right.color, BLACK)
        self.assertEqual(rbtree.root.right.key, 5)
        self.assertEqual(rbtree.root.right.color, BLACK)

        # grandchildren - left
        self.assertEqual(rbtree.root.left.left.key, 0)
        self.assertEqual(rbtree.root.left.left.color, RED)
        self.assertEqual(rbtree.root.left.right.key, 2)
        self.assertEqual(rbtree.root.left.right.color, RED)

        # grandchildren - right2
        self.assertEqual(rbtree.root.right.left.key, 4)
        self.assertEqual(rbtree.root.right.left.color, RED)
        self.assertEqual(rbtree.root.right.right.key, 6)
        self.assertEqual(rbtree.root.right.right.color, RED)

    def test_insert_eight_nodes(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(2))
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        rbtree.insert(Node(1))
        rbtree.insert(Node(0))
        rbtree.insert(Node(5))
        rbtree.insert(Node(6))
        rbtree.insert(Node(7))
        self.assertEqual(rbtree.root.key, 3)
        self.assertEqual(rbtree.root.color, BLACK)

        # children
        self.assertEqual(rbtree.root.left.key, 1)
        self.assertEqual(rbtree.root.left.color, BLACK)
        self.assertEqual(rbtree.root.right.key, 5)
        self.assertEqual(rbtree.root.right.color, RED)

        # grandchildren - left
        self.assertEqual(rbtree.root.left.left.key, 0)
        self.assertEqual(rbtree.root.left.left.color, RED)
        self.assertEqual(rbtree.root.left.right.key, 2)
        self.assertEqual(rbtree.root.left.right.color, RED)

        # grandchildren - right
        self.assertEqual(rbtree.root.right.left.key, 4)
        self.assertEqual(rbtree.root.right.left.color, BLACK)
        self.assertEqual(rbtree.root.right.right.key, 6)
        self.assertEqual(rbtree.root.right.right.color, BLACK)
        # great grandchildren - right-right
        self.assertEqual(rbtree.root.right.right.right.key, 7)
        self.assertEqual(rbtree.root.right.right.right.color, RED)

    def test_insert_ten_nodes(self):
        rbtree = RedBlackTree()
        rbtree.insert(Node(2))
        rbtree.insert(Node(3))
        rbtree.insert(Node(4))
        rbtree.insert(Node(1))
        rbtree.insert(Node(0))
        rbtree.insert(Node(5))
        rbtree.insert(Node(6))
        rbtree.insert(Node(7))
        rbtree.insert(Node(8))
        rbtree.insert(Node(9))
        self.assertEqual(rbtree.root.key, 5)
        self.assertEqual(rbtree.root.color, BLACK)

        # children
        self.assertEqual(rbtree.root.left.key, 3)
        self.assertEqual(rbtree.root.left.color, RED)
        self.assertEqual(rbtree.root.right.key, 7)
        self.assertEqual(rbtree.root.right.color, RED)

        # grandchildren - left
        self.assertEqual(rbtree.root.left.left.key, 1)
        self.assertEqual(rbtree.root.left.left.color, BLACK)
        self.assertEqual(rbtree.root.left.right.key, 4)
        self.assertEqual(rbtree.root.left.right.color, BLACK)
        # grandchildren - left-left
        self.assertEqual(rbtree.root.left.left.left.key, 0)
        self.assertEqual(rbtree.root.left.left.left.color, RED)
        self.assertEqual(rbtree.root.left.left.right.key, 2)
        self.assertEqual(rbtree.root.left.left.right.color, RED)

        # grandchildren - right
        self.assertEqual(rbtree.root.right.left.key, 6)
        self.assertEqual(rbtree.root.right.left.color, BLACK)
        self.assertEqual(rbtree.root.right.right.key, 8)
        self.assertEqual(rbtree.root.right.right.color, BLACK)
        # great grandchildren - right-right
        self.assertEqual(rbtree.root.right.right.right.key, 9)
        self.assertEqual(rbtree.root.right.right.right.color, RED)


if __name__ == '__main__':
    unittest.main()
