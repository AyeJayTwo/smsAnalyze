"""Note to self:
1) Remove need of database list, directly parse each text and input into the csv
file in one shot, no need to create a list of lists and then loop through it"""

import sms
from csv import writer #Needed to write to a csv file
from datetime import date #Needed to translate date to day of week

"""Set up the file to be read"""
with open("test_sms.xml", "r") as filetoberead:
    sms_file = filetoberead.readlines()

"""Get rid of header information and read only text messages"""
# header = sms_file[0:2]
# end_xml_line = sms_file[-1]
body = sms_file[3:-1]
del sms_file

print "You have %i texts" % (len(body))

#inbound = outbound = 0
#for text in body:
#    if sms.get_type(text) == 0: inbound += 1
#    else: outbound += 1
#    
#print "Inbound: %s\tOutbound: %s\n" % (inbound, outbound)
#test = body[0].strip()
#print test.split('address="',1)[1].split('" date=')

database = []
for (index,text) in enumerate(body):
    #Build outline for database, a giant list of lists
    #each individual list would be a recap of each text sent
    phone = sms.get_phone(text)
    name = sms.get_name(text)
    sent = sms.get_type(text)
    (year,month,day,hour,minute,second) = sms.get_date(text)
    database.append((index,
                     phone,
                     name,
                     sent,
                     year,
                     month,
                     day,
                     date(year,month,day).weekday(),
                     hour,
                     minute,
                     second))
    
writefile = 'texting_database.csv'
with open( writefile, 'w' ) as f:
    writer = writer(f)
    writer.writerow(('ID',
                     'Phone Number',
                     'Name',
                     'Sent',
                     'Year'
                     'Month'
                     'Day',
                     'Day of Week',
                     'Hour',
                     'Minute',
                     'Second'))
    for (index,text) in enumerate(database):
        entry = database[index]
        writer.writerow(entry)
        
#phonebook = {}
#for text in body:
#    #build up the phonebook with numbers and associated texts
#    x = sms.clean_phone(sms.get_phone(text))
#    z = sms.get_name(text)
#    if x not in phonebook:
#        phonebook[x] = [0,0,0,z]
#    
#    #Add in the text type counts
#    text_count = phonebook[x]
#    text_count[sms.get_type(text)] += 1
#    text_count[2] += 1
#
#print "You text %i unique friends\n" % (len(phonebook))
#
#writefile = 'phonebook.csv'
#with open( writefile, 'w' ) as f:
#    writer = csv.writer(f)
#    for phone in phonebook:
#        entry = phonebook[phone][0:3]
#        writer.writerow(entry)