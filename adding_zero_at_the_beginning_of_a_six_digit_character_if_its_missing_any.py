number = int(input("Enter a number (0 - 1000): "))
string = str(number)
making_it_six_digits = string.rjust(6, "0")
print(making_it_six_digits)