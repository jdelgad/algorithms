RED = 0
BLACK = 1


class Node(object):
    color = BLACK
    key = None
    left = None
    right = None
    parent = None

    def __init__(self, key):
        self.key = key


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def insert(self, z=Node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
        z.left = None
        z.right = None
        z.color = RED
        self.__insert_fixup(z)

    def __insert_fixup(self, z=Node):
        while z.parent is not None and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.__rotate_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.__rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y is not None and y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.__rotate_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.__rotate_left(z.parent.parent)
        self.root.color = BLACK

    def __rotate_left(self, x=Node):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    def __rotate_right(self, x=Node):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, key):
        z = self.find(key)
        if z is None:
            return

        if z.left is None or z.right is None:
            y = z
        else:
            y = self.__tree_successor(z)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left:
                 y.parent.left = x
            else:
                y.parent.right = x

        if y != z:
            z.key = y.key
        if y.color == BLACK:
            self.__delete_fixup(x)

    def __tree_successor(self, x):
        if x.right is not None:
            return self.__tree_minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def __tree_minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def __delete_fixup(self, x):
        while x is not None and x != self.root and x.color == BLACK:
            if x == x.parent.right:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.__rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.__rotate_right(w)
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.__rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.__rotate_right(w)
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.__rotate_left(x.parent)
                    x = self.root
        if x is not None:
            x.color = BLACK

    def find(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            if key > node.key:
                node = node.right
            else:
                node = node.left
        return node
