print("Vowel Counter")

while True:
    text = input("Enter your text: ")
   

    vowel_count = 0
    for letter in text.lower():
       if letter in ["a", "e", "i", "o", "u"]:
        vowel_count +=1
    print(f"Your text has {vowel_count} vowels in it")
    done = input("Wish to proceed (y/n): ")
    if done.lower() != "y":
        print("Goodbye!")
        break
    