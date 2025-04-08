print("Word Scrambler")
import random
word = input("Enter a word to scramble: ")
def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)
scrambled = scramble_word(word)
print(f"Scrambled word: {scrambled}")

