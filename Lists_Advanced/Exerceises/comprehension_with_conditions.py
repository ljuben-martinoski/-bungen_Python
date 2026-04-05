"""
Docstring for Lists_Advanced.Exerceises.comprehension_with_conditions
"""


"""Exercise 2: Comprehensions with Conditions"""

# Using list comprehensions:
# a) Numbers from 1-50 that are divisible by both 3 and 5
# b) Words from ["hello", "hi", "goodbye", "hey", "greetings"] longer than 3 chars
# c) Positive numbers from [-5, 3, -1, 8, -9, 2, 0, 7]
# d) Uppercase words from ["Python", "java", "RUBY", "golang"] (already uppercase)


numbers = [n for n in range(1, 51) if n % 3 == 0 and n % 5 == 0] # serching the numbers that are divisible by 3 and 5
print(numbers)

print("==========================================")


words = ["hello", "hi", "goodbye", "hey", "greetings"]
new_list = [word for word in words if len(word) > 3]
print(new_list)

print("=====================================================")

positive = [-5, 3, -1, 8, -9, 2, 0, 7]
pos_numbers = [n for n in positive if n > 0]
print(pos_numbers)

print("=====================================================")

languages = ["Python", "java", "RUBY", "golang"]
upprecase_words = [word for word in languages if word.isupper()]
print(upprecase_words)






