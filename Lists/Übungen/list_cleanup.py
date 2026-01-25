"""
Docstring for Lists.Übungen.list_cleanup
"""


# Given: scores = [85, 92, 78, 92, 88, 92, 95]
# Remove all occurrences of 92 (hint: use a while loop with .remove())
# Sort the remaining scores from highest to lowest
# Print the final list




def list_cleanup():
    scores = [85, 92, 78, 92, 88, 92, 95]
    i = 92 # wir geben welches number wir möchten suchen 
    while i in scores:
        scores.remove(i)# entfernen die number 92
    scores.sort(reverse = True) # sortieren die liste vom hohes bis kleinste 
    print(scores)

list_cleanup()    










