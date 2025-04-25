from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Bunchalka", ["Programmer", "Teacher"]],
    "J-p": ["Roberts", ["Programmer", "Teacher"]]
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-p"].append("uk")

original["Tim"][1].append("Cashier")
jp_list = original["J-p"]
jp_list[1].append("Courier")

print(original)
print(copy_1)
print(copy_2)
