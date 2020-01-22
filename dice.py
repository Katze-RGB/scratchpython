
import statistics
import random

rolls = input("how many dice do you want to roll? ")
rollhold = rolls
sides = input("how many sides should the dice have? ")
rolllist =[]

print ("Rolling "+rolls+" d"+sides)
while int(rolls) > 0:
	myroll= random.randint(1,int(sides))
	rolllist.append (myroll)
	rolls = (int(rolls)-1)
print (rolllist)

avg= sum(rolllist)/len(rolllist)
median= statistics.median(rolllist)

print ("Rolled "+str(rollhold)+" d"+str(sides)+" with an average of "+str(avg)+" and a median of "+str(median))

