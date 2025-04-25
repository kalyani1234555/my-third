# create a new python file - I've called this one "compchallenge1.py"

# use the conditional expression from the previous video to produce
# a list comprehension that returns the fizzbuzz results.

# if a number's divisible by 3, the value should be "fizz"
# if it's divisible by 5, the value should be "buzz"
# if it's divisible by both 3 and 5, the value should be "fizz buzz"
# finally , if none of those conditions apply, the value will be the number itself.

# the code from the end of last video appears below, so you can check the result

# for x in range(1, 31):
#     fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
#     print(fizzbuzz)

fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
              for x in range(1, 31)]
print(fizzbuzz)

for buzz in fizzbuzz:
    print(buzz.center(12, '*'))
