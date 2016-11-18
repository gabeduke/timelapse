from wioLeet.app.properties import *

loop = True
cont = False
user_input = None


def print_menu():
    print 2 * "\n"
    print 30 * "-", "MENU", 30 * "-"
    print "1. change wio1_token"
    print "2. change wio_pete_token"
    print "3. change thingspeak_apiKey"
    print "4. button1"
    print "5. button2"
    print "6. Print Variables"
    print "7. Exit"
    print 67 * "-"
    print "\n"


def print_variables():
    print 2 * "\n"
    print 30 * "-", "VARS", 30 * "-"
    print 'wio1_token: ' + wio1_token
    print 'wio_pete_token: ' + wio_pete_token
    print 'thingspeak_apiKey: ' + thingspeak_apiKey
    print 67 * "-"


while loop:
    if cont:
        print_variables()
    cont = True
    print_menu()
    choice = input("Make an assessment: ")

    if choice == 1:
        user_input = raw_input('Change wio1_token : ')
        wio1_token = user_input
    elif choice == 2:
        user_input = raw_input('Change wio_pete_token : ')
        wio_pete_token = user_input
    elif choice == 3:
        user_input = raw_input('Change thingspeak_apiKey : ')
        thingspeak_apiKey = user_input
    elif choice == 4:
        print 'i serve no purpose'
    elif choice == 5:
        print 'i server no purpose'
    elif choice == 6:
        print_variables()
    elif choice == 7:
        print "Exiting Program"
        loop = False
    else:
        raw_input("Invalid option. Enter any key to try again..")
