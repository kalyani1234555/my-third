print(__file__)

numbers = [1, 2, 3, 5, 6]

number = int(input("please enter the number, and I'll tell you it's square:"))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])
