'''
Project: Password Generator
Author : Vishnu
Description : It Generates the Random Password to prevent the Dictionary Attacks.
'''
import time
import mod1
try:
        def main(t):
                print(mod1.generate(t if(t>0) else 8))
        def verify(main, t):
                main(t)

        def welcome_msg():
                print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print("'         P A S S W O R D    G E N E R A T O R            '")
                print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                print("Author: Vishnu")
                print()
                print('NIST and Microsoft advise a minimum length of 8 characters for a user-generated password, \nand to bolster security for more sensitive accounts, \nNIST recommends organisations set the maximum password length at 64 characters.')
                print()

        welcome_msg()
        print('Enter the Length of the Password:')
        t=int(input())
        verify(main, t)
        print('Press Ctrl+C to exit...')
        time.sleep(10)
except:
        print('Some Error Occured')
