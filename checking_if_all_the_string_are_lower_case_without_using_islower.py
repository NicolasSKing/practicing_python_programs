text = input("Enter a text: ")
is_it_a_string = False
all_lower = True
for ch in text:
    if ch.isalpha():
        is_it_a_string = True
        if not ("a" <= ch <= "z"):
            all_lower = False
            break
if is_it_a_string and all_lower:
    print("True")
else:
    print("False")




