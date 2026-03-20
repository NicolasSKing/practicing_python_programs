text = input("enter a string: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
result = ""
for ch in text:
    if ch in lower:
        index = lower.index(ch)
        result += upper[index]
    elif ch in upper:
        index = upper.index(ch)
        result += lower[index]
    else:
        result += ch
print(result)