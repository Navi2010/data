numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

x = map(lambda x,y: x+y, numbers1, numbers2)
print(list(x))

numbers = [1, 2, 3, 4, 5]
def square (n):
    return n*n
y = list(map(square, numbers))
print(y)
