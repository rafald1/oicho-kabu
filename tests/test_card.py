import unittest

from oicho_kabu.card import Card


class CardTest(unittest.TestCase):
    def test_if_card_has_rank_attribute(self):
        card = Card(rank=1)
        self.assertEqual(card.rank, 1)

    def test_if_card_has_string_representation(self):
        card = Card(rank=2)
        self.assertEqual(str(card), "2")

    def test_if_card_has_technical_representation(self):
        card = Card(rank=3)
        self.assertEqual(repr(card), "Card('3')")

    def test_if_oicho_kabu_card_has_one_of_ten_possible_ranks(self):
        self.assertEqual(Card.OICHO_KABU_RANKS, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_if_card_has_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank="King")

    def test_if_oicho_kabu_set_can_be_created(self):
        cards = Card.create_oicho_kabu_set()
        self.assertEqual(len(cards), 40)
        self.assertEqual(cards[0], Card(1))
        self.assertEqual(cards[-1], Card(10))

    def test_if_two_cards_are_equal(self):
        self.assertEqual(Card(5), Card(5))
