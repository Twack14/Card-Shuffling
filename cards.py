import random

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9" ,"10" ,"Jack" ,"Queen", "King"]
    
    def __init__(self):
        self.__cards = [] ## start with empty list
        print(f"Creating {len(self.__cards)} Deck...\n")
        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                card = rank + ' of ' + suit
                self.__cards.append(card)
        print(self.__cards)
        

    def shuffle_deck(self):
        print(f"\nShuffling card deck...\n")
        random.shuffle(self.__cards)
        print(self.__cards)
    
    def draw(self, n):
        print(f"Drawing {n} cards from the deck...\n")
        print(self.__cards[-n::])

#initalize deck instance, create deck, shuffle deck
deck = Deck()
#shuffle deck
deck.shuffle_deck()
deck.draw(3)

