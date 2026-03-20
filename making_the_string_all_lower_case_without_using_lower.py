text = input("Enter a text: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
result = ""
for ch in text:
    if ch in upper:
        index = upper.index(ch)
        result += lower[index]
    else:
        result += ch
print(result)


