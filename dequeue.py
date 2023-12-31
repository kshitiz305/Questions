#question



# Have the function GraphChallenge(strArr) take strArr which will be an array of strings which models a non-looping Graph. The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) in the array as a string. The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes. They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.
#
# An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the first Node to the last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. Also, the connection A-B for example, means that A can get to B and B can get to A.

#####

from collections import deque

def GraphChallenge(strArr):
    num_nodes = int(strArr[0])
    nodes = strArr[1:num_nodes+1]
    edges = [tuple(edge.split('-')) for edge in strArr[num_nodes+1:]]

    graph = {node: [] for node in nodes}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    start, end = nodes[0], nodes[-1]
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return '-'.join(path)
        for next_node in graph[node]:
            if next_node not in path:
                queue.append((next_node, path + [next_node]))

    return -1
