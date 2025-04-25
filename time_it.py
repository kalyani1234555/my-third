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


def nested_loop():
    result = []
    for loc in sorted(locations):
        exists_to_destination_1 = []
        for xit in exists:
            if loc in exists[xit].values():
                exists_to_destination_1.append((xit, locations[xit]))
        result.append(exists_to_destination_1)
    # print the result before returning
    for x in result:
        pass
    return result


def loop_comp():
    result = []
    for loc in sorted(locations):
        exists_to_destination_2 = [(xit, locations[xit]) for xit in exists if loc in exists[xit].values()]
        result.append(exists_to_destination_2)
    # print the result before returning
    for x in result:
        pass
    return result


def nested_comp():
    exists_to_destination_3 = [[(xit, locations[xit]) for xit in exists if loc in exists[xit].values()]
                               for loc in sorted(locations)]
    # print the result before returning
    for x in exists_to_destination_3:
        pass
    return exists_to_destination_3
    # print the result before returning


def nested_gen():
    exists_to_destination_4 = ([(xit, locations[xit]) for xit in exists if loc in exists[xit].values()]
                               for loc in sorted(locations))
    for x in exists_to_destination_4:
        pass
    return exists_to_destination_4


print(nested_loop())
print(loop_comp())
print(nested_comp())
# print(nested_gen())
# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
result_1 = timeit.timeit(nested_loop, setup, number=10000)
result_2 = timeit.timeit(loop_comp, setup, number=10000)
result_3 = timeit.timeit(nested_comp, setup, number=10000)
result_4 = timeit.timeit(nested_gen, setup, number=10000)
print("Nested loop:\t{}".format(result_1))
print("loop and comp :\t{}".format(result_2))
print("Nested comp:\t{}".format(result_3))
print("Nested gen:\t{}".format(result_4))
