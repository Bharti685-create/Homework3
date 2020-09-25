"""Calculating Change using the fewest number of coins"""

n = int(input('Enter the value in  cents:')) # prompting user to input a number
change = 100 - n
quarters = int(change // 25) #enters the value of quarter, one quarter = 25 cents
dimes = int((change - 25 * quarters) // 10) # enters the value of dime, one dime = 10 cents
pennies = int((change - 25 * quarters - 10 * dimes))# enter the vlue of penneies, one penny = 1 cent
nickle = int((change -25 * quarters) // 5) #enter the value of nickle one nickle = 5 cents

print(quarters, 'quarter') #prints the value of quarter
print(dimes, 'dime') # pritnts the value of dime
print(pennies, 'pennies') # prints the value of penny
print(nickle, 'nickle') # prints the value og nickle
