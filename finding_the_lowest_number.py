all_of_the_numbers = []
while True:
    try:
        numbers = float(input("Enter a number: "))
        all_of_the_numbers.append(numbers)
    except ValueError:
        break
all_of_the_numbers.sort()
print(all_of_the_numbers[0])