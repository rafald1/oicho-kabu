import unittest
from unittest.mock import patch

from oicho_kabu.card import Card
from oicho_kabu.deck import Deck


class DeckTest(unittest.TestCase):
    def test_if_deck_stores_no_cards(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_if_cards_can_be_added_to_a_deck(self):
        card = Card(2)
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(deck.cards, [card])

    @patch("random.shuffle")
    def test_if_cards_are_shuffled(self, mock_shuffle):
        cards = [Card(2), Card(3), Card(4), Card(5), Card(6)]
        deck = Deck()
        deck.add_cards(cards)
        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_if_card_is_removed_from_deck(self):
        card_to_be_removed = Card(6)
        cards = [Card(2), Card(3), Card(4), Card(5), card_to_be_removed]
        deck = Deck()
        deck.add_cards(cards)
        self.assertEqual(deck.remove_card(), card_to_be_removed)
        self.assertEqual((len(deck.cards)), 4)

    def test_if_deck_provides_its_length(self):
        deck = Deck()
        cards = [Card(2), Card(3), Card(4), Card(5)]
        deck.add_cards(cards)
        self.assertEqual(len(deck), 4)
