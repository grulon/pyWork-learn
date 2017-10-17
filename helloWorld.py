#print('Hello world')
# easily split lists or iterators into variables
'''
a, b, *rest = range(10)
print(a)     # prints 0
print(b)     # prints 1
print(rest)  # prints [2, 3, 4, 5, 6, 7, 8, 9]

# or even

a, *rest, b = range(10)
print(rest)  # prints [1, 2, 3, 4, 5, 6, 7, 8]

# in python 2 it's a lot more verbose

l = list(range(10))
a = l[0]
rest = l[1:-1]
b = l[-1]
'''

x = [[1, 2], [3, 4], [5, 6]]
x = [x for i in x for x in i]

print(x, type(x))


def change_nth(items, index, value):
    items[index] = value

c = [2, 4, 6, 8]
change_nth(c, 1, 5)
print (c, type(c))

x = {'a':1, 'b': 2}
print(type(x))
y = {'b':10, 'c': 11}
z = x.copy()
z.update(y)
print(z, type(z))