"""
Beispiel für das Schreiben von Textdateien in Python 
"""

import sys # Für die Ausnahmebehandlung

try:
    text = input("Geden sie bitte eine text ein: \n")
    file = open("Beispiel.txt","w") # erstellen file als daeiobjekt im schreibmodus
    file.write(text) # Schreiben des Textes in die Datei
    file.close()
    print("Der text wurde erfolgreich gespeichert")
except IOError: # Input Output error
    print("Datei kann nichte geöffnet werden")
except: 
    print("Es ist folgender Fehler ausgetreten:", sys.exc_info()[0])        

