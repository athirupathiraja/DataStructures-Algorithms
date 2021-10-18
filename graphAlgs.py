numNodes1 = 5
edges1 = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]



class Graph:
    def __init__(self, numNodes, edges):
        self.numNodes = numNodes,
        self.data = [[] for _ in range(numNodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return '\n'.join(['{}: {}'.format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

    def addEdge(self, edge):
        n1, n2 = edge
        if n1 >= len(self.data):
            self.data.extend([[n2]])
            self.data[n2].append(n1)
        elif n2 >= len(self.data):
            self.data.extend([[n1]])
            self.data[n1].append(n2)
        else:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def removeEdge(self, edge):
        n1, n2 = edge
        self.data[n1].remove(n2)
        self.data[n2].remove(n1)


graph1 = Graph(numNodes1, edges1)


def breadthFirstSearch(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True
    distance[root] = 0
    queue.append(root)
    index = 0

    while index < len(queue):
        currentNode = queue[index]
        index += 1

        for nextNode in graph.data[currentNode]:
            if not discovered[nextNode]:
                distance[nextNode] = 1 + distance[currentNode]
                parent[nextNode] = currentNode
                queue.append(nextNode)
                discovered[nextNode] = True

    return queue, distance, parent


def depthFirstSearch(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:

        currentNode = stack.pop()

        if not discovered[currentNode]:
            discovered[currentNode] = True
            result.append(currentNode)
            for nextNode in graph.data[currentNode]:
                if not discovered[nextNode]:
                    stack.append(nextNode)

    return result


class GraphWithWeights:
    def __init__(self, numNodes, edges, directed=False, weighted=False):
        self.numNodes = numNodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(numNodes)]
        self.weight = [[] for _ in range(numNodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)

            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ''
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += '{}: {}\n'.format(i, list(zip(nodes, weights)))
            return result
        else:
            for i, nodes in enumerate(self.data):
                result += '{}: {}\n'.format(i, nodes)
            return result


graph2 = GraphWithWeights(num_nodes5, edges5, weighted=True)
graph3 = GraphWithWeights(num_nodes6, edges6, directed=True)
graph4 = GraphWithWeights(num_nodes7, edges7, weighted=True, directed=True)


def updateDistances(graph, current, distance, parent=None):
    neighbors = graph.data[current]
    weights = graph.weight[current]

    for i, nextNode in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[nextNode]:
            distance[nextNode] = distance[current] + weight
            if parent:
                parent[nextNode] = current


def pickNextUnvisitedNode(distance, visited):
    minDistance = float('inf')
    minNode = None

    for node in range(len(distance)):
        if not visited[node] and distance[node] < minDistance:
            minDistance = distance[node]
            minNode = node
    return minNode


def shortestPath(graph, startingNode, targetNode):
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None]*len(graph.data)
    queue = []

    distance[startingNode] = 0
    visited[startingNode] = True
    queue.append(startingNode)
    index = 0

    while index < len(queue) and not visited[targetNode]:
        currentNode = queue[index]


        # update the distances of the neighbors
        updateDistances(graph, currentNode, distance, parent)

        # get the next node
        nextNode = pickNextUnvisitedNode(distance, visited)
        if nextNode is not None:
            # if the next node exits, enqueue it
            visited[nextNode] = True
            queue.append(nextNode)
        index += 1

    return distance[targetNode], distance, parent


def printDepthFirstSearch():
    print(depthFirstSearch(graph1, 3))


def printBreadthFirstSearch():
    print(breadthFirstSearch(graph1, 3))


def printShortestDistance():
    print('shortest distance for graph 4 from node 0 to node 5:', shortestPath(graph4, 0, 5))


def printGraph():
    print(graph4)
    print(graph3)
    print(graph2)
    # print(graph1)
