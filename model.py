#!/usr/bin/env python3

######################### MODELS ######################################
# get data from io_wrapper.py
import io_wrapper
import datetime
import sqlite3  #TODO check with kenso if I have to import this since I already imported it in io_wrapper

class Client():

    def __init__(self, id):
        c = io_wrapper.do_connect()
        #check if user already exists, if not create it
        if io_wrapper.get_user_permission(c[0],[id]) == False:  #user does not exist
            created_id = io_wrapper.insert_users_data(c[0],[datetime.datetime.now(),'client'])   #insert it in
            print('    New user created. User ID:', created_id)
            #Populate class instance
            self.id = created_id
            self.permission_level = 'client'
        #if user already exists, populate instance attributes with DB data
        else:
            #populate 
            perm_out = io_wrapper.get_user_permission(c[0],[id])
            if perm_out == 'client':
                self.id = id
                self.permission_level = perm_out
            else:
                print('    Sorry, this user ID is not a valid Client ID')  #in case user ID exists, but not of same type, create new user
                created_id = io_wrapper.insert_users_data(c[0],[datetime.datetime.now(),'client'])   #insert it in
                self.id = created_id
                self.permission_level = 'client'   
        io_wrapper.dis_connect(c)

    def ViewAccounts(self):
        current_user_id = self.id
        c = io_wrapper.do_connect()
        ans = io_wrapper.get_user_accounts(c[0],[current_user_id])
        io_wrapper.dis_connect(c)
        self.currentaccounts = ans
        return ans

    def DepositFunds(self, account_id, amount):
        c = io_wrapper.do_connect()
        try:
            current_balance = io_wrapper.get_account_balance(c[0],[account_id])
            new_balance = current_balance + amount
            ans = io_wrapper.update_account_data(c[0],[new_balance, account_id])
            io_wrapper.dis_connect(c)
            newaccountstatus = self.ViewAccounts()  #needed to update self.currentaccounts, otherwise changes don't show up until you run VIewAccounts again
            print(self.currentaccounts)
            print('    LOG >> MODEL >> Deposit Successful, Account updated')
        except:
            print('    LOG >> MODEL >> Deposit Error, no update')
            c[0].close
            c[1].close
    def WithdrawFunds():
        pass
    def TransferFunds():
        pass

class Banker():
    def __init__(self, id):
        c = io_wrapper.do_connect()
        #check if user already exists, if not create it
        if io_wrapper.get_user_permission(c[0],[id]) == False:  #user does not exist
            created_id = io_wrapper.insert_users_data(c[0],[datetime.datetime.now(),'banker'])   #insert i$
            print('    New user created. User ID:', created_id)
            #Populate class instance
            self.id = created_id
            self.permission_level = 'banker'
        #if user already exists, populate instance attributes with DB data
        else:
            #populate
            perm_out = io_wrapper.get_user_permission(c[0],[id])
            if perm_out == 'banker':
                self.id = id
                self.permission_level = perm_out
            else:
                print('    Sorry, this user ID is not a valid Banker ID')
                created_id = io_wrapper.insert_users_data(c[0],[datetime.datetime.now(),'banker'])   #insert i$
                self.id = created_id
                self.permission_level = 'banker'
                print('    Your ID is:',created_id)
        io_wrapper.dis_connect(c)


    def CreateAccount(self, inputdata):   #inputdata = [user_id, balance]
        user_id = inputdata[0]
        balance = inputdata[1]
        #Banker should be able to create accounts for clients
        c = io_wrapper.do_connect()
        created_id = io_wrapper.insert_accounts_data(c[0],inputdata)
        c[1].commit()   #TODO for some reason if I don't commit here, it doesn't save into db, even though the io_wrapper.dis_connect(c) does it 7 lines down
        if type(created_id) == type(1): #if the inserting operation returns an integer(account_id)
            print('    LOG >> MODEL >> Account Created, Account ID: ',created_id)
            return created_id  
        else:
            print('    LOG >> MODEL >> An error occured, no account was created')
            return 0  #return 0 as the account ID if the account could not be created
        io_wrapper.dis_connect(c)

    def ViewAccounts(self,type):
        c = io_wrapper.do_connect()
        client_accounts = {}
        banker_accounts = {}
        if type.upper() == 'CLIENT':
            client_accounts = io_wrapper.get_all_users(c[0],['client'])
            return client_accounts
        elif type.upper() == 'BANKER':
            client_accounts = io_wrapper.get_all_users(c[0],['banker'])
            return banker_accounts
        else:
            print("    LOG >> MODEL >> User type not recognized")
            emptydict = {}
            return emptydict
        io_wrapper.dis_connect(c)

    def Deposit():
        pass
    def Withdraw():
        pass
    def Transfer():
        pass









