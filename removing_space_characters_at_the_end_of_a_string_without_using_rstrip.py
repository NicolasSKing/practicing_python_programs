text = input("Enter a text: ")
while text != "" and text[-1] == " ":
    text = text[:-1]
print(repr(text))
