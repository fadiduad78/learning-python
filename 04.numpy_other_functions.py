import numpy as np 

 
'''Sum of whole array'''
random = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(random))

'''Column wise sum of an array'''

print(np.sum(random , axis= 0))

'''Row wise sum of an array'''

print(np.sum(random , axis=1))

'''Checking condition'''

random_two = np.array([10,20,30,40,50])

print(np.where( random_two > 10))


'''to replace values '''

''' If value > 25 → put 100
          Else → put 0  '''
result = np.where( random_two > 25 , 100 , 0)
print(result)

'''to sort values'''

random_three = np.array([1,3,5,6,3,5,7,9,5,4,38])
print(np.sort(random_three))


arr = np.array([
    [3,1,2],
    [9,7,8]
])

print(np.sort(arr))


''' to remove duplicates '''

arr1 = np.array([1,1,1,3,4,3,3,3,5,5,5,5,8,8,8])

print(np.unique(arr1))


''' to choose random numbers '''

array = np.random.randint(1,199,(3,3))
print(array)


print(np.random.rand(2,2))

