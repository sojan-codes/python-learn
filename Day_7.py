scores = (72, 85, 90, 85)

print(scores[0], scores[-1])

print(scores.count(85))

a, b, c = scores[:3]
print(a, b, c)

try:
    scores[0] = 100
except:
    print('Error')

print('----------------------------')
days = ('Mon', 'Tue', 'Mon', 'Wed')

print(days.count('Mon'), days.index('Wed'))

value = (3, 8, 1)

ref1 = value[0]
ref2 = value[0]
for i in value:
    if ref1 > i:
        ref1 = i
    elif ref2 < i:
        ref2 = i

tup = (ref1, ref2)
print(tup)

print("=========")
tuple = (10, 20, [30, 40], 50, 60)
tuple[2].append(70)
print(tuple)

tuple[2].insert(1,[100, 200])
print(tuple)


print('Dictionaries')


d = {'a': 1, 'b': 2}
print(d.get('a'))
print(d.get('z', 0)) #0 is default value if key is missing
print(list(d.keys()))
print(list(d.values()))
print('a' in d)
print(len(d))
print(d.pop('a'))
print(d)
try:
    print(d['z'])
except:
    print('Error')

dict = {
    'a' : {
        'name' : 'sojan',
        'age' : 20
    },
    'b' : {
        'name' : 'hari',
        'age' : 14
    }
}
print(dict)

