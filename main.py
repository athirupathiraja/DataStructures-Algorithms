import math
from graphAlgs import printGraph
from graphAlgs import printShortestDistance
from graphAlgs import printBreadthFirstSearch
from graphAlgs import printDepthFirstSearch


from recursiveNDynamic import printLCSRecursive
from recursiveNDynamic import printMaxProfitsRecursive
from sorting import printBubbleSort
from sorting import printMergeSort
from sorting import printNotebooks


from hashNDictionaries import HashTableWithProbing

from binaryTrees import insert
from binaryTrees import TreeNode
from binaryTrees import displayKeys
from binaryTrees import Users
import binaryTrees

from linBinSearch import LinBinSearch



# printDepthFirstSearch()
printGraph()
printShortestDistance()
# printBreadthFirstSearch()
# -------------------------------------------------------------------------------------------------
# printLCSRecursive()
# printMaxProfitsRecursive()

# -------------------------------------------------------------------------------------------------
# printMergeSort()
# printBubbleSort()
# printNotebooks()
# -------------------------------------------------------------------------------------------------
# HASH TABLES

# probingHashTable = HashTableWithProbing()
#
# # inserting & checking for a value in hash table using key value pair
# probingHashTable.insert('listen', 99)
# print(probingHashTable.find('listen') == 99)
#
# # inserting a COLLIDING key and checking if linear probing worked
# probingHashTable.insert('silent', 200)
# print(probingHashTable.find('listen') == 99 and probingHashTable.find('silent') == 200)
#
# # updating a value in a key and checking for it
# probingHashTable.update('listen', 100)
# print(probingHashTable.find('listen') == 100)

# -------------------------------------------------------------------------------------------------
# BINARY TREES
# Regular Binary trees

# # parsing tuples
# tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
# # creating a tree using tuples
# binTree = TreeNode.parseTuple(tree_tuple)
# displayKeys(binTree)
# # traversing the binary tree
# print(binTree.traverseInOrder())
# print(binTree.traversePreOrder())
# print(binTree.isBST())
#
# # Binary Search Trees:
#
# # creating key-value pairs
# jade = Users('jade', 'Jade H', 'jade@example.com')
# ben = Users('ben', 'Ben S', 'ben@example.com')
# son = Users('son', 'Son J', 'son@example.com')
# ali = Users('ali', 'Ali S', 'ali@example.com')
# hesh = Users('hesh', 'Hesh A', 'hesh@example.com')
# sam = Users('sam', 'Sam G', 'sam@example.com')
# zach = Users('zach', 'Zach B', 'zach@example.com')
# tan = Users('tan', 'Tan M', 'tan@example.com')
#
# # array of key-value pairs
# users = [ali, ben, hesh, jade, sam, son, zach]
# dataArray = [(user.key, user) for user in users]
# # making a balanced tree from the array
# bstTree1 = binaryTrees.makeBalancedBST(dataArray)
# displayKeys(bstTree1)
# print(binaryTrees.listAll(bstTree1))
#
# # inserting each key-value to a tree: NOTE- the order of insertion is import to make it balanced
# bstTree2 = insert(None, jade.key, jade)
# insert(bstTree2, hesh.key, hesh)
# insert(bstTree2, ben.key, ben)
# insert(bstTree2, ali.key, ali)
# insert(bstTree2, zach.key, zach)
# insert(bstTree2, sam.key, sam)
# insert(bstTree2, son.key, son)
# insert(bstTree2, tan.key, tan)
# displayKeys(bstTree2)
#
# # balancing the bst if the order of insertion is not correct
# bstTree2 = binaryTrees.balanceAnBST(bstTree2)
# displayKeys(bstTree2)
# node = binaryTrees.findNode(bstTree2, zach.key)
# print(binaryTrees.isBalanced(bstTree2))
# print(binaryTrees.listAll(bstTree2))
# print(node.key)


# -------------------------------------------------------------------------------------------------
# LINEAR AND BINARY SEARCH

# linSearch = LinBinSearch().printLinSearch()
# binSearch = LinBinSearch().printBinSearch()
