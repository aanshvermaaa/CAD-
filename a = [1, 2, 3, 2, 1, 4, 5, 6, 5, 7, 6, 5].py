a = [1, 2, 3, 2, 1, 4, 5, 6, 5, 7, 6, 5]

result = []

for i in a:
    if i == 5:
        continue   
    result.append(i)

print(result)