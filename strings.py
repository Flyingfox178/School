string = "Hallo"

#Bestimmen der Länge einer Zeichenkette
print("Die Länge von der Zeichenkette ist: ", len(string)) #Die Funktion len() gibt die Länge der Zeichenkette zurück.


#Auslesen eines Zeichens an einer bestimmten Position
print("Das 3. Zeichen von der Zeichenkette ist: ", string[2]) #Man kann wie in einer Reihung auf bestimmte Stellen in der Zeichenkette indexbasiert zugreifen.

#Verändern eines Zeichens an einer bestimmten Stelle
def setCharAt(string, index, char):
    newString = ""
    for i in range(len(string)):
        if(i == index):
            newString += char
        else:
            newString += string[i]
    return newString

string = setCharAt(string, 1, 'e')
print(string)

#Verbinden von zwei Zeichenketten zu einer
newString = string + " Welt" #Man kann zwei oder mehr Zeichenketten zu einer neuen Zeichenkette addieren. Die neue Zeichenkette ist dann einen aneinanderreihung der Zeichenketten.
print(newString)


#Prüfen des Inhalts von zwei Zeichenketten auf Gleichheit
str1 = "Hund"
str2 = "Hund"
str3 = "Katze"

print("Sind str1 und str2 gleich? ", str1 == str2) #Man kann zwei Zeichenketten mit dem == auf Gleichheit überprüfen.
print("Sind str1 und str3 gleich? ", str1 == str3) #Als Rückgabe erhält man einen Wahrheitswert (Boolean) also True oder False.


#Lexikographisches (alphabetisches) Vergleichen von zwei Zeichenketten
strAbc = "abc"
strDef = "def"

print("Ist strAbc im Alphabet weiter vorne als strDef? ", strAbc < strDef) #Zwei Zeichenketten werden mit den uns bekannten Vergleichszeichen verglichen, auch hier wird ein Wahrheitswert (Boolean) zurückgegeben.