from timeFunc import timeit

T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

tests = [T0, T1, T2, T3, T4, T5, T6, T7]


def lcsRecursive(seq1, seq2, index1=0, index2=0):
    if index1 == len(seq1) or index2 == len(seq2):
        return 0
    elif seq1[index1] == seq2[index2]:
        return 1 + lcsRecursive(seq1, seq2, index1 + 1, index2 + 1)
    else:
        leftNode = lcsRecursive(seq1, seq2, index1 + 1, index2)
        rightNode = lcsRecursive(seq1, seq2, index1, index2 + 1)
        return max(leftNode, rightNode)


# MEMOIZED VERSION OF LCS
def memoryLCS(seq1, seq2):
    memory = {}

    def recurse(index1, index2):
        key = (index1, index2)
        if key in memory:
            return memory[key]
        elif index1 == len(seq1) or index2 == len(seq2):
            memory[key] = 0
        elif seq1[index1] == seq2[index2]:
            memory[key] = 1 + recurse(index1 + 1, index2 + 1)
        else:
            memory[key] = max(recurse(index1 + 1, index2), recurse(index1, index2 + 1))
        return memory[key]

    return recurse(0, 0)


@timeit
def dynamicLCS(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])

    return table[-1][-1]


@timeit
def getDynamicLCSValue(i):
    return dynamicLCS(tests[i]['input']['seq1'], tests[i]['input']['seq2'])


@timeit
def getMemoryLCSValue(i):
    return memoryLCS(tests[i]['input']['seq1'], tests[i]['input']['seq2'])


@timeit
def getLCSValue(i):
    return lcsRecursive(tests[i]['input']['seq1'], tests[i]['input']['seq2'])


def printLCSRecursive():
    for i in range(len(tests)):
        print('EDGE CASE #', i)
        dynamicLCSValue = getDynamicLCSValue(i)
        lcsValue = getLCSValue(i)
        memoryLCSValue = getMemoryLCSValue(i)
        print('longest common subsequence: ', dynamicLCSValue)
        print('did it pass: ', dynamicLCSValue == tests[i]['output'], '\n')


# -------------------------------------------------------------------------------------------------
# KNAPSACK Problem

# inputs:
# 1. weights: list of numbers containing weights
# 2. profits: list of numbers containing profits (same length as weights)
# 3. capacity: maxmimum weight allowed

# outputs:
# 1. maximum profits: max profit obitained by selecting weights with optimized profits for the given capacity

test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}

tests2 = [test0, test1, test2, test3, test4, test5]


def maxProfitsRecursive(weights, profits, capacity, index=0):
    if index >= len(weights):
        return 0

    if weights[index] > capacity:
        return maxProfitsRecursive(weights, profits, capacity, index + 1)
    else:
        didntPickWeight = maxProfitsRecursive(weights, profits, capacity, index + 1)
        pickedTheWeight = profits[index] + maxProfitsRecursive(weights, profits, capacity - weights[index], index + 1)
        return max(didntPickWeight, pickedTheWeight)


def memoryMaxProfits(weights, profits, capacity1):
    memory = {}

    def recurse(capacity, index):
        key = (capacity, index)
        if key in memory:
            return memory[key]
        elif index == len(weights):
            memory[key] = 0
        elif weights[index] > capacity:
            memory[key] = recurse(capacity, index + 1)
        else:
            memory[key] = max(recurse(capacity, index + 1), profits[index] + recurse(capacity - weights[index], index + 1))
        return memory[key]

    return recurse(capacity1, 0)


def dynamicMaxProfits(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(n):
        for c in range(1, capacity+1):
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], profits[i] + table[i][c-weights[i]])
    return table[-1][-1]

@timeit
def getDynamicMaxProfits(i):
    return dynamicMaxProfits(tests2[i]['input']['weights'], tests2[i]['input']['profits'], tests2[i]['input']['capacity'])


@timeit
def getMemoryMaxProfits(i):
    return memoryMaxProfits(tests2[i]['input']['weights'], tests2[i]['input']['profits'], tests2[i]['input']['capacity'])


@timeit
def getMaxProfitsValue(i):
    return maxProfitsRecursive(tests2[i]['input']['weights'], tests2[i]['input']['profits'],
                               tests2[i]['input']['capacity'])


def printMaxProfitsRecursive():
    for i in range(len(tests2)):
        print('EDGE CASE #', i)
        dynamicMaxProfits = getDynamicMaxProfits(i)
        memoizedMaxProfits = getMemoryMaxProfits(i)
        maxProfits = getMaxProfitsValue(i)
        print('max profits: ', dynamicMaxProfits)
        print('did it pass? ', dynamicMaxProfits == tests2[i]['output'], '\n')
