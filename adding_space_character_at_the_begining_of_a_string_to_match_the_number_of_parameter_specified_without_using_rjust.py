text = input("Enter a text: ")
width = int(input("Enter a width: "))
if len(text) < width:
    result = (width - len(text)) * " " + text
else:
    result = text
print(result)
