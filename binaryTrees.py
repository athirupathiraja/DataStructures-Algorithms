class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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
