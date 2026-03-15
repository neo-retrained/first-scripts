# IMPORTED LIBRARIES

# I only used this library as a small experiment to implement the 'time.sleep()' function in the program. It's not actually necessary, but it helps me get used to working with libraries.
import time

# GLOBAL VARIABLES

## LISTS

### List containing only the names of the available lists to the user
main_menu = ["TO-DO \u2705", "EINKAUFSLISTE \U0001F6D2", "NEUJAHRSWÜNSCHE \u2728"]

### List 1: TO-DO
todo_list = ["Eltern anrufen", "Wohnung putzen", "Autoöl wechseln", "Arzttermin vereinbaren"]
### List 2: EINKAUFSLISTE
shopping_list = ["Gemüse", "Rindfleisch", "Käse", "Cola"]
### List 3: NEUJAHRSWÜNSCHE
wishes_list = ["Fahrrad fahren", "Twitter abmelden", "Urlaub in Japan", "Sparen"]

### List with all lists. Each item corresponds to each of the full lists that the user can modify.
all_lists_list = [todo_list, shopping_list, wishes_list]

def main():

    time.sleep(2)

    # Main menu
    print("========================================================================================================")
    print("NOTIZEN-APP")
    print("---")
    print("IHRE LISTEN")
    print()

    # I use the 'enumerate()' function to ensure that, whenever a list is deleted or a new list is added, their position shows correctly in relation to the other lists.
    for position, list_name in enumerate(main_menu, 1):

        print("Liste " + str(position) + ": " + list_name)

    print("---")
    print("N. NEUE LISTE")
    print("L. LISTE LÖSCHEN")
    print("---")
    print("0. PROGRAMM BEENDEN")
    print("---")
    print("Wählen Sie die Nummer der Liste aus, die Sie verarbeiten möchten, oder eine der anderen Optionen.")
    print("Ihre Wahl: ", end="")

    # Prompts the user to select an option from the main menu and stores it.
    input_list = input()

    def print_list(list_name, entries):
    # Prints to the console the name of the selected or modified list and all its items.

        time.sleep(2)

        print("========================================================================================================")
        print("NOTIZEN-APP")
        print("---")
        print("Liste " + list_name)
        print()

        for entry in range(len(entries)):

            print(str(entry + 1) + ". " + entries[entry])

    while True:

        try:

            # 0. Exit programm
            if input_list == "0":

                time.sleep(2)

                print("---")
                print("Programm beendet")

                break

            # N. New list
            elif input_list.lower() == "n":

                time.sleep(2)

                print("---")

                # Prompts the user to type in the name of the new list and stores it.
                input_new_list = input("Tippen Sie den Namen der neuen Liste ein, oder kehren Sie mit '0' zurück zum Hauptmenü: ")

                # 0. Back to main menu
                if input_new_list == "0":

                    main()

                # Creating the new list
                else:

                    time.sleep(2)

                    print("---")

                    main_menu.append(input_new_list.upper())
                    # The name of the new list is added to the end of the 'main_menu' list, which contains the names of all the lists.

                    input_new_list = []
                    # Creates the new empty list.

                    all_lists_list.append(input_new_list)
                    # Adds the newly created empty list to the end of the 'all_lists_list', which contains all the other full lists.

                    print("Die neue 'Liste " + str(len(main_menu)) + ": " + main_menu[-1] + "' wurde erstellt. In Kürze werden Sie zum Hauptmenü zurückgeleitet.")

                    time.sleep(4)

                    main()

            # L. Delete list
            elif input_list.lower() == "l":

                time.sleep(2)

                print("---")

                print("Wählen Sie die Nummer der Liste aus, die Sie löschen möchten oder kehren Sie mit '0' zurück zum Hauptmenü: ", end="")
                input_delete_list = input()

                while True:

                    try:

                        # 0. Back to main menu
                        if input_delete_list == "0":

                            main()

                        # Deleting the new list
                        elif int(input_delete_list) - 1 in range(len(all_lists_list)):

                            time.sleep(2)
                            print("---")
                            print("'Liste " + input_delete_list + ": " + main_menu[int(input_delete_list) - 1] +
                                  "' würde gelöscht. In Kürze werden Sie zum Hauptmenü zurückgeleitet.")

                            del main_menu[int(input_delete_list) - 1]
                            del all_lists_list[int(input_delete_list) - 1]

                            time.sleep(4)

                            main()

                        # User input not in range
                        else:

                            time.sleep(2)

                            print("---")
                            print("Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ",
                                  end="")
                            input_delete_list = input()

                            continue

                    # User input cannot be converted to an integer
                    except ValueError:

                        time.sleep(2)

                        print("---")
                        print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
                        input_delete_list = input()

                        continue

            # Options to modify a list
            elif int(input_list) - 1 in range(len(all_lists_list)):
            # Checks if the user input (minus 1) is a valid index for accessing a list in the 'all_lists_list'.

                def list_options():
                # Prints to the console the options for modifying a list.

                    print_list(main_menu[int(input_list) - 1], all_lists_list[int(input_list) - 1])
                    # Calls the function that displays the modified list in the console.

                    print("---")
                    print("OPTIONEN")
                    print()
                    print("Option 1: Neuen Eintrag in die Liste einfügen")
                    print("Option 2: Eintrag aus der Liste löschen")
                    print("Option 3: Einträge in alphabetischer Reihenfolge anzeigen")
                    print("---")
                    print("0. HAUPTMENÜ")
                    print("---")

                    # Prompts the user to choose an option to modify the selected list and stores it.
                    input_option = input("Wählen Sie eine Option aus, oder kehren Sie mit '0' zurück zum Hauptmenü: ")

                    while True:

                        try:

                            # 0. Back to main menu
                            if input_option == "0":

                                main()

                            # 1. New entry
                            elif input_option == "1":

                                time.sleep(2)

                                print("---")

                                # Prompts the user to type in a new list entry and stores it.
                                input_add_entry = input("Tippen Sie Ihren neuen Eintrag oder geben Sie die 0 ein, zurück zu den Optionen: ")

                                # Back to the options
                                if input_add_entry == "0":

                                    list_options()

                                # Saving the new entry
                                else:

                                    (all_lists_list[int(input_list) - 1]).append(input_add_entry.capitalize())

                                    time.sleep(2)

                                    print("---")
                                    print("Ihr neuer Eintrag '" + all_lists_list[int(input_list) - 1][-1] + "' wurde in der Liste " + main_menu[int(input_list) - 1] + " eingefügt.")

                                    list_options()

                            # 2. Delete an entry
                            elif input_option == "2":

                                time.sleep(2)

                                print("---")
                                print("Wählen Sie den Eintrag aus, den Sie löschen möchten, oder geben Sie die 0 ein, zurück zu den Optionen: ", end="")

                                # Prompts the user to select the list entry that he or she wants to delete and stores it.
                                input_delete_entry = input()

                                while True:

                                    try:

                                        # Back to the options
                                        if input_delete_entry == "0":

                                            list_options()

                                        # Deleting the entry
                                        elif int(input_delete_entry) - 1 in range(len(all_lists_list[int(input_list) - 1])):

                                            time.sleep(2)

                                            print("---")
                                            print("Ihr Eintrag '" + all_lists_list[int(input_list) - 1][int(
                                                input_delete_entry) - 1] + "' wurde aus der Liste " + main_menu[
                                                int(input_list) - 1] + " gelöscht.")

                                            del all_lists_list[int(input_list) - 1][int(input_delete_entry) - 1]

                                            list_options()

                                        # User input not in range
                                        else:

                                            time.sleep(2)

                                            print("---")
                                            print("Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ", end="")
                                            input_delete_entry = input()

                                            continue

                                    # User input cannot be converted to an integer
                                    except ValueError:

                                        time.sleep(2)

                                        print("---")
                                        print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
                                        input_delete_entry = input()

                                        continue

                            # 3. Alphabetical order
                            elif input_option == "3":

                                time.sleep(2)

                                print(
                                    "========================================================================================================")
                                print("'Liste " + main_menu[int(input_list) - 1] + "' in "
                                                                                                        "ALPHABETISCHER REIHENFOLGE")
                                print()

                                # Displaying the list in alphabetical order
                                for entry in sorted(all_lists_list[int(input_list) - 1]):

                                    print(entry)

                                list_options()

                            # User input not in range
                            else:

                                time.sleep(2)

                                print("---")
                                print(
                                    "Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ",
                                    end="")
                                input_option = int(input())

                                continue

                        # User input cannot be converted to an integer
                        except ValueError:

                            time.sleep(2)

                            print("---")
                            print("Ihre Angabe ist keine Zahl. Versuchen Sie es bitte noch einmal: ", end="")
                            input_option = input()

                            continue

                list_options()

            # User input not in range
            else:

                time.sleep(2)

                print("---")
                print("Ihre Eingabe liegt außerhalb den gültigen Bereich. Versuchen Sie es bitte noch einmal: ", end="")
                input_list = input()

                continue

        # User input is not n or l (case-insensitive) or cannot be converted to an integer
        except ValueError:

            time.sleep(2)

            print("---")
            print("Ihre Eingabe ist weder eine Zahl noch eine andere gültige Option. Versuchen Sie es bitte noch einmal: ", end="")
            input_list = input()

            continue

if __name__ == "__main__":
    main()
