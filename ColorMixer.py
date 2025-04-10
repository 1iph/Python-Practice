print("Color Mixer")


color_mixes= {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
}
while True:
  first_color = input("Enter your first color: ")
  second_color = input("Enter your second color: ")
  mix = None

  if (first_color,second_color) in color_mixes:
    mix =  color_mixes[(first_color,second_color)]
  if mix:
    print(f"When you mix {first_color} and {second_color}, you get {mix}!")  
  else:
    print("Hmm, Im not sure")  
  proceed = input("Would you like to continue? (y/n): ") 
  if proceed != "y":
    print("Goodbye")
    break