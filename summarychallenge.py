choice = "_"   # initialise choice to something invalid
while choice != "0":
    # if choice in list("12345"):
    # if choice in "12345":
    # if choice in set("12345"):
    if choice in {'1', '2', '3', '4', '5'}:
        print("you chose {} ".format(choice))
    else:
        print("please choose your option from the list below:")
        print("1.\t Learn python")
        print("2.\t Learn Java")
        print("3.\t Go swimming")
        print("4.\t Have dinner")
        print("5.\t Go to bed")
        print("0.\t exit")

    choice = input()
