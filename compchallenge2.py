# create comprehension that returns a list of all the locations that have an exist to the forest
# The list should contain the description of each location, if it's possible to get to the forest from there.

# The forest is location 5 in the locations dictionary
# The exist for each location are represented by the exists dictionary

# Remember that a dictionary has a .values () method, to return a list of the values.

# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list

# Test your program with different destinations (such as 1 for the road) to make sure it works

# once it's working, modify the programs so that the comprehension returns a list of tuples.
# each tuple consist of the location number and the description

# finally, wrap your comprehension in a for loop, and print the lists of all the locations that
# lead to each of the other location in turn
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary

locations = {0: "you are sitting in front of a computer learning python",
             1: "you are sitting in end of a road before a small brick building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in the forest",
             }

exists = {0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0}}

loc = 1
forest = [locations[xit] for xit in exists if loc in exists[xit].values()]
print(forest)

# loc = 5
forest = []

for xit in exists:
    if loc in exists[xit].values():
        # dic = (exists[xit].values())
        # value = locations[xit]
        forest.append(locations[xit])

print(forest)

print()

# for loc in sorted(locations):
#     forest = [(exit, locations[exit]) for exit in exists if loc in exists[exit].values()]
#     print("Locations leading to {}".format(loc), end='\t')
#     print(forest)

for loc in sorted(locations):
    forest = []
    for xit in exists:
        if loc in exists[xit].values():
            forest.append((xit,locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(forest)
