#!usr/bin/env python3

#Wrapper to handle I/O to from database

#REMEMBER TO OPEN A CURSOR FIRST TO PASS, THEN COMMIT, THEN CLOSE 
# ONLY THE CREATE DB function does that for you

#Functions Available
#    io_wrapper.
#               do_connect()
#               dis_connect()
#               create_db(filename)
#               insert_users_data(c,data)
#               insert_accounts_data(c,data)
#               update_user_data(c,data)
#               update_account_data(c,data)
#               get_user_permission(c,ID)
#               get_account_balance(c,ID)
#               get_user_accounts(c,[ID])
#               get_all_users(c,[permission_level])
import traceback
import sqlite3

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
def do_connect():
    database = 'bank.db'
    conn = sqlite3.connect(database, check_same_thread=False)
    out = (conn.cursor(), conn)
    return out
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
def dis_connect(inn):
    try:
        conn = inn[1]
        c = inn[0]
        conn.commit()
        c.close()
        conn.close()
        return True
    except:
        return False
#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD


########################################################
def create_db(filename):
    import sqlite3

    try:
        #Open Connection
        conn = sqlite3.connect(filename)
        c = conn.cursor()

        #CREATE TABLE
        c.execute(
            '''CREATE TABLE users(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             created_on INTEGER,
             permission_level VARCHAR);'''
        )

        c.execute(
            '''CREATE TABLE accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            balance FLOAT);'''
        )

        #Commit & Close
        conn.commit()
        c.close()
        conn.close()

        print('    Database',filename,'was created successfuly')

    except:
        print('Some error occured in function(create_db), call your programmer')
        print(traceback.format_exc())
##########################################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def insert_users_data(c,data): 
# data=[created_on, permission_level]
# INSERT DATA INTO TABLES
# RETURNS created user ID if data correctly inserted, False if error
    try:         
        c.execute(
        '''INSERT INTO users(
        created_on,
        permission_level
        )
        VALUES(
        ?,
        ?
        );''',data)

        created_id = c.execute('SELECT MAX(id) FROM users;').fetchall()[0][0]

        return created_id
    except:  #TODO since the except is sometimes used in the model to check if users
             # already exist, catch various exceptions depending on code 
        #print('An error has occured trying to insert data into the Users table of the DB')
        
        #print(traceback.format_exc())
        return False
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def insert_accounts_data(c,data):
# data=[user_id, balance]
# RETURNS newly created account ID if data correctly inserted, False if error
    try:
        c.execute(
        '''INSERT INTO accounts(
            user_id,
            balance
            )
            VALUES(
            ?,
            ?
            );''',data)

        created_id = c.execute('SELECT MAX(id) FROM accounts;').fetchall()[0][0]   #TODO ask Kenso if there is a better way to ensure that the newly created account is the one we're fetching....what if many accounts created rapidly
        return created_id
    except:
        print('''An error has occured trying to insert data into the
                Accounts table of the DB''')
        print(traceback.format_exc())
        return False    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
def update_user_data(c,data):
# ID is the table primary key by which you are referencing
# data = [permission level, ID] (type:list)
# RETURNS True if data correctly updated, False if error
    try:
        c.execute(
            '''UPDATE users SET
            permission_level=?
            WHERE
            ID=?;''',data)
        return True
    except:
        print('''An error has occured trying to update data in the
                Users table of the DB, User ID:''',data[1])
        print(traceback.format_exc())
        return False
#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII            

#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
def update_account_data(c,data):
# ID is the table primary key  <-----ACCOUNT ID not user ID
# data = [balance, id]
    try:
        if isinstance(data[0], (int, float)):
            c.execute(
                '''UPDATE accounts SET
                balance=?
                WHERE
                ID=?;''',data)
            
            return True
        else:
            return False
    except:
        print('''An error has occured trying to update data in the
                Accounts table of the DB, Account ID:''',data[1])
        print(traceback.format_exc())
        return False
#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU


#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
def get_user_permission(c,ID):
# INPUT ID is of type list... [ID]
# Returns: permission level as a type<str>
#
    try:
        return c.execute('SELECT permission_level FROM users WHERE id=?;',ID).fetchall()[0][0]
    except:
        #print("An error has occured trying to get data in the USERS table of the DB: get_user_permission")
        #print(traceback.format_exc())
        return False
#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS


#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
def get_account_balance(c,ID):
# INPUT ID is of type list... [ID]  <--- ACCOUNT ID not USER ID
# Returns: balance as a type<float>
#
    try:
        return c.execute('''SELECT balance FROM accounts WHERE id=?;''',ID).fetchall()[0][0]
    except:
        print('''An error has occured trying to get data in the
                ACCOUNT table of the DB: get_account_balance''')
        print(traceback.format_exc())
        return False
#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
def get_user_accounts(c,ID):
# INPUT ID is of type list... [ID]  <--- USER ID not ACCOUNT ID
# Returns: all account IDs and balances type<[list]>
#
    try:
        ans = c.execute('''SELECT id,balance FROM accounts WHERE user_id=?;''',ID).fetchall()
        accounts = {}
        for i in ans:
            accounts[i[0]] = i[1]
        return accounts    
    except:
        print('''An error has occured trying to get data in the
                ACCOUNTS table of the DB: get_user_accounts''')
        print(traceback.format_exc())
        return False
#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def get_all_users(c,permission_level):
# Permission level is of type list... [permission_level]  <--- ['Client'] or ['banker']
# Returns: all user IDs of Clients type<[list]>
#
    try:
        ans = c.execute('''SELECT id FROM users WHERE permission_level=? ORDER BY id;''',permission_level).fetchall()
        accounts = []
        for i in ans:
            accounts.append(i[0])
        return accounts
    except:
        print('''An error has occured trying to get data in the
                USERS table of the DB: get_all_users''')
        print(traceback.format_exc())
        return False

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




if __name__ == '__main__':
    print('Running this will delete and create a new DB, are you sure?(Y/N)')
    in_put = input()
    if in_put.upper() == 'Y':   
        print('Name your database file(with extension):')        
        db_name = input()
        create_db(db_name)
    else:
        print('Goodbye')

    
