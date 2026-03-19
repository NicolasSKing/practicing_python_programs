numbers = []
while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        break
    numbers.append(int(user_input))

