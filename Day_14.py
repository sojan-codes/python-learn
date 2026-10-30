def greet(name, city):
    print(f"Hi {name} from {city}")

greet('Asha', 'Pokhara')
greet(city="Pokhara", name="Asha")

# 10
def area(l, w):
    return l * w

print(area(w=2, l=5))

#because positional cannot be after keyword
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("milk"))

def add_item(item, cart = None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("milk"))


# Task 1
def power(base, exp=2):
    return base**exp

print(power(3))
print(power(2, 10))

# task 2
def add(item, box=[]):
    box.append(item)
    return box
print(add(1))
print(add(2))

# task 3
def add(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box
print(add(1))
print(add(2))


def total(*numbers):
    print(type(numbers), numbers)
    return sum(numbers)

print(total(5, 10))
print(total(1, 2, 3, 4))

def order(customer, *items):
    print(customer, "ordered", items)

order("asha", "momo", "tea")


# positional argument
def demo(a, *args, **kwargs):
    print(a, args, kwargs)
    
demo(1, 2, 3, x=4, y=5)

# Task 1
def total(*nums):
    return sum(nums)

print(total(1,2,3))
print(total())

# Task 2
def profile(**info):
    for key, value in info.items():
        print(key, ":", value)

profile(name = "Ram", age = 21)

# Task 3
def order(item, *extras, **notes):
    print(item)
    print(extras)
    print(notes)

order("momo", "achar", spicy=True)


def connect(host, * , timeout = 10, ip = '192.168.1'):
    print(host, timeout, ip)

connect("db.local", timeout=10, ip="192.222")

# Generators
def first_three():
    yield 1
    yield 2
    yield 3

gen = first_three()
print(gen)
for n in gen:
    print(n)
    
# def countdown(n):
#     print("Start")
#     while n > 0:
#         yield n
#         n -= 1
#     print("Done")
# gen = countdown(3)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Task 1
def countdonw(n):
    while n > 0:
        yield n
        n -= 1
        
print(list(countdonw(3)))

# Task 2
# moves to next yield and third throws error

# Task 3
def squares(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1
        
# gen = squares(4)
for s in squares(4):
    print(s)


