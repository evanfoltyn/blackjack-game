#!/usr/bin/env python
# coding: utf-8

# In[26]:


import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Blackjack:
    def __init__(self):
        self.deck = [(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.deck)
        self.balance = 500
        self.bet = 0

    def deal_card(self):
        return self.deck.pop()

    def calculate_score(self, hand):
        score = sum(card_values[card[0]] for card in hand)
        num_aces = sum(1 for card in hand if card[0] == 'Ace')

        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1

        return score

    def display_hand(self, hand):
        for card in hand:
            print(f"{card[0]} of {card[1]}")

    def place_bet(self):
        while True:
            bet = int(input(f"Place your bet (balance: ${self.balance}): "))
            if bet > self.balance:
                print("Insufficient balance. Please enter a valid bet.")
            else:
                self.bet = bet
                break

    def play_game(self):
        print("Welcome to Blackjack!")

        while self.balance > 0:
            print(f"Your current balance: ${self.balance}")
            self.place_bet()

            player_hand = [self.deal_card(), self.deal_card()]
            dealer_hand = [self.deal_card(), self.deal_card()]

            print("Your hand:")
            self.display_hand(player_hand)
            print("Dealer's hand:")
            print(f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")
            print("Unknown card")

            # Check for dealer blackjack
            if self.calculate_score(dealer_hand) == 21:
                print("Dealer has blackjack! You lose!")
                self.balance -= self.bet
                continue

            # Check for player blackjack
            if self.calculate_score(player_hand) == 21:
                print("Blackjack! You win!")
                self.balance += self.bet
                continue

            # Player's turn
            score = self.calculate_score(player_hand)
            while score < 21:
                choice = input("Do you want to hit, stand, split, or double? ").lower()
                if choice == 'hit':
                    player_hand.append(self.deal_card())
                    print("Your hand:")
                    self.display_hand(player_hand)
                    score = self.calculate_score(player_hand)
                elif choice == 'stand':
                    break
                elif choice == 'split':
                    if player_hand[0][0] == player_hand[1][0]:
                        player_hand_1 = [player_hand[0], self.deal_card()]
                        player_hand_2 = [player_hand[1], self.deal_card()]
                        print("First hand:")
                        self.display_hand(player_hand_1)
                        print("Second hand:")
                        self.display_hand(player_hand_2)
                        self.play_hand(player_hand_1)
                        self.play_hand(player_hand_2)
                        break
                    else:
                        print("You cannot split your hand.")
                elif choice == 'double':
                    if self.balance >= self.bet * 2:
                        self.bet *= 2
                        player_hand.append(self.deal_card())
                        print("Your hand:")
                        self.display_hand(player_hand)
                        break
                    else:
                        print("Insufficient balance to double.")
                else:
                    print("Invalid choice. Please enter 'hit', 'stand', 'split', or 'double'.")

            if score == 21:
                print("Auto-stand: You have 21.")

            # Dealer's turn
            if score <= 21:
                print("Dealer's turn:")
                while self.calculate_score(dealer_hand) < 17:
                    dealer_hand.append(self.deal_card())
                    print("Dealer hits.")

                print("Dealer's hand:")
                self.display_hand(dealer_hand)

                # Determine winner
                player_score = self.calculate_score(player_hand)
                dealer_score = self.calculate_score(dealer_hand)

                if dealer_score > 21:
                    print("Dealer busts! You win!")
                    self.balance += self.bet
                elif player_score > dealer_score:
                    print("You win!")
                    self.balance += self.bet
                elif player_score < dealer_score:
                    print("Dealer wins!")
                    self.balance -= self.bet
                else:
                    print("It's a tie!")

        print("Game over! You are out of money.")

    def play_hand(self, hand):
        print("Playing hand:")
        self.display_hand(hand)
        score = self.calculate_score(hand)
        while score < 21:
            choice = input("Do you want to hit or stand? ").lower()
            if choice == 'hit':
                hand.append(self.deal_card())
                print("Your hand:")
                self.display_hand(hand)
                score = self.calculate_score(hand)
            elif choice == 'stand':
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

        if score == 21:
            print("Auto-stand: You have 21.")

if __name__ == "__main__":
    game = Blackjack()
    game.play_game()


# In[ ]:




