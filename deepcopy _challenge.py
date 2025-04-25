# animals = {
#     "lion": ["scary", "big", "cat"],
#     "elephant": ["big", "grey", "wrinkled"],
#     "teddy": ["cuddly", "stuffed"],
# }
#
# copy_dict = {}
# for key, values in animals.items():
#     chosen_keys = animals[key]
#     # print(chosen_keys)
#    copy_dict.copy(chosen_keys)


from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """ copy a dictionary, creating copies of the list and dict values
    The function will crash with an attributeError if the values aren't
    list or dictionaries.
    :param d: The dictionary to copy.
    :return : A copy of d, with the values being copies of the original values.
    """
    new_dict = {}
    for key, values in d.items():
        new_value = values.copy()
        new_dict[key] = new_value
    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
