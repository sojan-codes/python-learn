# Classwork 4: /, * and unpacking​
# Task 1
# ok, error, ok, error 

# Task 3
opts = {"sep": "-","end": "!\n"}

print("a", "b", **opts)

# Task 1
def average(*nums):
    avg = sum(nums) / len(nums)
    return avg

print(average(2, 4, 6))

# Task 2
def receipt(customer, **items):
    total = 0
    print("Name: ", customer)
    for key, value in items.items():
        print(key, ":", value)
        total += value
    print("Total: ", total)

receipt("Asha", tea=50, momo=150)

# Task 3
def log(msg, history=None):
    if history is None:
        history = []

    history.append(msg)
    return history
print(log("hi"))

# Task 4
def evens(limit):
    for i in range(1, limit + 1):
        if i % 2 == 0:
            yield i
            
print(list(evens(10)))
print(sum(evens(10)))