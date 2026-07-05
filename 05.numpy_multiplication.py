import numpy as np


a = np.array([
    [1,2],
    [3,4]
])


b = np.array([
    [9,8],
    [7,6]
])

print(np.dot(a,b))



''' vertical stacking '''


c= np.array([1,2,3])

d= np.array([1,2,321])


print(np.vstack((c,d)))




''' horizontal stacking '''


e= np.array([1,2,3])

f= np.array([1,2,321])


print(np.hstack((e,f)))