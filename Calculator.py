print("Simple Calculator")




while True:
 print("1. Addition")
 print("2. Subtraction")
 print("3. Multiplication")
 print("4. Division")
 calc_type = int (input("Enter choice (1-4): "))
 first_number = int (input("Enter first number: "))
 second_number = int (input("Enter second number: "))

 if calc_type == 1:
   result = first_number + second_number
   print(f"{first_number} + {second_number} = {result}")
 elif calc_type == 2:
   result = first_number - second_number
   print(f"{first_number} - {second_number} = {result}")
 elif calc_type == 3:
   result = first_number * second_number
   print(f"{first_number} x {second_number} = {result}")
 elif calc_type == 4:
   if second_number == 0:
     print("You cannot divide by zero 😅")
   else:
     result = first_number / second_number
     print(f"{first_number} ÷ {second_number} = {result} ")
 proceed = input("Would you like to do another calculation? (yes/no): ")
 if proceed != "yes":
  ("Thank you for using this app! Goodbye")
  break