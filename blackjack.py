import random
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter




def load_images(card_images):
     suits = ['heart', 'club', 'diamond', 'spade']
     face_cards = ['jack', 'queen', 'king']
     if tkinter.TkVersion > 8.6:
         extension = 'png'
     else:
          extension = 'ppm'

    # for each suit, retrieve the image for the cards

     for suit in suits:
         # first the number cards 1 to 10
          for card in range(1, 11):
             name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
             image = tkinter.PhotoImage(file = name)
             card_images.append((card, image,))

          # next the face cards
          for card in face_cards:
             name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
             image = tkinter.PhotoImage(file = name)
             card_images.append((10, image,))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    #add it back to the pack
    deck.append(next_card)
    # add image to Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list
    # only one ace can have the value 11, and this will be reduce to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value =11
        score += card_value
        # if we would bust, check if there is an ace and substract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

def initial_deal():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # embedded frame to hold the card images
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")
    # create the list to store the dealer's and player's hand
    dealer_hand = []
    player_hand = []
    initial_deal()


    # global player_score
    # global player_ace
    # # player_score = 0
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there ia an ace and substract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins !")
    # print(locals())

def shuffle():
    random.shuffle(deck)

# print(__name__)


def play():
    initial_deal()
    if __name__ == '__main__':
        mainwindow.mainloop()


mainwindow = tkinter.Tk()

# set up the screen and frames for a dealer and player

mainwindow.title("Black Jack")
mainwindow.geometry("640x480")
mainwindow.config(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainwindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg='white').grid(row=1, column=0)

# embadded frame to hold the card images

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text="Player", background="green", fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg='white').grid(row=3, column=0)

# embadded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command = deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command = deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command = new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="shuffle", command = shuffle)
shuffle_button.grid(row=0, column=3)

#loads cards
cards = []
load_images(cards)
print(cards)

# create the list to store the dealer's and player's hand
dealer_hand = []
player_hand = []

# create new deck of cards and shuffle them
# deck = list(cards)
deck = list(cards) + list(cards) + list(cards)
# random.shuffle(deck)
shuffle()

# create the list to store the dealer's and player's hand
dealer_hand = []
player_hand = []

new_game()

deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

if __name__ == "__main__":
    play()
