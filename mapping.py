import pickle
import sms
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
from colorsys import hsv_to_rgb as colorswap

"""Load up dictionary with area code to longitude/latitude directions"""

area_codes = pickle.load(open('area_codes.pkl','rb'))

long1,lat1 = area_codes[847][1:]
n = Basemap(width=12000000,height=9000000,projection='gnom',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
#n.drawcoastlines() #developing with a coastline is much faster than waiting for bluemarble to load up
n.bluemarble()


#n.bluemarble()

with open("test_sms.xml", "r") as filetoberead:
    body = filetoberead.readlines()[3:-1] #Read in all the texts
    
areas = {} #Create a database and associate each text with a frequency
for text in body:
    num = sms.get_area(text)
    if num in areas:
        areas[num] += 1
    else:
        areas[num] = 1

codes = sorted(areas, key=areas.get)
results = []
for each in codes:
    results.append(areas[each])
    
#results.reverse() #Reversed the values so the color would end up darker for more usage; lighter for lighter usage
    
for i, num in enumerate(codes):
    scale = (ceil(np.log(results[i])))/10 #Creates a log scale for the relative frequencies
    rgb = colorswap(0.3,0.3,scale) #alter the HSV scale to RGB to keep a single color and adjust the tone
    try:
        long2,lat2 = area_codes[int(num)][1:]
        z = n.gcpoints(lat2,long2, lat1,long1,10)
        n.plot(z[0],z[1],color=rgb,linewidth = 1.3)
    except: pass #I have tried to code for many of the exceptions, but i was getting strange area codes which do not exist. Not sure what to do with them....

plt.show()
