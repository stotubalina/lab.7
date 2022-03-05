numbers = [63, -85, 1, 0, -2, 2, 1, 0, -7]
allMulti = 1
rep = 0
allSum = 0

for i in range(len(numbers)):
    if i % 2 == 0:
        allMulti = allMulti * numbers[i]

    if numbers[i] == 0:
        rep += 1

    if rep == 1:
        allSum += numbers[i]

print("Произведение: ", allMulti)
print("Сумма между '0': ", allSum)

numbers.sort()
numbers.reverse()
print(numbers)
