from menuHelper import *
import os

# variables
loop = True
exportPath = os.getcwd() + '/export'

def print_menu():
    print 30 * "-", "MENU", 30 * "-"
    print "1. Continue with Defaults"
    print "2. Rename Timelapse"
    print "3. Set FPS"
    print "4. Set Quality"
    print "5. Set Directory"
    print "4. Exit"
    print 67 * "-"


def export_render():
    if exportPath:
        export()
        listFiles()
        render()
    else:
        listFiles()
        render()



while loop:
    print_menu()
    choice = input("What will you choose: ")

    if choice ==1:
        export()
        listFiles()
        render()
    elif choice == 2:
        rename()
    elif choice == 3:
        sync_hotfix(hotfix_ssh)
    elif choice == 4:
        print "Exiting Program"
        loop = False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
