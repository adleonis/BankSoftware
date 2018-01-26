#!/usr/bin/env python3

############################# CONTROLLER ##############################

import model
import view

def bank_interface():
    view.intro1()
    in1 = view.menu1()

    client_input = ['C', 'CLIENT']
    banker_input = ['B', 'BANKER']
    signout_input = ['S', 'SIGNOUT']
    quit_input   = ['Q', 'QUIT']
    valid_input = client_input + banker_input + signout_input + quit_input
    switched_on = True
    while switched_on: #TODO switch on user input is valid?
        user_input = in1.upper()
        if user_input.upper() in valid_input:
            if user_input.upper() in client_input:
                #Progress to Client logic
                print(' ')
            elif user_input.upper() in banker_input:
                #Progress to Banker logic
                #Accreditation
                inA = view.b_checkvalidid()
                b1 = model.Banker(inA)
                
                #Accredited Banker Options
                in2 = view.b_menu1()
                if in2 == 'A': #Create Client Account
                    #TODO write a list_all_usersclients method in the bankerclass, and print results here
                    users = ['1', '4', '5', '6', '8']
                    in3 = view.b_create_account(users)
                    if in3 in users: #create account
                        initial_balance = view.b_create_account_setinitialbalance()
                        c1 = b1.CreateAccount([in3, initial_balance])
                    else:            #user ID invalid 
                        print('    This user is not a client or does not exist')    
                elif in2 == 'B': #Deposit into client account
                     print('    Not yet Implemented ')
                elif in2 == 'C': #Withdraw
                     print('    Not yet implemented ')
                elif in2 == 'D':  #Transfer
                     print('    Not yet implemented ')
                else:
                    print("    >>> Invalid input")    
            elif user_input.upper() in signout_input:
                #Progress to Signout logic
                print(' ')
            elif user_input.upper() in quit_input:
                print('Thanks for using SBANK!')
                switched_on = False
        else:
            print('Invalid Input: Please enter valid input')
            bank_interface()
            #switched_on = False

if __name__ == '__main__':
    bank_interface()

