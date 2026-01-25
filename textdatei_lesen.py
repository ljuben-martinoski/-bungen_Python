"""
Lesen von textdatei
"""

import sys

try:
    file = open("Beispiel.txt", "r")
    text = file.read()#
    print(text)
    file.close()
except IOError:
    print("Datei kann nicht geöffnet werden")
except Exception as e:
    print("Es ist die folgender Fehler aufgetreten: \n", sys.exc_info()[0])   
         