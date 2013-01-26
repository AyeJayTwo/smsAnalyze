def get_area(txt):
    """Returns area code from sms xml"""
    phone = txt.split('address="', 1)[1].split('" date=')[0]
    return clean_area(phone)

def clean_area(test):
    number = ""  # create an empty number
    for i in test:
        if i in "0123456789":  # iterate over each item and extract only the numbers
            number += i
    
    # Remove leading 1 from country code
    if number[0] == "1": number = number[1:] 
    
    return number[0:3]

def get_phone(txt):
    """Returns phone number from sms xml"""
    phone = txt.split('address="', 1)[1].split('" date=')[0]
    return clean_phone(phone)

def clean_phone(test):
    number = ""  # create an empty number
    for i in test:
        if i in "0123456789":  # iterate over each item and extract only the numbers
            number += i
    
    # Remove leading 1 from country code
    if number[0] == "1": number = number[1:] 
    
    # Format normal phone numbers, ignoring SMS Codes
    if len(number) == 10:
        number = "(%s)%s-%s" % (number[0:3], number[3:6], number[6:10])
    
    return number


def get_type(txt):
    """Returns whether text was sent or received"""
    if 'type="1"' in txt: return 0 #Type 1 is user received
    else: return 1 #Type 2 is user sent
    
def get_date(txt):
    """Returns the date and time of the text"""
    date = txt.split('readable_date="',1)[1].split('" contact_name=')[0]
    """YEAR""" 
    year = int(date.split(',')[1][:6].strip())
    """MONTH"""
    month = date.split(',')[0][:3]
    """DAY"""
    day = int(date.split(',')[0][-2:].strip())
    """HOUR"""
    if date[-2:] == 'PM':hour = int(date.split(':')[0][-2:].strip())+12
    else: hour = int(date.split(':')[0][-2:].strip())
    """MINUTE"""
    minute = int(date.split(':')[1].strip())
    """SECOND"""
    seconds = int(date.split(':')[2][:2].strip())

    return (year,numMonth(month),day,hour,minute,seconds)

def numMonth(txt):
    number = {'Jan':1,
              'Feb':2,
              'Mar':3,
              'Apr':4,
              'May':5,
              'Jun':6,
              'Jul':7,
              'Aug':8,
              'Sep':9,
              'Oct':10,
              'Nov':11,
              'Dec':12}
    return number[txt]
    
def get_nameday (d):
    """Returns translation of number day to name of day"""
    day = {0:'Monday',
           1:'Tuesday',
           2:'Wednesday',
           3:'Thursday',
           4:'Friday',
           5:'Saturday',
           6:'Sunday'}
    return day[d]
    
def get_name(txt):
    """Returns the name of the person you are texting"""
    z =  txt.split('contact_name=', 1)[1].split(' />\n')[0]
    name = ""
    for i in z:
        if i.isalpha() or i.isspace(): name += i #removes any weird symbols from their names, 
    return name                                  #maintaining white space

def get_body(txt):
    """Returns the body of the sms"""
    z = txt.split('body=',1)[1].split(' toa=')[0]
    return z[1:-1]