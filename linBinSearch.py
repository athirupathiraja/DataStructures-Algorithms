



class LinBinSearch:
    def linearSearch(self, query):
        # Create a variable position with the value 0
        position = 0
        print('self: ', self)
        print('query:', query)

        while position < len(self):
            if self[position] == query:
                print('position: ')
                return position
            position += 1
        return -1

    def binarySearch(self, query):
        low, high = 0, len(self) - 1

        while low <= high:
            midpoint = (high + low) // 2
            midNumber = self[midpoint]

            print('lowerBound: ', low, ' upperBound: ', high, ' midpoint: ', midpoint, 'numberAtMidpoint: ', midpoint)

            # NOTE: self array is in descending order:
            if midNumber == query and self[midpoint - 1] != query:
                print('position: ')
                return midpoint
            elif midNumber < query or (midNumber == query and self[midpoint - 1]):
                high = midpoint - 1
            elif midNumber > query:
                low = midpoint + 1

        return -1

    test = {
        'input': {
            'self': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    }

    tests = []

    # Edge cases:
    tests.append(test)

    tests.append({
        'input': {
            'self': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    })

    # query is the first element
    tests.append({
        'input': {
            'self': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    })

    # query is the last element
    tests.append({
        'input': {
            'self': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    })

    # self contains just one element, query
    tests.append({
        'input': {
            'self': [6],
            'query': 6
        },
        'output': 0
    })

    # self does not contain query
    tests.append({
        'input': {
            'self': [9, 7, 5, 2, -9],
            'query': 4
        },
        'output': -1
    })

    # self is empty
    tests.append({
        'input': {
            'self': [],
            'query': 7
        },
        'output': -1
    })

    # numbers can repeat in self
    tests.append({
        'input': {
            'self': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    })

    # query occurs multiple times
    tests.append({
        'input': {
            'self': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
        },
        'output': 2
    })

    @staticmethod
    def printBinSearch():
        print('BINARY SEARCH')
        for x in range(len(LinBinSearch.tests)):
            print('Test Case #', x)
            print(LinBinSearch.binarySearch(LinBinSearch.tests[x]['input']['self'],
                                            LinBinSearch.tests[x]['input']['query']), '\n')

    @staticmethod
    def printLinSearch():
        print('LINEAR SEARCH')
        for x in range(len(LinBinSearch.tests)):
            print('Test Case #', x)
            print(
                LinBinSearch.linearSearch(LinBinSearch.tests[x]['input']['self'],
                                          LinBinSearch.tests[x]['input']['query']),
                '\n')


