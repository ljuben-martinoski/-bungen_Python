""" Combining What You Know
Given a list of names:
pythonnames = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice"]
Build a dictionary that counts how many times each name appears, using a loop (no imports — do it manually). Result should be: {"Alice": 3, "Bob": 2, "Carol": 1}
Hint: Use .get() with a default of 0 to handle names you haven't seen yet."""


names = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice"]

# The intended approach — O(n), touches each name exactly once
count_dic = {}
for name in names:
    count_dic[name] = count_dic.get(name, 0) + 1

