import time

start = time.time()


def print_function(l, r, s):
    print("(" + l, "+", r + ")²", "=", s)


for i in range(10, 100):

    left = str(i)[0:1]
    right = str(i)[1:]

    sqsum = (int(left) + int(right))**2

    if int(left+right) == sqsum:
        print_function(left, right, sqsum)

for i in range(100, 1000):

    left = str(i)[0:1]
    right = str(i)[1:]

    sqsum = (int(left) + int(right))**2

    if int(left+right) == sqsum:
        print_function(left, right, sqsum)

for i in range(100, 1000):

    left = str(i)[0:2]
    right = str(i)[2:]

    sqsum = (int(left) + int(right))**2

    if int(left+right) == sqsum:
        print_function(left, right, sqsum)

for i in range(1000, 10000):

    left = str(i)[0:2]
    right = str(i)[2:]

    sqsum = (int(left) + int(right)) ** 2

    if int(left + right) == sqsum:
        print_function(left, right, sqsum)


for i in range(10000, 100000):

    left = str(i)[0:2]
    right = str(i)[2:]

    sqsum = (int(left) + int(right)) ** 2

    if int(left + right) == sqsum:
        print_function(left, right, sqsum)

for i in range(10000, 100000):

    left = str(i)[0:3]
    right = str(i)[3:]

    sqsum = (int(left) + int(right)) ** 2

    if int(left + right) == sqsum:
        print_function(left, right, sqsum)

for i in range(100000, 1000000):

    left = str(i)[0:3]
    right = str(i)[3:]

    sqsum = (int(left) + int(right)) ** 2

    if int(left + right) == sqsum:
        print_function(left, right, sqsum)

for i in range(1000000, 100000000):
    left = str(i)[0:3]
    right = str(i)[3:]

    sqsum = (int(left) + int(right))**2

    if int(left+right) == sqsum:
        print_function(left, right, sqsum)

for i in range(1000000, 100000000):
    left = str(i)[0:4]
    right = str(i)[4:]

    sqsum = (int(left) + int(right))**2

    if int(left+right) == sqsum:
        print_function(left, right, sqsum)

end = time.time()

print("took:", end-start, "seconds")

'''
(8 + 1)² = 81
(10 + 0)² = 100
(20 + 25)² = 2025
(30 + 25)² = 3025
(98 + 01)² = 9801
(88 + 209)² = 88209
(100 + 00)² = 10000
(494 + 209)² = 494209
(998 + 001)² = 998001
(494 + 1729)² = 4941729
(744 + 1984)² = 7441984
(238 + 04641)² = 23804641
(1000 + 000)² = 1000000
(2450 + 2500)² = 24502500
(2550 + 2500)² = 25502500
(5288 + 1984)² = 52881984
(6048 + 1729)² = 60481729
(9998 + 0001)² = 99980001
'''