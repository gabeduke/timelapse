from menuHelper import *
from properties import *
import os


# variables
loop = True
user_input = None


def print_menu():
    print 2 * "\n"
    print 30 * "-", "MENU", 30 * "-"
    print "1. Export Timelapse"
    print "2. Rename"
    print "3. Set FPS"
    print "4. Set Quality"
    print "5. Set Directory"
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
    print "\n"
    raw_input("Hit any key to continue... ")


def export_render():
    file_extensions = ['.CR2', '.cr2']
    for filename in os.listdir(os.curdir):
        if filename.endswith(file_extensions):
            raw_dir = True

    if raw_dir and os.path.isdir(EXPORT_DIR):
        export()
        list_files()
        render()
    elif raw_dir:
        list_files()
        render()
    else:
        render_jpegs()


while loop:
    print_menu()
    choice = input("Make an assessment: ")

    if choice == 1:  # TODO these functions need to wait until the bash commands finish to move one & print output
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
