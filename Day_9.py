s = {10, 20, 30}
s.discard(99)
print(s)
try:
    s.remove(99)
except:
    print('Throws error')
s.pop()
print(s)

print("=====")
A = {1,2,3,4}
B = {3,4,5,6}

print(A | B) #all unique elements
print(A & B)
print(A - B)
print(A ^ B)

print("=====")
print({1,2} <= {1,2,3})
print({1,2} < {1,2})
print({1,2}.isdisjoint({3,4}))
print({1, True, 1.0})

print("")
list_items = [3,1,3,2,1]
new_list = []
for i in list_items:
    if i not in new_list:
        new_list.append(i)

print(new_list)


