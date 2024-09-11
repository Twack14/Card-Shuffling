import random

## Create Card Object
class Card:

    # initialize Card object
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank
        self.__card_name = f"{self.__rank} of {self.__suit}"
    
    # return card suit & rank
    def get_card_name(self):
        return self.__card_name

class Deck:

    #List of Suits and Ranks
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9" ,"10" ,"Jack" ,"Queen", "King"]

    #initialize shuffled Deck object
    def __init__(self):
        self.__removed_cards = [] 
        self.__final_deck = self.create_deck()
        print(self.__final_deck)
        self.shuffle_deck()
        
    #create list of card objects
    def create_deck(self):
        print("Creating Initial Deck..\n")
        self.__deck = []
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank)
                self.__deck.append(card.get_card_name())
        return self.__deck
    
    #shuffle current deck
    def shuffle_deck(self):
        print("\nShuffling Deck...\n")
        random.shuffle(self.__final_deck)
        print(self.__final_deck)
    
    def draw(self, n):
        print(f"\nDrawing {n} cards from top of deck...\n")
        self.__removed_cards = self.__final_deck[0:n]
        del self.__final_deck[0:n]
        print(self.__removed_cards)
        print(f"\n{len(self.__final_deck)} Cards Remaining in Deck: \n")
        print(self.__final_deck)
    
    def placeBottom(self, card):
        chosen = self.__final_deck.pop(card)
        print(f"\nSelected {chosen} at index {card}\n")
        print(f"Moving {chosen} to bottom of deck...\n")
        self.__final_deck.append(chosen)
        print(self.__final_deck)
    
    def placeTop(self, card):
        chosen = self.__final_deck.pop(card)
        print(f"\nSelected {chosen} at index {card}\n")
        print(f"Moving {chosen} to top of deck...\n")
        self.__final_deck.insert(0, chosen)
        print(self.__final_deck)

        

#initalize deck instance, create deck, shuffle deck, draw 3 cards, move chosen card to bottom, move chosen card to top.
deck = Deck()
deck.shuffle_deck()
deck.draw(3)
deck.draw(6)
deck.placeBottom(4)
deck.placeTop(10)




