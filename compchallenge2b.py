import timeit

setup = """\
gc.enable()
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
"""

print("nested for loops")
print("----------------")
nested_loop = """\
for loc in sorted(locations):
    exists_to_destination_1 = []
    for xit in exists:
        if loc in exists[xit].values():
            exists_to_destination_1.append((xit, locations[xit]))
    print("Location leading to {}".format(loc), end='\t')
    print(exists_to_destination_1)
"""
print()

print("List comprehension inside a for loop")
print("------------------------------------")
loop_comp = """\
for loc in sorted(locations):
    exists_to_destination_2 = [(xit, locations[xit]) for xit in exists if loc in exists[xit].values()]
    print("Location leading to {}".format(loc), end='\t')
    print(exists_to_destination_2)
"""

print("nested comprehension")
print("------------------------------------")
nested_comp = """\
exists_to_destination_3 = [[(xit, locations[xit]) for xit in exists if loc in exists[xit].values()]
                           for loc in sorted(locations)]
# print(exists_to_destination_3)
#
# print()
for index, loc in enumerate(exists_to_destination_3):
    print("Location leading to {}".format(index), end='\t')
    print(loc)
"""
# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
result_1 = timeit.timeit(nested_loop, setup, number=10000)
result_2 = timeit.timeit(loop_comp, setup, number=10000)
result_3 = timeit.timeit(nested_comp, setup, number=10000)
print("Nested loop:\t{}".format(result_1))
print("loop and comp :\t{}".format(result_2))
print("Nested loop:\t{}".format(result_3))
