import math
from binaryTrees import insert
from binaryTrees import TreeNode
from binaryTrees import displayKeys
import binaryTrees
from linBinSearch import LinBinSearch

# linSearch = LinBinSearch().printLinSearch()
# binSearch = LinBinSearch().printBinSearch()

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

# bstTree = binaryTrees.BSTNode('jade')
bstTree = insert(None, 'jade')
insert(bstTree, 'ben')
insert(bstTree, 'son')
insert(bstTree, 'ali')
insert(bstTree, 'hesh')
insert(bstTree, 'sam')
insert(bstTree, 'zach')
displayKeys(bstTree)
node = binaryTrees.findNode(bstTree, 'zach')
print(binaryTrees.listAll(bstTree))
print(node.key)
binTree = TreeNode.parseTuple(tree_tuple)


displayKeys(binTree)
print(binTree.traverseInOrder())
print(binTree.traversePreOrder())
print(binTree.isBST())
