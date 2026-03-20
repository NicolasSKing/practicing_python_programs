def find_index(text, target):
    for i in range(len(text)):
        if text[i] == target:
            return i
    return -1
word = input("Enter a word: ")
letter = input("Enter a letter to find: ")
result = find_index(word, letter)
if result != -1:
    print(f"Found at index: {result}")
else:
    print("Word not found")
