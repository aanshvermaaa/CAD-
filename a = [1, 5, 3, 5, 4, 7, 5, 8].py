a = [1, 5, 3, 5, 4, 7, 5, 8]

result = []

for i in a:
    if i == 5:
        continue
    result.append(i)

print(result)