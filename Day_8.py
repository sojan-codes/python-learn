result = {
    'ram': [85, 90, 75, 85, 20],
    'hari': [70, 65, 35, 60, 60],
    'sita': [60, 75, 35, 70, 60],
}

print(result.get('shyam','Not Found.'))

avgResult = {
    'ram' : 0,
    'hari' : 0,
    'sita' : 0
}

for i in result:
    avg = sum(result[i]) / 5
    avgResult[i] = avg

print(avgResult)

for i in result:
    result[i].sort()     

print(result)

print("=======================")
dict = {
    'hari' : [10, 40, 30],
    'ram' : [40, 30, 30],
    'sita' : [80, 40, 70],
}

avgDict = {}

for i in dict:
    sum = 0
    for j in dict[i]:
        sum += j
    avgDict[i] = sum / 5

print(avgDict)

sortDict = {}
for i in dict:
    sortDict[i] = sorted(dict[i])

print(sortDict)
