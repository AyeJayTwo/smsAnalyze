#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
#import matplotlib.ticker as ticker
#from common import *

#r = mlab.csv2rec('../data/aapl.csv')
#r.sort()
#r = r[-30:]  # get the last 30 days
#
#N = len(r)
#ind = np.arange(N)  # the evenly spaced plot indices
#
#def format_date(x, pos=None):
#    thisind = np.clip(int(x+0.5), 0, N-1)
#    return r.date[thisind].strftime('%Y-%m-%d')
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(ind, r.adj_close, 'o-')
#ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
#fig.autofmt_xdate()
#
#plt.show()

