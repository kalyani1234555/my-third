# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number. We used an iterative approach, and also used a recursive function.

# The challenge is to use the timeit module to see which performs better.
# The two functions appear below

# Hint: change the number of iterations to 1,000 or 10,000. The default
# of one million will take a long time to run.

import timeit

fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
x = fact(10)
"""

factorial_test = """\
def factorial(n):
    # n! can also be defined as n* (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

y = factorial(10)
"""


# result_1 = timeit.timeit(fact_test, number=1000)
# result_2 = timeit.timeit(factorial_test,  number=1000)
# print("fact:\t{}".format(result_1))
# print("factorial:\t{}".format(result_2))

print(timeit.timeit(fact_test, number=1000))
print(timeit.timeit(factorial_test, number=1000))
