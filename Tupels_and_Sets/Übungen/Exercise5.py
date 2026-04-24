"""Exercise 5 — Set Operations
Two classes took an exam:
pythonclass_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
class_b = {"Charlie", "Diana", "Frank", "Grace", "Eve"}
Using set operations, find and print:

All students across both classes (union)
Students in both classes (intersection)
Students only in Class A (difference)
Students only in Class B (difference)
Students in exactly one class, not both (symmetric difference)"""


class_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
class_b = {"Charlie", "Diana", "Frank", "Grace", "Eve"}


all_students = class_a | class_b

both_classes = class_a & class_b
only_classA = class_a - class_b
only_classB = class_b - class_a
exclusiv = class_a ^ class_b
print(f"All Students: {all_students}\nBoth classes:  {both_classes}\nOnly in class A {only_classA}\nOnly in Class B {only_classB}\nStudents exactly in one class not in the both {exclusiv}")
