raw_datas = """
Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.
"""
raw_datas = raw_datas.strip().split("\n")
# print(raw_datas)
datas = [[line.split()[0], int(line.split()[3]), int(line.split()[6]), int(line.split()[13])] for line in raw_datas]
# print(datas)
total_time = 2503


# part1
def distance(total_time, speed, flight_time, rest_time):
    step_time = flight_time + rest_time
    steps = total_time // step_time
    bonus = min(total_time % step_time, flight_time)
    return (steps * flight_time + bonus) * speed

def part1():
    distances = {}
    for animal in datas:
        distances[animal[0]] = distance(total_time, animal[1], animal[2], animal[3])
    print(max(distances), distances)


# part2
def part2():
    tot_time = 2503
    distances = {animal[0]:[0] for animal in datas}
    # print(distances)
    for animal in datas:
        time = 0
        dist = 0
        speed = animal[1]
        flight_time = animal[2]
        rest_time = animal[3]
        while time < tot_time+1:
            steps = min(flight_time, tot_time+1-flight_time)
            for _ in range(steps):
                time += 1
                dist += speed
                distances[animal[0]].append(dist)
            steps = min(tot_time+1-time, rest_time)
            distances[animal[0]] += steps*[dist]
            time += steps
    # print(distances)
    reverse_distances = [{animal[0]:distances[animal[0]][i] for animal in datas} for i in range(tot_time+1)]
    # print(distances, reverse_distances)
    points = {animal[0]:0 for animal in datas}
    for i in range(1, tot_time+1):
        # print("\n", i, "\t", end="")
        max_distance = max(reverse_distances[i].values())
        for key, val in reverse_distances[i].items():
            if val == max_distance:
                # print(key, points[key], end = '\t')
                points[key] += 1
    # print(points)
    print("part2: ", max(points.values()))



# part1()
part2()
