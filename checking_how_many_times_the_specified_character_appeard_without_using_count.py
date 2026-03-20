text = input("Enter a text: ")
target = input("Enter a string or word that you want to count: " )
count = 0
for ch in text:
    if ch == target:
        count += 1
print(count)





