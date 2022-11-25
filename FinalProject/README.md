# CPE 551 Final Project

I pledge my honor that I have abided by the Stevens Honor System

## About

The objective of this project was to create a card game in Python using object oriented programming. In [Lecture Notes 9](../Notes/EE%20551%20Lecture%20Notes%209.ipynb), we were provided some of the basic classes neede to get started, including player hands, cards, and decks.

For this project, I decided to make the card game I played the most when I was young, War.

## Rules

In order to avoid any confusion, I used a set of rules provided by [Bicycle Cards](https://bicyclecards.com/how-to-play/war) which state:

- Number of players - 2
- The goal is to be the first player to win all 52 cards
- The deck is divided evenly, with each player receiving 26 cards. Players do not know what cards they have.
- Each round, both players play a card from their deck, and the player with the higher ranked card takes both cards, and puts them in their deck.
- If the cards played are the same rank, this starts a war! Each player then must play one card face down as a sacrifice, and another face up as a fighter. The player with the higher ranked fighter card is the winner of the war and takes all cards in play, which go back into their deck.
  - In the event that the two fighter cards also tie, war will happen again until one player wins a war.
  - If a player does not have enough extra cards to participate in a war, they will forfeit and lose the
- The game ends once a single player has all 52 cards.

## Notes

- As the game does not end until one player has all 52 cards, and the order of the cards is randomized, it is possible (but highly unlikely) the game could go on ***forever**.

## Sources

There are four sources that I used to make this:

- Initial classes from [Lecture Notes 9](../Notes/EE%20551%20Lecture%20Notes%209.ipynb). This was used to generate cards, decks, and hands.
- Colored text output from [Stack Overflow](https://stackoverflow.com/a/17303428). This was used to make it easier to distinguish between the human and the computer, and other important lines of text.
- A count down timer from [GeeksForGeeks](https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/). This was used to add a live counter between turn times. I decided to go with this as I believed there should be a delay in between turns so a useer could see what is happening, while also a live indicator of when the next turn will begin.
- Game rules from [Bicycle Cards](https://bicyclecards.com/how-to-play/war).
