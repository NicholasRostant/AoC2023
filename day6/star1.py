import functools
with open("./day6/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]


def possible_finishes(time:int, distance:int) -> int:
    times = 0
    for i in range(0, time+1, 1):
        # For each possible button hold
        attempt = i*(time-i)
        if attempt > distance:
            times = times+1
    return times

times = input[0].split()[1:]
distances = input[1].split()[1:]
races = list(zip(times,distances))

finishes = [possible_finishes(int(i[0]), int(i[1])) for i in races]
score = functools.reduce(lambda x,y: x*y,finishes)
print(score)