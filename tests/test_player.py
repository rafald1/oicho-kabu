import unittest
from unittest.mock import MagicMock

from oicho_kabu.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_hand = MagicMock()
        self.player = Player("Johnny", self.mock_hand, ai=True)

    def test_if_player_has_name_hand_and_ai_status(self):
        self.assertEqual(self.player.name, "Johnny")
        self.assertEqual(self.player.hand, self.mock_hand)
        self.assertEqual(self.player.ai, True)

    def test_if_player_final_hand_is_calculated(self):
        self.mock_hand.calculate_hand.return_value = "regular", 3
        self.assertEqual(self.player.current_hand(dealer=True), ("regular", 3))

    def test_if_new_cards_are_added_to_hand(self):
        self.mock_card = MagicMock()
        self.player.add_card(self.mock_card)
        self.mock_hand.add_card.assert_called_once_with(self.mock_card)
