
with open("./day4/input.txt", 'r') as f:
    input = f.readlines()
    input = [i.strip() for i in input]

class Card():
    def __init__(self, input:str):
        self.id = int(input.split(':')[0].split()[1])
        self.winning = input.split(':')[1].strip().split('|')[0].strip().split(' ')
        self.owned = input.split(':')[1].strip().split('|')[1].strip().split(' ')

    def score(self) -> int:
        score = 0
        for num in self.winning:
            if num in self.owned and num != ' ' and num != '':
                if score == 0:
                    score = 1
                else:
                    score = score + 1
        return score

cards = [Card(i) for i in input]
indexed_cards = {card.id: card for card in cards}
total = 0

def process_cards(card_list):
    cards = card_list
    for card in cards:
        global total 
        total = total + 1
        score = card.score()
        if score != 0:
            for i in range(1,score+1,1):
                copy_card = indexed_cards.get(card.id+i)
                cards.append(copy_card)

process_cards(cards)
print(total)
