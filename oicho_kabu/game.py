import random


class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def _shuffle_deck(self):
        self.deck.shuffle()

    def _deal_one_card_to_each_player(self):
        for player in self.players:
            card = self.deck.remove_card()
            player.add_card(card)

    def _choose_dealer(self):
        dealer = self.players
        while len(dealer) > 1:
            d = {player: random.choice(self.deck.cards) for player in dealer}
            min_val = min(d.values())
            dealer = [key for key, value in d.items() if value == min_val]
        return dealer

    def _choose_new_dealer(self, dealer=None):
        i = self.players.index(dealer) if dealer else 1
        self.players = self.players[i:] + self.players[:i]

    def _calculate_player_hands(self):
        hand_values = [self.players[0].current_hand(dealer=True)]
        for player in self.players[1:]:
            hand_values.append(player.current_hand(dealer=False))
        return hand_values

    def _deal_third_card(self, hand_values):
        for index, value in enumerate(hand_values):
            if value[0] == "regular" and value[1] <= 3:
                card = self.deck.remove_card()
                self.players[index].add_card(card)
            # Computer player has 50% chance to draw third card if he has a choice
            elif value[0] == "regular" and value[1] < 7 and self.players[index].ai and random.choice([True, False]):
                card = self.deck.remove_card()
                self.players[index].add_card(card)

    def _ask_if_not_ai_player_wants_to_draw_third_card(self):
        for player in self.players:
            if not player.ai and len(player.hand) == 2:
                input_value = input("Do you want to draw the third card? [y/n] ")
                if input_value == "Y" or input_value == "y":
                    card = self.deck.remove_card()
                    player.add_card(card)

    def _print_player_names_and_their_hands(self):
        offset = 17
        print(f"{self.players[0].name} (dealer){(offset - len(self.players[0].name) - 9) * ' '}"
              f"{self.players[1].name}{(offset - len(self.players[1].name)) * ' '}"
              f"{self.players[2].name}{(offset - len(self.players[2].name)) * ' '}"
              f"{self.players[3].name}")
        print(f"{self.players[0].hand}{(offset - len(str(self.players[0].hand))) * ' '}"
              f"{self.players[1].hand}{(offset - len(str(self.players[1].hand))) * ' '}"
              f"{self.players[2].hand}{(offset - len(str(self.players[2].hand))) * ' '}"
              f"{self.players[3].hand}")

    def _determine_who_wins(self, hand_values):
        # Compare dealer hand with each player
        for i in range(1, 4):
            if hand_values[0][1] < hand_values[i][1]:
                return self.players[i]
        return self.players[0]

    def play(self):
        self._shuffle_deck()
        dealer = self._choose_dealer()[0]
        self._choose_new_dealer(dealer)
        self._deal_one_card_to_each_player()
        self._deal_one_card_to_each_player()
        self._print_player_names_and_their_hands()
        player_hands = self._calculate_player_hands()
        print(player_hands)
        self._deal_third_card(player_hands)
        self._ask_if_not_ai_player_wants_to_draw_third_card()
        self._print_player_names_and_their_hands()
        player_hands = self._calculate_player_hands()
        print(player_hands)
        winner = self._determine_who_wins(player_hands)
        print(f"{winner.name} won the game.")
