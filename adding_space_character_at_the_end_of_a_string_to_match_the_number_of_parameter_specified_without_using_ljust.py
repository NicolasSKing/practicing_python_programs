text = input("Enter a text: ")
width = int(input("Enter a width: "))
if len(text) < width:
    result = text + "0" * (width - len(text))
else:
    result = text
print(result)

