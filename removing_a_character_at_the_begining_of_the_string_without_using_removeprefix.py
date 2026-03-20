text = input("Enter a string: ")
prefix = input("Enter a word that you want to remove in the beginning: ")
if text.startswith(prefix):
    result = text[len(prefix):]
else:
    result = text
print(result)