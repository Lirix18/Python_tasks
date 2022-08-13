src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2]
#  result = [23, 1, 3, 10, 4, 11]

print(src)
unique = []
repeat = []

for elem in src:
    if elem in repeat:
        continue
    if elem in unique:
        repeat.append(elem)
        unique.remove(elem)
        continue
    unique.append(elem)


print(unique)
print(repeat)

