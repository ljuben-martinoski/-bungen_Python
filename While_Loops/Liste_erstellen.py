"""
Es soll die Eingabe der Temperaturen so gestaltet werden, dass diese in einer Liste für weitere 
Verwendungen gespeichert werden. 
"""


def liste_erstellen():
    try:

        anzahl = 6
        i = 0
        temperaturen = []
        summe = 0
        while i < anzahl:
            print("Geben Sie die {0} Temperatur in °C ein:".format(i + 1))
            eingabe = float(input())
            temperaturen.append(eingabe)
            summe = summe + temperaturen[i]
            i = i + 1
        durchschnitt = summe / anzahl#
        print("Der Durchschnitt beträgt:", durchschnitt)
        


    except Exception as e:
         print(" Es istn die folgende Fehler aufgethreten: \n" + e.args[0])

liste_erstellen()                 