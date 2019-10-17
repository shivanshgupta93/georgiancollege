"""Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

The Deck class should have a deal method to deal two cards from the deck one for the user and one for the opponent (computer) 
After the cards are dealt, tell the user which one is bigger or if they are equal say WAR, then remove the cards from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

"""

import random
from random import shuffle

class Card:  
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.cardvalue = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.deck = []
    
    def shuffledeck(self):
        for suit in self.suits:
            for card in self.cardvalue:
                self.deck.append((suit, card,))
                
        shuffle(self.deck)


class Deck(Card):
    
    def __init__(self):
        Card.__init__(self)
        self.shuffledeck()
    
    def deal(self):
        
        card_dic ={'A':1, 'J':11, 'Q':12, 'K':13}
        
        print("Before")
        print(len(self.deck))
        
        user_card = random.choice(self.deck)
        self.deck.remove(user_card)
        ####print(user_card)
        
        dealer_card = random.choice(self.deck)
        self.deck.remove(dealer_card)
        #####print(dealer_card)
        
        print("After")
        print(len(self.deck))
        
        ####print(card_dic[user_card[1]])
        
        user = card_dic.get(user_card[1],user_card[1])
        ####print(user)
        dealer = card_dic.get(dealer_card[1], dealer_card[1])
        ####print(dealer)
        
        if int(user) == int(dealer):
            print("WAR: Customer got %s of %s &\nDealer got %s of %s" %(user_card[1],user_card[0],dealer_card[1],dealer_card[0]))
        elif int(user) > int(dealer):
            print("Cutomer Won: Customer got %s of %s &\nDealer got %s of %s" %(user_card[1],user_card[0],dealer_card[1],dealer_card[0]))
        elif int(user) < int(dealer):
            print("Dealer Won: Customer got %s of %s &\nDealer got %s of %s" %(user_card[1],user_card[0],dealer_card[1],dealer_card[0]))

    def card_shuffle(self):
        
        Card.__init__(self)
        self.shuffledeck()
        
if __name__ == '__main__':
    deal_count = 0
    
    deckobj = Deck()
    
    while True:
        user_input = input("Please select the option below: \n1. Deal\n2. Shuffle\n3. Exit\n")
        
        if deal_count >= 26:
            deckobj.card_shuffle()
            deal_count = 0
            
        if user_input.upper() == "DEAL" or user_input == 1:
            deckobj.deal()   
            deal_count += 1
            
        if user_input.upper() == "SHUFFLE" or user_input == 2:
            deckobj.card_shuffle()
                
        if user_input.upper() == "EXIT":
            break
        