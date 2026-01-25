"""

Laut Pflichtenheft soll ein Programm entwickelt werden, welches folgende Figur auf dem Bildschirm 
ausgibt: -----1-----1-----1----
Hinweis: Es sind 23 Zeichen. Nach jeweils fünf waagerechten Strichen kommt ein senkrechter Strich. 
Verwenden Sie eine kopfgesteuerte Schleife. Bitte jedes Zeichen einzeln ausgeben und nicht die 
Möglichkeiten von print verwenden. 
"""


def figur_erstellen():
    try:
        for i in range(23):
            if (i + 1) % 6 == 0: #  Jede sechste Position ist ein senkrechter Strich
                print("|", end="")
            else:
                print("-", end="")
        print()  # Für einen Zeilenumbruch nach der Ausgabe der Figur
    except Exception as e:
        print("Es ist die folgende Fehler aufgetreten: \n" + e.args[0])


figur_erstellen()          