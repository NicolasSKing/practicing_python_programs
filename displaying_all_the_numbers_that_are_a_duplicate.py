numbers = []
for i in range(10):
    inputed_numbers = int(input("Enter a number: "))
    numbers.append(inputed_numbers)
print("Numbers with duplicates:")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers[i] not in numbers[:i]:
                print(numbers[i])


