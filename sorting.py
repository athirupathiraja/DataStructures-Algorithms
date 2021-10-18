import random

# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

# An empty list
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

# a really long list
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]


def bubbleSort(nums):
    nums = list(nums)

    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


def insertionSort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j + 1, cur)
    return nums


def printBubbleSort():
    for x in range(len(tests)):
        print('TEST CASE # ', x)
        print(bubbleSort(tests[x]['input']['nums']), '\n')


def mergeSort(nums, depth=0):
    print('  ' * depth, 'mergeSort:', nums)
    if len(nums) <= 1:
        return nums
    # finding the middle index
    midIndex = len(nums) // 2

    # splitting nums into two arrays
    left = nums[:midIndex]
    right = nums[midIndex:]

    # merge sorting each of the arrays
    leftSorted, rightSorted = mergeSort(left, depth + 1), mergeSort(right, depth + 1)

    sortedNums = merge(leftSorted, rightSorted, depth + 1)
    return sortedNums


def merge(nums1, nums2, depth=0):
    print('  ' * depth, 'merge:', nums1, nums2)
    mergedList = []

    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        # sorting logic to append the new list mergedList
        if nums1[i] <= nums2[j]:
            mergedList.append(nums1[i])
            i += 1
        else:
            mergedList.append(nums2[j])
            j += 1

    # adding the tailing values in each both of the arrays must do this step because if either the left or right
    # array runs out of elements, the rest of the elements in the other array were not added
    nums1Tail = nums1[i:]
    nums2Tail = nums2[j:]

    return mergedList + nums1Tail + nums2Tail


def printMergeSort():
    print(mergeSort(tests[1]['input']['nums']), '\n')
    # for x in range(len(tests)):
    #     print('TEST CASE # ', x)
    #     print(bubbleSort(tests[x]['input']['nums']), '\n')


def quickSort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        #finds the pivoting index, which is the last element of nums in this case
        pivotIndex = partition(nums, start, end)
        quickSort(nums, start, pivotIndex - 1)
        quickSort(nums, pivotIndex + 1, end)

    return nums


def partition(nums, start, end):
    if end is None:
        end = len(nums) - 1  # pivot is the last element in this case

    l, r = start, end - 1

    # partitioning the elements in two arrays with with left array containing elements less than pivot and right array
    # containing the greater elements
    while r > l:
        if nums[l] >= nums[end]:
            l += 1
        elif nums[r] <= nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]

    # adding the pivot into the final partitioned array
    if nums[l] >= nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


# -------------------------------------------------------------------------------------------------
# answer to Jovian question: sorting objects with merge sort
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)


nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)
notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]


def customCompare(x, y):
    if x > y:
        return 'greater'
    elif x < y:
        return 'less'
    else:
        return 'equal'


def customMergeSort(objs, compare=customCompare):
    if len(objs) <= 1:
        return objs

    midIndex = len(objs) // 2

    return customMerge(customMergeSort(objs[:midIndex], compare), customMergeSort(objs[midIndex:], compare), compare)


def customMerge(objs1, objs2, compare=customCompare):
    mergedList = []

    i, j = 0, 0

    while i < len(objs1) and j < len(objs2):

        if compare(objs1[i], objs2[j]) == 'less' or compare(objs1[i], objs2[j]) == 'equal':
            mergedList.append(objs1[i])
            i += 1
        else:
            mergedList.append(objs2[j])
            j += 1

    return mergedList + objs1[i:] + objs2[j:]


def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'less'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'


sortedNotebooks = customMergeSort(notebooks, compare_likes)


def printNotebooks():
    print(sortedNotebooks)
