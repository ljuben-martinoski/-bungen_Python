

# a) Flatten this nested list: [[1, 2], [3, 4, 5], [6]]
# b) Find the index of the maximum value in [23, 67, 12, 89, 45]
# c) Create pairs from two lists: [1,2,3] and ['a','b','c'] → [(1,'a'), (2,'b'), (3,'c')]
# d) Remove duplicates from [1, 2, 2, 3, 4, 3, 5, 1] while preserving order


#a)
nested = [[1, 2], [3, 4, 5], [6]]
flat = [item for sublist in nested for item in sublist] # basicaly is saying that take the items from this list and put tehm in normal not nested list.
print(flat)


#b)
numbers = [23, 67, 12, 89, 45]
max_value = max(numbers) # finding the max value in the list
max_index = numbers.index(max_value) # finding at waht index is the max value
print(f"Max: {max_value} at index {max_index}")


#c)

numb = [1,2,3]
leter = ['a','b','c']
combination = list(zip(numb, leter)) # list ()- funktion that converts other data types in lists, zip() funktion that takes elements from the same position in each list and pairs them together
print(combination)

#d)

original = [1, 2, 2, 3, 4, 3, 5, 1]
rem_duplicates = []
[rem_duplicates.append(x) for x in original if original not in rem_duplicates] # with list comprehesions, with .append() in the empty list 
# then with for loop to select and remove the duplicates
print(rem_duplicates)


















