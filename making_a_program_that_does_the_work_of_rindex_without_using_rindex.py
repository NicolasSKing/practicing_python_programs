def find_last_index(text, target):
    for i in range(len(text) -1,-1,-1):
        if text[i] == target:
            return i
    return -1
word = input("Enter a word: ")
letter = input("Enter a letter to find: ")
result = find_last_index(word, letter)
if result != -1:
    print(f"last occurrence at index: {result}")
else:
    print("Word not found")

