"""
Schreiben Sie ein Programm, dass nach der Eingabe dreier Gleitkommazahlen die größte Zahl aus
gibt. 
"""

def gleitkommazahl_vergleichung():

    try:
        print("Bitte geben sie drei zahlen ein,und ich sage dir welche zahl ist die großest!")

        zahl1 = float(input("Geben sie die erste Zahl ein: "))
        zahl2 = float(input("Geben sie die zweite Zhal ein: "))
        zahl3 = float(input("Geben sie die dritte Zahl ein: "))

        if zahl1 > zahl2 and zahl1 > zahl3:
         print("Die erste zahl ist die großest! ")
        if zahl2 > zahl1 and zahl2 > zahl3:
         print("Die zweite zahl ist die großest! ")
        if zahl3 > zahl2 and zahl3 > zahl1:
         print("Die dritte zahl ist die großest! ")

    except Exception as e:
      print("Es ist die folgende Fehler aufgetreten: \n" + e.args[0])

gleitkommazahl_vergleichung()

    


