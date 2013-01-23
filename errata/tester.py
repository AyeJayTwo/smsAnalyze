#import sqlite3
#
#persons = [
#    ('Hugo', "Boss"),
#    ("Calvin", "Klein")
#    ]
#
#con = sqlite3.connect(":memory:")
#
## Create the table
#con.execute("create table person(firstname, lastname)")
#
## Fill the table
#con.executemany("insert into person(firstname, lastname) values (?, ?)", persons)
#
## Print the table contents
#for row in con.execute("select firstname, lastname from person"):
#    b = list(row)
#    for item in b:
#        print str(item)
#
#print "I just deleted", con.execute("delete from person").rowcount, "rows"
import numpy as np
str = ("I","am","sam")

print str.index("b")