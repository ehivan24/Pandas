'''
Created on Feb 26, 2015

@author: edwingsantos
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




filename = 'worldcitiespop.txt'

data = pd.read_csv(filename)


def locate(x, y):
    # locations is a Ncities x 2 array with the cities positions
    locations = data[['Latitude','Longitude']].as_matrix()
    d = locations - np.array([x, y])
    # squared distances from every city to the position (x,y)
    distances = d[:,0] ** 2 + d[:,1] ** 2
    # closest in the index of the city achieving the minimumdistance to the position (x,y)
    closest = distances.argmin()
    # we return the name of that city

    return data.AccentCity[closest]

    
"""

#print(locate(48.861, 2.3358))

print type(data)
print data.shape, data.keys()
print data.head()
print data.tail()
print '*' * 30

print data.AccentCity[30000] 

print data[data.AccentCity=='New York']


ny = 2990572

print data.ix[ny] 


print "City found: ", locate(40.71417,-74.00639 )

plt.plot(data['Longitude'], data['Latitude'], ',')
plt.subplot(1,2,2, polar=True)
#plt.show()
print '*' * 40

"""

print data[[name.endswith('York') for name in data.AccentCity]]
print '*' * 40

print data[[name.startswith('York') for name in data.AccentCity]]


if __name__ == '__main__':
    pass