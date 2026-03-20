text = input("Enter a text: ")
parameter = input("Enter a prefix to check: ")
if text[:len(parameter)] == parameter and len(parameter) < len(text):
    print("True")
else:
    print("False")