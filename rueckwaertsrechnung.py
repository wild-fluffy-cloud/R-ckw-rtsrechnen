print("Hallo und herzlich willkommen beim Rückwärtsrechner.")
gewinn_raw = input("Welche Gewinnsumme soll ausgeschüttet werden? - ")
gewinn = float(gewinn_raw)
rabatt_raw = input("Welcher Rabatt wird dem Kunden gutgeschrieben (in %) ?")
rabatt = float(rabatt_raw)
prozent_liste = gewinn / (100-rabatt)
liste = prozent_liste * 100
print(liste)