
with open("./day4/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]

class Card():
    def __init__(self, input:str):
        self.id = input.split(':')[0]
        self.winning = input.split(':')[1].strip().split('|')[0].strip().split(' ')
        self.owned = input.split(':')[1].strip().split('|')[1].strip().split(' ')

    def score(self) -> int:
        score = 0
        for num in self.winning:
            if num in self.owned and num != ' ' and num != '':
                if score == 0:
                    score = 1
                else:
                    score = score*2
        return score

cards = [Card(i) for i in input]
print(sum([card.score() for card in cards]))