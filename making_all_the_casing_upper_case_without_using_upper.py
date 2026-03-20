text = input("Enter a text: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
result = ""
for ch in text:
    if ch in lower:
        index = lower.index(ch)
        result += upper[index]
    else:
        result += ch
print(result)