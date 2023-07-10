from oicho_kabu.card import Card
from oicho_kabu.deck import Deck
from oicho_kabu.hand import Hand
from oicho_kabu.player import Player
from oicho_kabu.game import Game

deck = Deck()
cards = Card.create_oicho_kabu_set()
deck.add_cards(cards)

player1 = Player(name="Johnny", hand=Hand(), ai=False)
player2 = Player(name="Robot A", hand=Hand(), ai=True)
player3 = Player(name="Robot B", hand=Hand(), ai=True)
player4 = Player(name="Robot C", hand=Hand(), ai=True)

players = [player1, player2, player3, player4]

game = Game(deck, players)
game.play()
