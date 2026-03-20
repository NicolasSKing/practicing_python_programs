text = input("Enter a text: ")
suffix = input("Enter a text that you want to remove at the end of it: ")
if text[-len(suffix):] == suffix:
    text = text[:-len(suffix)]
    print(text)