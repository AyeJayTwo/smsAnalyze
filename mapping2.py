from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sms
import pickle
from math import log10
# setup Lambert Conformal basemap.
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
#m.drawmapboundary(fill_color='aqua')
#m.fillcontinents(color='coral',lake_color='aqua')
parallels = np.arange(0.,81,10.)
m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(10.,351.,20.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.bluemarble()

with open("test_sms.xml", "r") as filetoberead:
    body = filetoberead.readlines()[3:-1] #Read in all the texts
    
freq = {} #Create a dictionary and associate each text with a frequency
for text in body:
    num = sms.get_area(text)
#    print num
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

codes = sorted(freq, key=freq.get)
##print codes
#results = []
#for each in codes:
#    results.append(freq[each])
##print codes, results

area_codes = pickle.load(open('area_codes.pkl','rb'))

def get_latlon(area_code):
    lat, lon = area_codes[int(area_code)][1:]
    return lat,lon

for each in codes:
    
    try:
        lat,lon = get_latlon(each)
        s = freq[each]
        scaled = (log10(int(s))+1)*8
# plot blue dot on Boulder, colorado and label it as such.
#lon, lat = -104.237, 40.125 # Location of Boulder
# convert to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
        xpt,ypt = m(lon,lat)
# convert back to lat/lon
        lonpt, latpt = m(xpt,ypt,inverse=True)
        m.plot(xpt,ypt,'go',markersize = scaled)  # plot a blue dot there
    except: pass
# put some text next to the dot, offset a little bit
# (the offset is in map projection coordinates)
#plt.text(xpt+100000,ypt+100000,'Boulder (%5.1fW,%3.1fN)' % (lonpt,latpt))
plt.show()