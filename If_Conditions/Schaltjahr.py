"""
Schreiben Sie ein Programm, welches nach der Eingabe einer Jahreszahl ausgibt, ob es sich um ein 
Schaltjahr handelt oder nicht. Ein Jahr ist ein Schaltjahr, wenn die Jahreszahl durch 4 und nicht 
durch 100 teilbar ist. Ausnahme: Ein Jahr ist ein Schaltjahr, wenn es durch 4 und durch 100 und 
durch 400 teilbar ist. 
"""


def schaltjahr_berechnen():
    try:
        schaltjahr = int(input("Geben sie die Jahr, und ich sag dir wenn das ist ein Schaltjahr: "))
        if schaltjahr % 4 == 0 and schaltjahr % 100 != 0 or schaltjahr % 400 == 0:
            print(f"{schaltjahr} ist ein Schaltjahr.")
        else:
            print(f"{schaltjahr} ist kein Schaltjahr.")
                   
    except Exception as e:
        print("Es ist die folgende Fehler aufgethreten: \n" + e.args[0])

schaltjahr_berechnen()
                    
