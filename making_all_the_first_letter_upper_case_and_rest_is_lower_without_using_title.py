text = input("Enter text: ")
words = text.split()
result = ""
for word in words:
    result += word[0].upper() + word[1:].lower() + " "
result = result.strip()
print(result)

