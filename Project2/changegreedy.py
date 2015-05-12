#Peter Rissberger
#5/5/15
#ChangeGreedy
#CS 325

import sys

#Global Vars
values = []		#Array of of coin sets (array of arrays)
amounts = []	#Array of target sums associated with coin sets
amountIndex = 0 #Number of amounts scanned so far 

#Scans 'Amount.txt' and creates an array of the coin sets as well as their target amounts
def scanInput():
	global values
	global amounts

	infile = open('Amount.txt', 'r')	#File containing all arrays to be tested
	outfile = open('Amountchange.txt', 'w')	#Outfile used as a temp file for arrays

	#Cleanup junk brackets and commas from file 
	string = infile.read()
	string = string.translate(None, '[],') 	#Clean up junk commas and brackets from input
	outfile.write(string)
	outfile.seek(0)
		
	#Make array of arrays contained in infile
	with open('Amountchange.txt') as f: 
		index = 0	#Use to iterate through lines in input file 
		
		#Append every other line to values, every other *other* line to amounts
		for line in f: 
			if index % 2 == 0:
				line = line.split() 
				line = [int(i) for i in line]
				values.append(line)
			else: 
				line = int(line)
				amounts.append(line)
			index += 1

	#Clean up outfile used as temp work file
	outfile.truncate(0)
	outfile.close()

def changegreedy(v, a):
	global amountIndex
	coins = v[amountIndex] #Set of coins used to reach target sum
	target = a[amountIndex] #Target sum for coins 
	change = [] #Array of count of each type of coin needed to reach target sum 
	coinIndex = len(coins) - 1 #Used to iterate through coin values 

	#Outer loop: Cycle through every coin type 
	while(coinIndex >= 0): 
		coinCounter = 0 #Counts the number necessary of given coin type
		#print "   Top of coins while. coinCounter = " + str(coinCounter) + " coinIndex = " + str(coinIndex) + " target = " + str(target)

		#Inner loop: Add as many of a given coin type as needed 
		while(target >= coins[coinIndex]):
			target -= coins[coinIndex]
			coinCounter += 1	
		
		change.insert(0, coinCounter) #Add number of coin types to beginning of 'change'
		coinIndex -= 1 #Cycle to next coin type

	return change


#############
#MAIN PROGRAM
#############
#Read input file and display results 
scanInput()
# print "Values: " 
# print values
# print "Amounts: "
# print amounts

outfile = open('Amountchange.txt', 'w')
outfile.write("ChangeGreedy Algorithm Resutls:\n")

#Run algorithm for all amounts
for x in range(len(amounts)):
	change = changegreedy(values, amounts)
	
	#File output
	outfile.write("Results for problem " + str(amountIndex) + "\nCoins: " + str(values[amountIndex]) + "\n")
	outfile.write("Amount: " + str(amounts[amountIndex]) + "\n") 
	outfile.write("Change: " + str(change) + "\n")

	#Calculate minimum number of required coins
	minimum = 0
	for x in change: 
		minimum += x
	outfile.write("Minimum: " + str(minimum) + "\n\n")	
	
	amountIndex += 1

