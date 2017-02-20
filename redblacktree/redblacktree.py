RED = 0
BLACK = 1


class Node(object):
    def __init__(self, key):
        self.color = BLACK
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


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
                    y.color = BLACK #same as above
                    z.parent.parent.color = RED
                    z = z.parent.parent  #noop
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
