#!/usr/bin/env python3

############ UNIT TESTS for MODEL.py ######################
import model




#1 -- check Client()  __init__
#checked -- passed
'''
c1 = model.Client(1)
print('ID: ',c1.id)
print('Permission Level: ',c1.permission_level)
print('********')
c2 = model.Client(15)
print('ID: ',c2.id)
print('Permission Level: ',c2.permission_level)

c3 = model.Client(25)
print('ID: ',c3.id)
print('Permission Level: ',c3.permission_level)
'''


#2 -- Check Banker() __init__
# checked, passed
'''
c1 = model.Banker(1)
print('ID: ',c1.id)
print('Permission Level: ',c1.permission_level)
print('********')
c2 = model.Banker(25)
print('ID: ',c2.id)
print('Permission Level: ',c2.permission_level)
'''

#3 --Check Banker.CreateAccount()
# checked, passed, but weird commit behavior, see TODO in Banker.CreatAccount()
'''
b2 = model.Banker(2)
print('Banker ID: ',b2.id)
print('Banker Permission: ',b2.permission_level)
data = [4,50]
accountid = b2.CreateAccount(data)
print(accountid)
'''

#4 check Client.ViewAccounts()
# pass, with questions below
'''
c1 = model.Client(15)
#print(c1.currentaccounts)   #QUESTION ask Kenso, if I try to print this before calling Client.ViewAccounts() then there's no class attribute...but if I try to set a class attribute earlier to an empty dict, it gives me an error
print('Client ID:', c1.id)
c1.ViewAccounts()
print(c1.currentaccounts)
'''

#5 check DepositFunds
#checked, passed
'''
c1 = model.Client(1)
print('Client ID:', c1.id)
c1.ViewAccounts()
print(c1.currentaccounts)
c1.DepositFunds(1, 10000.00)
print(c1.currentaccounts)
c1.DepositFunds(2, 33.50)
print(c1.currentaccounts)
'''

