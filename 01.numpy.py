import numpy as np

marks = np.array([

    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

print(marks) 
print('---------')

print(marks.shape)     
print('---------')

print(marks[1,0])     
print('---------')

print(marks[0,:])     
print('---------')

bonus = np.array([1,2,3])
new_marks = marks + bonus 

print(new_marks)
print('---------')

average = np.mean(new_marks , axis=1)
print(average)       
print('---------')

top_value = np.argmax(average)
print(top_value)
print('---------')


