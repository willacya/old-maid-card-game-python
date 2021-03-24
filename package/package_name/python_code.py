class Card:
    
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    
    # print out card rank and suit
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
    
   # compare cards
    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0
    
    
    def __eq__(self, other): # ie. a == b
        return self.cmp(other) == 0

    def __le__(self, other): # ie. a <= b
        return self.cmp(other) <= 0

    def __ge__(self, other): # ie. a >= b
        return self.cmp(other) >= 0

    def __gt__(self, other): # ie. a > b
        return self.cmp(other) > 0

    def __lt__(self, other): # ie. a < b
        return self.cmp(other) < 0

    def __ne__(self, other): # ie. a != b
        return self.cmp(other) != 0
    
class Deck:
    
    """"
    Populates a deck of cards by cycling through all 
    the cards in Card class.
    """"
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
                
    