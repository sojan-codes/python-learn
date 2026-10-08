def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y

x = 10
y = 20

x, y = swap(x, y)
print(x)
print(y)

