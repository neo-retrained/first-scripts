# IMPORTIERTE BIBLIOTHEKEN

# import os
#
# def clear_terminal():
#     os.system("clear")
#
# 'clear_terminal():'-Importierte Funktion aus 'import os', die das Terminal leeren sollte. Das funktioniert nicht,
# es muss etwas zusätzlich in PyCharm oder direkt im System konfiguriert werden.

# import subprocess
#
# subprocess.call("clear")
# COMMENT

import time

# GLOBALE VARIABLEN

## LISTEN

### Listennamen
main_menu = ["TO-DO \u2705", "EINKAUFSLISTE \U0001F6D2", "NEUJAHRSWÜNSCHE \u2728"]
# Liste mit den Namen aller Listen. Diese Namen sind nicht direkt mit den Listen verbunden, sodass eine manuelle Änderung zu Inkongruenzen führen kann.

### Liste 1: To-Do
todo_list = ["Eltern anrufen", "Wohnung putzen", "Autoöl wechseln", "Arzttermin vereinbaren"]
### Liste 2: Einkaufsliste
shopping_list = ["Gemüse", "Rindfleisch", "Käse", "Cola"]
### Liste 3: Neujahrswünsche
wishes_list = ["Fahrrad fahren", "Twitter abmelden", "Urlaub in Japan", "Sparen"]

### Liste mit allen zu verarbeitenden Listen, für einen einfacheren Zugriff durch ihren Index.
all_lists_list = [todo_list, shopping_list, wishes_list]

