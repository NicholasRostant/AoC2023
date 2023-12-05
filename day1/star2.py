DIGITDICT = {"zero":"0",
                "one":"1",
                "two":"2",
                "three":"3",
                "four":"4",
                "five":"5",
                "six":"6",
                "seven":"7",
                "eight":"8",
                "nine":"9"}

with open("./day1/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]


def processline(line:str)->int:
    fline = texttodigit(line, False)
    rline = texttodigit(line, True)
    fdigits = [char for char in fline if char.isnumeric()]
    rdigits = [char for char in rline if char.isnumeric()]
    return (fdigits[0] + rdigits[-1])

def texttodigit(line:str, direction:bool)->str:
    # Process sequentially
    subline = ''
    if direction == False:
        for char in line:
            subline += char
            for digit in DIGITDICT:
                if digit in subline:
                    subline = subline.replace(digit, DIGITDICT[digit])
    else:
        for char in reversed(line):
            subline = char + subline
            for digit in DIGITDICT:
                if digit in subline:
                    subline = subline.replace(digit, DIGITDICT[digit])
      
    return subline

for i in input:
    print(f"{i} -> {texttodigit(i,False)} -> {texttodigit(i,True)} -> {processline(i)}")
    results = sum([int(processline(i)) for i in input])

print(results)