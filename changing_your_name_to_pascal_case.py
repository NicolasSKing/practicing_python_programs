full_name = input("Please enter your full name in incorrect casing: ")
print("".join(word.capitalize() for word in full_name.split()))