class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])

    def __repr__(self):
        return f"{[card for card in self.cards]}"

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        hand_value = sum([card.rank for card in self.cards]) % 10
        return hand_value

    def arashi(self):
        if len(self.cards) < 3:
            return False
        return self.cards[0].rank == self.cards[1].rank == self.cards[2].rank

    def kuppin(self):
        if len(self.cards) == 2:
            return (self.cards[0].rank == 9 and self.cards[1].rank == 1) \
                or (self.cards[0].rank == 1 and self.cards[1].rank == 9)
        return False

    def shippin(self):
        if len(self.cards) == 2:
            return (self.cards[0].rank == 4 and self.cards[1].rank == 1) \
                or (self.cards[0].rank == 1 and self.cards[1].rank == 4)
        return False

    def calculate_hand(self, dealer):
        # To be able to evaluate winning hand shippin has fictional value of 10,
        # kuppin has fictional value of 11 and arashi has value increased by 12.
        if self.arashi():
            return "arashi", 12 + self.calculate_value()
        if self.kuppin() and dealer:
            return "kuppin", 11
        if self.shippin() and not dealer:
            return "shippin", 10
        return "regular", self.calculate_value()
