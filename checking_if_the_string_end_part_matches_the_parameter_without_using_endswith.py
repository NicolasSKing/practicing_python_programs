text = input("Enter a text: ")
suffix = input("Enter suffix to check: ")
if text[-len(suffix):] == suffix and len(suffix) <= len(text):
    print("True")
else:
    print("False")