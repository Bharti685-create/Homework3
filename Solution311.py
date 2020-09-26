"""Calculating miles per gallon"""
# Initializing the variable for the values

SENTINEL = -1 #SENTINEL is a special value that marks the end
miles = 0 
gallons = 0
avg_miles_per_gallon = 0

while True: # loop until break
    current_g_reading = float(input('Enter gallons used : ')) # prompting user to enter the input
    if current_g_reading == SENTINEL:
        break # if SENTINEL is entered break the loop

    gallons_used = current_g_reading + gallons
    current_m_reading = float(input('Enter miles driven: '))
    miles = miles + current_m_reading
    current_avg_reading = current_m_reading / current_g_reading 
    print('Avg miles / gallon : ' + str(current_avg_reading))

avg_miles_per_gallon = miles / gallons
print('Avg miles / gallon : ' + str(avg_miles_per_gallon))
