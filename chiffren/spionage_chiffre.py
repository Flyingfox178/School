# Spionage Chiffre
# Joris, Alexander, Nils
# 27.09.2024

def spionage(pt, kw, knm1, knm2, knc): #pt = Plain Text/Klartext, kw = keyword/Schlüsselwort, knm = Key Numbers matrix/Schlüsselzahlen Matrix, kns = Key Number Columns/Schlüsselzahl Spalten
    
    chiffre = st(knc, matrix(pt, kw, knm1, knm2))
    
    return chiffre

def matrix(pt, kw, kn1, kn2): #pt = Plain Text/Klartext, kw = keyword/Schlüsselwort, kn = Key Numbers/Schlüsselzahlen
    
    pt = pt.lower()
    kw = kw.lower()
    
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","*","/"]
    for i in set(kw):
        alph.remove(i) #Keywordbuchstaben aus dem Alphabet entfernen

    
    matrix_list = [[],[],[]]

    col = 0
    row = 0

    for i in kw:
        if row == 0 and col == kn1 or col == kn2:
            matrix_list[row].append("")
            if col >= 9:
                row += 1
                col = 0
            else:
                col += 1
        matrix_list[row].append(i)
        if col >= 9:
            row += 1
            col = 0
        else:
            col += 1

    for i in alph:
        matrix_list[row].append(i)
        if col >= 9:
            row += 1
            col = 0
        else:
            col += 1

    
    cipher = ""

    for i in pt:
        for row in range(len(matrix_list)):
            for col in range(len(matrix_list[row])):
                if i == matrix_list[row][col]:
                    if row == 0:
                        cipher += str(col)
                    elif row == 1:
                        cipher += str(kn1) + str(col)
                    else:
                        cipher += str(kn2) + str(col)
    #print(f"Debug: cipher= {cipher}")
    return cipher

    # Spionage - Chiffre
def st(schluessel, klartext):
    # 1. Tabelle erstellen und zeilenweise mit den Werten füllen

    #print(f"Debug: schlüssel = {schluessel}, kt = {klartext}")
    
    klartext = list(klartext)  # Klartext in Liste umwandeln
    liste = [[] for _ in range(3)] # Leere zweidimensionale-Liste/ Tabelle mit fester Zeilenanzahl (3) erstellen
    
    index = 0
    for i in range(3):  # Zeilen
        for j in range(schluessel):  # Spalten
            if index < len(klartext):  # Überprüfen, ob es noch Elemente in Klartext gibt
                liste[i].append(klartext[index])
                index += 1
            else:
                break # wenn keine weiteren Klartextzeichen verfügbar, Listen nicht weiter auffüllen
    
    #print(liste) # ursprüngliche Tabelle zum debuggen ausgeben
    
    
    # 2. Tabelle spaltenweise auslesen

    geheimtext = "" # Geheimtext als leere Liste anlegen
    
    for x in range(schluessel):
        for y in range(len(liste)):
            if x < len(liste[y]):  # Überprüfen, ob es ein Element in dieser Spalte gibt
                geheimtext += str(liste[y][x])  # Einfügen in die entsprechende Spalte

    return geheimtext

# Beispielaufruf
#print(st(4, "328547091"))

print(spionage("Dreiuhr", "Steinrad", 1, 4, 4))