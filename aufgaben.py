#aufgabe 2
#print ("Hallo Welt, das ist Zweite Aufgabe")
 
name = input("Geben Sie Ihren Namen ein: ")
print (f"Hallo {name}!")

#Aufgabe 3
print("Das ist Aufgabe 3")
def main():
    # Eingabe von drei Variablen
    string_var = input("Gib einen String ein: ")
    int_var = int(input("Gib eine ganze Zahl ein: "))
    float_var = float(input("Gib eine Dezimalzahl ein: "))

    # Ausgabe der eingegebenen Werte
    #print("\nEingegebene Werte:")
    #print("String Variable:", string_var)
    #print("Integer Variable:", int_var)
    #print("Float Variable:", float_var)

    # Berechnung und Ausgabe der Division der beiden Zahlen
    if int_var != 0:
        result = float_var / int_var
        #print("\nErgebnis der Division (Dezimalzahl durch Ganzzahl):", result)
    else:
        #print("\nDivision durch Null nicht möglich. Ändere den Wert der Ganzzahl.")

if __name__ == "__main__":
    main()
#Aufgabe 4
#print("Das ist Aufgabe 4")

def main():
    # Eingabe von zwei natürlichen Zahlen
    zahl1 = int(input("Gib die erste natürliche Zahl ein: "))
    zahl2 = int(input("Gib die zweite natürliche Zahl ein: "))
    
    # Berechnung der Summe
    summe = zahl1 + zahl2
    #25= 10+15
    
    # Ausgabe der Summe
 #print("Die Summe der beiden Zahlen ist:", summe)

if __name__ == "__main__":
    main()
    
#Das ist meine 5 Aufgabe
#print("Das ist meine 5 Aufgabe")
def main():
    # Eingabe von drei Dezimalzahlen
    zahl1 = float(input("Gib bitte die erste Dezimalzahl ein: "))
    zahl2 = float(input("Gib  bitte die zweite Dezimalzahl ein: "))
    zahl3 = float(input("Gib  bitte die dritte Dezimalzahl ein: "))
    
    # Berechnung der Summe
    summe = zahl1 + zahl2 + zahl3
    
    # Ausgabe formatiert in Spalten von 10 Zeichen inkl. zwei Nachkommastellen
    #print(f"{zahl1:10.2f} {zahl2:10.2f} {zahl3:10.2f} {summe:10.2f}")

if __name__ == "__main__":
    main()
    
    #Das ist meine 6 Aufgabe
    
    import math
    
    # Gegebene Radien
    radien = [4.0; 7.1; 18.5] 
    # das wird mit folgenden Formeln berechnet:
    Umfang: U = 2πr
    Fläche: F = πr2
    Volumen: V = 4/3 πr3
    
    print(math.pi)
    
    #
    import math

def main():
    # Gegebene Radien
    radien = [4.0, 7.1, 18.5]

    for r in radien:
        # Berechnungen
        umfang = 2 * math.pi * r
        flaeche = math.pi * r**2
        volumen = (4/3) * math.pi * r**3
        
        # Ausgabe
        print(f"Für r = {r}:")
        print(f"Umfang des Kreises: {umfang:.2f}")
        print(f"Fläche des Kreises: {flaeche:.2f}")
        print(f"Volumen der Kugel: {volumen:.2f}\n")

if __name__ == "__main__":
    main()

    
    
    
    
    
    




