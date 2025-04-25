available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "mouse",
                   "4": "mouse mat",
                   "5": "hdmi cable",
                   "6": "dvd drive"
}
current_choice = "None"
computer_parts = [] #empty the list
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            print(f"remove {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"your list now contains: {computer_parts}")
    else:
        print("please choose the below options from the list")
        for key, value in available_parts.items():
            print(f"{key}:{value}")
        print("0: to finish")

    current_choice = input("> ")
