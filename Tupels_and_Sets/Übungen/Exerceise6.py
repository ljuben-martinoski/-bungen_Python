"""Exercise 6 — Practical Application
Write a program that:

Asks the user to enter a sentence
Finds all unique words in the sentence (use .split() and a set)
Prints the number of total words and the number of unique words
Prints the unique words in sorted order (hint: sorted() works on sets)"""

def word_game():
    user = str(input("Please enter a whole sentence and i will tell you: \nHow many uniqe words are there.\nNumber of all the words and unique words.\n"))
    word_list = user.lower().split()
    unique_words = set(word_list)
    total_words = len(word_list)
    sorted_words = sorted(unique_words)

    print(f"Total Words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Sorted unique words: {sorted_words}")


word_game()
               