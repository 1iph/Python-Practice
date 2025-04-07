print("TEXT FORMATER")
text = input("Enter a text: ")
print("1. Uppercase")
print("2. Lowercase")
print("3. Titlecase")
print("4. Capitalize")
 
format = input("Choose a format (1-4): ")
if format == "1":
    print(text.upper())
elif format == "2":
    print(text.lower())
elif format == "3":
    print(text.title())
elif format == "4":
    print(text.capitalize())
else:
    print("Invalid format")