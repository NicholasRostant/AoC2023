R_THRESH = 12
G_THRESH = 13
B_THRESH = 14

with open("./day2/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]

class Game(object):
    def __init__(self, input:str):
        values = self.parse_input(input)
        self.id = values[0]
        self.max_r = values[1]
        self.max_g = values[2]
        self.max_b = values[3]

    def parse_input(self, input:str) -> tuple[int,int,int,int]:
        game_id = input.split(':')[0].split(' ')[-1].strip()
        game_steps = input.split(':')[1].split(';')
        r,g,b = 0,0,0
        for step in game_steps:
            moves = step.strip().split(';')
            for move in moves:
                pulls = move.strip().split(',')
                for pull in pulls:
                    colour = pull.strip().split(' ')[1].strip()
                    count = int(pull.strip().split(' ')[0].strip())
                    if colour == "red":
                        r = count if count > r else r
                    if colour == "green":
                        g = count if count > g else g
                    if colour == "blue":
                        b = count if count > b else b
        return ((game_id, r, g, b))
    
    def check_possible(self, r:int, g:int, b:int) -> bool:
        return(r >= self.max_r and
               g >= self.max_g and
               b >= self.max_b)
    
    def get_power(self) -> int:
        return (self.max_r * self.max_g * self.max_b)


games = [Game(i) for i in input]

print(sum([int(i.id) for i in games if i.check_possible(R_THRESH,G_THRESH,B_THRESH) == True]))
print(sum([i.get_power() for i in games]))
# print([f'{i.max_r} {i.max_g} {i.max_b}' for i in games])
        
    
