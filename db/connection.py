import mysql.connector as mycon


con = mycon.connect(host='localhost', user='root', passwd='ghouse@1974', database='project')

if con.is_connected():
    print('Connected to MySQL')
    cursor = con.cursor()
else:
    print('Error, connection not established')
    cursor = con.cursor()
