from datetime import date # Needed to translate date to day of week
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sms
import sqlite3


"""Set up the file to be read"""
with open("sms_demo.xml", "r") as filetoberead:
    sms_file = filetoberead.readlines()

"""Get rid of header information and read only text messages"""
# header = sms_file[0:2]
# end_xml_line = sms_file[-1]
body = sms_file[3:-1]  # 1437 text messages total
del sms_file

database = []
for (index, text) in enumerate(body):
    # Build outline for database, a giant list of lists
    # each individual list would be a recap of each text sent
    phone = sms.get_phone(text)
    name = sms.get_name(text)
    sent = sms.get_type(text)
    (year, month, day, hour, minute, second) = sms.get_date(text)
    database.append((index,
                     phone,
                     name,
                     sent,
                     year,
                     month,
                     day,
                     date(year, month, day).weekday(),
                     hour,
                     minute,
                     second,
                     date(year, month, day)))
    
# Create SQLITE3 Connection in memory. Not sure 
con = sqlite3.connect(":memory:")
cursor = con.cursor()
# Create the table
cursor.execute("create table sms(id,phone,name,sent,year,month,day,weekday,hour,minute,second,date)")
# Fill the table
cursor.executemany("insert into sms(id,phone,name,sent,year,month,day,weekday,hour,minute,second,date) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)", database)    
    

"""-----------------------------------------------
Draw bar graph based showing texts per person, 
also demonstrating sent/receive proportion
------------------------------------------------"""
# Discriminate sent/received
sq4 = "SELECT name, COUNT(*) as TextSent FROM sms WHERE sent=? GROUP BY name"
x = cursor.execute(sq4,[(0)]).fetchall() #Received
y = cursor.execute(sq4,[(1)]).fetchall() #Sent
# Create intermediary tables
cursor.execute("create table smsR(name, received)")
cursor.executemany("insert into smsR(name,received) values (?, ?)", x)
cursor.execute("create table smsS(name, sent)")
cursor.executemany("insert into smsS(name,sent) values (?, ?)", y)
#Combine Tables 
z = cursor.execute("SELECT * FROM smsR INNER JOIN smsS on smsR.name=smsS.name ORDER by received DESC").fetchall()

name = []
receive = []
sent = []

print len(z)
for each in z:
    print each
    name.append(each[0])
    receive.append(each[1])
    sent.append(each[3])

print len(receive)

ind = np.arange(len(z))
width = 0.9
p1 = plt.bar(ind, receive, width, color = 'r')
p2 = plt.bar(ind, sent, width, color = 'b', bottom = receive)
plt.xlabel('Unknown People')
plt.ylabel('Total Sent')
plt.legend( (p1[0], p2[0]), ('Received','Sent'))
plt.show()


"""-----------------------------------------------
Plot total texts sent on each day of the week
-----------------------------------------------"""
sq1 = "SELECT * FROM sms WHERE weekday=?"
dates = []
for i in range(0, 7):
    cursor.execute(sq1, [(i)])
    dates.append(len(cursor.fetchall()))

ind = np.arange(7)
width = .85
p1 = plt.bar(ind, dates, width, color='b')
plt.xticks(ind + width / 2., ('M', 'T', 'W', 'Th', 'F', 'S', 'S'))
plt.ylabel('Total Texts')
plt.title('Total Texts by Day')
plt.show()

"""-----------------------------------------------
Select based on month of the year; possibly more
useful if we had aggregate data or multiple years
-----------------------------------------------"""
sq2 = "SELECT * FROM sms WHERE month=?"
months = []
for i in range(1, 13):
    cursor.execute(sq2, [(i)])
    months.append(len(cursor.fetchall()))
    
ind = np.arange(len(months))
width = 0.85
p2 = plt.bar(ind, months, width, color='r')
plt.xticks(ind + width / 2., ('J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'))
plt.ylabel('Total Texts')
plt.title('Total Texts by Month')
plt.show()


"""-----------------------------------------------
Create a time series demonstration of the 
texts/day...also includes an option for a smoother
curve which does a sliding window against the 
time series data
-----------------------------------------------"""
sq5 = "SELECT year,month,day,date, COUNT(*) as TextTotal FROM sms GROUP BY date"
x = cursor.execute(sq5).fetchall()

totals = []
ordinal_dates = []
for i in range(len(x)):
    totals.append(x[i][4])
    ordinal_dates.append(date(x[i][0],x[i][1],x[i][2]))
    
d = matplotlib.dates.date2num(ordinal_dates)

win_size = 30
window = [1./win_size]*win_size
q = (np.convolve(window,totals,'same'))
p1 = plt.plot_date(d,totals, '-',color='c')
p2 = plt.plot_date(d,q, '-',color='r')
plt.ylabel('Total Texts/Day Window = 7')
plt.grid(True)
plt.show()