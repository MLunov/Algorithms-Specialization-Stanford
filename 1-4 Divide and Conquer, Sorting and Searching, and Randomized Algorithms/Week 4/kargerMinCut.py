import random, copy


def chooseRandomEdge(g):
    v1 = list(g.keys())[random.randint(0, len(g) - 1)]
    v2 = g[v1][random.randint(0, len(g[v1]) - 1)]
    return v1, v2


def contraction(g):
    v1, v2 = chooseRandomEdge(g)
    # removing the common edges (self-loops):
    g[v1] = [item for item in g[v1] if item != v2]
    g[v2] = [item for item in g[v2] if item != v1]
    # adding v2's adjacent vertices to v1:
    g[v1].extend(g[v2])
    # replacing all appearance of v2 as v1:
    for i in set(g[v2]):
        for j in range(0, len(g[i])):
            if g[i][j] == v2:
                g[i][j] = v1
    # removing v2's list:
    del g[v2]


def kargerMinCut(g):
    while len(g) > 2:
        contraction(g)
    return len(g[list(g.keys())[0]])


g = {}
# with open('sample.txt') as f:
with open('kargerMinCut.txt') as f:
    for l in f:
        items = list(map(int, l.split()))
        g[items[0]] = items[1:len(items)]

min_cut = kargerMinCut(copy.deepcopy(g))
# running several tests:
print('how many times to run a test:')
for i in range(int(input())):
    cut = kargerMinCut(copy.deepcopy(g))
    print('test {}:'.format(i + 1), cut)
    if cut < min_cut:
        min_cut = cut
print(("\nThe most likely min cut is {}").format(min_cut))

# assignment 4: the right answer is 17


# {1: [2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3]}
# (1, 2)
# {1: [3, 4, 3], 3: [1, 1, 4], 4: [1, 3]}
# (1, 3)
# {1: [4, 4], 4: [1, 1]}
#
#
# {1: [2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3]}
# (1, 2)
# {1: [3, 4, 3], 3: [1, 1, 4], 4: [1, 3]}
# (3, 4)
# {1: [3, 3, 3], 3: [1, 1, 1]}
