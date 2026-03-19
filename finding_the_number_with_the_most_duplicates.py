numbers = []
while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        break
    numbers.append(int(user_input))
most = numbers[0]
max_count = numbers.count(most)
for num in numbers:
    if numbers.count(num) > max_count:
        most = num
        max_count = numbers.count(num)
print("Number with most duplicates:", most)

