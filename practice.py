list_items = [1,2,3,4]

even = [n for n in list_items if n % 2 == 0]
print(even)

odd = [n for n in list_items if n % 2 != 0]
print(odd)

double = [n * 2 for n in list_items]
print(double)

import time 

list_items = [1,2,3,4,5]
def time_check(ref):
    def wrapper():
        start = time.time()
        ref()
        stop = time.time()
        print("Time taken: ", start - stop)
    return wrapper

@time_check
def square(n):
    return n ** 2


square()
sq = [num ** 2 for num in list_items]


