"""
Docstring for Lists_Advanced.Exerceises.Exerceise_1_basic_comprehension
"""
"""
1. Excerseisess for List Comprehension"""



# Create these lists using list comprehensions:
# a) Squares of numbers from 1-10
# b) Only the odd numbers from 1-20
# c) First letter of each word in ["python", "java", "ruby", "golang"]
# d) Lengths of words in ["cat", "elephant", "dog", "hippopotamus"]


squares = [x ** 2 for x in range(1, 11)]
print(squares)

print("========================================================")

squares2 = [i for i in range(1, 21) if i % 2 == 0] # i for i in range(1,21) gets each number from 1 to 20, if i % 2 == 0 filters only the even numbers
print(squares2)

print("=====================================================")

words = ["python", "java", "ruby", "golang"]
first_letters = [item[0] for item in words] # item[0] gets the first letter of each word in the list words
print(first_letters)

words2 = ["cat", "elephant", "dog", "hippopotamus"]
find = [len(word) for word in words2]
print(find)
