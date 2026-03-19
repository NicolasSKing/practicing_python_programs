numbers = []
while True:
    input_numbers = input("Enter numbers: ")
    if not input_numbers.isdigit():
        break
    num = int(input_numbers)
    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
    numbers.append(num)

