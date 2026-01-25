"""
Screiben sie eine Funktion das über prüft die Alter.
"""


def age_checker():
    try:
        print("Eingebe deinen Alter und ich sagt Ihne bist du Erwachsen, Oder Junge.")
        alter = int(input("Gibt hier deine Alter: "))
        if alter < 18:
            print("Du bist ein Junge.")
        else:
            print("Du bist Erwachsen.")
 
    except Exception as e:
        print("Es ist die folgenden Fehler gethreten: \n" + e.args[0])      
age_checker()