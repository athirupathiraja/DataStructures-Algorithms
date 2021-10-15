def displayKeys(node, space='\t', level=0):
    # if node is empty
    if node is None:
        print(space * level + '∅')
        return

    # if node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    displayKeys(node.right, space, level + 1)
    print(space * level + str(node.key))
    displayKeys(node.left, space, level + 1)


def insert(node, key):
    if node is None:
        node = BSTNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key)
        node.right.parent = node
    return node


def listAll(node):
    if node is None:
        return []
    else:
        return listAll(node.left) + [node.key] + listAll(node.right)


def findNode(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return findNode(node.left, key)
    if key > node.key:
        return findNode(node.right, key)


def updateNode(node, key, updatedKey):
    targetNode = findNode(node, key)
    if targetNode is not None:
        targetNode.key = updatedKey


class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        else:
            return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        else:
            return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    @staticmethod
    def parseTuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parseTuple(data[0])
            node.right = TreeNode.parseTuple(data[2])
        else:
            node = TreeNode(data)
        return node

    def traverseInOrder(self):
        if self is None:
            return []
        else:
            return TreeNode.traverseInOrder(self.left) + [self.key] + TreeNode.traverseInOrder(self.right)

    def traversePreOrder(self):
        if self is None:
            return []
        else:
            return [self.key] + TreeNode.traversePreOrder(self.left) + TreeNode.traversePreOrder(self.right)

    def removeNone(nums):
        return [x for x in nums if x is not None]

    def isBST(self):
        if self is None:
            return True, None, None

        isBstL, minL, maxL = TreeNode.isBST(self.left)
        isBstR, minR, maxR = TreeNode.isBST(self.right)

        isBSTNode = (isBstL and isBstR and (maxL is None or self.key > maxL) and (maxR is None or self.key < minR))

        min_key = min(TreeNode.removeNone([minL, self.key, minR]))
        max_key = max(TreeNode.removeNone([maxL, self.key, maxR]))

        return isBSTNode, min_key, max_key


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
