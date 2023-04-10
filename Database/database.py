# mysql -- pymysql or myslqclient
    # pip install mysqlclient

# importing the mysql module.

import MySQLdb

# Connect with the database server..

conn = MySQLdb.connect(user='root',password='',host='localhost',database='python_9am')


# create the cursor

cur_obj = conn.cursor()

# cur_obj.execute('create database python_9am')

# create a table.

# cur_obj.execute("create table player_info(name varchar(25),ipl_team varchar(20),bid_amt integer(9),strike_rate FLOAT)")

# print(cur_obj.execute("desc player_info"))

# print(cur_obj.fetchall())

# cur_obj.execute("insert into player_info(name,ipl_team,bid_amt,strike_rate) values('virat','RCB',150000000,145.67),('rohit','MI',150000000,150.12),('Raina','CSK',120000000,160.67)")

# print(cur_obj.execute("select * from player_info where bid_amt=150000000 and ipl_team='CSK'"))

# cur_obj.execute("select name,ipl_team from player_info where bid_amt=150000000")
# print(cur_obj.fetchall())

# cur_obj.execute("update player_info set ipl_team = 'GL' where name='raina'")

# cur_obj.execute('alter table player_info add notouts integer')

# cur_obj.execute("delete from player_info where name='raina'")

# cur_obj.execute('truncate player_info')

# cur_obj.execute('drop table player_info')

cur_obj.execute('drop database python_9am')
conn.commit()
print(conn)