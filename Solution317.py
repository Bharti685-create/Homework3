"""Script to Display different triangle Pattern"""

#Initialize variables
i = 0
j = 0

print('Pattern A')
for i in range(10): #outer loop to handle the number of rows
    for j in range(i + 1): # inner loop to handle the number of columns
        print('*', end=' ') # printing stars
    print()
print('') # ending line after eahc row

print('Pattern B')

for i in range(10): #outer loop to handle the number of rows
    for j in range(10 - i): # inner loop to handle the number of columns
        print('*', end=' ') # printing stars
    print()
print('')

print('Pattern C')
for i in range (10, 0, -1): #outer loop to handle the number of rows, values changing as per requirement
    for j in range (10 - i): # inner loop to handle the number of columns
        print (' ', end =' ')
    for j in range (i):
        print ('*', end =' ') # printing stars
    print()
print('')

print('Pattern D')

for i in range (11): #outer loop to handle the number of rows
    for j in range (11 - i):  # inner loop to handle the number of columns, values changing as per requirement
        print (' ', end = ' ')
    for j in range (i):
        print ('*', end = ' ') # printing stars
    print()
