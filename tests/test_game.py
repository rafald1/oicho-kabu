import io
import unittest
from unittest.mock import MagicMock, call, patch

from oicho_kabu.card import Card
from oicho_kabu.game import Game


class GameTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_deck = MagicMock()
        self.mock_deck.cards = [Card(3), Card(1), Card(10), Card(9), Card(5)]
        self.mock_player1 = MagicMock()
        self.mock_player2 = MagicMock()
        self.mock_player3 = MagicMock()
        self.mock_player4 = MagicMock()
        self.mock_players = [self.mock_player1, self.mock_player2, self.mock_player3, self.mock_player4]
        self.game = Game(deck=self.mock_deck, players=self.mock_players)

    def test_if_game_has_deck_and_players(self):
        self.assertEqual(self.game.deck, self.mock_deck)
        self.assertEqual(self.game.players, self.mock_players)

    def test_if_game_shuffles_deck(self):
        self.game._shuffle_deck()
        self.mock_deck.shuffle.assert_called_once()

    def test_if_game_deals_one_card_to_each_player(self):
        card1 = MagicMock()
        card2 = MagicMock()
        card3 = MagicMock()
        card4 = MagicMock()
        self.mock_deck.remove_card.side_effect = [card1, card2, card3, card4]
        self.game._deal_one_card_to_each_player()
        self.mock_deck.remove_card.assert_has_calls([call(), call(), call(), call()])
        self.mock_player1.add_card.assert_has_calls([call(card1)])
        self.mock_player2.add_card.assert_has_calls([call(card2)])
        self.mock_player3.add_card.assert_has_calls([call(card3)])
        self.mock_player4.add_card.assert_has_calls([call(card4)])

    def test_if_dealer_is_chosen_correctly(self):
        dealer = self.game._choose_dealer()
        self.assertEqual(len(dealer), 1)
        self.assertIn(dealer[0], self.mock_players)

    def test_if_players_are_rearranged_and_a_new_dealer_is_chosen(self):
        self.game._choose_new_dealer()
        self.assertEqual(self.game.players[-1], self.mock_player1)

    def test_if_game_calculates_player_hands(self):
        self.game._calculate_player_hands()
        self.mock_player1.current_hand.assert_has_calls([call(dealer=True)])
        self.mock_player2.current_hand.assert_has_calls([call(dealer=False)])
        self.mock_player3.current_hand.assert_has_calls([call(dealer=False)])
        self.mock_player4.current_hand.assert_has_calls([call(dealer=False)])

    def test_if_game_should_deal_third_card(self):
        hand_values = [("kuppin", 11), ("shippin", 10), ("regular", 7), ("regular", 3)]
        self.game._deal_third_card(hand_values)
        self.mock_player1.add_card.assert_not_called()
        self.mock_player2.add_card.assert_not_called()
        self.mock_player3.add_card.assert_not_called()
        self.mock_player4.add_card.assert_called_once()

    def test_if_a_player_is_asked_to_draw_third_card_if_possible(self):
        self.mock_player1.hand = [Card(4), Card(10)]
        self.mock_player1.ai = False
        with patch("builtins.input", return_value="y") as raw_input:
            self.game._ask_if_not_ai_player_wants_to_draw_third_card()
            raw_input.assert_called_once_with("Do you want to draw the third card? [y/n] ")

    def test_if_game_prints_player_names_and_their_hands(self):
        self.mock_player1.name = "Johnny"
        self.mock_player2.name = "Robot A"
        self.mock_player3.name = "Robot B"
        self.mock_player4.name = "Robot C"
        self.mock_player1.hand = [4, 1]
        self.mock_player2.hand = [9, 9, 9]
        self.mock_player3.hand = [1, 10]
        self.mock_player4.hand = [4, 2, 2]

        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.game._print_player_names_and_their_hands()
            self.assertEqual(
                mock_stdout.getvalue(),
                f"{self.mock_player1.name} (dealer){2 * ' '}{self.mock_player2.name}{10 * ' '}{self.mock_player3.name}"
                f"{10 * ' '}{self.mock_player4.name}\n"
                f"{self.mock_player1.hand}{11 * ' '}{self.mock_player2.hand}{8 * ' '}{self.mock_player3.hand}"
                f"{10 * ' '}{self.mock_player4.hand}\n"
            )

    def test_if_game_can_determine_who_wins(self):
        hand_values_to_be_tested = [
            [("kuppin", 11), ("shippin", 10), ("regular", 7), ("regular", 3)],
            [("kuppin", 11), ("arashi", 19), ("regular", 7), ("regular", 3)],
            [("regular", 7), ("regular", 8), ("arashi", 19), ("regular", 3)],
            [("regular", 7), ("regular", 7), ("arashi", 19), ("regular", 3)],
            [("regular", 7), ("regular", 7), ("regular", 5), ("regular", 8)]
        ]
        list_of_winners = [self.mock_players[0], self.mock_players[1], self.mock_players[1], self.mock_players[2],
                           self.mock_players[3]]
        for index, value in enumerate(hand_values_to_be_tested):
            self.assertEqual(self.game._determine_who_wins(value), list_of_winners[index])
