class Player:
    def __init__(self, name, hand, ai):
        self.name = name
        self.hand = hand
        self.ai = ai

    def current_hand(self, dealer):
        return self.hand.calculate_hand(dealer)

    def add_card(self, card):
        self.hand.add_card(card)
