from random import randint
from math import sqrt
numbers = []

size = int(input("size:"))
size **= 2

print("\n"*4)

while len(numbers) < size:
    r = randint(1, size)
    if r not in numbers:
        numbers.append(r)

count = 0
for i in range(size):
    print(f"{numbers[i]: 6n}", end="")
    count += 1

    if count == int(sqrt(size)):
        print("\n")
        count = 0

print("\n\n\n\n")
