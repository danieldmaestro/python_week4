from random import shuffle

# Card.VALUE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# define card class
class Card:
    SUIT = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUE = ["Ace", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit


    @property
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self._value
    
    @property
    def image_name(self):
        return str(self).replace(" ", "_") + ".png"

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def __repr__(self):
        return f"Card(face='{self.value}', suit='{self.suit}')"
    
    def __format__(self, format):
        return f"{str(self):{format}}"
    

# define deck class
class DeckOfCards:
    NUMBER_OF_CARDS = 52
    # initialise class with 52 cards
    def __init__(self):
        self._current_card = 0
        self._deck = [Card(Card.VALUE[count % 13], Card.SUIT[count // 13]) for count in range(DeckOfCards.NUMBER_OF_CARDS)]

        # for count in range(DeckOfCards.NUMBER_OF_CARDS):
        #     self._deck.append(Card(Card.VALUE[count % 13], Card.SUIT[count // 13]))
        # list comprehension method
        # cards = [Card(s,v) for s in suit for v in value]
        # self.all_cards = cards

    def __repr__(self):
        return f"Deck of {self.count()} cards."
# counts all cards in the deck
    def count(self):
        return len(self._deck)

# shuffle deck but only if deck has 52 cards
    def shuffle(self):
        self._current_card = 0
        shuffle(self._deck)
    
    def split_deck(self):
        mid_index = DeckOfCards.NUMBER_OF_CARDS // 2
        one_half, second_half = self._deck[:mid_index], self._deck[mid_index:]
        return [one_half, second_half]
    
    def __str__(self):
        s = ""
        for index,card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'

        return s


class Hand:
    def __init__(self, half_deck):
        self.hand = half_deck

    def count(self):
        return len(self.hand)
    
    def add_card(self, card):
        self.hand.insert(0, card)

    def remove_card(self):
        c = self.hand.pop()
        return c

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def hand_count(self):
        return self.hand.count()

# GAMEPLAY

print("Welcome to War. Let's begin")
player = input("You are Player 1. Type in your name to start the game: ")

d = DeckOfCards()
d.shuffle()
print(d)
p1_hand = Hand(d.split_deck()[0])
p2_hand = Hand(d.split_deck()[1])
p1 = Player(player, p1_hand)
p2 = Player("Skynet", p2_hand)

while p1.hand_count() > 0 and p2.hand_count() > 0:
    p1_temp = []
    p2_temp = []
    p1_temp.append(p1_hand.remove_card())
    print(f"{p1.name}'s card is - ", p1_temp[0])
    p2_temp.append(p2_hand.remove_card())
    print(f"{p2.name}'s card is - ", p2_temp[0])


    if Card.VALUE.index(p1_temp[0].value) == Card.VALUE.index(p2_temp[0].value):
        print("WAR!!!!!!!!!")
        p1_temp.append(p1_hand.remove_card())
        print(f"{p1.name}'s card is - ", p1_temp[-1])
        p2_temp.append(p2_hand.remove_card())
        print(f"{p2.name}'s card is - ", p2_temp[-1])

        while Card.VALUE.index(p1_temp[-1].value) == Card.VALUE.index(p2_temp[-1].value):
            p1_temp.append(p1_hand.remove_card())
            print(f"{p1.name}'s card is - ", p1_temp[-1])
            p2_temp.append(p2_hand.remove_card())
            print(f"{p2.name}'s card is - ", p2_temp[-1])
        
        if Card.VALUE.index(p1_temp[-1].value) > Card.VALUE.index(p2_temp[-1].value):
            p1_temp.append(p1_hand.remove_card())
            p2_temp.append(p2_hand.remove_card())

            for card in p1_temp:
                p1_hand.add_card(card)
            for card in p2_temp:
                p1_hand.add_card(card)
            
            print(p1.name, "has", p1.hand_count(), "cards left")
            print(p2.name, "has", p2.hand_count(), "cards left")
            print(p1.name, "wins this battle.")
        else:
            p1_temp.append(p1_hand.remove_card())
            print(f"{p1.name}'s card is - ", p1_temp[-1])
            p2_temp.append(p2_hand.remove_card())
            print(f"{p2.name}'s card is - ", p2_temp[-1])

            for card in p1_temp:
                p2_hand.add_card(card)
            for card in p2_temp:
                p2_hand.add_card(card)
            
            
            print(p1.name, "has", p1.hand_count(), "cards left")
            print(p2.name, "has", p2.hand_count(), "cards left")
            print(p2.name, "wins this battle.")

    elif Card.VALUE.index(p1_temp[0].value) > Card.VALUE.index(p2_temp[0].value):
        p1_hand.add_card(p1_temp[0])
        p1_hand.add_card(p2_temp[0])
        print(p1.name, "has", p1.hand_count(), "cards left")
        print(p2.name, "has", p2.hand_count(), "cards left")
        print(p1.name, "wins this battle.")

    else:
        p2_hand.add_card(p1_temp[0])
        p2_hand.add_card(p2_temp[0])
        print(p1.name, "has", p1.hand_count(), "cards left")
        print(p2.name, "has", p2.hand_count(), "cards left")
        print(p2.name, "wins this battle.")


if p1.hand_count() > p2.hand_count():
    print(f"Congratulations, {p1.name}. You win the game.")
else:
    print(f"Congratulations, {p2.name}. You win the game.")
    












