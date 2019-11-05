import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __lt__(self, other):
        return ranks.index(self.get_rank()) < ranks.index(other.get_rank())

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_two_pair(self):
        count = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    count = count + 1

        if count >= 2:
            return True
        else:
            return False

    def three_of_kind(self):
        count = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    count = count + 1

        if count >= 3:
            return True
        else:
            return False

    def is_straight(self):
        self.cards.sort()

        if self.cards[0].get_rank() == "2" and \
                self.cards[1].get_rank() == "3" and \
                self.cards[2].get_rank() == "4" and \
                self.cards[3].get_rank() == "5" and \
                self.cards[4].get_rank() == "A":
            return True

        for i in range(4):
            if ranks.index(self.cards[i].get_rank()) + 1 != ranks.index(self.cards[i + 1].get_rank()):
                return False
        return True

    def is_flush(self):
        suit = self.cards[0].get_suit()
        for i in range(1,5):
            if self.cards[i].get_suit() != suit:
                return False
        return True

    def full_house(self):
        count = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    count = count + 1

        if count == 4:
            return True
        else:
            return False

    def four_of_kind(self):
        self.cards.sort()
        count = 0
        if self.cards[1].get_rank() == self.cards[4].get_rank():
            return True
        elif self.cards[0].get_rank() == self.cards[3].get_rank():
            return True
        else:
            return False

    def straight_flush(self):
        if self.is_flush() and self.is_straight():
            return True
        else:
            return False


    def royal_straight(self):
        self.cards.sort()
        if self.cards[0].get_rank() == "10" and \
                self.cards[1].get_rank() == "J" and \
                self.cards[2].get_rank() == "Q" and \
                self.cards[3].get_rank() == "K" and \
                self.cards[4].get_rank() == "A":
            return True
        else:
            return False

    def royal_flush(self):
        if self.is_flush() and self.royal_straight():
            return True
        else:
            return False


pair = 0
two_pair = 0
three_of_kind = 0
straight = 0
flush = 0
full_house = 0
four_of_kind = 0
straight_flush = 0
royal_flush = 0

for i in range(10000):
    new_deck = Deck()
    new_deck.shuffle()
    hand = Hand(new_deck)
    if hand.is_pair():
        pair += 1
    if hand.is_two_pair():
        two_pair += 1
    if hand.three_of_kind():
        three_of_kind += 1
    if hand.is_straight():
        straight += 1
    if hand.is_flush():
        flush += 1
    if hand.full_house():
        full_house += 1
    if hand.four_of_kind():
        four_of_kind += 1
    if hand.straight_flush():
        straight_flush += 1
    if hand.royal_flush():
        royal_flush += 1

print("pairs: ", pair)
print("two pairs: ", two_pair)
print("three of kind ", three_of_kind)
print("straight ", straight)
print("flush ", flush)
print("full house ", full_house)
print("four of kind ", four_of_kind)
print("straight flush", straight_flush)
print("royal flush", royal_flush)
