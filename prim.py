"""The first task is basically Prim's algorithm for minimum spanning tree"""
with open('in.txt') as f:
    n = f.readline()  # adjacency list is NxN
    graph = f.read()
f.closed
n = int(n)

graph_matrix = [[None for _ in range(n)]
                for _ in range(n)]  # initialize a list

for row, line in enumerate(graph.split('\n')):  # parse the file
    for col, val in enumerate(line.split(' ')):
        graph_matrix[row][col] = int(val)

# Prim's algorithm starts here

# this list will be used for representing adjacency list for output
result = [[] for _ in range(n)]
T = set()
X = set()
sum_spt = 0  # sum of all edges in spanning tree
X.add(0)
while len(X) != n:
    crossing = set()
    for x in X:
        for k in range(n):
            # 32767 means there is no edge
            if k not in X and graph_matrix[x][k] != 32767:
                crossing.add((x, k))
    # sort edges and choose the shortest one
    edge = sorted(crossing, key=lambda e: graph_matrix[e[0]][e[1]])[0]
    result[edge[0]].append(edge[1]+1)  # forming adjacency list
    result[edge[1]].append(edge[0]+1)
    # sum of all edges in spanning tree
    sum_spt += graph_matrix[edge[0]][edge[1]]
    T.add(edge)
    X.add(edge[1])

for item in result:  # required format of output
    item.sort()
result = [[i+1] + result[i] + [0]
          for i in range(len(result))]  # required format of output

# print(*result)
# print(sum_spt)

with open('out.txt', 'w') as out:
    for item in result:
        out.write(' '.join(map(str, item)))
        out.write('\n')
    out.write(str(sum_spt))
