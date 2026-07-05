import numpy as np


marks = np.array([
    [98,87,91,69],
    [88,89,85,91],
    [91,97,99,56],
    [91,89,87,89],
    [71,79,89,100]
])

print('Shapes of Marks: ')
print(marks.shape)

print('Student 1 data : ')
print(marks[0,:])

print('last student all marks: ')
print(marks[3,:])

print(f"second studnet's third subject marks : {marks[1,2]}")


print(f"entire third column : {marks[:,2]}")


bonus = np.array([2,2,2,2])
updated_marks = bonus + marks


average = np.mean(updated_marks , axis= 1)
print(f'Average Marks : {average}')

topper = np.argmax(average)
print(f'Topper amoung 5 Studnets : {topper} ')


high_scores = average > 80
print(f'Marks above 80% : {high_scores}')

# rearrage = np.reshape(2,10)
# print(rearrage)
#i dont understad how to do

print(updated_marks.flatten())


print(f'Highest marks {np.max(updated_marks)}')
print(f'Lowest marks {np.min(updated_marks)}')


subject_wise_avg = np.mean(updated_marks , axis= 0)
print(subject_wise_avg)