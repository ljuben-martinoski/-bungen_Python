"""Schreiben Sie ein Programm, dass nach der Eingabe zweier Gleitkommazahlen die kleinste Zahl aus
gibt. """



def gleikommzahlen_vergleichung():
    try:
     zahl1 = float(input("Geben sie eine Gleitkommazahl ein: "))
     zahl2 = float(input("Geben sie eine weitere Gleitkommazahl ein: "))
    
     if zahl1 > zahl2:
        print("Die erste zahl ist größer dan die zweite zahl")
     else:
        print("Die zweite zahl ist großer dan die erste zahl")

    except Exception as e:
       print("Es ist die folgender Fehler aufgetrete: \n" + e.args[0])

gleikommzahlen_vergleichung()