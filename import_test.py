import blackjack

# from blackjack import *
g = sorted(globals())
for x in g:
    print(x)

# print(__name__)
blackjack.play()
# print(blackjack.cards)
blackjack.deal_card(blackjack.dealer_card_frame)
