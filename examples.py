print(__file__)
text = "what have the romans ever done for us"

captials = [char.upper() for char in text]

print(captials)

words = [word.upper() for word in text.split(" ")]

print(words)

lc_words = text.split(" ")
print(lc_words)

lc_words = [word for word in text.split(" ")]  # it's not required to use list comprehension

print(words)
