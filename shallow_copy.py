import copy
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}


# animals["teddy"] = "toy"
# perform a shallow copy
things = animals.copy()

# perform deep copy
# things = copy.deepcopy(animals)
print(things["teddy"])
print(animals["teddy"])

things["teddy"].append("toy")
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])
