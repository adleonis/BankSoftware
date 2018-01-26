#!/usr/bin/env python3
# USER INTERACTION
import os


def intro1():
    unused_variable = os.system("clear")
    print(''' \n
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$  HELLO, WELCOME TO SBANK $$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n''')

def menu1():
    user_input = input("    Are you a Client, or a Banker? (C/B)")
    return user_input


def b_menu1():
    user_input = input('''\n    You can:\n    
    A.Create a Client Account (A)\n
    B.Make a Deposit to a Client Account (B)\n
    C.Withdraw from a Client Account (C)\n
    D.Transfer funds from one account to another (D)\n
    E.Sign Off\n    >>>''')
    return user_input

def b_checkvalidid():
    user_input = input('''\n    Please enter your Account ID:''')
    return user_input

def b_create_account(users):
    user_input = input('''\n    Please enter a valid User ID:  ''')
    return user_input

def b_create_account_setinitialbalance():
    user_input = ("\n    WOuld you like to set an initial balance?\n    >>>")
    return user_input
