import random

cards = []
card = """
{1} of {3}
 ________________________
|                        |
|  {2}                {2}    |
|                        |
|                        |
|                        |
|                        |
|           {0:>2}           |
|                        |
|                        |
|                        |
|                        |
|                        |
|  {2}                {2}    |
|                        |
|________________________|

"""

numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
symbols_names = ["hearts", "spades", "clubs", "diamonds"]
symbols = ['❤', '♠', '♣', '♦']
used_cards = []

while len(used_cards) < 52:
    num = random.randint(0, len(numbers)-1)
    sym = random.randint(0, len(symbols)-1)
    if not used_cards.__contains__((num, sym)):

        if numbers[num] == 'A':
            cards.append(card.format(
                'A', "Ace", symbols[sym], symbols_names[sym]))

        elif numbers[num] == 'J':
            cards.append(card.format(
                'J', "Jack", symbols[sym], symbols_names[sym]))

        elif numbers[num] == 'Q':
            cards.append(card.format(
                'Q', "Queen", symbols[sym], symbols_names[sym]))

        elif numbers[num] == 'K':
            cards.append(card.format(
                'K', "King", symbols[sym], symbols_names[sym]))

        else:
            cards.append(card.format(numbers[num], numbers[num],
                                     symbols[sym], symbols_names[sym]))

        used_cards.append((num, sym))

for i in range(52):
    input()
    random_card = random.randint(0, len(cards)-1)
    print(cards[random_card])
    cards.pop(random_card)
