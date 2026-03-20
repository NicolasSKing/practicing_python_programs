text = input("Enter a text: ")
width = int(input("Enter a width: "))
if len(text) < width:
    total_space = width - len(text)
    left = total_space // 2
    right = total_space - left
    result = "*" * left + text + "*" * right
else:
    result = text
print(result)
