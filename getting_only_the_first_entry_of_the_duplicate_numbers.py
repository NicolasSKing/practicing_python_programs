numbers = []
for i in range(10):
    input_numbers = float(input("Enter a number: "))
    numbers.append(input_numbers)
    print(numbers)
print("No duplicate numbers: ")
for i in range(len(numbers)):
    if numbers[i] not in numbers[:i]:
        print(numbers[i], end=" ")