from primes_and_squares import squares_generator, primes_generator
evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.difference(primes))  # removes all items in primes
print(odds - primes)     # removes all items in primes
print(primes - odds)     # removes all items in odds
