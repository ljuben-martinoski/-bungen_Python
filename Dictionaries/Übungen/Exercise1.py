"""Exercise 1 — Build and Access
Create a dictionary called book with these keys: 
title, author, year, pages. 
Then print each value using both [] notation and .get(). 
Try .get() on a key that doesn't exist (like "rating") and provide a default value of "Not rated"."""

book = {
    "title": "John Greshanm",
    "author": "John Wayn",
    "year": 2002,
    "pages": 345
}

print(book["author"])
print(book["year"])
print(book.get("pages"))

