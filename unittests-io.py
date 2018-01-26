########################### TESTS for IO.py ###########################
import io_wrapper
import sqlite3


#1 create DB
#run io.py in terminal, __main__ handles that
# checked  #TODO add bash script in __name__ == '__main__' to 
# automatically remove file in case a file with the same filename 
# already exists

#2 Insert users data 
# Checked, works.  
'''
import datetime

conn = sqlite3.connect('bank.db')
c = conn.cursor()

data = [datetime.datetime.now(), 'user']
ans = io_wrapper.insert_users_data(c,data)
print(ans)

conn.commit()
c.close()
conn.close()
'''

#3 Check insert_accounts_data()
# Checked, works
'''
conn = sqlite3.connect('bank.db')
c = conn.cursor()

data = [2, 2000]
ans = io_wrapper.insert_accounts_data(c,data)
print(ans)

conn.commit()
c.close()
conn.close()
'''

#4 Check update_user_data()
#checked, works
'''
conn = sqlite3.connect('bank.db')
c = conn.cursor()

data =['banker',2]
ans = io_wrapper.update_user_data(c,data)
print(ans)

conn.commit()
c.close()
conn.close() 
'''

#5 Check update_account_data
#checked, works, also works if you try to input the wrong datatype
'''
conn = sqlite3.connect('bank.db')
c = conn.cursor()

#data =['banker',2]
data =[500,2]
ans = io_wrapper.update_account_data(c,data)
print(ans)

conn.commit()
c.close()
conn.close()
'''


#6 Check get_user_permission()

conn = sqlite3.connect('bank.db')
c = conn.cursor()

data = [1]
ans = io_wrapper.get_user_permission(c,data)
print(ans)

conn.commit()
c.close()
conn.close()


#7 Check get_account_balance()
'''
conn = sqlite3.connect('bank.db')
c = conn.cursor()

data = [1]
ans = io_wrapper.get_account_balance(c,data)
print(ans)

conn.commit()
c.close()
conn.close()
'''

#8 check do_connect() & dis_connect()
#Checked, works
'''
ans1 = io_wrapper.do_connect()
print(ans1)
ans2 = io_wrapper.dis_connect(ans1)
print(ans2)
'''

