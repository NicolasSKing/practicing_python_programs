text = input("Enter a word: ")
index = 0
while index < len(text) and text[index] == " ":
    index += 1
new_text = text[index:]
print("Result:", new_text)


