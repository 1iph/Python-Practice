print("CHARACTER CHECKER")
text = input("Enter a text: ")
if text.isalpha():
    print("The text is a letter.")
elif text.isdigit():
    print("The text is a number.")
elif text.isspace():
    print("The text is a space.")
elif text.isupper():
    print("The text is uppercase.")
elif text.islower():
    print("The text is lowercase.")
