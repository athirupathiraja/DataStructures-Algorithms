import math


def linearSearch(cards, query):
    # Create a variable position with the value 0
    position = 0
    print('cards: ', cards)
    print('query:', query)

    while position < len(cards):
        if cards[position] == query:
            print('position: ')
            return position
        position += 1
    return -1


def binarySearch(cards, query):
    low, high = 0, len(cards) - 1


    while low <= high:
        midpoint = (high + low) // 2
        midNumber = cards[midpoint]

        print('lowerBound: ', low, ' upperBound: ', high, ' midpoint: ', midpoint, 'numberAtMidpoint: ', midpoint)

        # NOTE: cards array is in descending order:
        if midNumber == query and cards[midpoint-1] != query:
            print('position: ')
            return midpoint
        elif midNumber < query or (midNumber == query and cards[midpoint-1]):
            high = midpoint - 1
        elif midNumber > query:
            low = midpoint + 1

    return -1


test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests = []

# Edge cases:
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
print('LINEAR SEARCH')
for x in range(len(tests)):
    print('Test Case #', x)
    print(linearSearch(tests[x]['input']['cards'], tests[x]['input']['query']), '\n')

print('BINARY SEARCH')
for x in range(len(tests)):
    print('Test Case #', x)
    print(binarySearch(tests[x]['input']['cards'], tests[x]['input']['query']), '\n')
