import numpy as np

numbers = np.array([
    [10,20,30],
    [97,50,60],
    [70,80,90]
])

'''Average of whole array'''
average = np.mean(numbers,axis=0)
print(average)

'''Highest Value Find'''
highest_value = np.argmax(numbers)
print(highest_value)

'''Boolean Masking'''
high_scores = numbers > 80
print(high_scores)

'''Matrix Multiplication'''
weights = np.array([
    [0.2],
    [0.3],
    [0.4]
])

final_value = np.dot(numbers , weights) 
print(final_value)