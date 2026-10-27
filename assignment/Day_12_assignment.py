from functools import reduce
# Task 1
def apply_twice(fnc, x):
    return fnc(fnc(x))

print(apply_twice(lambda x: x + 3, 10))

# Task 2
def make_greeting(greeting):
    def greet(name):
        return f"{greeting} {name}"
    return greet

print(make_greeting("Namaste")("Ram"))

# Task 3
def shout(fnc):
    def wrapper():
        return fnc().upper()
    return wrapper

@shout
def help():
    return "Helppppppppppp"

print(help())

# Task 4
value = ["10", "20", "30"]

def val_int(x):
    return int(x)

new_val = list(map(val_int, value))

sum = reduce(lambda x, y: x + y, new_val)
print(sum)

# Task 5
word = ["Ram", "Raghav", "Vishnu", "shyam"]

new_words = list(filter(lambda x: len(x) > 4, word))
print(new_words)

# Task 6
people = [
    ("Ram", 20),
    ("Sita", 25),
    ("Hari", 18),
    ("Gita", 30)
]

sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
print(sorted_people)

# Task 7
num = [4, 5, 70, 2, 9]
largest_num = reduce(lambda x, y: x if x > y else y, num)
print(largest_num)