import unittest

from oicho_kabu.card import Card
from oicho_kabu.hand import Hand


class HandTest(unittest.TestCase):
    def test_if_hand_stores_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_if_card_can_be_added_to_a_hand(self):
        hand = Hand()
        card = Card(10)
        hand.add_card(card)
        self.assertEqual(hand.cards, [card])

    def test_if_hand_has_string_representation(self):
        hand = Hand()
        hand.add_card(Card(4))
        hand.add_card(Card(1))
        self.assertEqual(str(hand), "4, 1")

    def test_if_hand_has_technical_representation(self):
        hand = Hand()
        hand.add_card(Card(4))
        hand.add_card(Card(1))
        self.assertEqual(repr(hand), "[Card('4'), Card('1')]")

    def test_if_hand_value_is_determined_correctly(self):
        hand = Hand()
        hand.add_card(Card(6))
        hand.add_card(Card(4))
        self.assertEqual(hand.calculate_value(), 0)

    def test_if_arashi_is_present_in_a_hand(self):
        hand = Hand()
        hand.add_card(Card(8))
        hand.add_card(Card(8))
        hand.add_card(Card(8))
        self.assertTrue(hand.arashi(), True)

    def test_if_kuppin_is_present_in_a_hand(self):
        hand = Hand()
        hand.add_card(Card(9))
        hand.add_card(Card(1))
        self.assertTrue(hand.kuppin(), True)

    def test_if_shippin_is_present_in_a_hand(self):
        hand = Hand()
        hand.add_card(Card(4))
        hand.add_card(Card(1))
        self.assertTrue(hand.shippin(), True)

    def test_if_final_hand_is_calculated_properly(self):
        hand = Hand()
        hand.add_card(Card(7))
        hand.add_card(Card(5))
        hand.add_card(Card(4))
        self.assertEqual(hand.calculate_hand(dealer=False), ("regular", 6))

    def test_if_hand_provides_its_length(self):
        hand = Hand()
        hand.add_card(Card(7))
        hand.add_card(Card(5))
        hand.add_card(Card(4))
        self.assertEqual(len(hand), 3)
