# In case it's not obvious, a list comprehension produces a list, but
# It doesn't have to be given a list to iterate over.

# you can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimetres

# our dimensions will be represented by a tuple, for the length, width and height.
# There are 2.54 centimetres to 1 inch.

inch_measurement = (3, 8, 20)

cm_measurement = [(inch * 2.54) for inch in inch_measurement]
print(cm_measurement)

# once you've got the correct values, change the code to produce a tuple, rather than a list,
cm_measurement = tuple([(inch * 2.54) for inch in inch_measurement])
print(cm_measurement)


for inch, breadth, length in [inch_measurement]:
    print(inch)
