from itertools import permutations

with open('Day9.txt') as f:
    datas = f.readlines()
f.closed
dist1 = {(s.strip().split()[0], s.strip().split()[2]):int(s.strip().split()[4]) for s in datas}
dist2 = {(s.strip().split()[2], s.strip().split()[0]):int(s.strip().split()[4]) for s in datas}
dist = dist1 | dist2
loc1 = set([pair[0] for pair in dist1.keys()])
loc2 = set([pair[0] for pair in dist2.keys()])
loc = loc1.union(loc2)

# part 1
def distance(trip):
    res = 0
    for i in range(len(trip) - 1):
        res += dist[trip[i],trip[i+1]]
    return res


def part1():
    # print(dist)
    # print(loc)
    d_min = 1e10
    d_max = 0
    for trip in permutations(loc):
        d = distance(trip)
        if d < d_min:
            d_min = d
            # print("min: ", d_min, d, trip)
        if d > d_max:
            d_max = d
            # print("max: ", d_max, d, trip)
    print("min : ", d_min)
    print("max : ", d_max)

part1()
