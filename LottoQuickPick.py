from random import randint
# import collections


lines = int(input("how many lines would you like?"))

for i in range(lines):
    numbers = []
    while len(numbers) < 6:
        num = randint(1, 48)
        if num not in numbers:
            numbers.append(num)
    print(sorted(numbers))

    #Test

    # x = [item for item, count in collections.Counter(numbers).items() if count > 1]
    #
    # print(f"------------> {x}" if len(x) > 0 else "")