def main():
# main():-

    time.sleep(2)

    # HAUPTMENÜ
    print("========================================================================================================")
    print("NOTIZEN-APP")
    print()
    print("---")
    print("IHRE LISTEN")
    print()

    # Alter Code, um die Listennamen im Hauptmenü anzuzeigen:
    # print(main_menu[0]) # Output: Liste 1: To-Do
    # print(main_menu[1]) # Output: Liste 2. Einkaufsliste
    # print(main_menu[2]) # Output: Liste 3. Neujahrswünsche

    # Ich gebe hier die Listennummern mit einer 'for'-Schleife aus. Wenn ich eventuell Listen einfüge, werden sie auch automatisch nummeriert d. H. ist skalierbar.
    for position, list_name in enumerate(main_menu, 1):
    # 'enumerate()' Wird verwendet, um eine Iteration durchzulaufen und gleichzeitig sowohl den Index als auch das Element zu erhalten. Sie gibt ein Enumerate-Objekt zurück, das Paare in der Form (index, element) erzeugt.

    # SYNTAX
    # enumerate(iterable, start)
    # 'iterable' - Iterierbares Objekt (Liste, Tupel, etc.).
    # 'start' Integer, ab der das erste Element des iterierbaren Objekts numeriert werden soll. Standardartwert is "0".Es kann auch ein negativer Integer sein, aber im Prinzip läuft der Zähler nur vorwärts.

        print("Liste " + str(position) + ": " + list_name)
        # Druck alle Listen korrekt numeriert untereinander aus.

    print()
    print("---")
    print("N. Neue Liste erstellen")
    print()
    print("---")
    print("L. Liste löschen")
    print()
    print("---")
    print("0. Programm beenden")
    print()

    print("---")
    print("Wählen Sie eine Liste für weitere Optionen aus.")
    print("Drücken Sie die Taste 'N', um eine neue Liste zu erstellen oder die '0', um das Programm zu beenden.")
    print()
    print("Ihre Wahl: ", end="")
    # ' end="" ' Optionaler Parameter von 'print()', um den standardmäßigen Zeilenumbruch zu unterdrücken. Das Standardargument ist dann ' end="\n" '

    # VARIABLE: Greift der Wahl der Benutzer aus dem Hauptmenü.
    input_list = input()

    # FUNKTION: Gibt den Namen der vom Benutzer ausgewählten oder verarbeiteten Liste und ihrer Elemente aus.
    def print_list(list_name, entries):


        time.sleep(2)

        print("========================================================================================================")
        print("NOTIZEN-APP --> Liste " + list_name)
        print()

        for entry in range(len(entries)):
            # 'for'-Schleife. Iteriert über alle Elemente der vom Benutzer gewählten Liste.

            print(str(entry + 1) + ". " + entries[entry])
            # 'print()' Gibt die iterierten Elemente der Liste in der Konsole aus.

    while True:
    # 'while True:' Erzeugt eine Endlosschleife, die solange ausgeführt wird, bis sie durch eine 'break'-Anweisung, eine Ausnahme oder das Beenden des Programms von innerhalb der Schleife beendet wird.

        try:
        # 'try:' Die 'try:'- und 'except:'-Anweisung wird verwendet, um Fehler innerhalb des Codes zu behandeln, ohne dass das Programm abstürzen muss. Der 'try:'-Block wird ausgeführt, wenn kein Fehler vorliegt. Stößt das Programm im 'try:'-Block auf einen Fehler, wird der Code innerhalb des Except-Blocks ausgeführt. Eine 'try:'-Anweisung kann mehrere 'except:'-Anweisungen enthalten.

            # 0. PROGRAMM BEENDEN
            if input_list == "0":
            # Ein Benutzer-Input ist immer ein String. Ich möchte, dass er weiterhin als String behandelt wird, sodass er nie als Integer interpretiert werden kann. Das würde bedeuten, dass Index gleich 0 ist, was zu einem Fehler führt. Das gilt für jede andere "0" im Rest des Programms.

                time.sleep(2)

                print("---")
                print("Programm beendet")

                break
                # 'break' Beendet die 'while True'-Schleife und hier auch das Programm. Warum auch das Programm beendet wird, verstehe ich nicht ganz.

            # NEUE LISTE ERSTELLEN
            elif input_list.lower() == "n":
            # '.lower()' Die Benutzereingabe wird case-insensitiv gemacht, da der Vergleich mit "n" (kleingeschrieben) durchgeführt wird. Wenn der Benutzer ein großes „N” eingibt, "fragt" sich Python, ob es in ein kleines "n" umgewandelt werden kann. Tatsächlich ist es so. Wenn der Benutzer ein kleines "n" eingibt, funktioniert der Vergleich logischerweise auch.

                time.sleep(2)

                print("---")

                # VARIABLE: Greift den Input der Benutzer, das ist entweder der Name der neuen Liste oder "0" für das Hauptmenü.
                input_new_list = input("Tippen Sie den Namen der neuen Liste ein, oder kehren Sie mit '0' zurück zum Hauptmenü: ")

                # 0. ZURÜCK ZUM HAUPTMENÜ
                if input_new_list == "0":

                    main()
                    # 'main()' Führt das Programm vom Anfang aus bzw. kehrt zum Hauptmenü zurück.

                # NEUE LISTE WURDE ERSTELLT
                else:

                    time.sleep(2)

                    print("---")

                    main_menu.append(input_new_list.upper())
                    # Fügt der Name der neuen Liste am Ende der 'main_menu'-Liste ein.

                    input_new_list = []
                    # Erzeugt aus 'input_new_list' eine leere Liste.

                    all_lists_list.append(input_new_list)
                    # Fügt die neue Liste zur 'function_lists = []' hinzu, also zur Hauptliste mit allen Listen. Ich kann die neue Liste noch über ihren direkten Namen zugreifen.

                    print("Die neue 'Liste " + str(len(main_menu) + 1) + ": " + main_menu[-1] + "' wurde erstellt. "
                                                                                                "Sie werden in 10 "
                                                                                                "sekunden zurück zum "
                                                                                                "Hauptmenü weitergeleitet.")

                    time.sleep(10)

                    main()
                    # 'main()' Führt das Programm vom Anfang aus bzw. kehrt zum Hauptmenü zurück.

            elif input_list.lower() == "l":

                time.sleep(2)

                print("---")

                print("Wählen Sie die Liste aus, die Sie löschen möchten oder kehren Sie mit '0' zurück zum "
                      "Hauptmenü: ", end="")
                input_delete_list = input()

                while True:

                    try:

                        # 0. ZURÜCK ZUM HAUPTMENÜ
                        if input_delete_list == "0":

                            main()

                        elif int(input_delete_list) - 1 in range(len(all_lists_list)):

                            del main_menu[int(input_delete_list) - 1]
                            del all_lists_list[int(input_delete_list) - 1]

                            main()

                        else:

                            time.sleep(2)

                            print("---")
                            print("Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ",
                                  end="")
                            input_delete_list = input()

                            continue
                            # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

                    except ValueError:

                        time.sleep(2)

                        print("---")
                        print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
                        input_delete_list = input()

                        continue
                        # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

            # OPTIONEN ZUR LISTE VERARBEITUNG
            elif int(input_list) - 1 in range(len(all_lists_list)):
            # Universal Code, das erlaubt es, eine Liste mit ihrem Index aus der Hauptliste 'function_lists' auszuwählen.

                # FUNKTION: Gibt die Optionen zur Verarbeitung einer Liste aus.
                def list_options():

                    print_list(main_menu[int(input_list) - 1], all_lists_list[int(input_list) - 1])
                    # Hier wird die Funktion 'print_list()', nach dem Ende der Ausführung einer Option, aufgerufen.

                    print()
                    print("---")
                    print("OPTIONEN")
                    print()
                    print("Option 1: Neuen Eintrag in die Liste einfügen")
                    print("Option 2: Eintrag aus der Liste löschen")
                    print("Option 3: Einträge in alphabetischer Reihenfolge anzeigen")
                    print()
                    print("---")
                    print("0. Hauptmenü")
                    print()
                    print("---")

                    # VARIABLE: Greift den Input der Benutzer, das ist entweder eine Option zur Listeverarbeitung oder "0" für das Hauptmenü.
                    input_option = input("Wählen Sie eine Option aus, oder kehren Sie mit '0' zurück zum Hauptmenü: ")

                    # OPTION WÄHLEN ODER ZURÜCK ZUM HAUPTMENÜ
                    while True:

                        try:

                            # 0. ZURÜCK ZUM HAUPTMENÜ
                            if input_option == "0":

                                main()
                                # 'main()' Führt das Programm vom Anfang aus bzw. kehrt zum Hauptmenü zurück.

                            # 1. NEUE EINTRAG
                            elif input_option == "1":

                                time.sleep(2)

                                print("---")

                                # VARIABLE: Greift den Input der Benutzer, das ist ein neuer Eintrag in der zuvor gewählten Liste oder "0" zurück zu den Optionen zur Verarbeitung der Liste.
                                input_add_entry = input("Tippen Sie Ihren neuen Eintrag oder geben Sie die 0 ein, zurück zu den Optionen: ")

                                # NEUE EINTRAG EINGEBEN ODER ZURÜCK ZU DEN OPTIONEN

                                # ZURÜCK ZU DEN OPTIONEN
                                if input_add_entry == "0":

                                    list_options()

                                # NEUE EINTRAG WURDE EINGEFÜGT
                                else:

                                    (all_lists_list[int(input_list) - 1]).append(input_add_entry.capitalize())
                                    # string.capitalize()
                                    # - Wandelt den ersten Buchstaben eines einer Zeichenfolge in Großbuchstaben um.
                                    # - Wandelt alle anderen Buchstaben in Kleinbuchstaben um.
                                    # - Ignoriert alle Leerzeichen vor den erste Buchstabe.
                                    #
                                    # - Wenn die Zeichenkette mit einem Nicht-Buchstaben beginnt, z. B. einer Zahl oder einem Symbol, bleibt sie unverändert.

                                    time.sleep(2)

                                    print("---")
                                    print("Ihr neuer Eintrag '" + all_lists_list[int(input_list) - 1][-1] + "' wurde in der Liste " + main_menu[int(input_list) - 1] + " eingefügt.")

                                    list_options()

                            # 2. EINTRAG LÖSCHEN
                            elif input_option == "2":

                                time.sleep(2)

                                print("---")
                                print("Wählen Sie den Eintrag aus, den Sie löschen möchten, oder geben Sie die 0 ein, zurück zu den Optionen: ", end="")
                                # VARIABLE: Greift den Input der Benutzer auf, um eine Liste zu löschen oder "0" zurück zu den Optionen zur Verarbeitung der Liste.
                                input_delete_entry = input()

                                # EINTRAG WÄHLEN ODER ZURÜCK ZU DEN OPTIONEN
                                while True:

                                    try:

                                        # ZURÜCK ZU DEN OPTIONEN
                                        if input_delete_entry == "0":

                                            list_options()

                                        # EINTRAG WURDE GELÖSCHT
                                        elif int(input_delete_entry) - 1 in range(len(all_lists_list[int(input_list) - 1])):

                                            time.sleep(2)

                                            print("---")
                                            print("Ihr Eintrag '" + all_lists_list[int(input_list) - 1][int(
                                                input_delete_entry) - 1] + "' wurde aus der Liste " + main_menu[
                                                int(input_list) - 1] + " gelöscht.")

                                            del all_lists_list[int(input_list) - 1][int(input_delete_entry) - 1]

                                            list_options()

                                        # FALSCHE EINGABE BEIM EINTRAG WÄHLEN
                                        else:

                                            time.sleep(2)

                                            print("---")
                                            print("Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ", end="")
                                            input_delete_entry = input()

                                            continue
                                            # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

                                    # FALSCHE EINGABE BEIM EINTRAG WÄHLEN
                                    except ValueError:

                                        time.sleep(2)

                                        print("---")
                                        print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
                                        input_delete_entry = input()

                                        continue
                                        # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

                            # 3. ALPHABETISCHE REIHENFOLGE
                            elif input_option == "3":

                                time.sleep(2)

                                print(
                                    "========================================================================================================")
                                print("Liste " + main_menu[int(input_list) - 1] + " in ALPHABETISCHER REIHENFOLGE:")
                                print()

                                # LISTE IN ALPHABETISCHE REIHENFOLGE AUSGEGEBEN
                                for entry in sorted(all_lists_list[int(input_list) - 1]):
                                    # 'sorted(list)' Zeigt die Liste in alphabetischer Reihenfolge in der Konsole an, anstatt eine neue Liste zu speichern.
                                    # Ist das Gegenteil von 'list_name.sort()'.Speichert eine neue Liste in alphabetischer Reihenfolge, anstatt die Liste einfach nur für die Konsole in alphabetischer Reihenfolge einzuordnen. Das scheint nicht so praktisch zu sein, da sich die Liste tatsächlich ändert.

                                    print(entry)

                                list_options()

                            # FALSCHE EINGABE BEIM OPTION WÄHLEN
                            else:

                                time.sleep(2)

                                print("---")
                                print(
                                    "Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ",
                                    end="")
                                input_option = input()

                                continue
                                # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

                        except ValueError:

                            time.sleep(2)

                            print("---")
                            print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
                            input_option = input()

                            continue
                            # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

                list_options()

            # FALSCHE EINTRAG BEIM LISTE WÄHLEN
            else:

                time.sleep(2)

                print("---")
                print("Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ", end="")
                input_list = input()

                continue
                # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

        # FALSCHE EINTRAG BEIM LISTE WÄHLEN
        except ValueError:
        # 'try:' Die 'try:'- und 'except:'-Anweisung wird verwendet, um Fehler innerhalb des Codes zu behandeln, ohne dass das Programm abstürzen muss. Der 'try:'-Block wird ausgeführt, wenn kein Fehler vorliegt. Stößt das Programm im 'try:'-Block auf einen Fehler, wird der Code innerhalb des Except-Blocks ausgeführt. Eine 'try:'-Anweisung kann mehrere 'except:'-Anweisungen enthalten.

            time.sleep(2)

            print("---")
            print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
            input_list = input()

            continue
            # 'continue'-Anweisung. Diese 'continue'-Anweisung bewirkt, dass der aktuelle Durchlauf der 'while'-Schleife abgebrochen wird und die nächste Iteration beginnt. Dadurch springt das Programm zurück zum Anfang der 'while'-Schleife.

if __name__ == "__main__":
    main()
    # 'main()' Führt das Programm vom Anfang aus bzw. kehrt zum Hauptmenü zurück.