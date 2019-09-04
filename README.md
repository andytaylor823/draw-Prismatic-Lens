# draw-TipTheScales
A Monte-Carlo simulation of many Hearthstone hands trying to draw Prismatic Lens before turn 4, motivated by the Tip The Scales Murloc Paladin deck currently in the meta.

Murloc Paladin has been a deck in Hearthstone that has recently resurged in popularity, this time carried by the powerful combo of Prismatic Lens + Tip The Scales, allowing a Murloc flood by as early as Turn 5 (or Turn 4 with the coin). Suppose that you hard-mulligan for Prismatic Lens every game--what are the odds you draw a Prismatic Lens by Turn 4 or 3 and **don't** draw both Tip The Scales by Turn 4? This simple program calculates those odds.

---------------------------------------

WHAT THE CODE DOES:

First, we begin with a critical function "random_card", which models drawing a card from your deck. We assign each card in the deck an integer value from 1-30, inclusive. We arbitrarily assign 4 and 5 to be the two Prismatic Lens and 8 and 9 to be the two Tip The Scales. This choice of values is arbitrary and is only motivated by the mana costs of the actual cards. Now, you cannot draw a card from your deck that you have already drawn, so the "random_card" function looks through all the cards in your hand and re-rolls the number if you draw a card that's already in your hand.

Next, we move onto the mulligan phase (using the aptly-named "mulligan" function), where we simulate drawing 3 cards (4 with the coin) and tossing back and re-drawing all cards if we did not draw Prismatic Lens. Now, we are trying to maximize the chances of a success and avoid the scenario where we have drawn both Tip The Scales by Turn 4, so if we have drawn the Lens in the mulligan, we keep all cards except Tip The Scales. In Hearthstone, you cannot draw back the cards you mulligan away, and the function "mulligan" accounts for this.

Finally, we simulate drawing the remaining 4 cards naturally with the "drawn_by_4" function. This is a simple process of drawing a random card until one is drawn which is not already in our hand, then repeating three more times.

In all instances in which we add a card to the hand, I use sets to reduce the time spent searching the hand for a duplicate card. There may be some faster way to search the hand for a duplicate since the hand size (N) is not very large. Searching using sets is O(k), and searching a sorted set is O(log(N)), but because N is not large, the constants buried in the large-O notation may become important. The code runs 10^5 simulations in around one second, and I find this sufficiently fast for the precision I desire.

---------------------------------------

RESULTS:

If the code is run as is listed (n = 1e5), it will produce the following output:

```
----------------------
Fraction of times without coin:   52495/100000 = 52.5 percent (+/- 0.2 percent)
Fraction of times with coin:      61296/100000 = 61.3 percent (+/- 0.2 percent)
Fraction of times to coin it out: 57914/100000 = 57.9 percent (+/- 0.2 percent)
----------------------
This took 1.07 seconds
```

Running with an increased number of trials (n = 1e6) and adjusting the precision of the output will produce the following:
```
----------------------
Fraction of times without coin:   526186/1000000 = 52.6 percent (+/- 0.05 percent)
Fraction of times with coin:      614362/1000000 = 61.4 percent (+/- 0.05 percent)
Fraction of times to coin it out: 580126/1000000 = 58.0 percent (+/- 0.05 percent)
----------------------
This took 10.55 seconds
```
