"""
Es soll mithilfe einer Schleife die Eingabe von sechs Temperaturdaten ermöglicht und die gleichzei
tige Berechnung der Durchschnittstemperatur durchgeführt werden. 
"""

def durchschnittstemperatur_berechnen():
    try:
        summe = 0 # initialisierung der summe
        anzahl = 6  # das sagt uns die anzahl der Temperaturen, die eingegeben werden sollen

        for i in range(anzahl):
            temperatur = float(input(f"Geben Sie die Temperatur {i + 1} ein: ")) # eingabe der temperatur das verbunds mit der anzahl(hier sechs mal zu eingeben)
            summe += temperatur # summierung der temperaturen

        durchschnitt = summe / anzahl # berechnung der durchschnittstemperatur
        print(f"Die Durchschnittstemperatur beträgt: {durchschnitt:.2f}°C") # ausgabe der durchschnittstemperatur mit zwei nachkommastellen

    except Exception as e:
        print("Es ist die folgende Fehler aufgetreten: \n" + e.args[0])

durchschnittstemperatur_berechnen()

