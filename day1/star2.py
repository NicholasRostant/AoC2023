
with open("./day1/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]


def processline(line:str)->int:
    digits = [char for char in line if char.isnumeric()]
    # print(f"{line} {(digits[0] + digits[-1])}")
    return (digits[0] + digits[-1])

def texttodigit(line:str)->str:
    digitdict = {"zero":"0",
                 "one":"1",
                 "two":"2",
                 "three":"3",
                 "four":"4",
                 "five":"5",
                 "six":"6",
                 "seven":"7",
                 "eight":"8",
                 "nine":"9"}
    for digit in digitdict:
        line = str.translate(line,digitdict)
        # line = line.replace(digit,str(digitdict[digit]))

    return(line)

for i in input:
    print(f"{i} -> {texttodigit(i)} -> {processline(texttodigit(i))}")
results = sum([int(processline(texttodigit(i))) for i in input])

print(results)