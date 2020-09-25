"""Calculating miles per gallon"""

# Initializing the variable for the values

SENTINEL = -1 #SENTINEL is a special value that marks the end
miles = 0 
gallons = 0
total_miles = 0
total_gallons_used = 0

while True: # loop until break
    miles = int(input('Enter the number of miles driven:')) # prompting user to enter the input
    if miles == SENTINEL:
        break # if SENTINEL is entered break the loop
    gallons_used = float(input('Enter the number of gallons of gas used(enter -1 to exit):')) #prompting user to enter the input
    print(f'The number of gallons of gas used is {gallons_used}') # print gallons_used
    print(f'The miles driven {miles}') #print miles driven
    miles_per_gallon = miles / gallons_used #calculate miles per gallon
    print(f'The miles_per_gallon is {miles_per_gallon: .5f}') #print miles_per_gallon with five digits after decimal