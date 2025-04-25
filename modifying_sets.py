# numbers = {}
# numbers = {*{}}
# numbers = {*""}
numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("please enter your next value"))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# create a set from the list, to remove duplicates

# unique_data = set(data)
unique_data = sorted(set(data))
print(unique_data)

# create a list of unique colours, keeping the order they appeared.
dict_keys = dict.fromkeys(data)
unique_data1 = list(dict.fromkeys(data))
print(unique_data1)
print(dict_keys)
