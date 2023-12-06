with open("./day1/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]


class NumberGroup(object):
    def __init__(self,line_num:int,start_col:int,end_col:int):
        self.line_num = line_num
        self.start_col = start_col
        self.end_col = end_col


def process_line(line):
    for 