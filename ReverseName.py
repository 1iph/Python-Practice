print("Reverse Name Generator")

while True:
   name = input("Enter you name: ")
   
   reversed_name = name[::-1]
   print(f"Your reversed name is {reversed_name}")

   proceed = input("Wish to continue? (y/n) ")
   if proceed != "y":
     print("Goodbye!")
     break
   