"""
Practices for strings.
"""
# take a sentence and print every other character
sentence = "Im learning python and im having fun!"
print(sentence[::2])

# revers  a string
print(sentence[::-1])
# count how mamny time the letter "a"´appear in the string
print(sentence.count("a"))

#Replace all spaces in a string with underscores.
print(sentence.replace(" ", "_"))

# Assignment:
#Create a text formatter program that:

#Takes a sentence (use a variable, don't use input() yet)
#Prints the sentence in uppercase
#Prints the sentence in title case
#Prints the number of words (hint: use .split())
#Prints the sentence reversed
#Replaces all vowels with asterisks

new_sentence = "Josif is mein Sohn und ich liebe ihn  sehr viel!" # hier wir zuordnen eine variable auf dem typ String. 
print(new_sentence.upper()) # alle buchstaben sind als groß außgegeben.
print(new_sentence.title())
print(len(new_sentence.split()))  # number of words
print("==================================================================")
print(new_sentence[::-1])
print(new_sentence.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*").replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*"))
