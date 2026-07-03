import os



if os.path.exists('demo.txt'):
    os.remove('demo.txt')
    print('file deleted')
else:
    print('file dont exist')

