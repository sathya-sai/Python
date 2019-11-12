import random


class DeckOfCard:
    def __init__(self):
        self.cards = {"Clubs": [], "Diamond": [], "Hearts": [], "Spades": []}
        # initialising the cards
        self.suits = ["Clubs", "Diamond", "Hearts", "Spades"]
        # initialize number of suits in game
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        # initialising the rank of cards
        self.player1 = {"Clubs": [], "Diamond": [], "Hearts": [], "Spades": []}
        self.player2 = {"Clubs": [], "Diamond": [], "Hearts": [], "Spades": []}
        self.player3 = {"Clubs": [], "Diamond": [], "Hearts": [], "Spades": []}
        self.player4 = {"Clubs": [], "Diamond": [], "Hearts": [], "Spades": []}
        # initialising the players
        self.player = (self.player1, self.player2, self.player3, self.player4)

    def dec_card(self):
        count = 52
        # setting count as 36
        while count > 0:
            random_suit = self.suits[random.randrange(0, 4, 1)]
            # generating random suit no
            random_rank = self.rank[random.randrange(0, 13, 1)]
            # generating random rank no.
            temp = self.cards[random_suit]
            # taking random cards in temp variable
            flag = True
            # setting flag true
            for i in range(len(temp)):
                if temp[i] == random_rank:
                    flag = False
                    break

            if flag:
                # if flag is true
                self.cards[random_suit].append(random_rank)
                # count decrease
                count -= 1

    def deck_of_card_assign_to_players(self):
        count = 0
        # initialize count to zero
        for i in self.suits:
            temp = self.cards[i]
            # taking suits in temp variable
            for j in range(len(temp)):
                if count >= 4:
                    count = 0
                self.player[count][i].append(temp[j])
                # appending cards from suits to player
                count += 1
                # increasing count to one

    def player_card_display(self):
        # print the payers cards
        for i in range(len(self.player)):
            print("\n******** Player",i + 1,"*********")
            print("Clubs : ", self.player[i]["Clubs"])
            print("Diamond : ", self.player[i]["Diamond"])
            print("Hearts : ", self.player[i]["Hearts"])
            print("Spades : ", self.player[i]["Spades"])


if __name__ == "__main__":
    obj = DeckOfCard()
    obj.dec_card()
    obj.deck_of_card_assign_to_players()
    obj.player_card_display()
