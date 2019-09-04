# draw-TipTheScales
A Monte-Carlo simulation of many Hearthstone hands trying to draw Tip The Scales before turn 4

Murloc Paladin has been a deck in Hearthstone that has recently resurged in popularity, this time carried by the powerful combo of Prismatic Lens + Tip The Scales, allowing a Murloc flood by as early as Turn 5 (or Turn 4 with the coin). Suppose that you hard-mulligan for Prismatic Lens every game--what are the odds you draw a Prismatic Lens by Turn 4 or 3 and **don't** draw both Tip The Scales by Turn 4? This simple program calculates those odds.

---------------------------------------

WHAT THE PROGRAM DOES:
First, we begin with a critical function, "random_card", which models drawing a card from your deck. We assign each card in the deck an integer value from 1-30, inclusive. We arbitrarily assign 4 and 5 to be the two Prismatic Lens and 8 and 9 to be the two Tip The Scales. This choice of values is arbitrary and is only motivated by the mana costs of the actual cards. Now, you cannot draw a card from your deck that you have already drawn, so the "random_card" function looks through all the cards in your hand and re-rolls the number if you draw a card that's already in your hand.

Next, we move onto the mulligan phase, where we simulate drawing 3 cards (4 with the coin) and hard-mulliganing for Prismatic Lens. Something to note is that we are trying to maximize the chances of a success, so if we have drawn the Lens in the mulligan, we keep all cards except Tip The Scales to minimize our chances of a failure, where we draw both Tip The Scales before Turn 4. In Hearthstone, you cannot draw back the cards you mulligan away, and the function "mulligan" accounts for this.

Finally, we simulate drawing the remaining 4 cards naturally. This is a simple process of drawing a random card until one is drawn which is not already in our hand, then repeating three more times.

	
