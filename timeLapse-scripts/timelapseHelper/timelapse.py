from menuHelper import *
from properties import *
import os

# variables
loop = True

def print_menu():
    print 30 * "-", "MENU", 30 * "-"
    print "1. Continue with Defaults"
    print "2. Rename Timelapse"
    print "3. Set FPS"
    print "4. Set Quality"
    print "5. Set Directory"
    print "6. Exit"
    print 67 * "-"


def export_render():
    if os.path.isdir(EXPORT):
        export()
        list_files()
        render()
    else:
        list_files()
        render()



while loop:
    print_menu()
    choice = input("Make an assessment: ")

    if choice == 1:
        export()
        list_files()
        render()
    elif choice == 2:
        NAME = input("Timelapse name: ")
    elif choice == 3:
        FPS = input('New frame rate: ')
    elif choice == 4:
        QUALITY = input("Quality: ")  # TODO make this a choice param
    elif choice == 5:
        EXPORT = input('Choose a new directory: ')
    elif choice == 6:
        print "Exiting Program"
        loop = False
    else:
        raw_input("Invalid option. Enter any key to try again..")
