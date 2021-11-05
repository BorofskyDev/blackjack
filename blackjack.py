from IPython.display import clear_output as os
import random

# Put card components in a tuple so that they don't change
# on accident while I'm debugging.
# Card face in a dictionary so I can access it.
# I think I could have done this as a module, but that's currently over my skillset
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    #used the method both Derek and Lucas taught to see what commands are available with each function. 
    #Saw that I could convert this to a string. Trying to get the cards to come out showing the suit and number just wasn't happening. Not sure if this is correct. 
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_structure = ''
        for card in self.deck:
            deck_structure += '\n ' + card.__str__()
        return "The deck has: " + deck_structure

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card
    
class Hand:
    def __init__(self):
        self.cards=[]
        self.value = 0 
    
    def deal_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
    
def hit(deck, hand):
    hand.deal_card(deck.deal())

def stand_or_hit(deck, hand):
    global playing 

    while True:
        ask = input("\n---->Enter 'h' to hit or enter 's' to stand: ")
        if ask.lower() == 'h':
            hit(deck, hand)
        elif ask.lower() == 's':
            print("It is now the Dealer's turn.")
            playing = False 
        else:
            print("\nThat is not a valid option. Please select 'h' or 's'.")
            continue 
        break 

#Can these be in their own class? If so, how? How would I init that? 
def show_partial_hand(player, dealer):
    print("\nDealer's Hand: ")
    print("_" * 20)
    print("---Card Hidden---")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    

def show_complete_hand(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand = ", player.value)

while True:
    print("=~=" * 25)
    print("Welcome to Joel's Blackjack Game: If it works, you might win.")
    print("=~=" * 25)

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.deal_card(deck.deal())
    player_hand.deal_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.deal_card(deck.deal())
    dealer_hand.deal_card(deck.deal())

    show_partial_hand(player_hand, dealer_hand)

    while playing:
        
        stand_or_hit(deck, player_hand)
        show_partial_hand(player_hand, dealer_hand)

        if player_hand.value > 21:
            print("-" * 20)
            print("You've busted!")
            print("-" * 20)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 18:
            hit(deck, dealer_hand)
        show_complete_hand(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            print("-" * 20)
            print("The dealer has busted!")
            print("-" * 20)

        elif dealer_hand.value > player_hand.value:
            print("-" * 20)
            print("The dealer has won the hand!")
            print("-" * 20)

        elif dealer_hand.value < player_hand.value:
            print("-" * 20)
            print("Congrats, you've won!")
            print("-" * 20)

        elif dealer_hand.value < player_hand.value:
            print("-" * 20)
            print("This hand is a push (a tie).")
            print("-" * 20)
        
        elif player_hand.value > 21:
            print("-" * 20)
            print("You've busted!")
            print("-" * 20)
    
    new_game = input("\n---------->Would you like to play again? Enter 'y' for 'Yes' or 'q' to 'Quit': ")
    if new_game.lower() == 'y':
        playing = True
        continue
    elif new_game.lower() == 'q':
        print("\nThank you for playing!")
        playing = False
        break
    else:
        print("\n----->Please enter 'n' or 'q,' no other option is acceptable. ")

# There's a glitch that I can't figure out where sometimes the program intially gives 3 cards instead of 2. Other than that, this works
# 