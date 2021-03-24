# Old Maid Card Game

This python package plays through a game of Old Maid with any number of players.

It is taken from the tutorial at [openbookproject](https://openbookproject.net/)

## Contributing

The package contains a python file `card_setup.py` with basic classes for setting up a deck, hand, and cards from a deck.
The old maid game is saved in `old_maid.py` and futher games can be added and pushed to the repo which makes use of the `card_setup.py` file.

```
import cards
>>> game = cards.OldMaidGame()
>>> game.play(["Allen","Jeff","Chris"])
```
