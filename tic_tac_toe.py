# GLOBALE VARIABLEN
field = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Ich habe eine einzige Liste erstellt, sodass die Elemente direkt über ihren Index gegriffen werden können. Die Alternative wäre gewesen, drei Listen zu erstellen, eine pro Zeile, was jedoch eine weitere Stufe zu den Zugriffsverfahren bedeutet hätte.
# Ich glaube, ich habe die die Elemente der Liste als String erstellt, sodass that ich nochmals mit 'try:' ('if:',  'else:') und 'except:' experimentieren konnte.

# SPIELFELD
def print_field():

    for element in range(len(field)):
    # 'element' Frei gewählte Variablenname. Normalerweise wird 'i' für Iterationen gewählt. Ich finde 'element' jedoch expliziter.
    # 'range' Nutz immer die Indices.
    # 'len' Bezieht sich nicht auf den Index, sondern auf die Länge der Liste. Das heißt von 1 bis 9. Man könnte hier sagen, das 'len' stellt die ganze Liste für 'range' zur Verfügung.

        if element in [2, 5, 8]:
        # '[2, 5, 8]' Sie sind der Index der Elemente, nach dem ein Zeilenumbruch eingefügt werden sollte.

            print(field[element])
            # 'print(field[element], end="\n")'
            # Fügt einer Zeilenumbruch nach den Elementen mit Index 2, 5 und 8. Der optionale Parameter ' end="" ' von "print()" - da optional, nicht explizit angegeben - erhält kein Argument. Deswegen wird der Standardwert angewendet d. h. ' end="\n" ', was einen Zeilenumbruch erzeugt.

        else:

            print(field[element], end=" | ")
            # ' end=" | " ' Eine Iteration gibt alle Elemente der Liste einzeln aus, ohne die eckigen Klammern am Anfang und Ende der Liste sowie ohne die Anführungszeichen jedes Elements. Außerdem gibt eine Iteration die Elemente nicht nacheinander, sondern untereinander aus.

print_field()
# 'print_field()'-Funktion wird direkt nach ihrer Definition aufgerufen.

## SPIELZUG UMSETZEN
def turn():


# ----
# Folgendes ist das, was ich eigentlich machen wollte. Hier geht es nur um die Umsetzung. Die Syntax ist höchstwahrscheinlich falsch.

# def turn(player, symbol)

