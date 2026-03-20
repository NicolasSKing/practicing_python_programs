text = input("Enter a text: ")
is_it_a_letter = False
all_upper = True
for ch in text:
    if ch.isalpha():
        is_it_a_letter = True
        if not ("A" <= ch <= "Z"):
            all_upper = False
            break
if is_it_a_letter and all_upper:
    print("True")
else:
    print("False")
