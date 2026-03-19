inputed_numbers = []
while True:
    try:
        numbers = float(input("Please enter a number: "))
        inputed_numbers.append(numbers)
    except ValueError:
        break
print(max(inputed_numbers))