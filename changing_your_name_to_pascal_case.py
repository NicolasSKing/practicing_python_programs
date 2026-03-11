full_name = input("Enter your full name in incorrect casing: ")
print("".join(word.capitalize() for word in full_name.split()))