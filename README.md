# oicho-kabu
### About Oicho-Kabu
Oicho-Kabu is a card game in which a group of players compete against the dealer to assemble a hand of cards whose value is as close as possible to 9. If the total of the hand exceeds 9, the first digit is excluded.

The dealer wins if there is a tie between a player and the dealer.

The deck contains 40 cards, consisting of four sets of cards with ranks from 1 to 10.

### Choosing the Dealer
Each player draws a card from the deck. The player with the lowest number becomes the dealer. The remaining players seat in anti-clockwise order around the table based on their scores.

In this implementation the player with the lowest card is the dealer and the remaining players are seated based to their relative original position to the player who became the dealer.

The game starts with the dealer and progresses anti-clockwise. There is an advantage in sitting closer to the dealer.

### Special Hands
Special hands will win against any regular hand.

Arashi (Three of a Kind) - A hand consisting of three cards with the same number.

Kuppin (9-1) - Valid for the dealer only. A two-card hand consisting of a 9 and a 1 in any order.

Shippin (4-1) - Valid for players only. A two-card hand consisting of a 4 and a 1 in any order.

### The Third Card
If a hand’s total value is 3 or lower, then a third card must be taken.
If a hand’s total value is 7 or higher, then a third card cannot be taken.

### About this project
The purpose of this project was to get familiar with test-driven development.
