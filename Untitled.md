{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2d09b71b-7fe2-4946-9b14-6ea5ddeef1ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Blackjack!\n",
      "Your hand:\n",
      "4 of Diamonds\n",
      "3 of Clubs\n",
      "Dealer's hand:\n",
      "7 of Hearts\n",
      "Unknown card\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to hit or stand?  hit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your hand:\n",
      "4 of Diamonds\n",
      "3 of Clubs\n",
      "4 of Spades\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to hit or stand?  hit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your hand:\n",
      "4 of Diamonds\n",
      "3 of Clubs\n",
      "4 of Spades\n",
      "9 of Spades\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to hit or stand?  stand\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dealer's turn:\n",
      "Dealer hits.\n",
      "Dealer's hand:\n",
      "7 of Hearts\n",
      "8 of Clubs\n",
      "3 of Diamonds\n",
      "You win!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']\n",
    "ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']\n",
    "\n",
    "card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,\n",
    "               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}\n",
    "\n",
    "class Blackjack:\n",
    "    def __init__(self):\n",
    "        self.deck = [(rank, suit) for rank in ranks for suit in suits]\n",
    "        random.shuffle(self.deck)\n",
    "\n",
    "    def deal_card(self):\n",
    "        return self.deck.pop()\n",
    "\n",
    "    def calculate_score(self, hand):\n",
    "        score = sum(card_values[card[0]] for card in hand)\n",
    "        num_aces = sum(1 for card in hand if card[0] == 'Ace')\n",
    "\n",
    "        while score > 21 and num_aces:\n",
    "            score -= 10\n",
    "            num_aces -= 1\n",
    "\n",
    "        return score\n",
    "\n",
    "    def display_hand(self, hand):\n",
    "        for card in hand:\n",
    "            print(f\"{card[0]} of {card[1]}\")\n",
    "\n",
    "    def play_game(self):\n",
    "        print(\"Welcome to Blackjack!\")\n",
    "\n",
    "        player_hand = [self.deal_card(), self.deal_card()]\n",
    "        dealer_hand = [self.deal_card(), self.deal_card()]\n",
    "\n",
    "        print(\"Your hand:\")\n",
    "        self.display_hand(player_hand)\n",
    "        print(\"Dealer's hand:\")\n",
    "        print(f\"{dealer_hand[0][0]} of {dealer_hand[0][1]}\")\n",
    "        print(\"Unknown card\")\n",
    "\n",
    "        if self.calculate_score(player_hand) == 21:\n",
    "            print(\"Blackjack! You win!\")\n",
    "            return\n",
    "\n",
    "        while True:\n",
    "            choice = input(\"Do you want to hit or stand? \").lower()\n",
    "            if choice == 'hit':\n",
    "                player_hand.append(self.deal_card())\n",
    "                print(\"Your hand:\")\n",
    "                self.display_hand(player_hand)\n",
    "                score = self.calculate_score(player_hand)\n",
    "                if score > 21:\n",
    "                    print(\"Bust! Dealer wins!\")\n",
    "                    return\n",
    "            elif choice == 'stand':\n",
    "                break\n",
    "            else:\n",
    "                print(\"Invalid choice. Please enter 'hit' or 'stand'.\")\n",
    "\n",
    "        print(\"Dealer's turn:\")\n",
    "        while self.calculate_score(dealer_hand) < 17:\n",
    "            dealer_hand.append(self.deal_card())\n",
    "            print(\"Dealer hits.\")\n",
    "\n",
    "        print(\"Dealer's hand:\")\n",
    "        self.display_hand(dealer_hand)\n",
    "\n",
    "        player_score = self.calculate_score(player_hand)\n",
    "        dealer_score = self.calculate_score(dealer_hand)\n",
    "\n",
    "        if dealer_score > 21:\n",
    "            print(\"Dealer busts! You win!\")\n",
    "        elif player_score > dealer_score:\n",
    "            print(\"You win!\")\n",
    "        elif player_score < dealer_score:\n",
    "            print(\"Dealer wins!\")\n",
    "        else:\n",
    "            print(\"It's a tie!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    game = Blackjack()\n",
    "    game.play_game()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a75cafa4-6dd3-440d-a00a-f0cf8240e673",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
