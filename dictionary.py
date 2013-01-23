import sms
import numpy as np
import matplotlib.pyplot as plt
from common import *
"""Set up the file to be read"""
with open("test_sms.xml", "r") as filetoberead:
    sms_file = filetoberead.readlines()

"""Get rid of header information and read only text messages"""
# header = sms_file[0:2]
# end_xml_line = sms_file[-1]
body = sms_file[3:-1]
del sms_file

database = []
score = []
window = 1

for xml_line in body:
    txt = sms.get_body(xml_line)
    txt = txt.translate(None,".,!?()'")
    splitter = txt.split(" ")
    for i in np.arange(len(splitter)-window):
        phrase = splitter[i:i+window]
        phrase = " ".join(phrase).lower()
        if phrase in database:
            score[database.index(phrase)]+=1
        else:
            database.append(phrase)
            score.append(1)
        

x = []
for (i,each) in enumerate(database):
    y = (each,score[i])
    x.append(y)
    
z = sorted (x, key=lambda text: text[1])
z2 = z[-1:-101:-1]

"""z has the top 100 words used"""
baseline = z2[0][1]

with open('dictionary3.txt','w+') as f:
    for each in z2:
        prop = float(each[1])/float(baseline)*100
        f.write("="*int(prop)+each[0]+"\n")
        
with open('toWordle.txt','w+') as w:
    for each in x:
        w.write(each[0]+"\t")
        
words = []
score = []
show = 100
for each in z:
    if not common_words(each[0],100):
        words.append(each[0])
        score.append(each[1])
words = words[-1::-1]
score = score[-1::-1]

ind = np.arange(len(words))
p1 = plt.bar(ind[0:show], score[0:show], 0.85, color='b')
plt.ylabel('Frequency of Word')
plt.title('How many times I have sent/received a text with a particular word')
plt.xticks(ind[0:show], words[0:show], rotation=90)
plt.show()

print words[0:20]
print score[0:20]