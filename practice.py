items = list(range(10000))


def byfun(*x):
    for i in x:
        if i % 2 == 0:
            print("even")
        else:
            print("odd")


y = byfun(*items)
import sys
x = sys.getsizeof(y)
print(x)
