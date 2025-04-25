# In an early video, we used a for loop to print the times tables, for values from 1 to 10.
# That was a nested loop, which appears below

# The challenge is to use a nested comprehension, to produce the same values.
# you can iterate over the list, to produce the same output as the for loop, or just print out the list.

for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)


for nested_comp in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(nested_comp)

print()

for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)

print()

nested_comp = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(nested_comp)

nested_comp2 = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
print(nested_comp2)

for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)) :
    print(x, y)
