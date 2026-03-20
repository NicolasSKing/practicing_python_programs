text = input("Enter text: ")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
if text:
    first_char = text[0]
    if first_char in lower:
        result += upper[lower.index(first_char)]
    else:
        result += first_char
    for ch in text[1:]:
        if ch in upper:
            result += lower[upper.index(ch)]
        else:
            result += ch
print("Capitalized:", result)