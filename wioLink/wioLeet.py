from menuHelper import *
from properties import *
import os


# variables
loop = True
cont = False
user_input = None


def print_menu():
    print 2 * "\n"
    print 30 * "-", "MENU", 30 * "-"
    print "1. "
    print "2. "
    print "3. "
    print "4. "
    print "5. "
    print "6. Print Variables"
    print "7. Exit"
    print 67 * "-"
    print "\n"


def print_variables():
    print 2 * "\n"
    print 30 * "-", "VARS", 30 * "-"
    print 'Name: ' + NAME
    print 'Quality: ' + QUALITY
    print 'FPS: ' + str(FPS)
    print 67 * "-"


while loop:
    if cont:
        print_variables()
    cont = True
    print_menu()
    choice = input("Make an assessment: ")

    if choice == 1:
        export()
        list_files()
        render()
    elif choice == 2:
        user_input = raw_input("Timelapse name: ")
        NAME = user_input
    elif choice == 3:
        user_input = raw_input('New frame rate: ')
        FPS = user_input
    elif choice == 4:
        user_input = raw_input("Quality (Low, Normal, High): ")
        QUALITY = user_input
    elif choice == 5:
        user_input = raw_input('Choose a new directory: ')
        EXPORT = user_input
    elif choice == 6:
        print_variables()
    elif choice == 7:
        print "Exiting Program"
        loop = False
    else:
        raw_input("Invalid option. Enter any key to try again..")
