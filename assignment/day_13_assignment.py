# Task 01
data =  [("Asha", 21), ("Ram", 19)]
young = sorted(data, key=lambda x: x[1])
print(young)


# Task 02
val = list(range(1, 21))
div_3 = [x for x in val if x % 3 == 0]
print(div_3)

# Task 03
value = ["apple", "kiwi", "banana"]

result = {x: len(x) for x in value}
print(result)

# task 04
list_items = [3, 8, 11, 14]
bool_value = ["even" if x % 2 == 0 else "odd" for x in list_items]
print(bool_value)