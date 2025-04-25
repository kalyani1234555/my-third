from contents import pantry, recipes

# print(pantry)
# print(recipes)
def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """ Add a tuple containing 'item' and 'amount' to the data dict"""
    # data.append((item, amount)) # this is a tuple
    # if item in data:   # it is dict
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


# display_dict = {str(index+1): meal for index, meal in enumerate(recipes)}
# shopping_list = []
shopping_list = {}
display_dict = {}
for index, key in enumerate(recipes):
    # print(index, key)
    display_dict[str(index + 1)] = key


while True:
    print("please choose the recipes")
    print("---------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_items = display_dict[choice]
        print(f"you have selected {selected_items}")
        print("checking ingredients....")
        ingredients = recipes[selected_items]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t you need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

# for things in sorted(shopping_list):
for things in shopping_list.items():
    print(things)
