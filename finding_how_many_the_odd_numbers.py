odd_numbers = 0
for i in range(10):
    numbers = float(input("Enter a number: "))
    if numbers % 2 != 0:
        odd_numbers += 1
print(f"There are {odd_numbers} odd numbers")