all_of_the_numbers = []
sum_of_the_numbers = 0
while True:
    try:
        numbers = float(input("Enter a number: "))
        sum_of_the_numbers += numbers
        all_of_the_numbers.append(numbers)
    except ValueError:
        break
length = len(all_of_the_numbers)
average = sum_of_the_numbers / length
print(average)
