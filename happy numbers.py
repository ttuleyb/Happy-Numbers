def ishappy(num):
    positiveinteger = str(num)
    knownsteps = []
    for i in range(200): # 200 steps maximum
        sumofall = 0
        for integer in list(positiveinteger): #square every digit
            sumofall += (int(integer) ** 2) #add up the results
        print(sumofall) #display the result
        if sumofall in knownsteps: #if a number repeats then terminate search, it isn't a happy number
            return False
        knownsteps.append(sumofall) #add to list of known numbers
        if sumofall == 1: #if it is 1 then it is a happy number
            return True
        positiveinteger = str(sumofall) #set the result for the next step
    return False #After 200 tries, return False

#print(ishappy(53))
happynumbers = [] #store found happy numbers
"""
for i in range(1000):
    if (ishappy(i)):
        happynumbers.append(i)
"""
i = 0
while len(happynumbers) <= 7: #Go until 8 happy numbers are found
    if (ishappy(i)): #if it is happy then store it
        happynumbers.append(i)
    i += 1
print("First 8 happy numbers are:\n" + str(happynumbers)) #list first 8 happy numbers