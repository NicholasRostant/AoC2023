
with open("./day1/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]


def processline(line:str)->int:
    digits = [char for char in line if char.isnumeric()]
    return (digits[0] + digits[-1])

results = sum([int(processline(i)) for i in input])

print(results)