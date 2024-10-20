from math import pi
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting at position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)


# List comprehension ==> Important Topic  (Optimised way of using list in Python)
str_lst = [str(round(pi, i)) for i in range(1, 6)]
print(str_lst)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

newmatrix = [[row[i] for row in matrix] for i in range(4)]
print(newmatrix)

# Three methods of doing this
# simple way
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)


# using function
squaresmap = list(map(lambda x: x**2, range(10)))
print(squaresmap)

# using list comprehension
squarescomp = [x**2 for x in range(10)]
print(squarescomp)


# Two methods of doing this
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

combsnew = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combsnew.append((x, y))

print(combsnew)
