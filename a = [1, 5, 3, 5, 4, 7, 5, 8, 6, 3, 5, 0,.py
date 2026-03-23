a = [1, 5, 3, 5, 4, 7, 5, 8, 6, 3, 5, 0, 9, 2, 7]

count = 0
result = []

for i in a:
    if i == 5 and count < 2:
        count += 1
        continue   
    result.append(i)

print(result)