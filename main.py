#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#import
import os
import apk

## Text menu in Python
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Choice APK"
    print "2. Choice PAYLOAD and configure it"
    print "3. Configure output APK name"
    print "4. Exit"
    print 67 * "-"
  


loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        choiceAPKpath = raw_input("Enter the path of your APK for decompilation ( .apk ): ")
        choiceNameDirectory = raw_input("Enter the path of Directory Name for decompile: ")
        #apk.decompilation(choiceAPKpath,choiceNameDirectory)
    elif choice==2:
        choicePAYLOAD = raw_input("Enter the path of your PAYLOAD: ")
        print choicePAYLOAD
    elif choice==3:
    	choiceNameNewAPK = raw_input("Enter the new name of the APK compilate ( .apk ): ")
        apk.compilation(choiceNameDirectory,choiceNameNewAPK)
        print "APK is compilated"
    elif choice==4:
        print "See you later"
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")