#   turn_odd_even = 1
#
#   while True:
#
#   if turn_odd_even % 2 == 1:
#
#       turn("SPIELER 1", "X")
#
#   elif turn_odd_even % 2 == 0:
#
#       turn("SPIELER 2", "0")
#
#   turn_odd_even += 1
# ----

    turn_odd_even = 1
    # Counter-Variable

    while True:

        if all(field[i] == "X" for i in [0, 1, 2]) or all(field[i] == "X" for i in [3, 4, 5]) or all(field[i] == "X" for i in [6, 7, 8]) or all(field[i] == "X" for i in [0, 3, 6]) or all(field[i] == "X" for i in [1, 4, 7]) or all(field[i] == "X" for i in [2, 5, 8]) or all(field[i] == "X" for i in [0, 4, 8]) or all(field[i] == "X" for i in [2, 4, 6]):
        # 'all()'-Prüft, ob alle Elemente an den Indizes 0, 1 und 2 der Liste 'field[]' den Wert "X" haben.

            print("SPIELER 1, du hast gewonnen!")
            break
            # 'break' Das Programm stoppt, sobald einer der Spieler gewinnt. Ich bin mit der 'break'-Lösung noch nicht ganz zufrieden, da ich sie nicht ganz verstehe.

        elif all(field[i] == "O" for i in [0, 1, 2]) or all(field[i] == "O" for i in [3, 4, 5]) or all(field[i] == "O" for i in [6, 7, 8]) or all(field[i] == "O" for i in [0, 3, 6]) or all(field[i] == "O" for i in [1, 4, 7]) or all(field[i] == "O" for i in [2, 5, 8]) or all(field[i] == "O" for i in [0, 4, 8]) or all(field[i] == "O" for i in [2, 4, 6]):
        # 'all()'-Prüft, ob alle Elemente an den Indizes 0, 1 und 2 der Liste 'field[]' den Wert "X" haben.

            print("SPIELER 2, du hast gewonnen!")
            break
            # 'break' Das Programm stoppt, sobald einer der Spieler gewinnt. Ich bin mit der 'break'-Lösung noch nicht ganz zufrieden, da ich sie nicht ganz verstehe.

        elif turn_odd_even % 2 == 1:
        # Wenn der Counter eine ungerade Zahl ist.

            player = "SPIELER 1"
            symbol = "X"

        # Dies ist eine explizitere und längere Version aber nicht notwendig. Siehe direkt danach.
        # elif turn_odd_even % 2 == 0:
            # player = "SPIELER 2"
            # symbol = "O"

        else:
        # Wenn der Counter eine gerade Zahl ist.

            player = "SPIELER 2"
            symbol = "O"

        choice = input(player + ", bitte gib das gewünschte Feld ein: ")

        try:
        # 'try:' Die 'try:'- und 'except:'-Anweisung wird verwendet, um Fehler innerhalb des Codes zu behandeln, ohne dass das Programm abstürzen muss. Der 'try:'-Block wird ausgeführt, wenn kein Fehler vorliegt. Stößt das Programm im 'try:'-Block auf einen Fehler, wird der Code innerhalb des Except-Blocks ausgeführt. Eine 'try:'-Anweisung kann mehrere 'except:'-Anweisungen enthalten.

            compare = int(choice) - 1
            # 'compare'-Variable nimmt den Benutzer-String von 'choice'-Input und versucht, ihn in eine Ganzzahl umzuwandeln. Wenn dies gelingt, wird 1 abgezogen, um einen Index in der 'field'-Liste zu referenzieren.

            # Dies ist eine explizitere und längere Version aber nicht notwendig. Siehe direkt danach.
            # if field[compare] == "X" or field[compare] == "O":
            # Hier wird logischerweise der Vergleichsoperator '==' und nicht der Zuweisungsoperator '=' nach dem Variablennamen verwendet. Es wird nun getestet, ob die beiden Werte gleich sind, und es wird 'True' oder 'False' zurückgegeben.

            if field[compare] in ["X", "O"]:

                print("Dieses Feld ist schon belegt. ", end="")

            elif compare in range(len(field)) and field[compare] not in ["X", "O"]:
            # 'range' Nutz immer die Indices.
            # 'len' Bezieht sich nicht auf den Index, sondern auf die Länge der Liste. Das heißt von 1 bis 9. Man könnte hier sagen, das 'len' stellt die ganze Liste für 'range' zur Verfügung.
            # 'field[compare] not in ["X", "O"]' Dies bedeutet, dass alle Elemente, die im Range sind, gewählt werden können, außer diejenigen, die bereits mit 'X' oder '0' belegt sind.

                field[compare] = symbol
                # Ersetzt das Element mit dem Index 'compare' durch "X" oder "O".

                print_field()
                # 'print_field()'-Funktion wird aufgerufen, um das Spielfeld mit der Veränderung erneut zu erzeugen.

                turn_odd_even += 1
                # Nur hier wird der Counter angewendet. Das bedeutet, dass der Benutzer eine korrekte Zahl eingegeben hat und die 'while'-Schleife für den nächsten Benutzer erneut beginnen kann.

            # Dies ist eine explizitere und längere Version aber nicht notwendig. Siehe direkt danach.
            # elif compare not in range(len(field)):

            else:

                print("Die eingegebene ganze Zahl muss zwischen 1 und 9 liegen. ", end="")
                # ' end="" ' Optionaler Parameter von 'print()', um den standardmäßigen Zeilenumbruch zu unterdrücken. Das Standardargument ist dann ' end="\n" '

        except ValueError:
        # Jeder Wert, der sich nicht in ein 'int' umwandeln lässt ('str', 'float'), führt hier zu einem 'ValueError'.
        # 'try:' Die 'try:'- und 'except:'-Anweisung wird verwendet, um Fehler innerhalb des Codes zu behandeln, ohne dass das Programm abstürzen muss. Der 'try:'-Block wird ausgeführt, wenn kein Fehler vorliegt. Stößt das Programm im 'try:'-Block auf einen Fehler, wird der Code innerhalb des Except-Blocks ausgeführt. Eine 'try:'-Anweisung kann mehrere 'except:'-Anweisungen enthalten.

            print("Ihre Angabe ist keine ganze Zahl. ", end="")
        # ' end="" ' Optionaler Parameter von 'print()', um den standardmäßigen Zeilenumbruch zu unterdrücken. Das Standardargument is ' end="\n" '

turn()